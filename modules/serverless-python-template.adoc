// Module included in the following assemblies
//
// * serverless/functions/serverless-developing-python-functions.adoc

:_mod-docs-content-type: REFERENCE
[id="serverless-python-template_{context}"]
= Python function template structure

When you create a Python function by using the Knative (`kn`) CLI, the project directory looks similar to a typical Python project. Python functions have very few restrictions. The only requirements are that your project contains a `func.py` file that contains a `main()` function, and a `func.yaml` configuration file.

Developers are not restricted to the dependencies provided in the template `requirements.txt` file. Additional dependencies can be added as they would be in any other Python project. When the project is built for deployment, these dependencies will be included in the created runtime container image.

Both `http` and `event` trigger functions have the same template structure:

.Template structure
[source,terminal]
----
fn
├── func.py <1>
├── func.yaml <2>
├── requirements.txt <3>
└── test_func.py <4>
----
<1> Contains a `main()` function.
<2> Used to determine the image name and registry.
<3> Additional dependencies can be added to the `requirements.txt` file as they are in any other Python project.
<4> Contains a simple unit test that can be used to test your function locally.
