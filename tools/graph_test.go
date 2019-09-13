package main

import (
	"reflect"
	"strings"
	"testing"

	"github.com/goombaio/dag"
)

const testDoc = `
:context: nodes-pods-viewing
[id="nodes-pods-viewing"]
= Viewing pods
include::modules/common-attributes.adoc[]

toc::[]

As an administrator, you can view the pods in your cluster and to determine the health of those pods and the cluster as a whole.

include::modules/nodes-pods-about.adoc[leveloffset=+1]

// The following include statements pull in the module files that comprise
// the assembly. Include any combination of concept, procedure, or reference
// modules required to cover the user story. You can also include other
// assemblies.

//include::modules/nodes-pods-viewing-project.adoc[leveloffset=+1]

//    include::modules/nodes-pods-viewing-usage.adoc[leveloffset=+1]
`

func TestFindIncludes(t *testing.T) {
	doc := strings.NewReader(testDoc)
	files := findIncludes(doc)

	expect := []string{
		"modules/common-attributes.adoc",
		"modules/nodes-pods-about.adoc",
	}

	for _, f := range files {
		t.Log(f)
	}
	if !reflect.DeepEqual(files, expect) {
		t.Fatalf("expected: %v, got: %v", expect, files)
	}
}

func TestFindRoot(t *testing.T) {
	dg := dag.NewDAG()
	a := dag.NewVertex("A", nil)
	b := dag.NewVertex("B", nil)
	c := dag.NewVertex("C", nil)
	d := dag.NewVertex("D", nil)

	dg.AddVertex(a)
	dg.AddVertex(b)
	dg.AddVertex(c)
	dg.AddVertex(d)
	dg.AddEdge(a, b)
	dg.AddEdge(b, c)
	dg.AddEdge(d, c)

	sources := findSources(dg, c)
	t.Logf("%#v", sources)
	// TODO: assert equality
}
