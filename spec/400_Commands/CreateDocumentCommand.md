# Voxarium Software Architecture Specification

Document Path:
spec/400_Commands/CreateDocumentCommand.md

Document ID: CMD-010

Title: CreateDocumentCommand

Version: 1.0.0

Status: Accepted

Classification: Normative

Depends On

- Document
- Project
- Project_Service
- Command_Model
- Command_Bus

Referenced By

- Document_Service
- Workflow_Engine
- User_Interface_Architecture

---

# 1. Purpose

CreateDocumentCommand requests creation of a new Document within an existing Project.

The command SHALL describe only the user's intent.

The command SHALL NOT contain business logic.

---

# 2. Responsibility

Execution SHALL be performed by CreateDocumentCommandHandler.

The handler SHALL create a new Document and register it within the specified Project.

---

# 3. Command Definition

## Name

CreateDocumentCommand

## Category

Document Commands

## Layer

Application

---

# 4. Parameters

## Required

### ProjectId

Type

Identifier

Identifier of the owning Project.

---

### Name

Type

String

Constraints

- SHALL NOT be empty.
- SHALL be trimmed.
- Maximum length SHALL be 256 Unicode characters.

---

## Optional

### ParentDocumentId

Type

Identifier

Specifies the parent Document when hierarchical document organization is supported.

---

### InitialContent

Type

String

Default:

Empty string.

---

### Metadata

Type

DocumentMetadata

Initial metadata assigned to the Document.

---

# 5. Validation Rules

Execution SHALL fail if:

- Project does not exist;
- Project is closed;
- Name is empty;
- Name exceeds the maximum length;
- ParentDocumentId does not exist.

Validation SHALL complete before execution begins.

---

# 6. Execution Rules

Execution SHALL:

1. Validate command parameters.
2. Create a new Document.
3. Initialize default metadata.
4. Attach the Document to the Project.
5. Update search indexes.
6. Publish lifecycle events.

Execution SHALL be atomic.

---

# 7. Result

Successful execution SHALL return:

DocumentId

The returned identifier SHALL uniquely identify the created Document.

---

# 8. Published Events

Successful execution SHALL publish:

- DocumentCreated

If indexing is enabled:

- SearchIndexUpdated

---

# 9. Error Conditions

Execution MAY fail with:

- ProjectNotFound
- InvalidDocumentName
- DuplicateDocument
- InvalidParentDocument
- ValidationFailed
- InternalError

---

# 10. Idempotency

The command is NOT idempotent.

Repeated execution SHALL create distinct Documents.

---

# 11. Transaction Requirements

Creation SHALL complete within a single Application transaction.

Incomplete Documents SHALL NOT remain after rollback.

---

# 12. Authorization

The caller SHALL possess permission to modify the Project.

---

# 13. Performance Requirements

Creation SHOULD complete within 200 milliseconds under normal conditions.

---

# 14. Thread Safety

Concurrent creation of Documents within the same Project MAY execute simultaneously.

Ordering conflicts SHALL be resolved deterministically.

---

# 15. AI Implementation Rules

AI-generated implementations SHALL:

- generate immutable command objects;
- preserve Project consistency;
- initialize Document metadata;
- update indexes after successful commit;
- publish events only after transaction completion.

---

# 16. Sequence

```text
GUI
 │
 ▼
CreateDocumentCommand
 │
 ▼
CommandBus
 │
 ▼
CreateDocumentCommandHandler
 │
 ▼
DocumentService
 │
 ▼
Project Aggregate
 │
 ▼
Repository
 │
 ▼
DocumentCreated Event
```

---

# 17. Compliance Checklist

The implementation conforms to this specification only if it:

- creates exactly one Document;
- attaches it to the specified Project;
- initializes required metadata;
- executes atomically;
- publishes DocumentCreated after successful completion.

---

End of Document