# Voxarium Software Architecture Specification

Document Path:
spec/400_Commands/SplitFragmentCommand.md

Document ID: CMD-023

Title: SplitFragmentCommand

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
- Timeline_Service
- Workflow_Engine
- User_Interface_Architecture

---

# 1. Purpose

SplitFragmentCommand requests splitting an existing Fragment into two or more independent Fragments.

The source Fragment SHALL cease to exist after successful execution.

New Fragments SHALL preserve the semantic meaning and ordering of the original content.

---

# 2. Responsibility

Execution SHALL be performed by SplitFragmentCommandHandler.

The handler SHALL replace one Fragment Aggregate with multiple new Fragment Aggregates.

---

# 3. Command Definition

## Name

SplitFragmentCommand

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

Identifier of the Fragment to split.

---

### SplitPoints

Type

Collection<Integer>

Character offsets where the Fragment SHALL be divided.

Offsets SHALL be sorted in ascending order.

Duplicate offsets SHALL NOT be permitted.

---

## Optional

### PreserveAssignments

Type

Boolean

Default:

true

When enabled, Roles, Voice Profiles, Generation Presets and other assignments SHALL be copied to every newly created Fragment.

---

# 5. Validation Rules

Execution SHALL fail if:

- Fragment does not exist;
- Fragment is locked;
- SplitPoints is empty;
- any SplitPoint is outside the Fragment text;
- SplitPoints are duplicated;
- SplitPoints are unordered.

Validation SHALL complete before execution begins.

---

# 6. Execution Rules

Execution SHALL:

1. Load the owning Document Aggregate.
2. Load the source Fragment.
3. Validate SplitPoints.
4. Split the text.
5. Create new Fragment Aggregates.
6. Copy metadata and assignments.
7. Insert new Fragments into the original position.
8. Remove the source Fragment.
9. Recalculate ordering.
10. Invalidate affected generated SpeechSegments.
11. Publish lifecycle events.

Execution SHALL be atomic.

---

# 7. Assignment Rules

Unless explicitly configured otherwise, every newly created Fragment SHALL inherit:

- Role;
- Voice Profile;
- Emotion;
- Generation Preset;
- Pronunciation Dictionary;
- Tags;
- User Metadata.

Generated SpeechSegments SHALL NOT be copied.

Generated Assets SHALL NOT be copied.

---

# 8. Result

Successful execution SHALL return:

SplitFragmentResult

The result SHALL contain:

- SourceFragmentId
- CreatedFragmentIds
- CreatedFragmentCount

---

# 9. Published Events

Successful execution SHALL publish:

- FragmentSplit

Additionally, the implementation MAY publish:

- FragmentCreated
- FragmentDeleted
- TimelineUpdated

---

# 10. Error Conditions

Execution MAY fail with:

- FragmentNotFound
- InvalidSplitPoint
- ValidationFailed
- FragmentLocked
- VersionConflict
- InternalError

---

# 11. Idempotency

The command is NOT idempotent.

Repeated execution SHALL fail because the original Fragment no longer exists.

---

# 12. Transaction Requirements

Either:

- the original Fragment SHALL be replaced completely,

or

- no changes SHALL occur.

Partial splitting SHALL NOT occur.

---

# 13. Authorization

The caller SHALL possess permission to modify the owning Project.

---

# 14. Performance Requirements

Splitting a Fragment SHOULD complete within 50 milliseconds.

Execution time SHOULD depend primarily on Fragment size rather than Document size.

---

# 15. Thread Safety

Concurrent modification of the same Fragment SHALL be serialized.

Concurrent splitting of different Fragments MAY execute simultaneously.

---

# 16. AI Implementation Rules

AI-generated implementations SHALL:

- preserve text order;
- preserve semantic ordering;
- preserve inherited assignments;
- generate new identifiers for every created Fragment;
- remove the original Fragment only after successful creation of all new Fragments;
- publish events only after successful commit.

---

# 17. Sequence

```text
GUI
 │
 ▼
SplitFragmentCommand
 │
 ▼
CommandBus
 │
 ▼
SplitFragmentCommandHandler
 │
 ▼
FragmentService
 │
 ▼
Document Aggregate
 │
 ├── Create Fragment A
 │
 ├── Create Fragment B
 │
 ├── Remove Original Fragment
 │
 ▼
Repository
 │
 ▼
FragmentSplit Event
```

---

# 18. Compliance Checklist

The implementation conforms to this specification only if it:

- replaces one Fragment with multiple Fragments;
- preserves text ordering;
- preserves inherited assignments;
- generates new identifiers;
- executes atomically;
- publishes FragmentSplit after successful completion.

---

End of Document