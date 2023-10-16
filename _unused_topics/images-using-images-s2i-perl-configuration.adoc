// Module included in the following assemblies:
//
// * openshift_images/using_images/using-images-source-to-image.adoc
// * Unused. Can be removed by 4.9 if still unused. Request full peer review for the module if it’s used.

[id="images-using-images-s2i-perl-configuration_{context}"]
= Configuring source-to-image for Perl

The Perl image supports a number of environment variables which can be set to control the configuration and behavior of the Perl runtime.

To set these environment variables as part of your image, you can place them into
a `.s2i/environment` file inside your source code repository, or define them in
the environment section of the build configuration's `sourceStrategy` definition.

You can also set environment variables to be used with an existing image when creating new applications, or by updating environment variables for existing objects such as deployment configurations.

[NOTE]
====
Environment variables that control build behavior must be set as part of the source-to-image (S2I) build configuration or in the `.s2i/environment` file to make them available to the build steps.
====

.Perl Environment Variables
[cols="4a,6a",options="header"]
|===

|Variable name |Description

|`ENABLE_CPAN_TEST`
|When set to `true`, this variable installs all the cpan modules and runs their tests. By default, the testing of the modules is disabled.

|`CPAN_MIRROR`
|This variable specifies a mirror URL which cpanminus uses to install dependencies. By default, this URL is not specified.

|`PERL_APACHE2_RELOAD`
|Set this to `true` to enable automatic reloading of modified Perl modules. By default, automatic reloading is disabled.

|`HTTPD_START_SERVERS`
|The https://httpd.apache.org/docs/2.4/mod/mpm_common.html#startservers[StartServers] directive sets the number of child server processes created on startup. Default is 8.

|`HTTPD_MAX_REQUEST_WORKERS`
|Number of simultaneous requests that will be handled by Apache. The default is 256, but it will be automatically lowered if memory is limited.
|===

//Verify` oc log` is still valid.
