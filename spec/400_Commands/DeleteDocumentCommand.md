# Voxarium Software Architecture Specification

Document Path:
spec/400_Commands/DeleteDocumentCommand.md

Document ID: CMD-011

Title: DeleteDocumentCommand

Version: 1.0.0

Status: Accepted

Classification: Normative

Depends On

- Document
- Project
- Fragment
- Command_Model
- Command_Bus

Referenced By

- Document_Service
- Workflow_Engine
- User_Interface_Architecture

---

# 1. Purpose

DeleteDocumentCommand requests permanent removal of a Document from a Project.

The command SHALL remove the Document together with all owned entities.

The command SHALL preserve overall Project consistency.

---

# 2. Responsibility

Execution SHALL be performed by DeleteDocumentCommandHandler.

The handler SHALL completely remove the Document Aggregate.

---

# 3. Command Definition

## Name

DeleteDocumentCommand

## Category

Document Commands

## Layer

Application

---

# 4. Parameters

## Required

### DocumentId

Type

Identifier

Identifier of the Document to delete.

---

## Optional

### DeleteGeneratedAssets

Type

Boolean

Default:

true

When enabled, all generated audio and intermediate artifacts belonging to the Document SHALL be removed.

---

# 5. Validation Rules

Execution SHALL fail if:

- Document does not exist;
- Document is locked;
- Document participates in an active Workflow;
- Document is currently being generated;
- caller lacks required permissions.

---

# 6. Execution Rules

Execution SHALL:

1. Validate Document state.
2. Cancel active Jobs associated with the Document.
3. Remove Timeline references.
4. Remove Fragment hierarchy.
5. Remove generated SpeechSegments.
6. Remove generated Assets.
7. Remove the Document.
8. Update search indexes.

Execution SHALL be atomic.

Partial deletion SHALL NOT occur.

---

# 7. Result

Successful execution SHALL return:

DeleteDocumentResult

The result SHALL contain:

- DocumentId
- RemovedFragments
- RemovedSpeechSegments
- RemovedAssets
- ReleasedStorage
- Duration

---

# 8. Published Events

Successful execution SHALL publish:

- DocumentDeleting
- DocumentDeleted

When background Jobs are cancelled:

- JobCancelled

When indexes are updated:

- SearchIndexUpdated

---

# 9. Error Conditions

Execution MAY fail with:

- DocumentNotFound
- DocumentLocked
- WorkflowRunning
- GenerationRunning
- ValidationFailed
- StorageFailure
- InternalError

---

# 10. Idempotency

The command is NOT idempotent.

Deleting an already deleted Document SHALL return DocumentNotFound.

---

# 11. Transaction Requirements

Deletion SHALL either:

- remove the complete Document Aggregate,

or

- leave the Project unchanged.

Rollback SHALL restore the previous valid state.

---

# 12. Authorization

The caller SHALL possess permission to modify the owning Project.

Deletion SHOULD require explicit user confirmation.

---

# 13. Performance Requirements

Deletion of medium-sized Documents SHOULD complete within one second.

Deletion of large generated Assets MAY continue asynchronously after the transaction has completed.

Progress SHALL be observable.

---

# 14. Thread Safety

Only one DeleteDocumentCommand SHALL execute for a Document.

Concurrent modification requests SHALL be rejected while deletion is in progress.

---

# 15. AI Implementation Rules

AI-generated implementations SHALL:

- treat Document as an Aggregate Root;
- remove owned entities before removing the aggregate itself;
- preserve referential integrity;
- remove orphaned Assets;
- rebuild affected search indexes;
- publish events only after successful transaction completion.

---

# 16. Sequence

```text
GUI
 │
 ▼
DeleteDocumentCommand
 │
 ▼
CommandBus
 │
 ▼
DeleteDocumentCommandHandler
 │
 ▼
DocumentService
 │
 ├── Cancel Jobs
 │
 ├── Remove Timeline References
 │
 ├── Delete Fragments
 │
 ├── Delete SpeechSegments
 │
 ├── Delete Assets
 │
 ▼
Repository
 │
 ▼
DocumentDeleted Event
```

---

# 17. Compliance Checklist

The implementation conforms to this specification only if it:

- removes the complete Document Aggregate;
- preserves Project consistency;
- removes dependent entities;
- removes generated Assets;
- updates search indexes;
- publishes DocumentDeleted only after successful completion.

---

End of Document