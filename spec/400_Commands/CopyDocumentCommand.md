# Voxarium Software Architecture Specification

Document Path:
spec/400_Commands/CopyDocumentCommand.md

Document ID: CMD-013

Title: CopyDocumentCommand

Version: 1.0.0

Status: Accepted

Classification: Normative

Depends On

- Document
- Project
- Fragment
- Asset
- Command_Model
- Command_Bus

Referenced By

- Document_Service
- Workflow_Engine
- User_Interface_Architecture

---

# 1. Purpose

CopyDocumentCommand requests creation of a new Document by copying an existing Document.

The copied Document SHALL become an independent Aggregate.

The source Document SHALL remain unchanged.

---

# 2. Responsibility

Execution SHALL be performed by CopyDocumentCommandHandler.

The handler SHALL create a deep copy of the Document Aggregate.

---

# 3. Command Definition

## Name

CopyDocumentCommand

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

Identifier of the source Document.

---

### NewName

Type

String

Constraints

- SHALL NOT be empty.
- SHALL be trimmed.
- Maximum length SHALL be 256 Unicode characters.

---

## Optional

### CopyGeneratedAssets

Type

Boolean

Default:

false

If disabled, generated Assets SHALL NOT be copied.

---

### CopyTimelineReferences

Type

Boolean

Default:

false

Timeline references SHALL be recreated only when enabled.

---

# 5. Validation Rules

Execution SHALL fail if:

- Document does not exist;
- Document is locked;
- NewName is invalid;
- another Document with the same name already exists.

---

# 6. Execution Rules

Execution SHALL:

1. Load the source Document.
2. Create a new Document identifier.
3. Clone Document metadata.
4. Clone Fragment hierarchy.
5. Clone SpeechSegments.
6. Optionally clone generated Assets.
7. Persist the new Document.
8. Update search indexes.
9. Publish lifecycle events.

Execution SHALL be atomic.

---

# 7. Result

Successful execution SHALL return:

DocumentId

The returned identifier SHALL reference the newly created Document.

---

# 8. Published Events

Successful execution SHALL publish:

- DocumentCopied
- DocumentCreated

If indexing is enabled:

- SearchIndexUpdated

---

# 9. Error Conditions

Execution MAY fail with:

- DocumentNotFound
- DuplicateDocumentName
- ValidationFailed
- StorageFailure
- InternalError

---

# 10. Idempotency

The command is NOT idempotent.

Each successful execution SHALL create a new Document.

---

# 11. Transaction Requirements

Either the complete Document Aggregate SHALL be copied, or no new Document SHALL exist.

Partial copies SHALL NOT remain after rollback.

---

# 12. Authorization

The caller SHALL possess permission to create Documents within the Project.

---

# 13. Performance Requirements

Copying Documents without Assets SHOULD complete within one second.

Large Asset collections MAY be copied asynchronously.

Progress SHOULD be observable.

---

# 14. Thread Safety

Multiple copy operations MAY execute concurrently for different Documents.

Concurrent copying of the same Document SHALL produce independent copies.

---

# 15. AI Implementation Rules

AI-generated implementations SHALL:

- generate new identifiers for every copied entity;
- preserve internal references inside the copied Aggregate;
- avoid sharing mutable state between source and copy;
- preserve metadata unless explicitly overridden;
- publish lifecycle events only after successful commit.

---

# 16. Sequence

```text
GUI
 │
 ▼
CopyDocumentCommand
 │
 ▼
CommandBus
 │
 ▼
CopyDocumentCommandHandler
 │
 ▼
DocumentService
 │
 ▼
Clone Aggregate
 │
 ▼
Repository
 │
 ▼
DocumentCopied Event
```

---

# 17. Compliance Checklist

The implementation conforms to this specification only if it:

- creates a deep copy of the Document Aggregate;
- assigns new identifiers to copied entities;
- preserves aggregate consistency;
- leaves the source Document unchanged;
- publishes DocumentCopied after successful completion.

---

End of Document