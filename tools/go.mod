module github.com/openshift/openshift-docs/tools

go 1.12

require (
	github.com/fsnotify/fsnotify v1.4.7
	github.com/ghodss/yaml v1.0.0 // indirect
	github.com/goombaio/dag v0.0.0-20181006234417-a8874b1f72ff
	github.com/spf13/cobra v0.0.5
	golang.org/x/sys v0.0.0-20190911201528-7ad0cfa0b7b5 // indirect
	gopkg.in/yaml.v3 v3.0.0-20190905181640-827449938966
)

replace github.com/fsnotify/fsnotify => github.com/Code0x58/fsnotify v1.4.8-0.20190413124741-5ebac3b44ada
