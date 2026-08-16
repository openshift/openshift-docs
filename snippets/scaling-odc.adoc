// Text snippet included in the following modules:
//
// * modules/odc-importing-codebase-from-git-to-create-application.adoc

:_mod-docs-content-type: SNIPPET

Scaling:: Click the *Scaling* link to define the number of pods or instances of the application you want to deploy initially.
+
If you are creating a serverless deployment, you can also configure the following settings:
+
* *Min Pods* determines the lower limit for the number of pods that must be running at any given time for a Knative service. This is also known as the `minScale` setting.
* *Max Pods* determines the upper limit for the number of pods that can be running at any given time for a Knative service. This is also known as the `maxScale` setting.
* *Concurrency target* determines the number of concurrent requests desired for each instance of the application at a given time.
* *Concurrency limit* determines the limit for the number of concurrent requests allowed for each instance of the application at a given time.
* *Concurrency utilization* determines the percentage of the concurrent requests limit that must be met before Knative scales up additional pods to handle additional traffic.
* *Autoscale window* defines the time window over which metrics are averaged to provide input for scaling decisions when the autoscaler is not in panic mode. A service is scaled-to-zero if no requests are received during this window. The default duration for the autoscale window is `60s`. This is also known as the stable window.
