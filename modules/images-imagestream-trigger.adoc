// Module included in the following assemblies:
// * openshift_images/images-understand.aodc

[id="images-imagestream-trigger_{context}"]
= Image stream triggers

An image stream trigger causes a specific action when an image stream tag changes. For example, importing can cause the value of the tag to change, which causes a trigger to fire when there are deployments, builds, or other resources listening for those.
