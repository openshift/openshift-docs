# OSD Plan Category - Update Log

## Update: 2026-10-02

### Changes Made

Based on the updated CSV file for OSD Plan category, the following changes were made:

#### Files Deleted (2)
1. `maps/hcm-jobs/choose-the-cloud-authentication-model-aws.adoc`
2. `maps/hcm-jobs/modules/choose-the-cloud-authentication-model-aws-intro.adoc`

#### Files Updated (1)
1. `maps/hcm-jobs/plan-an-osd-deployment-on-aws.adoc`
   - Removed include for `choose-the-cloud-authentication-model-aws.adoc`
   - Updated TODO comment to note the removal

### Reason for Changes

The updated CSV file no longer includes "Choose the cloud authentication model" as a sub-job for the AWS deployment path. This sub-job remains in the GCP deployment path.

### Updated Structure

**Plan an OSD deployment on Google Cloud** (7 sub-jobs):
1. Choose the subscription model
2. Plan network capacity and placement
3. Define how users and applications access the cluster
4. Plan outbound connectivity
5. Choose the cloud authentication model ✓
6. Choose the cluster encryption strategy
7. Plan compute resources

**Plan an OSD deployment on AWS** (6 sub-jobs):
1. Choose the subscription model
2. Plan network capacity and placement
3. Define how users and applications access the cluster
4. Plan outbound connectivity
5. Choose the cluster encryption strategy
6. Plan compute resources

**Note**: "Choose the cloud authentication model" is NOT included in AWS path.

### Updated Totals

- **OSD job maps**: 15 (was 16)
- **OSD intro modules**: 15 (was 16)
- **Total job maps across all distros**: 29 (was 30)

### Validation

All files validate cleanly:
- ✓ plan-an-osd-deployment-on-aws.adoc
- ✓ maps/osd/plan.adoc
- ✓ maps/osd/navigation.adoc
- ✓ No broken includes or missing files
