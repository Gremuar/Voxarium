# Voxarium Software Architecture Specification

Document Path:
spec/400_Commands/AnalyzeConsistencyCommand.md

Document ID: CMD-056

Title: AnalyzeConsistencyCommand

Version: 1.0.0

Status: Accepted

Classification: Normative

Depends On

- Project
- Document
- Fragment
- Role
- VoiceProfile
- GenerationPreset
- PronunciationDictionary
- Analysis_Service
- AnalysisJob
- Command_Model
- Command_Bus

Referenced By

- Analysis_Service
- Workflow_Engine
- Project_Service
- User_Interface_Architecture

---

# 1. Purpose

AnalyzeConsistencyCommand requests validation of logical consistency across a Project.

The command SHALL detect inconsistencies between related Project entities.

The command SHALL NOT modify Project data.

---

# 2. Responsibility

Execution SHALL be performed by AnalyzeConsistencyCommandHandler.

The handler SHALL create an Analysis Job and submit it to the Analysis Service.

---

# 3. Command Definition

## Name

AnalyzeConsistencyCommand

## Category

Analysis Commands

## Layer

Application

---

# 4. Parameters

## Required

### ProjectId

Type

Identifier

Identifier of the Project.

---

## Optional

### ValidateReferences

Type

Boolean

Default:

true

---

### ValidateRoles

Type

Boolean

Default:

true

---

### ValidateVoiceAssignments

Type

Boolean

Default:

true

---

### ValidateGenerationConfiguration

Type

Boolean

Default:

true

---

### ValidatePronunciationDictionaries

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

- Project does not exist;
- Project contains no Documents;
- Analysis Service is unavailable;
- an equivalent Analysis Job is already active.

Validation SHALL complete before execution begins.

---

# 6. Execution Rules

Execution SHALL:

1. Load the Project Aggregate.
2. Collect referenced entities.
3. Build an Analysis Plan.
4. Create an Analysis Job.
5. Register the Job with the Analysis Service.
6. Publish lifecycle events.

Execution SHALL complete immediately.

Consistency analysis SHALL execute asynchronously.

---

# 7. Analysis Rules

The analysis SHALL verify:

- broken references;
- duplicate identifiers;
- invalid Role assignments;
- missing Voice Profiles;
- invalid Generation Presets;
- missing Pronunciation Dictionaries;
- inconsistent language configuration;
- orphan Project objects;
- circular references.

Each finding SHALL be classified as:

- Error
- Warning
- Information

The analysis SHALL NOT modify any Project entity.

---

# 8. Result

Successful execution SHALL return:

AnalyzeConsistencyResult

The result SHALL contain:

- JobId
- ProjectId
- Errors
- Warnings
- Information

---

# 9. Published Events

Successful execution SHALL publish:

- ConsistencyAnalysisStarted
- JobQueued

Background execution SHALL additionally publish:

- ConsistencyAnalysisCompleted

Upon failure:

- ConsistencyAnalysisFailed

---

# 10. Error Conditions

Execution MAY fail with:

- ProjectNotFound
- EmptyProject
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

Consistency analysis SHALL execute outside the transaction.

---

# 13. Authorization

The caller SHALL possess permission to analyze the Project.

---

# 14. Performance Requirements

Command execution SHOULD complete within 30 milliseconds.

The command SHALL NOT wait for analysis completion.

---

# 15. Thread Safety

Only one active consistency analysis MAY exist for the same Project.

Independent Projects MAY be analyzed concurrently.

---

# 16. AI Implementation Rules

AI-generated implementations SHALL:

- validate persisted Project state only;
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
AnalyzeConsistencyCommand
 │
 ▼
CommandBus
 │
 ▼
AnalyzeConsistencyCommandHandler
 │
 ▼
AnalysisService
 │
 ├── Validate References
 │
 ├── Validate Roles
 │
 ├── Validate Voices
 │
 ├── Validate Dictionaries
 │
 ├── Validate Presets
 │
 ▼
JobQueued Event
 │
 ▼
Background Worker
 │
 ▼
Generate Consistency Report
 │
 ▼
ConsistencyAnalysisCompleted
```

---

# 18. Compliance Checklist

The implementation conforms to this specification only if it:

- validates all Project references;
- detects orphan and duplicate entities;
- validates generation configuration;
- never modifies Project data;
- creates exactly one Analysis Job;
- executes asynchronously;
- publishes ConsistencyAnalysisStarted after successful completion.

---

End of Document