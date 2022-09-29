// Module included in the following assemblies:
//
// * scalability_and_performance/what-huge-pages-do-and-how-they-are-consumed-by-apps.adoc
// * post_installation_configuration/node-tasks.adoc

[id="how-huge-pages-are-consumed-by-apps_{context}"]
= How huge pages are consumed by apps

Nodes must pre-allocate huge pages in order for the node to report its huge page
capacity. A node can only pre-allocate huge pages for a single size.

Huge pages can be consumed through container-level resource requirements using the
resource name `hugepages-<size>`, where size is the most compact binary
notation using integer values supported on a particular node. For example, if a
node supports 2048KiB page sizes, it exposes a schedulable resource
`hugepages-2Mi`. Unlike CPU or memory, huge pages do not support over-commitment.

[source,yaml]
----
apiVersion: v1
kind: Pod
metadata:
  generateName: hugepages-volume-
spec:
  containers:
  - securityContext:
      privileged: true
    image: rhel7:latest
    command:
    - sleep
    - inf
    name: example
    volumeMounts:
    - mountPath: /dev/hugepages
      name: hugepage
    resources:
      limits:
        hugepages-2Mi: 100Mi <1>
        memory: "1Gi"
        cpu: "1"
  volumes:
  - name: hugepage
    emptyDir:
      medium: HugePages
----
<1> Specify the amount of memory for `hugepages` as the exact amount to be
allocated. Do not specify this value as the amount of memory for `hugepages`
multiplied by the size of the page. For example, given a huge page size of 2MB,
if you want to use 100MB of huge-page-backed RAM for your application, then you
would allocate 50 huge pages. {product-title} handles the math for you. As in
the above example, you can specify `100MB` directly.

*Allocating huge pages of a specific size*

Some platforms support multiple huge page sizes. To allocate huge pages of a
specific size, precede the huge pages boot command parameters with a huge page
size selection parameter `hugepagesz=<size>`. The `<size>` value must be
specified in bytes with an optional scale suffix [`kKmMgG`]. The default huge
page size can be defined with the `default_hugepagesz=<size>` boot parameter.

*Huge page requirements*

* Huge page requests must equal the limits. This is the default if limits are
specified, but requests are not.

* Huge pages are isolated at a pod scope. Container isolation is planned in a
future iteration.

* `EmptyDir` volumes backed by huge pages must not consume more huge page memory
than the pod request.

* Applications that consume huge pages via `shmget()` with `SHM_HUGETLB` must run
with a supplemental group that matches *_proc/sys/vm/hugetlb_shm_group_*.
