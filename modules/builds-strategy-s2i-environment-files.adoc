// Module included in the following assemblies:
// * builds/build-strategies.adoc

:_mod-docs-content-type: PROCEDURE
[id="builds-strategy-s2i-environment-files_{context}"]
= Using source-to-image environment files

Source build enables you to set environment values, one per line, inside your application, by specifying them in a `.s2i/environment` file in the source repository. The environment variables specified in this file are present during the build process and in the output image.

If you provide a `.s2i/environment` file in your source repository, source-to-image (S2I) reads this file during the build. This allows customization of the build behavior as the `assemble` script may use these variables.

.Procedure

For example, to disable assets compilation for your Rails application during the build:

* Add `DISABLE_ASSET_COMPILATION=true` in the `.s2i/environment` file.

In addition to builds, the specified environment variables are also available in the running application itself. For example, to cause the Rails application to start in `development` mode instead of `production`:

* Add `RAILS_ENV=development` to the `.s2i/environment` file.


The complete list of supported environment variables is available in the using images section for each image.
