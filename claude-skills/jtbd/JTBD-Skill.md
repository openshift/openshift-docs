---
name: jtbd-docs
description: Apply Jobs-to-be-Done principles to documentation writing
---

# Jobs to be Done (JTBD) Documentation Strategy

Apply Jobs to be Done principles to all documentation work, focusing on user goals rather than feature descriptions.

## Core JTBD Framework

When creating or updating documentation:

1. **Frame around user goals** using the pattern: "When [situation], I want to [action], so that [outcome]"
2. **Focus on jobs** users are trying to accomplish, not just features
3. **Organize by use cases** rather than capabilities
4. **Make it timeless** by addressing underlying needs, not implementation details

## JTBD Principles for Technical Documentation

### Start with the Job Statement
Before documenting any feature, identify:
- **Situation**: What context or trigger prompts the user?
- **Motivation**: What does the user want to accomplish?
- **Outcome**: What success looks like for the user?

Example: "When deploying a multi-tenant API, I want to authenticate clients using their X.509 certificates, so that I can ensure only authorized organizations access specific resources."

### Structure Documentation Around Jobs

**Instead of feature-first:**
```
Authentication
├── Overview
├── API Key Authentication
├── JWT Authentication
├── X.509 Certificate Authentication
└── OAuth2 Authentication
```

**Use job-first:**
```
Secure API Access
├── Verify client identity with enterprise certificates
│   ├── Understanding X.509 client certificate authentication
│   ├── Configure certificate validation
│   └── Extract claims from certificates
├── Enable partner integration with API keys
└── Support user login with OAuth2
```

### Content Guidelines

**DO:**
- Lead with the user's goal or problem
- Provide complete workflows from job start to finish
- Include context about when to use this approach
- Show related capabilities in context of the job
- Use concrete, real-world scenarios

**DON'T:**
- Start with feature definitions or capability lists
- Document features in isolation
- Use abstract examples
- Organize solely by API or product structure
- Focus on "how the feature works" before "what job it solves"

### Documentation Patterns

#### Job-Focused Guide Structure
1. **Job statement**: When/want/so that
2. **Before you begin**: Prerequisites in context of the job
3. **Guided workflow**: Step-by-step path to job completion
4. **Verification**: How to confirm the job is done
5. **Related jobs**: What users might do next
6. **Reference**: Feature details for those who need them

#### Navigation Organization
Group by:
- User roles and responsibilities
- Workflow stages or lifecycle phases
- Problem domains or scenarios
- Business outcomes

Avoid grouping by:
- API resources or CRDs
- Product components
- Alphabetical feature lists

### Quality Checks

Before publishing documentation, verify:
- [ ] Title describes a job, not a feature ("Authenticate microservices with mTLS" not "X.509 AuthPolicy Configuration")
- [ ] Introduction states the user's goal and outcome
- [ ] Content follows a job workflow, not a feature tour
- [ ] Examples show realistic scenarios, not toy cases
- [ ] Related capabilities appear in context, not as isolated topics
- [ ] Structure remains stable even if feature implementation changes

## Application to Current Work

When working on documentation tasks:

1. **Identify the job**: Ask "What is the user really trying to accomplish?"
2. **Reframe the title**: Convert feature names to job statements
3. **Restructure content**: Lead with scenario, follow with solution path
4. **Add context**: Explain when and why to use this approach
5. **Connect jobs**: Show how this fits into larger workflows

## Examples from Kuadrant Context

**Feature-based** ❌
"Configuring X.509 Client Certificate Authentication in AuthPolicy"

**Job-based** ✅
"Authenticate API clients using enterprise X.509 certificates"

**Feature-based navigation** ❌
- AuthPolicy
  - Authentication methods
  - X.509 configuration
  - JWT validation
  - API key setup

**Job-based navigation** ✅
- Secure API access for different client types
  - Verify enterprise clients with X.509 certificates
  - Enable partner integration with API keys
  - Support user sessions with JWT tokens

---

**Usage**: Invoke this skill at the start of any documentation task to apply JTBD principles throughout the work.