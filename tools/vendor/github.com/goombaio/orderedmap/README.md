# orderedmap

Insertion ordered map implementation in golang.

[![License][License-Image]][License-URL]
[![CircleCI Status][CircleCI-Image]][CircleCI-URL]
[![Coverage Report][Coverage-Image]][Coverage-URL]
[![Go Report Card][GoReportCard-Image]][GoReportCard-URL]
[![CII Best Practices][CII-Image]][CII-URL]
[![GoDoc][GoDoc-Image]][GoDoc-URL]

## Install

```bash
go get github.com/goombaio/orderedmap
```

You can also update an already installed version:

```bash
go get -u github.com/goombaio/orderedmap
```

## Example of use

```go
package main

import (
    "github.com/goombaio/orderedmap"
)

func main() {
    m := orderedmap.NewOrderedMap()
    m.Put("one", "First element")
    m.Put("two", "Second element")
    m.Put("three", "Last element")

    for _, entry := range m.Values() {
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
[CircleCI-Image]: https://circleci.com/gh/goombaio/orderedmap.svg?style=svg
[CircleCI-URL]: https://circleci.com/gh/goombaio/orderedmap
[Coverage-Image]: https://codecov.io/gh/goombaio/orderedmap/branch/master/graph/badge.svg
[Coverage-URL]: https://codecov.io/gh/goombaio/orderedmap
[GoReportCard-Image]: https://goreportcard.com/badge/github.com/goombaio/orderedmap
[GoReportCard-URL]: https://goreportcard.com/report/github.com/goombaio/orderedmap
[CII-Image]: https://bestpractices.coreinfrastructure.org/projects/2183/badge
[CII-URL]: https://bestpractices.coreinfrastructure.org/projects/2183
[GoDoc-Image]: https://godoc.org/github.com/goombaio/orderedmap?status.svg
[GoDoc-URL]: http://godoc.org/github.com/goombaio/orderedmap
