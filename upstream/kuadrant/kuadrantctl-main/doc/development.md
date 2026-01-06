# Development Guide

## Technology stack required for development

* [git][git_tool]
* [go] version 1.21+

## Build the CLI
```
$ git clone https://github.com/kuadrant/kuadrantctl.git
$ cd kuadrantctl && make install
$ bin/kuadrantctl version
{"level":"info","ts":"2023-11-08T23:44:57+01:00","msg":"kuadrantctl version: latest"}
```

## Quick steps to contribute

* Fork the project.
* Download your fork to your PC (`git clone https://github.com/your_username/kuadrantctl && cd kuadrantctl`)
* Create your feature branch (`git checkout -b my-new-feature`)
* Make changes and run tests (`make test`)
* Add them to staging (`git add .`)
* Commit your changes (`git commit -m 'Add some feature'`)
* Push to the branch (`git push origin my-new-feature`)
* Create new pull request

[git_tool]:https://git-scm.com/downloads
[go]:https://golang.org/
