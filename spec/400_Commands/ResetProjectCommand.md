# Voxarium Software Architecture Specification

Document Path:

spec/400_Commands/ResetProjectCommand.md

Document ID: CMD-071

Title: ResetProjectCommand

Version: 1.0.0

Status: Accepted

Classification: Normative

Depends On

- Project
- Reset_Service
- Backup_Service
- Validation_Service
- Command_Model
- Command_Bus

Referenced By

- Maintenance_Service
- Workflow_Engine
- User_Interface_Architecture

---

# 1. Purpose

ResetProjectCommand requests restoration of a Project to its initial logical state.

The command SHALL remove all generated and derived artifacts while preserving the original user-authored Project content.

The command SHALL preserve repository consistency.

---

# 2. Responsibility

Execution SHALL be performed by ResetProjectCommandHandler.

The handler SHALL create a Reset Job and submit it to the Reset Service.

---

# 3. Command Definition

## Name

ResetProjectCommand

## Category

Administration Commands

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

### ResetMode

Type

Enumeration

Allowed values:

- GeneratedDataOnly
- DerivedData
- FullReset

Default:

GeneratedDataOnly

---

### CreateBackup

Type

Boolean

Default:

true

---

### ValidateAfterReset

Type

Boolean

Default:

true

---

### RemoveGeneratedAudio

Type

Boolean

Default:

true

---

### RemoveCaches

Type

Boolean

Default:

true

---

### RemoveAnalysisResults

Type

Boolean

Default:

true

---

### DryRun

Type

Boolean

Default:

false

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
- Reset Service is unavailable;
- another Reset Job is already active for the Project.

Validation SHALL complete before execution begins.

---

# 6. Execution Rules

Execution SHALL:

1. Load the Project Aggregate.
2. Build a Reset Plan.
3. Create a Reset Job.
4. Register the Job with the Reset Service.
5. Publish lifecycle events.

Execution SHALL complete immediately.

Reset SHALL execute asynchronously.

---

# 7. Reset Rules

The reset process MAY remove:

- generated audio;
- cached files;
- temporary artifacts;
- generated previews;
- search indexes;
- analysis results;
- optimization results;
- derived metadata.

The reset process SHALL preserve:

- Project;
- Documents;
- Fragments;
- Roles;
- Voice Profiles;
- Pronunciation Dictionaries;
- Generation Presets;
- user-authored metadata.

When `DryRun` is enabled, no modifications SHALL be performed.

When `CreateBackup` is enabled, a verified backup SHALL be created before reset.

If `ValidateAfterReset` is enabled, a Validation Job SHALL be scheduled after completion.

---

# 8. Result

Successful execution SHALL return:

ResetProjectResult

The result SHALL contain:

- JobId
- ProjectId
- ResetMode
- RemovedArtifacts
- ReclaimedStorageBytes

---

# 9. Published Events

Successful execution SHALL publish:

- ProjectResetStarted
- JobQueued

Background execution SHALL additionally publish:

- ProjectResetCompleted

If validation is enabled:

- ProjectValidationStarted

Upon failure:

- ProjectResetFailed

---

# 10. Error Conditions

Execution MAY fail with:

- ProjectNotFound
- ResetServiceUnavailable
- ResetAlreadyRunning
- ValidationFailed
- InternalError

---

# 11. Idempotency

Submitting an identical reset request while an equivalent Reset Job is active SHALL return the existing Job.

Duplicate Reset Jobs SHALL NOT be created.

Repeated execution SHALL remove only artifacts created after the previous reset.

---

# 12. Transaction Requirements

The transaction SHALL include:

- Reset Job creation;
- queue registration.

Reset SHALL execute outside the transaction.

Repository consistency SHALL be maintained throughout execution.

---

# 13. Authorization

The caller SHALL possess permission to administer the Project.

---

# 14. Performance Requirements

Command execution SHOULD complete within 30 milliseconds.

The command SHALL NOT wait for reset completion.

---

# 15. Thread Safety

Only one Reset Job MAY exist for the same Project.

Different Projects MAY be reset concurrently.

---

# 16. AI Implementation Rules

AI-generated implementations SHALL:

- remove only generated or derived artifacts;
- never modify user-authored content;
- support DryRun mode;
- create backups before reset when requested;
- execute asynchronously;
- publish lifecycle events only after successful transaction completion.

---

# 17. Sequence

```text
GUI
 │
 ▼
ResetProjectCommand
 │
 ▼
CommandBus
 │
 ▼
ResetProjectCommandHandler
 │
 ▼
ResetService
 │
 ├── Build Reset Plan
 │
 ├── Create Backup (optional)
 │
 ├── Queue Job
 │
 ▼
JobQueued Event
 │
 ▼
Background Worker
 │
 ▼
Remove Generated Data
 │
 │
 ├── Validate Project
 │
 ▼
ProjectResetCompleted
```

---

# 18. Compliance Checklist

The implementation conforms to this specification only if it:

- removes only generated or derived artifacts;
- preserves all user-authored entities;
- supports DryRun mode;
- optionally creates a backup before reset;
- creates exactly one Reset Job;
- executes asynchronously;
- publishes ProjectResetStarted after successful transaction completion.

---

End of Document