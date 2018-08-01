package main

import (
	"bytes"
	"flag"
	"fmt"
	"go/ast"
	"go/build"
	"log"
	"os"
	"path"
	"path/filepath"
	"runtime"
	"strings"
	"text/template"

	"golang.org/x/tools/godoc"
	"golang.org/x/tools/godoc/vfs"
)

var (
	pkgTemplate = `{{with .PDoc}}[[master-node-config-api]]
= Master and Node Configuration API
{product-author}
{product-version}
:data-uri:
:icons:
:experimental:
:toc: macro
:toc-title:

toc::[]
{{range .Types}}{{$tname := .Name}}{{$tname_html := html .Name}}
[[{{$tname_html}}]]
== {{$tname_html}}
{{.Doc}}{{.Decl | genDecl}}
{{end}}{{end}}
`
	pres *godoc.Presentation
	fs   = vfs.NameSpace{}

	funcs = map[string]interface{}{
		"base":    path.Base,
		"genDecl": handleDeclaration,
	}
)

// handleDeclaration parses ast.GenDecl object retrieving only type declarations
// and their structures.
func handleDeclaration(a *ast.GenDecl) string {
	var buf bytes.Buffer
	for _, s := range a.Specs {
		if ts, ok := s.(*ast.TypeSpec); ok {
			if st, ok := ts.Type.(*ast.StructType); ok {
				fmt.Fprintf(&buf, `[cols="2a,2a,6a",options="header"]
|===
|Field |Type| Description
`)
				for _, l := range st.Fields.List {
					fmt.Fprint(&buf, "|")
					for _, i := range l.Names {
						fmt.Fprintf(&buf, "%s", i.Name)
					}
					fmt.Fprintf(&buf, "|%s |", printType(l.Type))
					if l.Doc != nil {
						for _, c := range l.Doc.List {
							fmt.Fprintf(&buf, "%s", strings.TrimLeft(c.Text, "// "))
						}
					}
					fmt.Fprintf(&buf, "\n")
				}
				fmt.Fprintf(&buf, "|===")
			}
		}
	}
	return buf.String()
}

// printType is reponsible for parsing the type and returning human readable
// information about type, if necessary linking to other parts of this document.
func printType(typ ast.Expr) string {
	switch t := typ.(type) {
	case *ast.Ident:
		if isBuiltin(t.Name) {
			return t.Name
		}
		return fmt.Sprintf("xref:%s[%s]", t.Name, t.Name)
	case *ast.StarExpr:
		return printType(t.X)
	case *ast.ArrayType:
		return fmt.Sprintf("[]%s", printType(t.Elt))
	case *ast.MapType:
		return fmt.Sprintf("map[%s]%s", printType(t.Key), printType(t.Value))
	case *ast.SelectorExpr:
		return fmt.Sprintf("%s.%s", t.X, t.Sel)
	}
	return ""
}

// isBuiltin verifies if the given name is a builtin type for which we should
// not generate link.
func isBuiltin(name string) bool {
	return name == "bool" || name == "string" || strings.HasPrefix(name, "int") ||
		strings.HasPrefix(name, "uint") || strings.HasPrefix(name, "float")
}

func main() {
	flag.Parse()

	// use file system of underlying OS
	fs.Bind("/", vfs.OS(runtime.GOROOT()), "/", vfs.BindReplace)

	// Bind $GOPATH trees into Go root.
	for _, p := range filepath.SplitList(build.Default.GOPATH) {
		fs.Bind("/src/pkg", vfs.OS(p), "/src", vfs.BindAfter)
	}

	corpus := godoc.NewCorpus(fs)
	corpus.Verbose = true

	pres = godoc.NewPresentation(corpus)
	pres.TabWidth = 4
	pres.ShowTimestamps = false
	pres.ShowPlayground = false
	pres.ShowExamples = false
	pres.DeclLinks = true
	pres.SrcMode = false
	pres.HTMLMode = false

	var err error
	pres.PackageText, err = template.New("package.txt").Funcs(pres.FuncMap()).Funcs(funcs).Parse(pkgTemplate)
	if err != nil {
		log.Fatal("readTemplate: ", err)
	}

	if err = godoc.CommandLine(os.Stdout, fs, pres, flag.Args()); err != nil {
		log.Print(err)
	}
}
