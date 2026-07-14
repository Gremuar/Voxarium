# Voxarium Software Architecture Specification

Document Path:

spec/400_Commands/RestoreProjectCommand.md

Document ID: CMD-065

Title: RestoreProjectCommand

Version: 1.0.0

Status: Accepted

Classification: Normative

Depends On

- Project
- Backup_Service
- Restore_Service
- Storage_Service
- Command_Model
- Command_Bus

Referenced By

- Backup_Service
- Maintenance_Service
- Workflow_Engine
- User_Interface_Architecture

---

# 1. Purpose

RestoreProjectCommand requests restoration of a Project from a previously created backup.

The command SHALL reconstruct the complete persisted Project state.

The command SHALL preserve repository consistency throughout the restore process.

---

# 2. Responsibility

Execution SHALL be performed by RestoreProjectCommandHandler.

The handler SHALL create a Restore Job and submit it to the Restore Service.

---

# 3. Command Definition

## Name

RestoreProjectCommand

## Category

Administration Commands

## Layer

Application

---

# 4. Parameters

## Required

### BackupLocation

Type

Path

Location of the backup archive.

---

### TargetProjectId

Type

Identifier

Identifier of the Project to restore.

---

## Optional

### RestoreMode

Type

Enumeration

Allowed values:

- Replace
- Merge
- CreateCopy

Default:

Replace

---

### VerifyBackup

Type

Boolean

Default:

true

---

### ValidateAfterRestore

Type

Boolean

Default:

true

---

### RestoreGeneratedAudio

Type

Boolean

Default:

true

---

### RestoreCaches

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

- backup does not exist;
- backup is corrupted;
- Backup Service is unavailable;
- Restore Service is unavailable;
- another Restore Job for the same Project is already active.

Validation SHALL complete before execution begins.

---

# 6. Execution Rules

Execution SHALL:

1. Validate the backup.
2. Build a Restore Plan.
3. Create a Restore Job.
4. Register the Job with the Restore Service.
5. Publish lifecycle events.

Execution SHALL complete immediately.

Restoration SHALL execute asynchronously.

---

# 7. Restore Rules

The restore process SHALL restore:

- Project metadata;
- Documents;
- Fragments;
- Roles;
- Voice Profiles;
- Generation Presets;
- Pronunciation Dictionaries;
- Timeline;
- configuration data.

Generated audio SHALL be restored only when requested.

Temporary files SHALL NOT be restored.

Repository consistency SHALL be preserved at every stage.

Partial restoration SHALL NOT leave the Project in an inconsistent state.

---

# 8. Result

Successful execution SHALL return:

RestoreProjectResult

The result SHALL contain:

- JobId
- TargetProjectId
- RestoreMode
- RestoredObjects

---

# 9. Published Events

Successful execution SHALL publish:

- ProjectRestoreStarted
- JobQueued

Background execution SHALL additionally publish:

- ProjectRestoreCompleted

If validation is enabled:

- ProjectValidationStarted

Upon failure:

- ProjectRestoreFailed

---

# 10. Error Conditions

Execution MAY fail with:

- BackupNotFound
- BackupCorrupted
- RestoreServiceUnavailable
- RestoreAlreadyRunning
- ValidationFailed
- InternalError

---

# 11. Idempotency

Submitting an identical restore request while an equivalent Restore Job is active SHALL return the existing Job.

Duplicate Restore Jobs SHALL NOT be created.

---

# 12. Transaction Requirements

The transaction SHALL include:

- Restore Job creation;
- queue registration.

Restore operations SHALL execute outside the transaction.

Repository updates SHALL become visible atomically.

---

# 13. Authorization

The caller SHALL possess permission to restore Projects.

---

# 14. Performance Requirements

Command execution SHOULD complete within 30 milliseconds.

The command SHALL NOT wait for restoration completion.

---

# 15. Thread Safety

Only one Restore Job MAY exist for the same Project.

Different Projects MAY be restored concurrently.

---

# 16. AI Implementation Rules

AI-generated implementations SHALL:

- validate backups before restoration;
- restore only verified backups;
- preserve repository consistency;
- never expose partially restored state;
- execute asynchronously;
- publish lifecycle events only after successful transaction completion.

---

# 17. Sequence

```text
GUI
 │
 ▼
RestoreProjectCommand
 │
 ▼
CommandBus
 │
 ▼
RestoreProjectCommandHandler
 │
 ▼
RestoreService
 │
 ├── Verify Backup
 │
 ├── Build Restore Plan
 │
 ├── Create Restore Job
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
Restore Project
 │
 │
 ├── Validate Project
 │
 ▼
ProjectRestoreCompleted
```

---

# 18. Compliance Checklist

The implementation conforms to this specification only if it:

- restores only verified backups;
- preserves repository consistency;
- never exposes partially restored data;
- optionally validates the restored Project;
- creates exactly one Restore Job;
- executes asynchronously;
- publishes ProjectRestoreStarted after successful completion.

---

End of Document