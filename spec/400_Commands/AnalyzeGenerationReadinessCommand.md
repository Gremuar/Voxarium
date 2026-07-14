# Voxarium Software Architecture Specification

Document Path:
spec/400_Commands/AnalyzeGenerationReadinessCommand.md

Document ID: CMD-054

Title: AnalyzeGenerationReadinessCommand

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

- Generation_Service
- Workflow_Engine
- User_Interface_Architecture

---

# 1. Purpose

AnalyzeGenerationReadinessCommand evaluates whether a Project is ready for speech generation.

The command SHALL identify configuration issues preventing successful generation.

The command SHALL NOT modify Project data.

---

# 2. Responsibility

Execution SHALL be performed by AnalyzeGenerationReadinessCommandHandler.

The handler SHALL create an Analysis Job and submit it to the Analysis Service.

---

# 3. Command Definition

## Name

AnalyzeGenerationReadinessCommand

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

### ValidateRoles

Type

Boolean

Default:

true

---

### ValidateVoices

Type

Boolean

Default:

true

---

### ValidatePronunciation

Type

Boolean

Default:

true

---

### ValidateFragments

Type

Boolean

Default:

true

---

### ValidateGenerationPresets

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
2. Validate Project integrity.
3. Build a readiness validation plan.
4. Create an Analysis Job.
5. Register the Job with the Analysis Service.
6. Publish lifecycle events.

Execution SHALL complete immediately.

Analysis SHALL execute asynchronously.

---

# 7. Analysis Rules

The analysis SHALL verify:

- every Fragment contains text;
- every speaking Fragment has a Role assignment;
- every Role has a Voice Profile;
- referenced Voice Profiles exist;
- Generation Presets are valid;
- Pronunciation Dictionaries are available;
- unsupported languages are detected;
- Documents are internally consistent.

The analysis SHALL classify every finding as:

- Error
- Warning
- Information

The command SHALL NOT modify any Project object.

---

# 8. Result

Successful execution SHALL return:

AnalyzeGenerationReadinessResult

The result SHALL contain:

- JobId
- ProjectId
- ReadinessStatus
- Errors
- Warnings
- Information

---

# 9. Published Events

Successful execution SHALL publish:

- GenerationReadinessAnalysisStarted
- JobQueued

Background execution SHALL additionally publish:

- GenerationReadinessAnalysisCompleted

Upon failure:

- GenerationReadinessAnalysisFailed

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

Readiness analysis SHALL execute outside the transaction.

---

# 13. Authorization

The caller SHALL possess permission to analyze the Project.

---

# 14. Performance Requirements

Command execution SHOULD complete within 30 milliseconds.

The command SHALL NOT wait for analysis completion.

---

# 15. Thread Safety

Only one readiness analysis MAY exist for the same Project.

Independent Projects MAY be analyzed concurrently.

---

# 16. AI Implementation Rules

AI-generated implementations SHALL:

- validate only persisted Project state;
- never modify Project data;
- classify findings as Errors, Warnings or Information;
- execute asynchronously;
- publish lifecycle events only after successful transaction completion.

---

# 17. Sequence

```text
GUI
 │
 ▼
AnalyzeGenerationReadinessCommand
 │
 ▼
CommandBus
 │
 ▼
AnalyzeGenerationReadinessCommandHandler
 │
 ▼
AnalysisService
 │
 ├── Validate Project
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
Generate Readiness Report
 │
 ▼
GenerationReadinessAnalysisCompleted
```

---

# 18. Compliance Checklist

The implementation conforms to this specification only if it:

- validates every Document;
- validates every speaking Fragment;
- validates Role and Voice assignments;
- never modifies Project data;
- creates exactly one Analysis Job;
- executes asynchronously;
- publishes GenerationReadinessAnalysisStarted after successful completion.

---

End of Document