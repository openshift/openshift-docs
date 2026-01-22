// Module included in the following assemblies:
//
// * nodes/nodes-scheduler-default.adoc

:_mod-docs-content-type: CONCEPT
[id="nodes-scheduler-default-about_{context}"]
= Understanding default scheduling

The existing generic scheduler is the default platform-provided scheduler
_engine_ that selects a node to host the pod in a three-step operation:

Filters the nodes::
The available nodes are filtered based on the constraints or requirements
specified. This is done by running each node through the list of filter
functions called _predicates_, or _filters_.

Prioritizes the filtered list of nodes::
This is achieved by passing each node through a series of _priority_, or _scoring_, functions
that assign it a score between 0 - 10, with 0 indicating a bad fit and 10
indicating a good fit to host the pod. The scheduler configuration can also take
in a simple _weight_ (positive numeric value) for each scoring function. The
node score provided by each scoring function is multiplied by the weight
(default weight for most scores is 1) and then combined by adding the scores for each node
provided by all the scores. This weight attribute can be used by
administrators to give higher importance to some scores.

Selects the best fit node::
The nodes are sorted based on their scores and the node with the highest score
is selected to host the pod. If multiple nodes have the same high score, then
one of them is selected at random.
