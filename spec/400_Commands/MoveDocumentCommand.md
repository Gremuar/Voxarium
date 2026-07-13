# Voxarium Software Architecture Specification

Document Path:
spec/400_Commands/MoveDocumentCommand.md

Document ID: CMD-014

Title: MoveDocumentCommand

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

MoveDocumentCommand requests relocation of a Document within the logical Project hierarchy.

The command SHALL modify only the Document hierarchy.

The command SHALL NOT modify Document content.

The command SHALL preserve Document identity.

---

# 2. Responsibility

Execution SHALL be performed by MoveDocumentCommandHandler.

The handler SHALL update the Document hierarchy while preserving Project consistency.

---

# 3. Command Definition

## Name

MoveDocumentCommand

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

Identifier of the Document to move.

---

### TargetParentDocumentId

Type

Identifier | Null

Specifies the destination parent.

A null value SHALL move the Document to the Project root.

---

### Position

Type

Integer

Zero-based insertion position.

---

# 5. Validation Rules

Execution SHALL fail if:

- Document does not exist;
- destination parent does not exist;
- destination parent belongs to another Project;
- Document would become its own ancestor;
- Position is outside the valid range.

---

# 6. Execution Rules

Execution SHALL:

1. Validate hierarchy constraints.
2. Remove the Document from the current parent.
3. Insert the Document into the destination parent.
4. Recalculate ordering.
5. Persist hierarchy changes.
6. Publish lifecycle events.

Execution SHALL be atomic.

---

# 7. Result

Successful execution SHALL return:

MoveDocumentResult

The result SHALL contain:

- DocumentId
- PreviousParentId
- NewParentId
- PreviousPosition
- NewPosition

---

# 8. Published Events

Successful execution SHALL publish:

- DocumentMoved

If ordering changed:

- DocumentOrderChanged

---

# 9. Error Conditions

Execution MAY fail with:

- DocumentNotFound
- InvalidParentDocument
- CircularHierarchy
- InvalidPosition
- ValidationFailed
- InternalError

---

# 10. Idempotency

Moving a Document to its current location SHALL produce no state changes.

Repeated execution with identical parameters SHALL produce identical Project structure.

---

# 11. Transaction Requirements

The hierarchy SHALL remain valid throughout the transaction.

Rollback SHALL restore the original hierarchy.

---

# 12. Authorization

The caller SHALL possess permission to modify the owning Project.

---

# 13. Performance Requirements

Typical execution SHOULD complete within 100 milliseconds.

---

# 14. Thread Safety

Concurrent modifications affecting the same hierarchy SHALL be serialized.

Independent hierarchy modifications MAY execute concurrently.

---

# 15. AI Implementation Rules

AI-generated implementations SHALL:

- preserve Document identity;
- prevent cyclic hierarchies;
- preserve child ownership;
- update ordering deterministically;
- publish events only after successful commit.

---

# 16. Sequence

```text
GUI
 │
 ▼
MoveDocumentCommand
 │
 ▼
CommandBus
 │
 ▼
MoveDocumentCommandHandler
 │
 ▼
DocumentService
 │
 ▼
Hierarchy Validation
 │
 ▼
Repository
 │
 ▼
DocumentMoved Event
```

---

# 17. Compliance Checklist

The implementation conforms to this specification only if it:

- preserves Document identity;
- prevents circular hierarchies;
- preserves Project consistency;
- executes atomically;
- publishes DocumentMoved after successful completion.

---

End of Document