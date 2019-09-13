package main

import (
	"fmt"
	"io"
	"log"
	"os"
	"path"
	"sort"

	"gopkg.in/yaml.v3"
)

type topicMeta struct {
	Name    string      `yaml:"Name"`
	File    string      `yaml:"File"`
	Dir     string      `yaml:"Dir"`
	Distros string      `yaml:"Distros"`
	Topics  []topicMeta ` yaml:"Topics"`
}

func findTopicFiles(dir string) ([]string, error) {
	topicMap, err := loadTopicMeta(dir)
	if err != nil {
		return nil, err
	}
	files := map[string]struct{}{}
	for _, topic := range topicMap {
		topics := collectTopicFiles(topic, "")
		for _, topic := range topics {
			file := path.Join(dir, topic+".adoc")
			files[file] = struct{}{}
		}
	}
	var flattened []string
	for file := range files {
		flattened = append(flattened, file)
	}
	sort.Strings(flattened)
	return flattened, nil
}

func loadTopicMeta(basedir string) ([]topicMeta, error) {
	var topics []topicMeta

	filename := path.Join(basedir, "_topic_map.yml")
	topicMapFile, err := os.Open(filename)
	if err != nil {
		return topics, fmt.Errorf("couldn't open topics file from %s: %v", basedir, err)
	}
	defer func() {
		if err := topicMapFile.Close(); err != nil {
			log.Println(err)
		}
	}()

	decoder := yaml.NewDecoder(topicMapFile)
	for {
		var topic topicMeta
		if err := decoder.Decode(&topic); err != nil {
			if err == io.EOF {
				break
			}
			return topics, err
		}
		topics = append(topics, topic)
	}
	return topics, nil
}

func collectTopicFiles(topic topicMeta, parent string) []string {
	var files []string
	if len(topic.File) > 0 {
		files = append(files, path.Join(parent, topic.File))
	}
	for _, subtopic := range topic.Topics {
		files = append(files, collectTopicFiles(subtopic, path.Join(parent, topic.Dir))...)
	}
	return files
}
