# Voxarium Software Architecture Specification

Document Path:
spec/400_Commands/AnalyzeDuplicateContentCommand.md

Document ID: CMD-058

Title: AnalyzeDuplicateContentCommand

Version: 1.0.0

Status: Accepted

Classification: Normative

Depends On

- Project
- Document
- Fragment
- Analysis_Service
- AnalysisJob
- Command_Model
- Command_Bus

Referenced By

- Analysis_Service
- Workflow_Engine
- Generation_Service
- User_Interface_Architecture

---

# 1. Purpose

AnalyzeDuplicateContentCommand evaluates a Project for duplicated textual content.

The command SHALL identify duplicate or highly similar Fragments and Documents.

The command SHALL NOT modify Project data.

---

# 2. Responsibility

Execution SHALL be performed by AnalyzeDuplicateContentCommandHandler.

The handler SHALL create an Analysis Job and submit it to the Analysis Service.

---

# 3. Command Definition

## Name

AnalyzeDuplicateContentCommand

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

### SimilarityThreshold

Type

Percentage

Default:

95

---

### DetectExactDuplicates

Type

Boolean

Default:

true

---

### DetectNearDuplicates

Type

Boolean

Default:

true

---

### IgnoreWhitespace

Type

Boolean

Default:

true

---

### IgnoreCase

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
- no textual content exists;
- Analysis Service is unavailable;
- an equivalent Analysis Job is already active.

Validation SHALL complete before execution begins.

---

# 6. Execution Rules

Execution SHALL:

1. Load the target Aggregate.
2. Collect textual content.
3. Build an Analysis Plan.
4. Create an Analysis Job.
5. Register the Job with the Analysis Service.
6. Publish lifecycle events.

Execution SHALL complete immediately.

Duplicate analysis SHALL execute asynchronously.

---

# 7. Analysis Rules

The analysis SHALL detect:

- duplicate Fragments;
- duplicate Documents;
- highly similar Fragments;
- repeated paragraphs;
- repeated sentences;
- redundant content.

The analysis SHALL calculate similarity scores for every detected duplicate.

The command SHALL NOT modify:

- Projects;
- Documents;
- Fragments;
- Roles;
- Voice Profiles;
- Generation Presets.

The analysis SHALL produce recommendations only.

---

# 8. Result

Successful execution SHALL return:

AnalyzeDuplicateContentResult

The result SHALL contain:

- JobId
- Scope
- TargetId
- DuplicateGroups
- SimilarityScores
- Warnings

---

# 9. Published Events

Successful execution SHALL publish:

- DuplicateContentAnalysisStarted
- JobQueued

Background execution SHALL additionally publish:

- DuplicateContentAnalysisCompleted

Upon failure:

- DuplicateContentAnalysisFailed

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

Duplicate analysis SHALL execute outside the transaction.

---

# 13. Authorization

The caller SHALL possess permission to analyze the selected object.

---

# 14. Performance Requirements

Command execution SHOULD complete within 30 milliseconds.

The command SHALL NOT wait for analysis completion.

---

# 15. Thread Safety

Only one duplicate-content analysis MAY exist for the same target.

Independent targets MAY be analyzed concurrently.

---

# 16. AI Implementation Rules

AI-generated implementations SHALL:

- analyze persisted textual content only;
- never modify Project data;
- calculate similarity scores deterministically;
- produce recommendations only;
- execute asynchronously;
- publish lifecycle events only after successful transaction completion.

---

# 17. Sequence

```text
GUI
 │
 ▼
AnalyzeDuplicateContentCommand
 │
 ▼
CommandBus
 │
 ▼
AnalyzeDuplicateContentCommandHandler
 │
 ▼
AnalysisService
 │
 ├── Collect Text
 │
 ├── Normalize Content
 │
 ├── Compare Fragments
 │
 ├── Calculate Similarity
 │
 ├── Build Duplicate Report
 │
 ▼
JobQueued Event
 │
 ▼
Background Worker
 │
 ▼
DuplicateContentAnalysisCompleted
```

---

# 18. Compliance Checklist

The implementation conforms to this specification only if it:

- analyzes persisted textual content only;
- detects exact and near duplicates;
- calculates similarity scores;
- never modifies Project data;
- creates exactly one Analysis Job;
- executes asynchronously;
- publishes DuplicateContentAnalysisStarted after successful completion.

---

End of Document