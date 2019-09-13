package main

import (
	"bufio"
	"io"
	"log"
	"os"
	"path"
	"path/filepath"
	"regexp"
	"sort"

	"github.com/goombaio/dag"
)

// makeGraph builds a DAG out of topic and module files. Topics can
// depend on modules, and modules can depend on modules.
func makeGraph(basedir string, files []string) *dag.DAG {
	graph := dag.NewDAG()

	// Set up a processing queue. The file order is assumed to
	// be random. When a node is found that has dependencies which
	// haven't yet been processed, defer procesing of the unsatisfied
	// node by re-queueing.
	process := make(chan string, len(files))
	for _, file := range files {
		process <- file
	}
build:
	for {
		select {
		case current := <-process:
			includes, err := findIncludesInFile(current)
			if err != nil {
				log.Fatal(err)
			}
			var deps []*dag.Vertex
			for _, include := range includes {
				id := path.Join(basedir, include)
				dep, err := graph.GetVertex(id)
				if err != nil {
					process <- current
					continue build
				}
				deps = append(deps, dep)
			}
			v := dag.NewVertex(current, nil)
			if err := graph.AddVertex(v); err != nil {
				log.Fatal(err)
			}
			for _, dep := range deps {
				if err := graph.AddEdge(v, dep); err != nil {
					log.Fatal(err)
				}
			}
		default:
			break build
		}
	}
	return graph
}

func findFiles(basedir string) []string {
	// Find all topic files which are referenced by the topic map
	topicFiles, err := findTopicFiles(basedir)
	if err != nil {
		log.Fatal(err)
	}
	// Find all module files
	moduleFiles, err := filepath.Glob(path.Join(basedir, "modules", "*.adoc"))
	if err != nil {
		log.Fatal(err)
	}

	// Track every document filename we know about
	files := map[string]struct{}{}
	for _, file := range moduleFiles {
		files[file] = struct{}{}
	}
	for _, file := range topicFiles {
		files[file] = struct{}{}
	}
	var flattened []string
	for file := range files {
		flattened = append(flattened, file)
	}
	sort.Strings(flattened)
	return flattened
}

// findIncludesInFile finds the unique list of files `included`-ed by a document
// at the specified filename.
func findIncludesInFile(name string) ([]string, error) {
	file, err := os.Open(name)
	if err != nil {
		return []string{}, err
	}
	defer func() {
		if err := file.Close(); err != nil {
			log.Println(err)
		}
	}()
	return findIncludes(file), nil
}

// findIncludes finds the unique list of files `included`-ed by a document.
func findIncludes(doc io.Reader) []string {
	files := map[string]struct{}{}

	re := regexp.MustCompile(`^include::(.+)\[`)
	scanner := bufio.NewScanner(doc)
	for scanner.Scan() {
		line := scanner.Text()
		matches := re.FindAllStringSubmatch(line, -1)
		if matches == nil {
			continue
		}
		file := matches[0][1]
		files[file] = struct{}{}
	}
	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}

	var flattened []string
	for file := range files {
		flattened = append(flattened, file)
	}
	sort.Strings(flattened)
	return flattened
}

// findSources returns all predecessors of v which themselves have no parents.
//
// An example use is to find the topics which reference a given module.
func findSources(d *dag.DAG, v *dag.Vertex) []*dag.Vertex {
	if v.InDegree() == 0 {
		return []*dag.Vertex{v}
	}
	predecessors, err := d.Predecessors(v)
	if err != nil {
		panic(err)
	}
	var sources []*dag.Vertex
	for _, p := range predecessors {
		if p.InDegree() == 0 {
			sources = append(sources, p)
		} else {
			sources = append(sources, findSources(d, p)...)
		}
	}
	return sources
}
