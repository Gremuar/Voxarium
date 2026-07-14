# Voxarium Software Architecture Specification

Document Path:
spec/400_Commands/RebuildProjectIndexCommand.md

Document ID: CMD-059

Title: RebuildProjectIndexCommand

Version: 1.0.0

Status: Accepted

Classification: Normative

Depends On

- Project
- Document
- Fragment
- Index_Service
- Maintenance_Service
- Command_Model
- Command_Bus

Referenced By

- Maintenance_Service
- Index_Service
- Workflow_Engine
- User_Interface_Architecture

---

# 1. Purpose

RebuildProjectIndexCommand requests rebuilding every searchable index associated with a Project.

The command SHALL regenerate internal indexes from persisted Project data.

The command SHALL NOT modify business entities.

---

# 2. Responsibility

Execution SHALL be performed by RebuildProjectIndexCommandHandler.

The handler SHALL schedule an Index Rebuild Job.

---

# 3. Command Definition

## Name

RebuildProjectIndexCommand

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

### RebuildMode

Type

Enumeration

Allowed values:

- Incremental
- Full

Default:

Incremental

---

### IncludeSearchIndex

Type

Boolean

Default:

true

---

### IncludeFragmentIndex

Type

Boolean

Default:

true

---

### IncludeStatisticsIndex

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
- Maintenance Service is unavailable;
- Index Service is unavailable;
- another rebuild job for the same Project is already active.

Validation SHALL complete before execution begins.

---

# 6. Execution Rules

Execution SHALL:

1. Load the Project Aggregate.
2. Build an index rebuild plan.
3. Create a Maintenance Job.
4. Register the job with the Maintenance Service.
5. Publish lifecycle events.

Execution SHALL complete immediately.

Index rebuilding SHALL execute asynchronously.

---

# 7. Rebuild Rules

The rebuild process SHALL regenerate:

- search indexes;
- Fragment indexes;
- lookup indexes;
- statistics indexes;
- navigation indexes.

The rebuild SHALL use only persisted Project state.

Existing indexes MAY be replaced atomically.

The command SHALL NOT modify:

- Documents;
- Fragments;
- Roles;
- Voice Profiles;
- Generation Presets;
- Pronunciation Dictionaries.

---

# 8. Result

Successful execution SHALL return:

RebuildProjectIndexResult

The result SHALL contain:

- JobId
- ProjectId
- RebuildMode

---

# 9. Published Events

Successful execution SHALL publish:

- ProjectIndexRebuildStarted
- JobQueued

Background execution SHALL additionally publish:

- ProjectIndexRebuildCompleted

Upon failure:

- ProjectIndexRebuildFailed

---

# 10. Error Conditions

Execution MAY fail with:

- ProjectNotFound
- MaintenanceServiceUnavailable
- IndexServiceUnavailable
- RebuildAlreadyRunning
- ValidationFailed
- InternalError

---

# 11. Idempotency

Submitting an identical rebuild request while an equivalent Maintenance Job is active SHALL return the existing Job.

Duplicate rebuild jobs SHALL NOT be created.

---

# 12. Transaction Requirements

The transaction SHALL include:

- Maintenance Job creation;
- queue registration.

Index rebuilding SHALL execute outside the transaction.

---

# 13. Authorization

The caller SHALL possess permission to maintain the Project.

---

# 14. Performance Requirements

Command execution SHOULD complete within 30 milliseconds.

The command SHALL NOT wait for rebuild completion.

---

# 15. Thread Safety

Only one rebuild job MAY exist for the same Project.

Different Projects MAY rebuild indexes concurrently.

---

# 16. AI Implementation Rules

AI-generated implementations SHALL:

- rebuild indexes only from persisted Project data;
- replace indexes atomically whenever possible;
- never modify business entities;
- execute asynchronously;
- publish lifecycle events only after successful transaction completion.

---

# 17. Sequence

```text
GUI
 │
 ▼
RebuildProjectIndexCommand
 │
 ▼
CommandBus
 │
 ▼
RebuildProjectIndexCommandHandler
 │
 ▼
MaintenanceService
 │
 ├── Build Rebuild Plan
 │
 ├── Create Maintenance Job
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
Rebuild Indexes
 │
 ▼
ProjectIndexRebuildCompleted
```

---

# 18. Compliance Checklist

The implementation conforms to this specification only if it:

- rebuilds indexes from persisted data only;
- never modifies business entities;
- creates exactly one Maintenance Job;
- executes asynchronously;
- replaces indexes atomically;
- publishes ProjectIndexRebuildStarted after successful completion.

---

End of Document