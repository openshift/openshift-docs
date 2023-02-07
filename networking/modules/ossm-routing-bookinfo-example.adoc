// Module included in the following assemblies:
//
// * service_mesh/v1x/ossm-traffic-manage.adoc
// * service_mesh/v2x/ossm-traffic-manage.adoc

[id="ossm-routing-bookinfo_{context}"]
= Bookinfo routing tutorial

The {SMProductShortName} Bookinfo sample application consists of four separate microservices, each with multiple versions. After installing the Bookinfo sample application, three different versions of the `reviews` microservice run concurrently.

When you access the Bookinfo app `/product` page in a browser and refresh several times, sometimes the book review output contains star ratings and other times it does not. Without an explicit default service version to route to, {SMProductShortName} routes requests to all available versions one after the other.

This tutorial helps you apply rules that route all traffic to `v1` (version 1) of the microservices. Later, you can apply a rule to route traffic based on the value of an HTTP request header.

.Prerequisites:

* Deploy the Bookinfo sample application to work with the following examples.
