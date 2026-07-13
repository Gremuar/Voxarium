# Voxarium Software Architecture Specification

Document Path:
spec/400_Commands/AssignRoleCommand.md

Document ID: CMD-028

Title: AssignRoleCommand

Version: 1.0.0

Status: Accepted

Classification: Normative

Depends On

- Fragment
- Role
- Document
- Command_Model
- Command_Bus

Referenced By

- Fragment_Service
- Role_Service
- Workflow_Engine
- User_Interface_Architecture

---

# 1. Purpose

AssignRoleCommand requests assignment or replacement of the Role associated with a Fragment.

The command SHALL modify only the Role assignment.

The command SHALL preserve Fragment identity and content.

---

# 2. Responsibility

Execution SHALL be performed by AssignRoleCommandHandler.

The handler SHALL validate the requested Role and update the Fragment.

---

# 3. Command Definition

## Name

AssignRoleCommand

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

### RoleId

Type

Identifier

Identifier of the Role to assign.

---

## Optional

### ForceRegeneration

Type

Boolean

Default:

false

If enabled, all generated SpeechSegments associated with the Fragment SHALL be marked for regeneration.

---

# 5. Validation Rules

Execution SHALL fail if:

- Fragment does not exist;
- Role does not exist;
- Fragment is locked;
- Role belongs to another Project.

Validation SHALL complete before execution begins.

---

# 6. Execution Rules

Execution SHALL:

1. Load the Fragment Aggregate.
2. Validate the Role.
3. Assign the new Role.
4. Update derived properties.
5. Invalidate generated SpeechSegments when required.
6. Persist the Aggregate.
7. Publish lifecycle events.

Execution SHALL be atomic.

---

# 7. Assignment Rules

Assigning a new Role SHALL NOT modify:

- Fragment text;
- Fragment ordering;
- Voice Profile;
- Emotion;
- User metadata.

Generated audio SHALL become invalid if the assigned Role affects speech generation.

---

# 8. Result

Successful execution SHALL return:

AssignRoleResult

The result SHALL contain:

- FragmentId
- PreviousRoleId
- AssignedRoleId

---

# 9. Published Events

Successful execution SHALL publish:

- FragmentRoleAssigned

Additionally, the implementation MAY publish:

- FragmentGenerationInvalidated
- FragmentUpdated

---

# 10. Error Conditions

Execution MAY fail with:

- FragmentNotFound
- RoleNotFound
- InvalidRole
- FragmentLocked
- ValidationFailed
- InternalError

---

# 11. Idempotency

Assigning the currently assigned Role SHALL produce no state changes.

Repeated execution with identical parameters SHALL produce identical Fragment state.

---

# 12. Transaction Requirements

The Role assignment SHALL execute within a single Application transaction.

Rollback SHALL restore the previous Role assignment.

---

# 13. Authorization

The caller SHALL possess permission to modify the owning Project.

---

# 14. Performance Requirements

Typical execution SHOULD complete within 20 milliseconds.

The command SHALL NOT perform synchronous speech generation.

---

# 15. Thread Safety

Concurrent Role assignments targeting the same Fragment SHALL be serialized.

---

# 16. AI Implementation Rules

AI-generated implementations SHALL:

- validate Role existence before assignment;
- preserve Fragment identity;
- invalidate generated speech only when necessary;
- avoid modifying unrelated Fragment properties;
- publish events only after successful commit.

---

# 17. Sequence

```text
GUI
 │
 ▼
AssignRoleCommand
 │
 ▼
CommandBus
 │
 ▼
AssignRoleCommandHandler
 │
 ▼
FragmentService
 │
 ▼
Fragment Aggregate
 │
 ▼
Repository
 │
 ▼
FragmentRoleAssigned Event
```

---

# 18. Compliance Checklist

The implementation conforms to this specification only if it:

- validates the assigned Role;
- preserves Fragment identity;
- modifies only the Role assignment;
- invalidates generation state when required;
- executes atomically;
- publishes FragmentRoleAssigned after successful completion.

---

End of Document