# Voxarium Software Architecture Specification

Document Path:
spec/400_Commands/MergeFragmentsCommand.md

Document ID: CMD-024

Title: MergeFragmentsCommand

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

MergeFragmentsCommand requests merging two or more adjacent Fragments into a single Fragment.

The resulting Fragment SHALL replace all source Fragments.

The command SHALL preserve the semantic order of the merged text.

---

# 2. Responsibility

Execution SHALL be performed by MergeFragmentsCommandHandler.

The handler SHALL replace multiple Fragment Aggregates with one new Fragment Aggregate.

---

# 3. Command Definition

## Name

MergeFragmentsCommand

## Category

Fragment Commands

## Layer

Application

---

# 4. Parameters

## Required

### FragmentIds

Type

Collection<Identifier>

Identifiers of the Fragments to merge.

The collection SHALL contain at least two Fragments.

The Fragments SHALL belong to the same Document.

The Fragments SHALL be adjacent.

---

## Optional

### Separator

Type

String

Default:

Single Space

Inserted between merged text blocks.

---

### PreserveFirstFragmentId

Type

Boolean

Default:

true

If enabled, the resulting Fragment SHALL preserve the identifier of the first Fragment.

Otherwise a new Fragment identifier SHALL be generated.

---

# 5. Validation Rules

Execution SHALL fail if:

- fewer than two Fragments are specified;
- one or more Fragments do not exist;
- Fragments belong to different Documents;
- Fragments are not adjacent;
- one or more Fragments are locked;
- one or more Fragments participate in active generation.

Validation SHALL complete before execution begins.

---

# 6. Execution Rules

Execution SHALL:

1. Load the owning Document Aggregate.
2. Validate Fragment ordering.
3. Concatenate Fragment text.
4. Create the resulting Fragment.
5. Merge metadata.
6. Preserve inherited assignments where possible.
7. Remove source Fragments.
8. Insert the resulting Fragment.
9. Recalculate ordering.
10. Invalidate generated SpeechSegments.
11. Publish lifecycle events.

Execution SHALL be atomic.

---

# 7. Merge Rules

The resulting Fragment SHALL contain:

- concatenated text;
- merged metadata;
- inherited Role;
- inherited Voice Profile;
- inherited Generation Preset.

If source Fragments contain conflicting values, conflict resolution SHALL follow the rules defined in Fragment_Aggregate.md.

Generated SpeechSegments SHALL NOT be merged.

Generated Assets SHALL be discarded.

---

# 8. Result

Successful execution SHALL return:

MergeFragmentsResult

The result SHALL contain:

- ResultFragmentId
- SourceFragmentIds
- RemovedFragmentCount

---

# 9. Published Events

Successful execution SHALL publish:

- FragmentsMerged

Additionally, the implementation MAY publish:

- FragmentDeleted
- FragmentCreated
- TimelineUpdated

---

# 10. Error Conditions

Execution MAY fail with:

- FragmentNotFound
- InvalidFragmentSequence
- FragmentsNotAdjacent
- ValidationFailed
- FragmentLocked
- InternalError

---

# 11. Idempotency

The command is NOT idempotent.

Repeated execution SHALL fail because the original Fragment sequence no longer exists.

---

# 12. Transaction Requirements

Either:

- all specified Fragments SHALL be replaced by one Fragment,

or

- the Document SHALL remain unchanged.

Partial merge SHALL NOT occur.

---

# 13. Authorization

The caller SHALL possess permission to modify the owning Project.

---

# 14. Performance Requirements

Merging SHOULD complete within 50 milliseconds.

Execution time SHOULD scale linearly with the total merged text size.

---

# 15. Thread Safety

Concurrent modification of any participating Fragment SHALL be serialized.

Independent merge operations MAY execute concurrently.

---

# 16. AI Implementation Rules

AI-generated implementations SHALL:

- preserve text order;
- preserve semantic content;
- preserve inherited assignments whenever possible;
- invalidate generated SpeechSegments;
- avoid orphaned references;
- publish events only after successful commit.

---

# 17. Sequence

```text
GUI
 │
 ▼
MergeFragmentsCommand
 │
 ▼
CommandBus
 │
 ▼
MergeFragmentsCommandHandler
 │
 ▼
FragmentService
 │
 ▼
Document Aggregate
 │
 ├── Merge Text
 │
 ├── Remove Source Fragments
 │
 ├── Create Result Fragment
 │
 ▼
Repository
 │
 ▼
FragmentsMerged Event
```

---

# 18. Compliance Checklist

The implementation conforms to this specification only if it:

- merges only adjacent Fragments;
- preserves text ordering;
- preserves inherited assignments;
- removes all source Fragments;
- executes atomically;
- publishes FragmentsMerged after successful completion.

---

End of Document