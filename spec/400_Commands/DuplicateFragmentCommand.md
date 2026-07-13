# Voxarium Software Architecture Specification

Document Path:
spec/400_Commands/DuplicateFragmentCommand.md

Document ID: CMD-026

Title: DuplicateFragmentCommand

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

DuplicateFragmentCommand requests creation of a copy of an existing Fragment.

The duplicated Fragment SHALL become an independent Aggregate.

The source Fragment SHALL remain unchanged.

Generated runtime artifacts SHALL NOT be copied.

---

# 2. Responsibility

Execution SHALL be performed by DuplicateFragmentCommandHandler.

The handler SHALL create a deep copy of the source Fragment and insert it into the owning Document.

---

# 3. Command Definition

## Name

DuplicateFragmentCommand

## Category

Fragment Commands

## Layer

Application

---

# 4. Parameters

## Required

### FragmentId

Type

Identifier

Identifier of the source Fragment.

---

## Optional

### InsertMode

Type

Enumeration

Allowed values:

- AfterSource
- BeforeSource
- EndOfDocument

Default:

AfterSource

---

### DuplicateAssignments

Type

Boolean

Default:

true

Determines whether Role, Voice Profile, Emotion, Generation Preset and other assignments SHALL be copied.

---

# 5. Validation Rules

Execution SHALL fail if:

- Fragment does not exist;
- owning Document is locked;
- Fragment is currently being deleted;
- caller lacks sufficient permissions.

Validation SHALL complete before execution begins.

---

# 6. Execution Rules

Execution SHALL:

1. Load the owning Document Aggregate.
2. Load the source Fragment.
3. Create a new Fragment identifier.
4. Copy text.
5. Copy metadata.
6. Copy assignments when enabled.
7. Reset runtime state.
8. Insert the new Fragment.
9. Recalculate ordering.
10. Publish lifecycle events.

Execution SHALL be atomic.

---

# 7. Copy Rules

The duplicated Fragment SHALL inherit:

- Text;
- Role;
- Voice Profile;
- Emotion;
- Generation Preset;
- Pronunciation Dictionary;
- Tags;
- User Metadata.

The duplicated Fragment SHALL NOT inherit:

- FragmentId;
- SpeechSegments;
- Generated Audio;
- Runtime State;
- Generation Status;
- Timeline Cache.

---

# 8. Result

Successful execution SHALL return:

FragmentId

The returned identifier SHALL identify the duplicated Fragment.

---

# 9. Published Events

Successful execution SHALL publish:

- FragmentDuplicated
- FragmentCreated

Additionally, the implementation MAY publish:

- FragmentOrderChanged

---

# 10. Error Conditions

Execution MAY fail with:

- FragmentNotFound
- DocumentLocked
- ValidationFailed
- StorageFailure
- InternalError

---

# 11. Idempotency

The command is NOT idempotent.

Each successful execution SHALL create a new Fragment.

---

# 12. Transaction Requirements

Either:

- the duplicated Fragment SHALL be created completely,

or

- no new Fragment SHALL exist.

Partial duplication SHALL NOT occur.

---

# 13. Authorization

The caller SHALL possess permission to modify the owning Project.

---

# 14. Performance Requirements

Typical execution SHOULD complete within 20 milliseconds.

Execution time SHOULD depend primarily on Fragment size.

---

# 15. Thread Safety

Concurrent duplication of different Fragments MAY execute simultaneously.

Concurrent duplication of the same Fragment SHALL be serialized.

---

# 16. AI Implementation Rules

AI-generated implementations SHALL:

- generate a new Fragment identifier;
- preserve user-editable properties;
- reset runtime-generated state;
- preserve Document consistency;
- publish events only after successful commit.

---

# 17. Sequence

```text
GUI
 │
 ▼
DuplicateFragmentCommand
 │
 ▼
CommandBus
 │
 ▼
DuplicateFragmentCommandHandler
 │
 ▼
FragmentService
 │
 ▼
Document Aggregate
 │
 ├── Clone Fragment
 │
 ├── Assign New Identifier
 │
 ├── Reset Runtime State
 │
 ▼
Repository
 │
 ▼
FragmentDuplicated Event
```

---

# 18. Compliance Checklist

The implementation conforms to this specification only if it:

- creates exactly one new Fragment;
- preserves editable properties;
- generates a new identifier;
- resets runtime-generated state;
- executes atomically;
- publishes FragmentDuplicated after successful completion.

---

End of Document