# orderedset

Insertion ordered set implementation in golang.

[![License][License-Image]][License-URL]
[![CircleCI Status][CircleCI-Image]][CircleCI-URL]
[![Coverage Report][Coverage-Image]][Coverage-URL]
[![Go Report Card][GoReportCard-Image]][GoReportCard-URL]
[![CII Best Practices][CII-Image]][CII-URL]
[![GoDoc][GoDoc-Image]][GoDoc-URL]

## Install

```bash
go get github.com/goombaio/orderedset
```

You can also update an already installed version:

```bash
go get -u github.com/goombaio/orderedset
```

## Example of use

```go
package main

import (
    "github.com/goombaio/orderedset"
)

func main() {
    s := orderedset.NewOrderedSet()
    s.Add("First element")
    s.Add("Second element")
    s.Add("Last element")

    for _, entry := range s.Values() {
        fmt.Println(entry)
    }
    // Output:
    // First element
    // Second element
    // Last element
}
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
[CircleCI-Image]: https://circleci.com/gh/goombaio/orderedset.svg?style=svg
[CircleCI-URL]: https://circleci.com/gh/goombaio/orderedset
[Coverage-Image]: https://codecov.io/gh/goombaio/orderedset/branch/master/graph/badge.svg
[Coverage-URL]: https://codecov.io/gh/goombaio/orderedset
[GoReportCard-Image]: https://goreportcard.com/badge/github.com/goombaio/orderedset
[GoReportCard-URL]: https://goreportcard.com/report/github.com/goombaio/orderedset
[CII-Image]: https://bestpractices.coreinfrastructure.org/projects/2184/badge
[CII-URL]: https://bestpractices.coreinfrastructure.org/projects/2184
[GoDoc-Image]: https://godoc.org/github.com/goombaio/orderedset?status.svg
[GoDoc-URL]: http://godoc.org/github.com/goombaio/orderedset
