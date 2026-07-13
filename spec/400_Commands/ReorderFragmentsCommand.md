# Voxarium Software Architecture Specification

Document Path:
spec/400_Commands/ReorderFragmentsCommand.md

Document ID: CMD-027

Title: ReorderFragmentsCommand

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

ReorderFragmentsCommand requests simultaneous reordering of multiple Fragments within a single Document.

The command SHALL update only the ordering of Fragments.

The command SHALL preserve the identity and content of every Fragment.

---

# 2. Responsibility

Execution SHALL be performed by ReorderFragmentsCommandHandler.

The handler SHALL apply the requested ordering while preserving Document consistency.

---

# 3. Command Definition

## Name

ReorderFragmentsCommand

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

### FragmentOrder

Type

Collection<Identifier>

Complete ordered list of Fragment identifiers.

Every Fragment belonging to the Document SHALL appear exactly once.

---

# 5. Validation Rules

Execution SHALL fail if:

- Document does not exist;
- one or more Fragment identifiers are invalid;
- FragmentOrder contains duplicate identifiers;
- FragmentOrder omits one or more Fragments;
- FragmentOrder contains Fragments belonging to another Document;
- the Document is locked.

Validation SHALL complete before execution begins.

---

# 6. Execution Rules

Execution SHALL:

1. Load the Document Aggregate.
2. Validate the supplied ordering.
3. Replace the existing ordering.
4. Recalculate sequential indexes.
5. Update Timeline references when required.
6. Persist the Aggregate.
7. Publish lifecycle events.

Execution SHALL be atomic.

---

# 7. Ordering Rules

The supplied FragmentOrder SHALL represent the complete ordering of the Document.

Partial ordering updates SHALL NOT be accepted.

Every Fragment SHALL appear exactly once.

The relative ordering SHALL exactly match the supplied collection.

---

# 8. Result

Successful execution SHALL return:

ReorderFragmentsResult

The result SHALL contain:

- DocumentId
- FragmentCount
- ReorderedFragments

---

# 9. Published Events

Successful execution SHALL publish:

- FragmentsReordered

Additionally, the implementation MAY publish:

- TimelineUpdated
- DocumentModified

---

# 10. Error Conditions

Execution MAY fail with:

- DocumentNotFound
- FragmentNotFound
- InvalidFragmentOrder
- DuplicateFragmentIdentifier
- ValidationFailed
- VersionConflict
- InternalError

---

# 11. Idempotency

Submitting an ordering identical to the current ordering SHALL produce no state changes.

Repeated execution with the same ordering SHALL produce identical results.

---

# 12. Transaction Requirements

The complete ordering SHALL be updated within a single Application transaction.

Rollback SHALL restore the previous ordering.

---

# 13. Authorization

The caller SHALL possess permission to modify the owning Project.

---

# 14. Performance Requirements

Reordering SHOULD complete within 50 milliseconds for typical Documents.

Execution time SHOULD scale linearly with the number of reordered Fragments.

---

# 15. Thread Safety

Concurrent reorder operations affecting the same Document SHALL be serialized.

Independent Documents MAY be reordered concurrently.

---

# 16. AI Implementation Rules

AI-generated implementations SHALL:

- preserve Fragment identities;
- validate the complete ordering before modification;
- prevent duplicate or missing Fragments;
- update ordering deterministically;
- publish events only after successful commit.

---

# 17. Sequence

```text
GUI
 │
 ▼
ReorderFragmentsCommand
 │
 ▼
CommandBus
 │
 ▼
ReorderFragmentsCommandHandler
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
FragmentsReordered Event
```

---

# 18. Compliance Checklist

The implementation conforms to this specification only if it:

- accepts a complete Fragment ordering;
- preserves Fragment identities;
- rejects incomplete or duplicate orderings;
- executes atomically;
- publishes FragmentsReordered after successful completion.

---

End of Document