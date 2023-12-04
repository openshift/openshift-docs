// Module included in the following assemblies:
//
// security/certificates/replacing-default-ingress-certificate.adoc

:_mod-docs-content-type: CONCEPT
[id="understanding-default-ingress_{context}"]
= Understanding the default ingress certificate

By default, {product-title} uses the Ingress Operator to
create an internal CA and issue a wildcard certificate that is valid for
applications under the `.apps` sub-domain. Both the web console and CLI
use this certificate as well.

The internal infrastructure CA certificates are self-signed.
While this process might be perceived as bad practice by some security or
PKI teams, any risk here is minimal. The only clients that implicitly
trust these certificates are other components within the cluster.
Replacing the default wildcard certificate with one that is issued by a
public CA already included in the CA bundle as provided by the container userspace
allows external clients to connect securely to applications running under the `.apps` sub-domain.
