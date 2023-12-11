// Module included in the following assemblies:
// * openshift_images/templates-ruby-on-rails.adoc


:_mod-docs-content-type: PROCEDURE
[id="templates-rails-storing-application-in-git_{context}"]
= Storing your application in Git

Building an application in {product-title} usually requires that the source code be stored in a git repository, so you must install `git` if you do not already have it.

.Prerequisites

* Install git.

.Procedure

. Make sure you are in your Rails application directory by running the `ls -1` command. The output of the command should look like:
+
[source,terminal]
----
$ ls -1
----
+
.Example output
[source,terminal]
----
app
bin
config
config.ru
db
Gemfile
Gemfile.lock
lib
log
public
Rakefile
README.rdoc
test
tmp
vendor
----

. Run the following commands in your Rails app directory to initialize and commit your code to git:
+
[source,terminal]
----
$ git init
----
+
[source,terminal]
----
$ git add .
----
+
[source,terminal]
----
$ git commit -m "initial commit"
----
+
After your application is committed you must push it to a remote repository. GitHub account, in which you create a new repository.

. Set the remote that points to your `git` repository:
+
[source,terminal]
----
$ git remote add origin git@github.com:<namespace/repository-name>.git
----

. Push your application to your remote git repository.
+
[source,terminal]
----
$ git push
----
