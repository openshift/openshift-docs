// Module included in the following assemblies:
//
// * operators/understanding/olm-what-operators-are.adoc

[id="olm-maturity-model_{context}"]
= Operator maturity model

The level of sophistication of the management logic encapsulated within an Operator can vary. This logic is also in general highly dependent on the type of the service represented by the Operator.

One can however generalize the scale of the maturity of the encapsulated operations of an Operator for certain set of capabilities that most Operators can include. To this end, the following Operator maturity model defines five phases of maturity for generic Day 2 operations of an Operator:

.Operator maturity model
image::operator-maturity-model.png[]

The above model also shows how these capabilities can best be developed through
the Helm, Go, and Ansible capabilities of the Operator SDK.
