[IMPORTANT]
====
{product-title} ROSA 4.12 cluster creation can take a long time or fail. The default version of ROSA is set to 4.11, which means that only 4.11 resources are created when you create account roles or ROSA clusters using the default settings. Account roles from 4.12 are backwards compatible, which is the case for `account-role` policy versions. You can use the `--version` flag to create 4.12 resources.

For more information see the link:https://access.redhat.com/solutions/6996508[ROSA 4.12 cluster creation failure solution].
====