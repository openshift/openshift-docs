// Module included in the following assemblies:
//
// security/nbde-implementation-guide.adoc

[id="nbde-secret-sharing-encryption_{context}"]
= Secret sharing encryption

Shamir’s secret sharing (sss) is a cryptographic algorithm to securely divide up, distribute, and re-assemble keys. Using this algorithm, {product-title} can support more complicated mixtures of key protection.

When you configure a cluster node to use multiple Tang servers, {product-title} uses sss to set up a decryption policy that will succeed if at least one of the specified servers is available. You can create layers for additional security. For example, you can define a policy where {product-title} requires both the TPM and one of the given list of Tang servers to decrypt the disk.
