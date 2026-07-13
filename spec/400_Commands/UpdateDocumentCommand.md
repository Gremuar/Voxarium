# Voxarium Software Architecture Specification

Document Path:
spec/400_Commands/UpdateDocumentCommand.md

Document ID: CMD-012

Title: UpdateDocumentCommand

Version: 1.0.0

Status: Accepted

Classification: Normative

Depends On

- Document
- Project
- Command_Model
- Command_Bus

Referenced By

- Document_Service
- Workflow_Engine
- User_Interface_Architecture

---

# 1. Purpose

UpdateDocumentCommand requests modification of a Document.

The command SHALL modify only Document properties.

The command SHALL NOT directly modify Fragment content.

---

# 2. Responsibility

Execution SHALL be performed by UpdateDocumentCommandHandler.

The handler SHALL validate and apply changes to the Document aggregate.

---

# 3. Command Definition

## Name

UpdateDocumentCommand

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

Identifier of the Document.

---

### Changes

Type

DocumentChangeSet

Contains the set of modifications to apply.

The ChangeSet SHALL contain only modified properties.

---

## Optional

### ValidateOnly

Type

Boolean

Default:

false

If enabled, the command SHALL perform validation without persisting any changes.

---

# 5. Validation Rules

Execution SHALL fail if:

- Document does not exist;
- Document is locked;
- ChangeSet is empty;
- one or more modified properties are invalid;
- caller lacks sufficient permissions.

Validation SHALL complete before applying changes.

---

# 6. Execution Rules

Execution SHALL:

1. Load the Document aggregate.
2. Validate the ChangeSet.
3. Apply changes.
4. Recalculate derived metadata.
5. Update search indexes if required.
6. Persist the aggregate.
7. Publish lifecycle events.

Execution SHALL be atomic.

---

# 7. Result

Successful execution SHALL return:

UpdateDocumentResult

The result SHALL contain:

- DocumentId
- UpdatedProperties
- Version
- Timestamp

---

# 8. Published Events

Successful execution SHALL publish:

- DocumentUpdated

If search metadata changed:

- SearchIndexUpdated

---

# 9. Error Conditions

Execution MAY fail with:

- DocumentNotFound
- DocumentLocked
- ValidationFailed
- VersionConflict
- StorageFailure
- InternalError

---

# 10. Idempotency

The command is idempotent if the supplied ChangeSet produces no state changes.

Applying the same ChangeSet repeatedly SHALL produce the same Document state.

---

# 11. Transaction Requirements

All modifications SHALL be committed within a single Application transaction.

Rollback SHALL restore the previous Document state.

---

# 12. Authorization

The caller SHALL possess permission to modify the owning Project.

---

# 13. Performance Requirements

Typical execution SHOULD complete within 200 milliseconds.

Search index rebuilding MAY execute asynchronously.

---

# 14. Thread Safety

Concurrent modification of the same Document SHALL be serialized.

Updates to different Documents MAY execute concurrently.

---

# 15. AI Implementation Rules

AI-generated implementations SHALL:

- apply only supplied changes;
- preserve Document identity;
- preserve child entity ownership;
- avoid rewriting unchanged fields;
- publish events only after successful commit.

---

# 16. Sequence

```text
GUI
 │
 ▼
UpdateDocumentCommand
 │
 ▼
CommandBus
 │
 ▼
UpdateDocumentCommandHandler
 │
 ▼
DocumentService
 │
 ▼
Document Aggregate
 │
 ▼
Repository
 │
 ▼
DocumentUpdated Event
```

---

# 17. Compliance Checklist

The implementation conforms to this specification only if it:

- updates only Document properties;
- validates all requested modifications;
- preserves aggregate integrity;
- executes atomically;
- publishes DocumentUpdated after successful completion.

---

End of Document