////
This CONCEPT module included in the following assemblies:
* service_mesh/v1x/prepare-to-deploy-applications-ossm.adoc
* service_mesh/v2x/prepare-to-deploy-applications-ossm.adoc
////

[id="ossm-tutorial-bookinfo-overview_{context}"]
= Bookinfo example application

The Bookinfo example application allows you to test your {SMProductName} {SMProductVersion} installation on {product-title}.

The Bookinfo application displays information about a book, similar to a single catalog entry of an online book store. The application displays a page that describes the book, book details (ISBN, number of pages, and other information), and book reviews.

The Bookinfo application consists of these microservices:

* The `productpage` microservice calls the `details` and `reviews` microservices to populate the page.
* The `details` microservice contains book information.
* The `reviews` microservice contains book reviews. It also calls the `ratings` microservice.
* The `ratings` microservice contains book ranking information that accompanies a book review.

There are three versions of the reviews microservice:

* Version v1 does not call the `ratings` Service.
* Version v2 calls the `ratings` Service and displays each rating as one to five black stars.
* Version v3 calls the `ratings` Service and displays each rating as one to five red stars.
