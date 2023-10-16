// Module included in the following assemblies:
//
// security/nbde-implementation-guide.adoc

[id="nbde-logging-considerations_{context}"]
= Logging considerations

Centralized logging of Tang traffic is advantageous because it might allow you to detect such things as unexpected decryption requests. For example:

* A node requesting decryption of a passphrase that does not correspond to its boot sequence
* A node requesting decryption outside of a known maintenance activity, such as cycling keys
