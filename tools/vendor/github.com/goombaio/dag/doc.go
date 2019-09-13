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

/*
Package dag implements a directed acyclic graph data structure ( DAG ), a
finite directed graph with no directed cycles.
A DAG consists of finitely many vertices and edges, with each edge directed
from one vertex to another, such that there is no way to start at any vertex
v and follow a consitently-sequence of edges that eventually loops backto v
again.

A DAG is a directex graph that has a topological order, a sequence of vertices
such that every edge is directed from earlier to later in the sequence.

Example

	// Create the dag
	dag1 := dag.NewDAG()

	// Create the vertices. Value is nil to simplify.
	vertex1 := dag.NewVertex(nil)
	vertex2 := dag.NewVertex(nil)
	vertex3 := dag.NewVertex(nil)
	vertex4 := dag.NewVertex(nil)

	// Add the vertices to the dag.
	dag1.AddVertex(vertex1)
	dag1.AddVertex(vertex2)
	dag1.AddVertex(vertex3)
	dag1.AddVertex(vertex4)

	// Add the edges (Note that given vertices must exist before adding an
	// edge between them).
	dag1.AddEdge(vertex1, vertex2)
	dag1.AddEdge(vertex2, vertex3)
	dag1.AddEdge(vertex2, vertex4)
	dag1.AddEdge(vertex4, vertex3)
*/
package dag
