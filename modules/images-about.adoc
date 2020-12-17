// Module included in the following assemblies:
// * openshift_images/images-understand.aodc

[id="images-about_{context}"]
= Images

Containers in {product-title} are based on OCI- or Docker-formatted container _images_. An image is a binary that includes all of the requirements for running a single container, as well as metadata describing its needs and capabilities.

You can think of it as a packaging technology. Containers only have access to resources defined in the image unless you give the container additional access when creating it. By deploying the same image in multiple containers across multiple hosts and load balancing between them, {product-title} can provide redundancy and horizontal scaling for a service packaged into an image.

You can use the link:https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux_atomic_host/7/html-single/managing_containers/#using_podman_to_work_with_containers[podman] or `docker` CLI directly to build images, but {product-title} also supplies builder images that assist with creating new images by adding your code or configuration to existing images.

Because applications develop over time, a single image name can actually refer to many different versions of the same image. Each different image is referred to uniquely by its hash, a long hexadecimal number such as `fd44297e2ddb050ec4f...`, which is usually shortened to 12 characters, such as `fd44297e2ddb`.
