// Module included in the following assemblies:
//
// * operators/operator_sdk/osdk-ha-sno.adoc

[id="osdk-ha-sno-api-examples_{context}"]
= Example API usage in Operator projects

As an Operator author, you can update your Operator project to access the Infrastructure API by using normal Kubernetes constructs and the `controller-runtime` library, as shown in the following examples:

.`controller-runtime` library example
[source,go]
----
// Simple query
 nn := types.NamespacedName{
 Name: "cluster",
 }
 infraConfig := &configv1.Infrastructure{}
 err = crClient.Get(context.Background(), nn, infraConfig)
 if err != nil {
 return err
 }
 fmt.Printf("using crclient: %v\n", infraConfig.Status.ControlPlaneTopology)
 fmt.Printf("using crclient: %v\n", infraConfig.Status.InfrastructureTopology)
----

.Kubernetes constructs example
[source,go]
----
operatorConfigInformer := configinformer.NewSharedInformerFactoryWithOptions(configClient, 2*time.Second)
 infrastructureLister = operatorConfigInformer.Config().V1().Infrastructures().Lister()
 infraConfig, err := configClient.ConfigV1().Infrastructures().Get(context.Background(), "cluster", metav1.GetOptions{})
 if err != nil {
 return err
 }
// fmt.Printf("%v\n", infraConfig)
 fmt.Printf("%v\n", infraConfig.Status.ControlPlaneTopology)
 fmt.Printf("%v\n", infraConfig.Status.InfrastructureTopology)
----
