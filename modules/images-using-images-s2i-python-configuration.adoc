// Module included in the following assemblies:
//
// * openshift_images/using_images/using-images-source-to-image.adoc
// * Unused. Can be removed by 4.9 if still unused. Request full peer review for the module if it’s used.

[id="images-using-images-s2i-python-configuration_{context}"]
= Configuring source-to-image for Python

The Python image supports a number of environment variables which can be set to control the configuration and behavior of the Python runtime.

To set these environment variables as part of your image, you can place them into a `.s2i/environment` file inside your source code repository, or define them in the environment section of the build configuration's `sourceStrategy` definition.

You can also set environment variables to be used with an existing image when creating new applications, or by updating environment variables for existing objects such as deployment configurations.

[NOTE]
====
Environment variables that control build behavior must be set as part of the source-to-image (S2I) build configuration or in the `.s2i/environment` file to make them available to the build steps.
====

.Python Environment Variables
[cols="4a,6a",options="header"]
|===

|Variable name |Description

|`APP_FILE`
|This variable specifies the file name passed to the Python interpreter which is responsible for launching the application. This variable is set to `app.py` by default.

|`APP_MODULE`
|This variable specifies the WSGI callable. It follows the pattern `$(MODULE_NAME):$(VARIABLE_NAME)`, where the module name is a full dotted path and the variable name refers to a function inside the specified module. If you use `setup.py` for installing the application, then the module name can be read from that file and the variable defaults to `application`.

|`APP_CONFIG`
|This variable indicates the path to a valid Python file with a http://docs.gunicorn.org/en/latest/configure.html[gunicorn configuration].

|`DISABLE_COLLECTSTATIC`
|Set it to a nonempty value to inhibit the execution of `manage.py collectstatic` during the build. Only affects Django projects.

|`DISABLE_MIGRATE`
|Set it to a nonempty value to inhibit the execution of `manage.py migrate` when the produced image is run. Only affects Django projects.

|`*PIP_INDEX_URL*`
| Set this variable to use a custom index URL or mirror to download required
packages during build process. This only affects packages listed in the
*_requirements.txt_* file.

| `WEB_CONCURRENCY`
| Set this to change the default setting for the number of http://docs.gunicorn.org/en/stable/settings.html#workers[workers]. By default, this is set to the number of available cores times 4.
|===
