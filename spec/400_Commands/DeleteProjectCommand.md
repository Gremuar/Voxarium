# Voxarium Software Architecture Specification

Document Path:
spec/400_Commands/DeleteProjectCommand.md

Document ID: CMD-006

Title: DeleteProjectCommand

Version: 1.0.0

Status: Accepted

Classification: Normative

Depends On

- Project
- Project_Service
- Command_Model
- Command_Bus

Referenced By

- Workflow_Engine
- Use_Case_Handler
- User_Interface_Architecture

---

# 1. Purpose

DeleteProjectCommand requests permanent deletion of a Project.

Deletion SHALL remove the Project from persistent storage.

The command SHALL NOT perform partial deletion.

---

# 2. Responsibility

Execution SHALL be performed by DeleteProjectCommandHandler.

The handler SHALL ensure safe and irreversible removal of the Project.

---

# 3. Command Definition

## Name

DeleteProjectCommand

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

Identifier of the Project to delete.

---

## Optional

### DeleteFiles

Type

Boolean

Default:

true

If true, the Project directory SHALL be removed.

If false, only the Project registration SHALL be removed.

---

### Force

Type

Boolean

Default:

false

If enabled, active Jobs MAY be cancelled before deletion.

Force SHALL NOT bypass integrity validation.

---

# 5. Validation Rules

Execution SHALL fail if:

- Project does not exist;
- Project is currently locked;
- Project contains active transactions;
- caller lacks sufficient permissions.

---

# 6. Execution Rules

Execution SHALL perform the following steps:

1. Validate Project state.
2. Cancel active background Jobs.
3. Close the Project if it is currently opened.
4. Remove Project metadata.
5. Remove Project files.
6. Release Runtime resources.
7. Remove search indexes.
8. Remove cached artifacts.

Execution SHALL be atomic from the Application perspective.

---

# 7. Result

Successful execution SHALL return:

DeleteProjectResult

The result SHALL contain:

- ProjectId
- DeletedFiles
- ReleasedStorage
- DeletedAssets
- Duration

---

# 8. Published Events

Successful execution SHALL publish:

- ProjectDeleting
- ProjectDeleted

If cancellation of Jobs was required:

- JobCancelled

Failed execution SHALL publish:

- ProjectDeletionFailed

---

# 9. Error Conditions

Execution MAY fail with:

- ProjectNotFound
- ProjectLocked
- AccessDenied
- StorageFailure
- ActiveTransactionExists
- InternalError

---

# 10. Idempotency

Deleting an already deleted Project SHALL return ProjectNotFound.

The command is NOT idempotent.

---

# 11. Transaction Requirements

Either:

- the complete Project SHALL be deleted,

or

- no persistent changes SHALL occur.

Partial deletion SHALL NOT occur.

---

# 12. Authorization

The caller SHALL possess permission to delete Projects.

Deletion SHOULD require explicit user confirmation.

---

# 13. Performance Requirements

Deletion of Project metadata SHOULD complete within one second.

Removal of large Asset directories MAY continue asynchronously.

Progress SHALL be reportable.

---

# 14. Thread Safety

Only one deletion operation SHALL execute for a Project.

Concurrent modification requests SHALL be rejected.

---

# 15. AI Implementation Rules

AI-generated implementations SHALL:

- verify the Project before deletion;
- release all Runtime resources before removing storage;
- remove search indexes and caches;
- never leave orphaned files;
- publish ProjectDeleted only after successful completion.

---

# 16. Sequence

```text
GUI
 │
 ▼
DeleteProjectCommand
 │
 ▼
CommandBus
 │
 ▼
DeleteProjectCommandHandler
 │
 ▼
ProjectService
 │
 ├── Stop Runtime
 │
 ├── Cancel Jobs
 │
 ├── Delete Metadata
 │
 ├── Delete Assets
 │
 └── Delete Project Files
 │
 ▼
ProjectDeleted Event
```

---

# 17. Compliance Checklist

The implementation conforms to this specification only if it:

- validates Project state before deletion;
- removes all persistent Project data;
- releases Runtime resources;
- removes search indexes and caches;
- never leaves orphaned metadata;
- publishes ProjectDeleted after successful completion.

---

End of Document