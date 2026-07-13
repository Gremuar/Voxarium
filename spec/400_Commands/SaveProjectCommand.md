# Voxarium Software Architecture Specification

Document Path:
spec/400_Commands/SaveProjectCommand.md

Document ID: CMD-004

Title: SaveProjectCommand

Version: 1.0.0

Status: Accepted

Classification: Normative

Depends On

- Project
- Project_Service
- Command_Model
- Command_Bus
- Execution_Runtime

Referenced By

- Workflow_Engine
- Use_Case_Handler
- User_Interface_Architecture

---

# 1. Purpose

SaveProjectCommand requests persistence of the current Project state.

The command SHALL ensure that all modified Domain objects are durably written to persistent storage.

The command SHALL NOT modify business data.

---

# 2. Responsibility

Execution SHALL be performed by SaveProjectCommandHandler.

The command coordinates persistence of the current Project.

---

# 3. Command Definition

## Name

SaveProjectCommand

## Category

Project Commands

## Layer

Application

---

# 4. Parameters

## Required

### ProjectId

Type

Identifier

Identifier of the Project to save.

---

## Optional

### SaveMode

Type

Enumeration

Allowed values:

- Incremental
- Full

Default:

Incremental

Incremental mode SHALL persist only modified objects.

Full mode SHALL rewrite the complete Project.

---

### Force

Type

Boolean

Default:

false

Force MAY bypass optimization mechanisms.

Force SHALL NOT bypass validation.

---

# 5. Validation Rules

Execution SHALL fail if:

- Project does not exist;
- Project is not opened;
- Project is already saving;
- Project storage is unavailable.

---

# 6. Execution Rules

Execution SHALL:

1. Validate Project state.
2. Freeze write operations.
3. Flush pending Domain changes.
4. Persist Project metadata.
5. Persist Domain objects.
6. Persist Runtime state required for recovery.
7. Release write lock.

The save operation SHALL be atomic.

No partially saved Project SHALL remain.

---

# 7. Result

Successful execution SHALL return:

SaveProjectResult

The result SHALL contain:

- ProjectId
- SavedObjects
- WrittenBytes
- SaveDuration
- SaveMode

---

# 8. Published Events

Successful execution SHALL publish:

- ProjectSaving
- ProjectSaved

Failed execution SHALL publish:

- ProjectSaveFailed

---

# 9. Error Conditions

Execution MAY fail with:

- ProjectNotOpened
- StorageUnavailable
- SerializationFailed
- WriteFailure
- AccessDenied
- ValidationFailed
- InternalError

---

# 10. Idempotency

Executing SaveProjectCommand repeatedly without intervening modifications SHALL produce identical persistent state.

---

# 11. Transaction Requirements

Persistence SHALL be transactional.

Rollback SHALL restore the previous valid Project state.

---

# 12. Authorization

The caller SHALL possess permission to save the Project.

---

# 13. Performance Requirements

Incremental save SHOULD complete within one second for normally sized Projects.

Full save MAY execute asynchronously for large Projects.

---

# 14. Thread Safety

Only one save operation SHALL execute for a Project simultaneously.

Concurrent modification requests SHALL wait until persistence has completed.

---

# 15. AI Implementation Rules

AI-generated implementations SHALL:

- persist only validated Domain objects;
- guarantee transactional consistency;
- preserve object identities;
- avoid unnecessary serialization;
- publish events only after successful commit.

---

# 16. Sequence

```text
GUI
 │
 ▼
SaveProjectCommand
 │
 ▼
CommandBus
 │
 ▼
SaveProjectCommandHandler
 │
 ▼
ProjectService
 │
 ▼
Serializer
 │
 ▼
Storage
 │
 ▼
ProjectSaved Event
```

---

# 17. Compliance Checklist

The implementation conforms to this specification only if it:

- persists Project atomically;
- preserves Domain consistency;
- supports Incremental and Full save;
- prevents concurrent saves;
- publishes ProjectSaved after successful persistence.

---

End of Document