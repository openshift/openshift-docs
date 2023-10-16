// Module included in the following assemblies:
//
// * openshift_images/using_images/using-images-source-to-image.adoc
// * Unused. Can be removed by 4.9 if still unused. Request full peer review for the module if it’s used.

[id="images-using-images-s2i-ruby-configuration_{context}"]
= Configuring source-to-image for Ruby

The Ruby image supports a number of environment variables which can be set to control the configuration and behavior of the Ruby runtime.

To set these environment variables as part of your image, you can place them into a `_.s2i/environment` file inside your source code repository, or define them in the environment section of the build configuration's `sourceStrategy` definition.

You can also set environment variables to be used with an existing image when creating new applications, or by updating environment variables for existing objects such as deployment configurations.

[NOTE]
====
Environment variables that control build behavior must be set as part of the source-to-image (S2I) build configuration or in the `.s2i/environment` file to make them available to the build steps.
====

.Ruby Environment Variables
[cols="4a,6a",options="header"]
|===

|Variable name |Description

|`RACK_ENV`
|This variable specifies the environment within which the Ruby application is deployed, for example, `production`, `development`, or `test`. Each level has different behavior in terms of logging verbosity, error pages, and `ruby gem` installation. The application assets are only compiled if `RACK_ENV` is set to `production`. The default value is `production`.

|`RAILS_ENV`
|This variable specifies the environment within which the Ruby on Rails application is deployed, for example, `production`, `development`, or `test`. Each level has different behavior in terms of logging verbosity, error pages, and `ruby gem` installation. The application assets are only compiled if `RAILS_ENV` is set to `production`. This variable is set to `${RACK_ENV}` by default.

|`DISABLE_ASSET_COMPILATION`
|When set to `true`, this variable disables the process of asset compilation. Asset compilation only happens when the application runs in a production environment. Therefore, you can use this variable when assets have already been compiled.

|`PUMA_MIN_THREADS`, `PUMA_MAX_THREADS`
|This variable indicates the minimum and maximum number of threads that will be available in Puma's thread pool.

|`PUMA_WORKERS`
|This variable indicates the number of worker processes to be launched in Puma's clustered mode, when Puma runs more than two processes. If not explicitly set, the default behavior sets `PUMA_WORKERS` to a value that is appropriate for the memory available to the container and the number of cores on the host.

|`RUBYGEM_MIRROR`
|Set this variable to use a custom RubyGems mirror URL to download required gem packages during the build process. This environment variable is only available for Ruby 2.2+ images.
|===
