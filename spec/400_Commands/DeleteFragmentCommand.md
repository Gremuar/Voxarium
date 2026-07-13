# Voxarium Software Architecture Specification

Document Path:
spec/400_Commands/DeleteFragmentCommand.md

Document ID: CMD-022

Title: DeleteFragmentCommand

Version: 1.0.0

Status: Accepted

Classification: Normative

Depends On

- Fragment
- Document
- SpeechSegment
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

DeleteFragmentCommand requests permanent removal of a Fragment from its owning Document.

The command SHALL remove the complete Fragment Aggregate.

The command SHALL preserve Document consistency.

---

# 2. Responsibility

Execution SHALL be performed by DeleteFragmentCommandHandler.

The handler SHALL remove the Fragment and every owned object.

---

# 3. Command Definition

## Name

DeleteFragmentCommand

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

Identifier of the Fragment.

---

## Optional

### DeleteGeneratedAssets

Type

Boolean

Default:

true

If enabled, all generated Assets belonging to the Fragment SHALL be removed.

---

# 5. Validation Rules

Execution SHALL fail if:

- Fragment does not exist;
- Fragment is locked;
- Fragment participates in an active Workflow;
- Fragment is currently being generated;
- caller lacks required permissions.

Validation SHALL complete before execution begins.

---

# 6. Execution Rules

Execution SHALL:

1. Load the owning Document Aggregate.
2. Locate the Fragment.
3. Cancel active generation Jobs.
4. Remove Timeline references.
5. Remove SpeechSegments.
6. Remove generated Assets.
7. Remove the Fragment.
8. Recalculate Document ordering.
9. Publish lifecycle events.

Execution SHALL be atomic.

---

# 7. Result

Successful execution SHALL return:

DeleteFragmentResult

The result SHALL contain:

- FragmentId
- RemovedSpeechSegments
- RemovedAssets
- PreviousPosition
- Duration

---

# 8. Published Events

Successful execution SHALL publish:

- FragmentDeleting
- FragmentDeleted

Additionally, the following events MAY be published:

- TimelineUpdated
- SearchIndexUpdated
- JobCancelled

---

# 9. Error Conditions

Execution MAY fail with:

- FragmentNotFound
- FragmentLocked
- WorkflowRunning
- GenerationRunning
- ValidationFailed
- StorageFailure
- InternalError

---

# 10. Idempotency

The command is NOT idempotent.

Deleting an already deleted Fragment SHALL return FragmentNotFound.

---

# 11. Transaction Requirements

Either:

- the complete Fragment Aggregate SHALL be removed,

or

- the owning Document SHALL remain unchanged.

Rollback SHALL restore the previous valid state.

---

# 12. Authorization

The caller SHALL possess permission to modify the owning Project.

Deletion SHOULD require explicit user confirmation.

---

# 13. Performance Requirements

Deletion SHOULD complete within 50 milliseconds.

Large generated Assets MAY be removed asynchronously after transaction completion.

---

# 14. Thread Safety

Concurrent deletion of the same Fragment SHALL be serialized.

Independent Fragments MAY be deleted concurrently.

---

# 15. AI Implementation Rules

AI-generated implementations SHALL:

- preserve Document consistency;
- remove owned entities before removing the Fragment;
- preserve ordering of remaining Fragments;
- remove orphaned generated Assets;
- publish events only after successful transaction completion.

---

# 16. Sequence

```text
GUI
 │
 ▼
DeleteFragmentCommand
 │
 ▼
CommandBus
 │
 ▼
DeleteFragmentCommandHandler
 │
 ▼
FragmentService
 │
 ▼
Document Aggregate
 │
 ├── Remove SpeechSegments
 │
 ├── Remove Assets
 │
 ├── Update Timeline
 │
 ▼
Repository
 │
 ▼
FragmentDeleted Event
```

---

# 17. Compliance Checklist

The implementation conforms to this specification only if it:

- removes the complete Fragment Aggregate;
- preserves Document consistency;
- removes owned SpeechSegments;
- removes generated Assets;
- updates dependent structures;
- publishes FragmentDeleted after successful completion.

---

End of Document