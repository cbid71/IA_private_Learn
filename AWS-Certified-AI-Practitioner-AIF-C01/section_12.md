# AWS Security

This section is mostly about AWS concepts out of IA, AWS in general.


# How to secure

- IAM
- Users
- Groups
- Roles
- IAM Policies
- IAM Policies inheritance

# How to store

- Amazon S3
- Amazon S3 Storage classes (remember = s3 intelligent tiering when no particular pattern have been identified)

# How to Compute

- EC2
- Lambda

# Identify sensitive data while deep learning

- Macie

Alternate to Comprehend, both Macie and Comprehend are able to identify PII (personnal data)
But when Macie is designed to discover sensitive data in s3 buckets, comprehend of more of a natural langage processing which can discover PII.
To make it simple, Macie will directly analyse objects in S3 when comprehend parsed files.

Macie --> Sensitive data analysis.


# Manage configuration

AWS Config (meh ?)

# Audit

**Amazon Inspector** give you informations about what ressource is deployed and security assessments related to them 
`Linux Kernel : 4 security breaches`

# AWS Artifact

AWS Artifact is a service that provides access to compliance reports and security and privacy documentation for AWS services. It is mainly used by businesses and organizations to help them meet regulatory requirements and maintain security standards.
---

This whole section is about services of AWS outside of AI.
I bypass it, since I already got AWS SAA certification :3



