// Module included in the following assemblies:
//
// security/nbde-implementation-guide.adoc

[id="nbde-automatic-start-at-boot_{context}"]
= Automatic start at boot

Due to the sensitive nature of the key material the Tang server uses, you should keep in mind that the overhead of manual intervention during the Tang server’s boot sequence can be beneficial.

By default, if a Tang server starts and does not have key material present in the expected local volume, it will create fresh material and serve it.  You can avoid this default behavior by either starting with pre-existing key material or aborting the startup and waiting for manual intervention.
