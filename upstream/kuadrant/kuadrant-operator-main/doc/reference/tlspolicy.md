# The TLSPolicy Custom Resource Definition (CRD)

- [TLSPolicy](#TLSPolicy)
- [TLSPolicySpec](#tlspolicyspec)
- [TLSPolicyStatus](#tlspolicystatus)

## TLSPolicy

| **Field** | **Type**                            | **Required** | **Description**                                 |
|-----------|-------------------------------------|:------------:|-------------------------------------------------|
| `spec`    | [TLSPolicySpec](#tlspolicyspec)     |    Yes       | The specification for TLSPolicy custom resource |
| `status`  | [TLSPolicyStatus](#tlspolicystatus) |      No      | The status for the custom resource              |

## TLSPolicySpec

| **Field**              | **Type**                                                                                                                                     | **Required** | **Description**                                                                                                                                  |
|------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|:------------:|--------------------------------------------------------------------------------------------------------------------------------------------------|
| `targetRef`            | [Gateway API PolicyTargetReference](https://gateway-api.sigs.k8s.io/geps/gep-713/?h=policytargetreference#policy-targetref-api)              |     Yes      | Reference to a Kuberentes resource that the policy attaches to                                                                                   |
| `issuerRef`            | [CertManager meta/v1.ObjectReference](https://cert-manager.io/v1.13-docs/reference/api-docs/#meta.cert-manager.io/v1.ObjectReference)        |     Yes      | IssuerRef is a reference to the issuer for the created certificate                                                                               |
| `commonName`           | String                                                                                                                                       |      No      | CommonName is a common name to be used on the created certificate                                                                                |
| `duration`             | [Kubernetes meta/v1.Duration](https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration)                                              |      No      | The requested 'duration' (i.e. lifetime) of the created certificate.                                                                             |
| `renewBefore`          | [Kubernetes meta/v1.Duration](https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration)                                              |      No      | How long before the currently issued certificate's expiry cert-manager should renew the certificate.                                             |
| `usages`               | [][CertManager v1.KeyUsage](https://cert-manager.io/v1.13-docs/reference/api-docs/#cert-manager.io/v1.KeyUsage)                              |      No      | Usages is the set of x509 usages that are requested for the certificate. Defaults to `digital signature` and `key encipherment` if not specified |
| `revisionHistoryLimit` | Number                                                                                                                                       |      No      | RevisionHistoryLimit is the maximum number of CertificateRequest revisions that are maintained in the Certificate's history                      |
| `privateKey`           | [CertManager meta/v1.CertificatePrivateKey](https://cert-manager.io/v1.13-docs/reference/api-docs/#cert-manager.io/v1.CertificatePrivateKey) |      No      | Options to control private keys used for the Certificate                                                                                         | 


**IssuerRef certmanmetav1.ObjectReference**

## TLSPolicyStatus

| **Field**            | **Type**                                                                                            | **Description**                                                                                                                     |
|----------------------|-----------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| `observedGeneration` | String                                                                                              | Number of the last observed generation of the resource. Use it to check if the status info is up to date with latest resource spec. |
| `conditions`         | [][Kubernetes meta/v1.Condition](https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Condition) | List of conditions that define that status of the resource.                                                                         |
