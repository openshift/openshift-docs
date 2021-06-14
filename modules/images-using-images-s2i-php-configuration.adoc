// Module included in the following assemblies:
//
// * openshift_images/using_images/using-images-source-to-image.adoc
// * Unused. Can be removed by 4.9 if still unused. Request full peer review for the module if it’s used.

[id="images-using-images-s2i-php-configuration_{context}"]
= Configuring source-to-image for PHP

The PHP image supports a number of environment variables which can be set to control the configuration and behavior of the PHP runtime.

To set these environment variables as part of your image, you can place them into a `.s2i/environment` file inside your source code repository, or define them in the environment section of the build configuration's `sourceStrategy` definition.

You can also set environment variables to be used with an existing image when creating new applications, or by updating environment variables for existing objects such as deployment configurations.

[NOTE]
====
Environment variables that control build behavior must be set as part of the source-to-image (S2I) build configuration or in the `.s2i/environment` file to make them available to the build steps.
====

The following environment variables set their equivalent property value in the
`php.ini` file:

.PHP Environment Variables
[cols="4a,6a,6a",options="header"]
|===

|Variable Name |Description |Default

|`ERROR_REPORTING`
|Informs PHP of the errors, warnings, and notices for which you would like it to
take action.
|`E_ALL & ~E_NOTICE`

|`DISPLAY_ERRORS`
|Controls if and where PHP outputs errors, notices, and warnings.
|`ON`

|`DISPLAY_STARTUP_ERRORS`
|Causes any display errors that occur during PHP's startup sequence to be
handled separately from display errors.
|`OFF`

|`TRACK_ERRORS`
|Stores the last error/warning message in `$php_errormsg` (boolean).
|`OFF`

|`HTML_ERRORS`
|Links errors to documentation that is related to the error.
|`ON`

|`INCLUDE_PATH`
|Path for PHP source files.
|`.:/opt/openshift/src:/opt/rh/php55/root/usr/share/pear`

|`SESSION_PATH`
|Location for session data files.
|`/tmp/sessions`

|`DOCUMENTROOT`
|Path that defines the document root for your application (for example, `/public`).
|`/`
|===

The following environment variable sets its equivalent property value in the
`opcache.ini` file:

.Additional PHP settings
[cols="3a,6a,1a",options="header"]
|===

|Variable Name |Description |Default

|`OPCACHE_MEMORY_CONSUMPTION`
|The link:http://php.net/manual/en/book.opcache.php[OPcache] shared memory
storage size.
|`16M`

|`OPCACHE_REVALIDATE_FREQ`
|How often to check script time stamps for updates, in seconds. `0` results in
link:http://php.net/manual/en/book.opcache.php[OPcache] checking for updates on
every request.
|`2`
|===

You can also override the entire directory used to load the PHP configuration by setting:

.Additional PHP settings
[cols="3a,6a",options="header"]
|===

| Variable Name | Description

|`PHPRC`
|Sets the path to the `php.ini` file.

|`*PHP_INI_SCAN_DIR*`
|Path to scan for additional `.ini` configuration files
|===

You can use a custom composer repository mirror URL to download packages instead of the default `packagist.org`:

.Composer Environment Variables
[cols="4a,6a",options="header"]
|===

|Variable Name |Description

|`COMPOSER_MIRROR`
|Set this variable to use a custom Composer repository mirror URL to download required packages during the build process.
Note: This only affects packages listed in `composer.json`.
|===

[id="images-using-images-s2i-php-apache-configuration_{context}"]
== Apache configuration

If the `DocumentRoot` of the application is nested in the source directory `/opt/openshift/src`, you can provide your own `.htaccess` file to override the default Apache behavior and specify how application requests should be handled. The `.htaccess` file must be located at the root of the application source.
