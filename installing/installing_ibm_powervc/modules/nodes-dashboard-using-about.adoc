// Module included in the following assemblies:
//
// * nodes/nodes-dashboard-using.adoc

:_mod-docs-content-type: CONCEPT
[id="nodes-dashboard-using-about_{context}"]
= About the node metrics dashboard

The node metrics dashboard enables administrative and support team members to monitor metrics related to pod scaling, including scaling limits used to diagnose and troubleshoot scaling issues. Particularly, you can use the visual analytics displayed through the dashboard to monitor workload distributions across nodes. Insights gained from these analytics help you determine the health of your CRI-O and Kubelet system components as well as identify potential sources of excessive or imbalanced resource consumption and system instability.

The dashboard displays visual analytics widgets organized into the following categories:

Critical:: Includes visualizations that can help you identify node issues that could result in system instability and inefficiency
Outliers:: Includes histograms that visualize processes with runtime durations that fall outside of the 95th percentile
Average durations:: Helps you track change in the time that system components take to process operations
Number of operations:: Displays visualizations that help you identify changes in the number of operations being run, which in turn helps you determine the load balance and efficiency of your system