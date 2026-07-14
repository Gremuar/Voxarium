# Voxarium Software Architecture Specification

Document Path:
spec/400_Commands/AnalyzeRolesCommand.md

Document ID: CMD-053

Title: AnalyzeRolesCommand

Version: 1.0.0

Status: Accepted

Classification: Normative

Depends On

- Project
- Document
- Fragment
- Role
- Analysis_Service
- AnalysisJob
- Command_Model
- Command_Bus

Referenced By

- Role_Service
- Analysis_Service
- Workflow_Engine
- User_Interface_Architecture

---

# 1. Purpose

AnalyzeRolesCommand requests automatic identification and validation of speaking Roles within the selected scope.

The command SHALL analyze textual dialogue and narration.

The command SHALL NOT create, modify or delete Roles.

---

# 2. Responsibility

Execution SHALL be performed by AnalyzeRolesCommandHandler.

The handler SHALL create an Analysis Job and submit it to the Analysis Service.

---

# 3. Command Definition

## Name

AnalyzeRolesCommand

## Category

Analysis Commands

## Layer

Application

---

# 4. Parameters

## Required

### Scope

Type

Enumeration

Allowed values:

- Document
- Project

---

### TargetId

Type

Identifier

Identifier corresponding to the selected Scope.

---

## Optional

### DetectNarrator

Type

Boolean

Default:

true

---

### DetectDialogue

Type

Boolean

Default:

true

---

### MergeSimilarRoles

Type

Boolean

Default:

true

---

### ValidateAssignments

Type

Boolean

Default:

true

---

### Priority

Type

Enumeration

Allowed values:

- Low
- Normal
- High

Default:

Normal

---

# 5. Validation Rules

Execution SHALL fail if:

- the target object does not exist;
- no Fragments are available for analysis;
- Analysis Service is unavailable;
- an equivalent Analysis Job is already active.

Validation SHALL complete before execution begins.

---

# 6. Execution Rules

Execution SHALL:

1. Load the target Aggregate.
2. Collect dialogue structure.
3. Build an Analysis Plan.
4. Create an Analysis Job.
5. Register the Job with the Analysis Service.
6. Publish lifecycle events.

Execution SHALL complete immediately.

Analysis SHALL execute asynchronously.

---

# 7. Analysis Rules

The analysis MAY identify:

- speaker candidates;
- narrator fragments;
- unnamed speakers;
- duplicate Roles;
- inconsistent Role assignments;
- missing Role assignments;
- conflicting dialogue attribution.

The analysis SHALL produce recommendations only.

The command SHALL NOT modify:

- Roles;
- Fragments;
- Voice Profiles;
- Generation Presets;
- Pronunciation Dictionaries.

---

# 8. Result

Successful execution SHALL return:

AnalyzeRolesResult

The result SHALL contain:

- JobId
- Scope
- TargetId
- SuggestedRoles
- AssignmentRecommendations
- Warnings

---

# 9. Published Events

Successful execution SHALL publish:

- RoleAnalysisStarted
- JobQueued

Background execution SHALL additionally publish:

- RoleAnalysisCompleted

Upon failure:

- RoleAnalysisFailed

---

# 10. Error Conditions

Execution MAY fail with:

- TargetNotFound
- EmptyContent
- AnalysisServiceUnavailable
- AnalysisAlreadyRunning
- ValidationFailed
- InternalError

---

# 11. Idempotency

Submitting an identical analysis request while an equivalent Analysis Job is active SHALL return the existing Job.

Duplicate Analysis Jobs SHALL NOT be created.

---

# 12. Transaction Requirements

The transaction SHALL include:

- Analysis Job creation;
- queue registration.

Analysis SHALL execute outside the transaction.

---

# 13. Authorization

The caller SHALL possess permission to analyze the selected object.

---

# 14. Performance Requirements

Command execution SHOULD complete within 30 milliseconds.

The command SHALL NOT wait for analysis completion.

---

# 15. Thread Safety

Only one active role analysis MAY exist for the same target.

Independent targets MAY be analyzed concurrently.

---

# 16. AI Implementation Rules

AI-generated implementations SHALL:

- produce recommendations only;
- never create or modify Roles;
- never modify Project data;
- execute asynchronously;
- publish lifecycle events only after successful transaction completion.

---

# 17. Sequence

```text
GUI
 │
 ▼
AnalyzeRolesCommand
 │
 ▼
CommandBus
 │
 ▼
AnalyzeRolesCommandHandler
 │
 ▼
AnalysisService
 │
 ├── Analyze Dialogue
 │
 ├── Detect Speakers
 │
 ├── Validate Assignments
 │
 ▼
JobQueued Event
 │
 ▼
Background Worker
 │
 ▼
RoleAnalysisCompleted
```

---

# 18. Compliance Checklist

The implementation conforms to this specification only if it:

- analyzes existing content only;
- never modifies Roles;
- creates exactly one Analysis Job;
- executes asynchronously;
- produces recommendations only;
- publishes RoleAnalysisStarted after successful completion.

---

End of Document