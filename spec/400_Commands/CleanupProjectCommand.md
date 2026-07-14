# Voxarium Software Architecture Specification

Document Path:
spec/400_Commands/CleanupProjectCommand.md

Document ID: CMD-062

Title: CleanupProjectCommand

Version: 1.0.0

Status: Accepted

Classification: Normative

Depends On

- Project
- AudioAsset
- TemporaryAsset
- Cache
- Maintenance_Service
- Cleanup_Service
- Command_Model
- Command_Bus

Referenced By

- Maintenance_Service
- Cleanup_Service
- Workflow_Engine
- User_Interface_Architecture

---

# 1. Purpose

CleanupProjectCommand requests removal of obsolete and temporary Project resources.

The command SHALL reclaim storage occupied by non-essential artifacts.

The command SHALL NOT remove business entities.

---

# 2. Responsibility

Execution SHALL be performed by CleanupProjectCommandHandler.

The handler SHALL create a Cleanup Job and submit it to the Maintenance Service.

---

# 3. Command Definition

## Name

CleanupProjectCommand

## Category

Maintenance Commands

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

### CleanupMode

Type

Enumeration

Allowed values:

- Safe
- Standard
- Aggressive

Default:

Standard

---

### RemoveTemporaryFiles

Type

Boolean

Default:

true

---

### RemoveUnusedCaches

Type

Boolean

Default:

true

---

### RemoveOrphanAssets

Type

Boolean

Default:

true

---

### RemoveFailedGenerationArtifacts

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

When enabled, the command SHALL report resources that would be removed without performing cleanup.

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
- Maintenance Service is unavailable;
- an equivalent Cleanup Job is already active.

Validation SHALL complete before execution begins.

---

# 6. Execution Rules

Execution SHALL:

1. Load the Project Aggregate.
2. Build a Cleanup Plan.
3. Identify removable resources.
4. Create a Cleanup Job.
5. Register the Job with the Maintenance Service.
6. Publish lifecycle events.

Execution SHALL complete immediately.

Cleanup SHALL execute asynchronously.

---

# 7. Cleanup Rules

The cleanup process MAY remove:

- temporary files;
- expired caches;
- orphan audio assets;
- abandoned intermediate artifacts;
- failed generation outputs;
- obsolete export artifacts.

The cleanup process SHALL NOT remove:

- Projects;
- Documents;
- Fragments;
- Roles;
- Voice Profiles;
- Pronunciation Dictionaries;
- Generation Presets;
- completed generated audio referenced by the Project.

Resources referenced by any persisted Project entity SHALL NOT be deleted.

When `DryRun` is enabled, no resources SHALL be removed.

---

# 8. Result

Successful execution SHALL return:

CleanupProjectResult

The result SHALL contain:

- JobId
- ProjectId
- CleanupMode
- RemovedItems
- ReclaimedStorageBytes

When `DryRun` is enabled, the result SHALL instead contain the list of removable resources and the estimated storage recovery.

---

# 9. Published Events

Successful execution SHALL publish:

- ProjectCleanupStarted
- JobQueued

Background execution SHALL additionally publish:

- ProjectCleanupCompleted

Upon failure:

- ProjectCleanupFailed

---

# 10. Error Conditions

Execution MAY fail with:

- ProjectNotFound
- MaintenanceServiceUnavailable
- CleanupAlreadyRunning
- ValidationFailed
- InternalError

---

# 11. Idempotency

Submitting an identical cleanup request while an equivalent Cleanup Job is active SHALL return the existing Job.

Duplicate Cleanup Jobs SHALL NOT be created.

Repeated execution after a successful cleanup SHALL remove only resources created after the previous cleanup.

---

# 12. Transaction Requirements

The transaction SHALL include:

- Cleanup Job creation;
- queue registration.

Cleanup SHALL execute outside the transaction.

---

# 13. Authorization

The caller SHALL possess permission to maintain the Project.

---

# 14. Performance Requirements

Command execution SHOULD complete within 30 milliseconds.

The command SHALL NOT wait for cleanup completion.

---

# 15. Thread Safety

Only one Cleanup Job MAY exist for the same Project.

Different Projects MAY be cleaned concurrently.

---

# 16. AI Implementation Rules

AI-generated implementations SHALL:

- identify removable resources before deletion;
- never delete resources referenced by persisted Project entities;
- honor DryRun mode;
- execute asynchronously;
- publish lifecycle events only after successful transaction completion.

---

# 17. Sequence

```text
GUI
 │
 ▼
CleanupProjectCommand
 │
 ▼
CommandBus
 │
 ▼
CleanupProjectCommandHandler
 │
 ▼
MaintenanceService
 │
 ├── Build Cleanup Plan
 │
 ├── Scan Resources
 │
 ├── Create Cleanup Job
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
Delete Temporary Resources
 │
 ▼
ProjectCleanupCompleted
```

---

# 18. Compliance Checklist

The implementation conforms to this specification only if it:

- removes only non-essential resources;
- never deletes persisted business entities;
- respects DryRun mode;
- creates exactly one Cleanup Job;
- executes asynchronously;
- publishes ProjectCleanupStarted after successful completion.

---

End of Document