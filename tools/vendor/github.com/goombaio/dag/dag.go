// Copyright 2018, Goomba project Authors. All rights reserved.
//
// Licensed to the Apache Software Foundation (ASF) under one or more
// contributor license agreements.  See the NOTICE file distributed with this
// work for additional information regarding copyright ownership.  The ASF
// licenses this file to you under the Apache License, Version 2.0 (the
// "License"); you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
// http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
// WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.  See the
// License for the specific language governing permissions and limitations
// under the License.

package dag

import (
	"fmt"
	"sync"

	"github.com/goombaio/orderedmap"
)

// DAG type implements a Directed Acyclic Graph data structure.
type DAG struct {
	mu       sync.Mutex
	vertices orderedmap.OrderedMap
}

// NewDAG creates a new Directed Acyclic Graph or DAG.
func NewDAG() *DAG {
	d := &DAG{
		vertices: *orderedmap.NewOrderedMap(),
	}

	return d
}

// AddVertex adds a vertex to the graph.
func (d *DAG) AddVertex(v *Vertex) error {
	d.mu.Lock()
	defer d.mu.Unlock()

	d.vertices.Put(v.ID, v)

	return nil
}

// DeleteVertex deletes a vertex and all the edges referencing it from the
// graph.
func (d *DAG) DeleteVertex(vertex *Vertex) error {
	existsVertex := false

	d.mu.Lock()
	defer d.mu.Unlock()

	// Check if vertices exists.
	for _, v := range d.vertices.Values() {
		if v == vertex {
			existsVertex = true
		}
	}
	if !existsVertex {
		return fmt.Errorf("Vertex with ID %v not found", vertex.ID)
	}

	d.vertices.Remove(vertex.ID)

	return nil
}

// AddEdge adds a directed edge between two existing vertices to the graph.
func (d *DAG) AddEdge(tailVertex *Vertex, headVertex *Vertex) error {
	tailExists := false
	headExists := false

	d.mu.Lock()
	defer d.mu.Unlock()

	// Check if vertices exists.
	for _, vertex := range d.vertices.Values() {
		if vertex == tailVertex {
			tailExists = true
		}
		if vertex == headVertex {
			headExists = true
		}
	}
	if !tailExists {
		return fmt.Errorf("Vertex with ID %v not found", tailVertex.ID)
	}
	if !headExists {
		return fmt.Errorf("Vertex with ID %v not found", headVertex.ID)
	}

	// Check if edge already exists.
	for _, childVertex := range tailVertex.Children.Values() {
		if childVertex == headVertex {
			return fmt.Errorf("Edge (%v,%v) already exists", tailVertex.ID, headVertex.ID)
		}
	}

	// Add edge.
	tailVertex.Children.Add(headVertex)
	headVertex.Parents.Add(tailVertex)

	return nil
}

// DeleteEdge deletes a directed edge between two existing vertices from the
// graph.
func (d *DAG) DeleteEdge(tailVertex *Vertex, headVertex *Vertex) error {
	for _, childVertex := range tailVertex.Children.Values() {
		if childVertex == headVertex {
			tailVertex.Children.Remove(childVertex)
		}
	}

	return nil
}

// GetVertex return a vertex from the graph given a vertex ID.
func (d *DAG) GetVertex(id interface{}) (*Vertex, error) {
	var vertex *Vertex

	v, found := d.vertices.Get(id)
	if !found {
		return vertex, fmt.Errorf("vertex %s not found in the graph", id)
	}

	vertex = v.(*Vertex)

	return vertex, nil
}

// Order return the number of vertices in the graph.
func (d *DAG) Order() int {
	numVertices := d.vertices.Size()

	return numVertices
}

// Size return the number of edges in the graph.
func (d *DAG) Size() int {
	numEdges := 0
	for _, vertex := range d.vertices.Values() {
		numEdges = numEdges + vertex.(*Vertex).Children.Size()
	}

	return numEdges
}

// SinkVertices return vertices with no children defined by the graph edges.
func (d *DAG) SinkVertices() []*Vertex {
	var sinkVertices []*Vertex

	for _, vertex := range d.vertices.Values() {
		if vertex.(*Vertex).Children.Size() == 0 {
			sinkVertices = append(sinkVertices, vertex.(*Vertex))
		}
	}

	return sinkVertices
}

// SourceVertices return vertices with no parent defined by the graph edges.
func (d *DAG) SourceVertices() []*Vertex {
	var sourceVertices []*Vertex

	for _, vertex := range d.vertices.Values() {
		if vertex.(*Vertex).Parents.Size() == 0 {
			sourceVertices = append(sourceVertices, vertex.(*Vertex))
		}
	}

	return sourceVertices
}

// Successors return vertices that are children of a given vertex.
func (d *DAG) Successors(vertex *Vertex) ([]*Vertex, error) {
	var successors []*Vertex

	_, found := d.GetVertex(vertex.ID)
	if found != nil {
		return successors, fmt.Errorf("vertex %s not found in the graph", vertex.ID)
	}

	for _, v := range vertex.Children.Values() {
		successors = append(successors, v.(*Vertex))
	}

	return successors, nil
}

// Predecessors return vertices that are parent of a given vertex.
func (d *DAG) Predecessors(vertex *Vertex) ([]*Vertex, error) {
	var predecessors []*Vertex

	_, found := d.GetVertex(vertex.ID)
	if found != nil {
		return predecessors, fmt.Errorf("vertex %s not found in the graph", vertex.ID)
	}

	for _, v := range vertex.Parents.Values() {
		predecessors = append(predecessors, v.(*Vertex))
	}

	return predecessors, nil
}

// String implements stringer interface.
//
// Prints an string representation of this instance.
func (d *DAG) String() string {
	result := fmt.Sprintf("DAG Vertices: %d - Edges: %d\n", d.Order(), d.Size())
	result += fmt.Sprintf("Vertices:\n")
	for _, vertex := range d.vertices.Values() {
		vertex = vertex.(*Vertex)
		result += fmt.Sprintf("%s", vertex)
	}

	return result
}
