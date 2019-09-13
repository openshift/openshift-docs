package main

import (
	"fmt"
	"log"
	"net/http"
	"os"
	"os/exec"
	"os/signal"
	"path"
	"path/filepath"
	"strings"
	"syscall"
	"time"

	"github.com/fsnotify/fsnotify"

	"github.com/spf13/cobra"
)

func main() {
	var baseDir string
	var addr string

	var cmdBuild = &cobra.Command{
		Use:   "build",
		Short: "Tools for building documentation",
		Long:  `Build commands are for building docs using asciidoctor.`,
		Run: func(cmd *cobra.Command, args []string) {
		},
	}

	var cmdBuildRelated = &cobra.Command{
		Use:   "topics [doc file]",
		Short: "Builds topics related to a file",
		Long: `Find and build any topics associated with the given docs file. The file
can be a topic or a module.

If the file path is relative, the file is assumed to be a child of the base directory.
`,
		Args: cobra.MinimumNArgs(1),
		Run: func(cmd *cobra.Command, args []string) {
			file := args[0]
			if !strings.HasPrefix(file, "/") {
				file = filepath.Join(baseDir, file)
			}
			if err := rebuildFile(baseDir, file); err != nil {
				log.Fatal(err)
			}
		},
	}

	var cmdPreview = &cobra.Command{
		Use:   "preview",
		Short: "Start a live preview server",
		Long: `Watches for changes to documentation files, and builds any topics associated
with the changed file.`,
		Run: func(cmd *cobra.Command, args []string) {
			preview(baseDir, addr)
		},
	}

	var rootCmd = &cobra.Command{Use: "tools"}

	rootCmd.PersistentFlags().StringVarP(&baseDir, "basedir", "d", defaultBasedir(), "the openshift-docs directory")
	cmdPreview.Flags().StringVarP(&addr, "listen-addr", "l", ":9090", "preview server listen address")

	rootCmd.AddCommand(cmdBuild, cmdPreview)
	cmdBuild.AddCommand(cmdBuildRelated)

	if err := rootCmd.Execute(); err != nil {
		log.Fatal(err)
	}
}

func defaultBasedir() string {
	dir, err := os.Getwd()
	if err != nil {
		panic(err)
	}
	return dir
}

func rebuildFile(basedir, file string) error {
	files := findFiles(basedir)
	graph := makeGraph(basedir, files)

	v, err := graph.GetVertex(file)
	if err != nil {
		return fmt.Errorf("no graph node found for %s", file)
	}
	sources := findSources(graph, v)
	for _, source := range sources {
		err := rebuild(basedir, source.ID)
		if err != nil {
			log.Printf("error rebuilding %s: %v", source.ID, err)
		}
	}
	return nil
}

func preview(basedir, bindAddr string) {
	files := findFiles(basedir)
	graph := makeGraph(basedir, files)

	// Collect all unique directories
	dirs := map[string]struct{}{}
	for _, file := range files {
		dirs[path.Dir(file)] = struct{}{}
	}

	// Set up a watch on each directory
	watcher, err := fsnotify.NewWatcher()
	if err != nil {
		log.Fatal(err)
	}
	defer func() {
		if err := watcher.Close(); err != nil {
			log.Println(err)
		}
	}()

	go func() {
		for {
			select {
			case event, ok := <-watcher.Events:
				if !ok {
					log.Println("watcher event channel closed")
					return
				}
				v, err := graph.GetVertex(event.Name)
				if err != nil {
					log.Printf("no graph node found for %s", event.Name)
					continue
				}
				sources := findSources(graph, v)
				for _, source := range sources {
					// TODO: Going to need rate limiting. See https://github.com/howeyc/fsnotify/issues/62.
					err := rebuild(basedir, source.ID)
					if err != nil {
						log.Printf("error rebuilding %s: %v", source.ID, err)
					}
				}
			case err, ok := <-watcher.Errors:
				if !ok {
					log.Println("watcher event channel closed")
					return
				}
				log.Println("watcher error:", err)
			}
		}
	}()

	// Start watching all directories
	for dir := range dirs {
		if err := watcher.Add(dir); err != nil {
			log.Fatalf("watcher error (%s): %v", dir, err)
		}
		log.Printf("watching %s", dir)
	}

	// Serve the site
	fs := http.FileServer(http.Dir(filepath.Join(basedir, "_preview")))
	http.Handle("/", fs)
	go func() {
		if err := http.ListenAndServe(bindAddr, nil); err != nil {
			log.Println(err)
		}
	}()

	// Go until we're interrupted
	sigs := make(chan os.Signal, 1)
	signal.Notify(sigs, syscall.SIGINT)
	select {
	case <-sigs:
	}
}

// rebuild calls asciibinder to rebuild a single page by its filename
// relative to basedir.
func rebuild(basedir, name string) error {
	name, _ = filepath.Rel(basedir, name)
	name = strings.TrimRight(name, filepath.Ext(name))
	dir, file := filepath.Split(name)
	dir = strings.TrimRight(dir, "/")
	page := fmt.Sprintf("%s:%s", dir, file)
	script := fmt.Sprintf(`asciibinder build --page %s`, page)
	log.Println(script)
	cmd := exec.Command("sh", "-c", script)
	cmd.Dir = basedir
	start := time.Now()
	stdoutStderr, err := cmd.CombinedOutput()
	if err != nil {
		return err
	}
	elapsed := time.Now().Sub(start)
	log.Printf("rebuilt %s in %s: %s", page, elapsed, stdoutStderr)
	return nil
}
