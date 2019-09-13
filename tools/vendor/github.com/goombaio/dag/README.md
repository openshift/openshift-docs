# dag

A DAG, Directed acyclic graph implementation in golang.

## Badges

[![License][License-Image]][License-URL]
[![CircleCI Status][CircleCI-Image]][CircleCI-URL]
[![Coverage Report][Coverage-Image]][Coverage-URL]
[![Go Report Card][GoReportCard-Image]][GoReportCard-URL]
[![CII Best Practices][CII-Image]][CII-URL]
[![GoDoc][GoDoc-Image]][GoDoc-URL]

## Install

```bash
go get github.com/goombaio/dag
```

You can also update an already installed version:

```bash
go get -u github.com/goombaio/dag
```

## Example of use

```go
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
```

## License

Copyright (c) 2018 Goomba project Authors.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

[License-Image]: https://img.shields.io/badge/License-Apache-blue.svg
[License-URL]: http://opensource.org/licenses/Apache
[CircleCI-Image]: https://circleci.com/gh/goombaio/dag.svg?style=svg
[CircleCI-URL]: https://circleci.com/gh/goombaio/dag
[Coverage-Image]: https://codecov.io/gh/goombaio/dag/branch/master/graph/badge.svg
[Coverage-URL]: https://codecov.io/gh/goombaio/dag
[GoReportCard-Image]: https://goreportcard.com/badge/github.com/goombaio/dag
[GoReportCard-URL]: https://goreportcard.com/report/github.com/goombaio/dag
[CII-Image]: https://bestpractices.coreinfrastructure.org/projects/2177/badge
[CII-URL]: https://bestpractices.coreinfrastructure.org/projects/2177
[GoDoc-Image]: https://godoc.org/github.com/goombaio/dag?status.svg
[GoDoc-URL]: http://godoc.org/github.com/goombaio/dag
