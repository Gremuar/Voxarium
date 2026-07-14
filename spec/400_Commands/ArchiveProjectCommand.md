# Voxarium Software Architecture Specification

Document Path:

spec/400_Commands/ArchiveProjectCommand.md

Document ID: CMD-072

Title: ArchiveProjectCommand

Version: 1.0.0

Status: Accepted

Classification: Normative

Depends On

- Project
- Archive_Service
- Storage_Service
- Backup_Service
- Command_Model
- Command_Bus

Referenced By

- Archive_Service
- Workflow_Engine
- User_Interface_Architecture

---

# 1. Purpose

ArchiveProjectCommand requests moving a Project into archived state.

The command SHALL preserve all Project data while making the Project read-only.

Archived Projects SHALL remain restorable.

---

# 2. Responsibility

Execution SHALL be performed by ArchiveProjectCommandHandler.

The handler SHALL create an Archive Job and submit it to the Archive Service.

---

# 3. Command Definition

## Name

ArchiveProjectCommand

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

### ArchiveLocation

Type

Path

Optional destination for archived Project storage.

---

### CreateBackup

Type

Boolean

Default:

true

---

### CompressArchive

Type

Boolean

Default:

true

---

### VerifyArchive

Type

Boolean

Default:

true

---

### RetainSearchIndexes

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
- Project is already archived;
- Archive Service is unavailable;
- Storage Service is unavailable;
- another Archive Job is already active.

Validation SHALL complete before execution begins.

---

# 6. Execution Rules

Execution SHALL:

1. Load the Project Aggregate.
2. Build an Archive Plan.
3. Create an Archive Job.
4. Register the Job with the Archive Service.
5. Publish lifecycle events.

Execution SHALL complete immediately.

Archiving SHALL execute asynchronously.

---

# 7. Archive Rules

The archive process SHALL:

- preserve all Project entities;
- preserve all identifiers;
- preserve generated audio;
- preserve configuration;
- preserve metadata.

The archive process SHALL:

- mark the Project as archived;
- prohibit modifications;
- optionally compress archived data;
- optionally verify archive integrity.

No Project data SHALL be deleted.

Archived Projects SHALL remain eligible for restoration.

---

# 8. Result

Successful execution SHALL return:

ArchiveProjectResult

The result SHALL contain:

- JobId
- ProjectId
- ArchiveLocation
- ArchiveSize
- ArchiveTimestamp

---

# 9. Published Events

Successful execution SHALL publish:

- ProjectArchiveStarted
- JobQueued

Background execution SHALL additionally publish:

- ProjectArchived

If verification is enabled:

- ProjectArchiveVerified

Upon failure:

- ProjectArchiveFailed

---

# 10. Error Conditions

Execution MAY fail with:

- ProjectNotFound
- ProjectAlreadyArchived
- ArchiveServiceUnavailable
- StorageUnavailable
- ArchiveAlreadyRunning
- ValidationFailed
- InternalError

---

# 11. Idempotency

Submitting an identical archive request while an equivalent Archive Job is active SHALL return the existing Job.

Archiving an already archived Project SHALL NOT create another archive.

---

# 12. Transaction Requirements

The transaction SHALL include:

- Archive Job creation;
- queue registration.

Archive creation SHALL execute outside the transaction.

Archived state SHALL become visible atomically.

---

# 13. Authorization

The caller SHALL possess permission to archive Projects.

---

# 14. Performance Requirements

Command execution SHOULD complete within 30 milliseconds.

The command SHALL NOT wait for archive completion.

---

# 15. Thread Safety

Only one Archive Job MAY exist for the same Project.

Different Projects MAY be archived concurrently.

---

# 16. AI Implementation Rules

AI-generated implementations SHALL:

- preserve every persisted Project entity;
- never modify user-authored content;
- optionally compress archived data;
- optionally verify archive integrity;
- execute asynchronously;
- publish lifecycle events only after successful transaction completion.

---

# 17. Sequence

```text
GUI
 │
 ▼
ArchiveProjectCommand
 │
 ▼
CommandBus
 │
 ▼
ArchiveProjectCommandHandler
 │
 ▼
ArchiveService
 │
 ├── Build Archive Plan
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
Archive Project
 │
 │
 ├── Compress Archive
 │
 ├── Verify Archive
 │
 ▼
ProjectArchived
```

---

# 18. Compliance Checklist

The implementation conforms to this specification only if it:

- preserves all persisted Project data;
- never modifies user-authored content;
- marks the Project as archived;
- optionally compresses and verifies the archive;
- creates exactly one Archive Job;
- executes asynchronously;
- publishes ProjectArchiveStarted after successful completion.

---

End of Document