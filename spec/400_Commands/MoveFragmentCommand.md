# Voxarium Software Architecture Specification

Document Path:
spec/400_Commands/MoveFragmentCommand.md

Document ID: CMD-025

Title: MoveFragmentCommand

Version: 1.0.0

Status: Accepted

Classification: Normative

Depends On

- Fragment
- Document
- Timeline
- Command_Model
- Command_Bus

Referenced By

- Fragment_Service
- Timeline_Service
- Workflow_Engine
- User_Interface_Architecture

---

# 1. Purpose

MoveFragmentCommand requests relocation of a Fragment within its owning Document.

The command SHALL modify only the ordering of Fragments.

The command SHALL NOT modify Fragment content.

The command SHALL preserve Fragment identity.

---

# 2. Responsibility

Execution SHALL be performed by MoveFragmentCommandHandler.

The handler SHALL relocate the Fragment while preserving Document consistency.

---

# 3. Command Definition

## Name

MoveFragmentCommand

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

Identifier of the Fragment to move.

---

### TargetPosition

Type

Integer

Zero-based insertion index within the owning Document.

---

## Optional

### PlacementMode

Type

Enumeration

Allowed values:

- Before
- After
- Absolute

Default:

Absolute

Determines how TargetPosition SHALL be interpreted.

---

# 5. Validation Rules

Execution SHALL fail if:

- Fragment does not exist;
- Fragment is locked;
- TargetPosition is outside the valid range;
- the owning Document is locked;
- the requested move would produce an invalid ordering.

Validation SHALL complete before execution begins.

---

# 6. Execution Rules

Execution SHALL:

1. Load the owning Document Aggregate.
2. Locate the Fragment.
3. Validate the destination.
4. Remove the Fragment from its current position.
5. Insert the Fragment at the target position.
6. Recalculate ordering.
7. Update Timeline references when required.
8. Persist the Aggregate.
9. Publish lifecycle events.

Execution SHALL be atomic.

---

# 7. Result

Successful execution SHALL return:

MoveFragmentResult

The result SHALL contain:

- FragmentId
- PreviousPosition
- NewPosition

---

# 8. Published Events

Successful execution SHALL publish:

- FragmentMoved

Additionally, the implementation MAY publish:

- FragmentOrderChanged
- TimelineUpdated

---

# 9. Error Conditions

Execution MAY fail with:

- FragmentNotFound
- InvalidPosition
- FragmentLocked
- DocumentLocked
- ValidationFailed
- VersionConflict
- InternalError

---

# 10. Idempotency

Moving a Fragment to its current position SHALL produce no state changes.

Repeated execution with identical parameters SHALL produce the same Document ordering.

---

# 11. Transaction Requirements

The operation SHALL execute within a single Application transaction.

Rollback SHALL restore the original Fragment ordering.

---

# 12. Authorization

The caller SHALL possess permission to modify the owning Project.

---

# 13. Performance Requirements

Typical execution SHOULD complete within 20 milliseconds.

Execution time SHOULD depend only on the number of affected Fragments.

---

# 14. Thread Safety

Concurrent move operations affecting the same Document SHALL be serialized.

Independent Documents MAY be modified concurrently.

---

# 15. AI Implementation Rules

AI-generated implementations SHALL:

- preserve Fragment identity;
- preserve text content;
- preserve all metadata;
- update ordering deterministically;
- update dependent Timeline references when required;
- publish events only after successful commit.

---

# 16. Sequence

```text
GUI
 │
 ▼
MoveFragmentCommand
 │
 ▼
CommandBus
 │
 ▼
MoveFragmentCommandHandler
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
FragmentMoved Event
```

---

# 17. Compliance Checklist

The implementation conforms to this specification only if it:

- preserves Fragment identity;
- updates only Fragment ordering;
- preserves Document consistency;
- executes atomically;
- publishes FragmentMoved after successful completion.

---

End of Document