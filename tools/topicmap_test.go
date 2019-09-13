package main

import (
	"reflect"
	"testing"
)

func TestCollectTopicFiles(t *testing.T) {
	topics := []topicMeta{
		{
			Dir: "alpha",
			Topics: []topicMeta{
				{
					Dir: "bar",
					Topics: []topicMeta{
						{
							File: "a",
						},
						{
							File: "b",
						},
					},
				},
			},
		},
		{
			Dir: "beta",
			Topics: []topicMeta{
				{
					Name: "Name A",
					File: "a",
				},
				{
					Name: "Name B",
					File: "b",
				},
			},
		},
	}
	var files []string
	for _, topic := range topics {
		files = append(files, collectTopicFiles(topic, "")...)
	}

	expect := []string{
		"alpha/bar/a",
		"alpha/bar/b",
		"beta/a",
		"beta/b",
	}
	for _, file := range files {
		t.Logf(file)
	}
	if !reflect.DeepEqual(files, expect) {
		t.Fatalf("expected: %v, got: %v", expect, files)
	}
}
