# Voxarium Software Architecture Specification

Document Path:
spec/400_Commands/AnalyzeLanguageCommand.md

Document ID: CMD-057

Title: AnalyzeLanguageCommand

Version: 1.0.0

Status: Accepted

Classification: Normative

Depends On

- Project
- Document
- Fragment
- LanguageProfile
- Analysis_Service
- AnalysisJob
- Command_Model
- Command_Bus

Referenced By

- Analysis_Service
- Generation_Service
- Workflow_Engine
- User_Interface_Architecture

---

# 1. Purpose

AnalyzeLanguageCommand evaluates language usage within the selected scope.

The command SHALL identify language inconsistencies that may affect speech generation.

The command SHALL NOT modify Project data.

---

# 2. Responsibility

Execution SHALL be performed by AnalyzeLanguageCommandHandler.

The handler SHALL create an Analysis Job and submit it to the Analysis Service.

---

# 3. Command Definition

## Name

AnalyzeLanguageCommand

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

- Fragment
- Document
- Project

---

### TargetId

Type

Identifier

Identifier corresponding to the selected Scope.

---

## Optional

### DetectLanguages

Type

Boolean

Default:

true

---

### ValidateLanguageAssignments

Type

Boolean

Default:

true

---

### DetectMixedLanguageContent

Type

Boolean

Default:

true

---

### DetectUnsupportedLanguages

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

Language analysis SHALL execute asynchronously.

---

# 7. Analysis Rules

The analysis SHALL verify:

- detected language;
- assigned language;
- mixed-language Fragments;
- unsupported languages;
- inconsistent language assignments;
- unexpected language changes;
- language confidence.

Each finding SHALL be classified as:

- Error
- Warning
- Information

The analysis SHALL NOT modify Project entities.

---

# 8. Result

Successful execution SHALL return:

AnalyzeLanguageResult

The result SHALL contain:

- JobId
- Scope
- TargetId
- DetectedLanguages
- Errors
- Warnings
- Information

---

# 9. Published Events

Successful execution SHALL publish:

- LanguageAnalysisStarted
- JobQueued

Background execution SHALL additionally publish:

- LanguageAnalysisCompleted

Upon failure:

- LanguageAnalysisFailed

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

Language analysis SHALL execute outside the transaction.

---

# 13. Authorization

The caller SHALL possess permission to analyze the selected object.

---

# 14. Performance Requirements

Command execution SHOULD complete within 30 milliseconds.

The command SHALL NOT wait for analysis completion.

---

# 15. Thread Safety

Only one active language analysis MAY exist for the same target.

Independent targets MAY be analyzed concurrently.

---

# 16. AI Implementation Rules

AI-generated implementations SHALL:

- analyze persisted textual content only;
- never modify Project entities;
- classify findings as Errors, Warnings and Information;
- execute asynchronously;
- publish lifecycle events only after successful transaction completion.

---

# 17. Sequence

```text
GUI
 │
 ▼
AnalyzeLanguageCommand
 │
 ▼
CommandBus
 │
 ▼
AnalyzeLanguageCommandHandler
 │
 ▼
AnalysisService
 │
 ├── Detect Languages
 │
 ├── Validate Assignments
 │
 ├── Detect Mixed Content
 │
 ├── Validate Support
 │
 ▼
JobQueued Event
 │
 ▼
Background Worker
 │
 ▼
Generate Language Report
 │
 ▼
LanguageAnalysisCompleted
```

---

# 18. Compliance Checklist

The implementation conforms to this specification only if it:

- detects document languages;
- validates language assignments;
- identifies unsupported languages;
- never modifies Project data;
- creates exactly one Analysis Job;
- executes asynchronously;
- publishes LanguageAnalysisStarted after successful completion.

---

End of Document