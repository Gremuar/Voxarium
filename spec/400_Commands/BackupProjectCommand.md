# Voxarium Software Architecture Specification

Document Path:
spec/400_Commands/BackupProjectCommand.md

Document ID: CMD-064

Title: BackupProjectCommand

Version: 1.0.0

Status: Accepted

Classification: Normative

Depends On

- Project
- Backup_Service
- Storage_Service
- Command_Model
- Command_Bus

Referenced By

- Backup_Service
- Workflow_Engine
- User_Interface_Architecture

---

# 1. Purpose

BackupProjectCommand requests creation of a complete backup of a Project.

The command SHALL create a consistent snapshot of all persisted Project data.

The command SHALL NOT modify Project contents.

---

# 2. Responsibility

Execution SHALL be performed by BackupProjectCommandHandler.

The handler SHALL create a Backup Job and submit it to the Backup Service.

---

# 3. Command Definition

## Name

BackupProjectCommand

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

### Destination

Type

Path

Destination where the backup SHALL be stored.

---

## Optional

### BackupFormat

Type

Enumeration

Allowed values:

- Native
- ZIP
- TAR
- TAR_GZ

Default:

Native

---

### IncludeGeneratedAudio

Type

Boolean

Default:

true

---

### IncludeCaches

Type

Boolean

Default:

false

---

### IncludeLogs

Type

Boolean

Default:

false

---

### VerifyBackup

Type

Boolean

Default:

true

---

### CompressionLevel

Type

Enumeration

Allowed values:

- None
- Fast
- Normal
- Maximum

Default:

Normal

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
- Destination is unavailable;
- Backup Service is unavailable;
- Storage Service is unavailable;
- an equivalent Backup Job is already active.

Validation SHALL complete before execution begins.

---

# 6. Execution Rules

Execution SHALL:

1. Load the Project Aggregate.
2. Build a Backup Plan.
3. Create a Backup Job.
4. Register the Job with the Backup Service.
5. Publish lifecycle events.

Execution SHALL complete immediately.

Backup creation SHALL execute asynchronously.

---

# 7. Backup Rules

The backup SHALL include:

- Project metadata;
- Documents;
- Fragments;
- Roles;
- Voice Profiles;
- Generation Presets;
- Pronunciation Dictionaries;
- Timeline data;
- Project configuration.

Generated audio SHALL be included only when `IncludeGeneratedAudio` is enabled.

Temporary files SHALL NOT be included.

The backup SHALL represent a consistent Project snapshot.

Project data SHALL remain unchanged.

---

# 8. Result

Successful execution SHALL return:

BackupProjectResult

The result SHALL contain:

- JobId
- ProjectId
- BackupLocation
- BackupFormat
- BackupSize

---

# 9. Published Events

Successful execution SHALL publish:

- ProjectBackupStarted
- JobQueued

Background execution SHALL additionally publish:

- ProjectBackupCompleted

If verification is enabled:

- ProjectBackupVerified

Upon failure:

- ProjectBackupFailed

---

# 10. Error Conditions

Execution MAY fail with:

- ProjectNotFound
- DestinationUnavailable
- BackupServiceUnavailable
- StorageServiceUnavailable
- BackupAlreadyRunning
- ValidationFailed
- InternalError

---

# 11. Idempotency

Submitting an identical backup request while an equivalent Backup Job is active SHALL return the existing Job.

Duplicate Backup Jobs SHALL NOT be created.

---

# 12. Transaction Requirements

The transaction SHALL include:

- Backup Job creation;
- queue registration.

Backup generation SHALL execute outside the transaction.

---

# 13. Authorization

The caller SHALL possess permission to back up the Project.

---

# 14. Performance Requirements

Command execution SHOULD complete within 30 milliseconds.

The command SHALL NOT wait for backup completion.

---

# 15. Thread Safety

Only one Backup Job MAY exist for the same Project.

Different Projects MAY be backed up concurrently.

---

# 16. AI Implementation Rules

AI-generated implementations SHALL:

- create consistent Project snapshots;
- never modify Project data;
- exclude temporary resources;
- optionally verify the resulting backup;
- execute asynchronously;
- publish lifecycle events only after successful transaction completion.

---

# 17. Sequence

```text
GUI
 │
 ▼
BackupProjectCommand
 │
 ▼
CommandBus
 │
 ▼
BackupProjectCommandHandler
 │
 ▼
BackupService
 │
 ├── Build Backup Plan
 │
 ├── Create Backup Job
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
Create Project Snapshot
 │
 ▼
Compress Archive
 │
 ▼
Verify Backup
 │
 ▼
ProjectBackupCompleted
```

---

# 18. Compliance Checklist

The implementation conforms to this specification only if it:

- creates a consistent Project snapshot;
- never modifies Project data;
- excludes temporary resources;
- optionally verifies the backup;
- creates exactly one Backup Job;
- executes asynchronously;
- publishes ProjectBackupStarted after successful completion.

---

End of Document