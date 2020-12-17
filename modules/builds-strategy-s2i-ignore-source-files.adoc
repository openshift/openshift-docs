// Module included in the following assemblies:
// * builds/build-strategies.adoc

[id="builds-strategy-s2i-ignore-source-files_{context}"]
= Ignoring source-to-image source files

Source-to-image (S2I) supports a `.s2iignore` file, which contains a list of file patterns that should be ignored. Files in the build working directory, as provided by the various input sources, that match a pattern found in the `.s2iignore` file will not be made available to the `assemble` script.

//For more details on the format of the `.s2iignore` file, see the S2I documentation.
