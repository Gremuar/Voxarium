# Voxarium Software Architecture Specification

Document Path:
spec/400_Commands/CreateFragmentCommand.md

Document ID: CMD-020

Title: CreateFragmentCommand

Version: 1.0.0

Status: Accepted

Classification: Normative

Depends On

- Fragment
- Document
- Command_Model
- Command_Bus

Referenced By

- Fragment_Service
- Workflow_Engine
- User_Interface_Architecture

---

# 1. Purpose

CreateFragmentCommand requests creation of a new Fragment within a Document.

A Fragment represents the smallest independently editable unit of textual content.

The command SHALL create exactly one Fragment.

---

# 2. Responsibility

Execution SHALL be performed by CreateFragmentCommandHandler.

The handler SHALL insert the new Fragment into the specified Document while preserving document integrity.

---

# 3. Command Definition

## Name

CreateFragmentCommand

## Category

Fragment Commands

## Layer

Application

---

# 4. Parameters

## Required

### DocumentId

Type

Identifier

Identifier of the owning Document.

---

### Position

Type

Integer

Zero-based insertion index.

---

## Optional

### InitialText

Type

String

Default:

Empty string.

---

### RoleId

Type

Identifier

Optional Role assigned during creation.

---

### VoiceProfileId

Type

Identifier

Optional Voice Profile assigned during creation.

---

# 5. Validation Rules

Execution SHALL fail if:

- Document does not exist;
- Position is outside the valid range;
- RoleId does not exist;
- VoiceProfileId does not exist;
- the Document is locked.

Validation SHALL complete before execution begins.

---

# 6. Execution Rules

Execution SHALL:

1. Load the owning Document.
2. Validate parameters.
3. Create the Fragment.
4. Assign initial properties.
5. Insert the Fragment into the Document.
6. Recalculate ordering.
7. Persist changes.
8. Publish lifecycle events.

Execution SHALL be atomic.

---

# 7. Result

Successful execution SHALL return:

FragmentId

The returned identifier SHALL uniquely identify the created Fragment.

---

# 8. Published Events

Successful execution SHALL publish:

- FragmentCreated

If ordering changed:

- FragmentOrderChanged

---

# 9. Error Conditions

Execution MAY fail with:

- DocumentNotFound
- InvalidPosition
- InvalidRole
- InvalidVoiceProfile
- DocumentLocked
- ValidationFailed
- InternalError

---

# 10. Idempotency

The command is NOT idempotent.

Each successful execution SHALL create a new Fragment.

---

# 11. Transaction Requirements

The operation SHALL execute within a single Application transaction.

Rollback SHALL restore the original Document state.

---

# 12. Authorization

The caller SHALL possess permission to modify the owning Project.

---

# 13. Performance Requirements

Typical execution SHOULD complete within 50 milliseconds.

---

# 14. Thread Safety

Concurrent creation of Fragments within different Documents MAY execute simultaneously.

Concurrent modifications of the same Document SHALL be serialized.

---

# 15. AI Implementation Rules

AI-generated implementations SHALL:

- preserve Document consistency;
- generate a unique Fragment identifier;
- insert the Fragment deterministically;
- preserve ordering of existing Fragments;
- publish events only after successful commit.

---

# 16. Sequence

```text
GUI
 │
 ▼
CreateFragmentCommand
 │
 ▼
CommandBus
 │
 ▼
CreateFragmentCommandHandler
 │
 ▼
FragmentService
 │
 ▼
Document Aggregate
 │
 ▼
Repository
 │
 ▼
FragmentCreated Event
```

---

# 17. Compliance Checklist

The implementation conforms to this specification only if it:

- creates exactly one Fragment;
- inserts it into the specified Document;
- preserves Document consistency;
- executes atomically;
- publishes FragmentCreated after successful completion.

---

End of Document