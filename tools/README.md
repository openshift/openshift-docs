# OpenShift Documentation Tools

A collection of handy tools for OpenShift documentation development.

## Installation

Requires Go 1.11 or newer.

To build `tools`, run:

```shell
make
```

## Commands

The `tools` program has several subcommands for working with docs. Run `tools help` for details about
each of them.

### Live preview

Running `tools preview` starts a server that watches for changes to all module and topic files,
rebuilding any affected topics using the `asciibinder` incremental build mode (i.e. the `--page`
option).

Documentation is served at http://localhost:9090 by default. 

```shell
tools preview --basedir /openshift-docs
```

### Integrate with other tools

The `tools build topics` command can incrementally rebuild any topics associated with a given
document file. This enables integration with other tools (e.g. editors) which may provide their
own file watching and task execution systems.

```shell
tools build topics --basedir /openshift-docs /openshift-docs/modules/any.adoc
```

## Notes

* Relies on a patched fsnotify ([fsnotify#289](https://github.com/fsnotify/fsnotify/pull/289)) to handle
the modules directory symlink cycles ([fsnotify#199](https://github.com/fsnotify/fsnotify/issues/199)).
* `tools` builds a [DAG](https://en.wikipedia.org/wiki/Directed_acyclic_graph) of the entire document
set, which as a useful side effect can detect errors with document references. However, the way
relationships are discovered (e.g. regex) may not be totally reliable.

## TODO

* preview: Rate limit and coalesce events ([fsnotify#62](https://github.com/howeyc/fsnotify/issues/62)) 
* Optimize away apparent `asciibinder` performance issues with git remotes
* Update graph when topological changes are detected
* Integrate with browser reload plugin?
* Clean up and document containerization stuff
