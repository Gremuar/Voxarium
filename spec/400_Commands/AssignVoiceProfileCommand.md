# Voxarium Software Architecture Specification

Document Path:
spec/400_Commands/AssignVoiceProfileCommand.md

Document ID: CMD-029

Title: AssignVoiceProfileCommand

Version: 1.0.0

Status: Accepted

Classification: Normative

Depends On

- Fragment
- VoiceProfile
- Role
- Document
- Command_Model
- Command_Bus

Referenced By

- Fragment_Service
- Voice_Service
- Workflow_Engine
- User_Interface_Architecture

---

# 1. Purpose

AssignVoiceProfileCommand requests assignment or replacement of the Voice Profile associated with a Fragment.

The command SHALL modify only the Voice Profile assignment.

The command SHALL preserve Fragment identity and textual content.

---

# 2. Responsibility

Execution SHALL be performed by AssignVoiceProfileCommandHandler.

The handler SHALL validate the requested Voice Profile and update the Fragment.

---

# 3. Command Definition

## Name

AssignVoiceProfileCommand

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

### VoiceProfileId

Type

Identifier

Identifier of the Voice Profile to assign.

---

## Optional

### OverrideRoleVoice

Type

Boolean

Default:

true

Specifies whether the assigned Voice Profile SHALL override the default Voice Profile inherited from the assigned Role.

---

### ForceRegeneration

Type

Boolean

Default:

false

If enabled, generated SpeechSegments SHALL be invalidated immediately.

---

# 5. Validation Rules

Execution SHALL fail if:

- Fragment does not exist;
- Voice Profile does not exist;
- Voice Profile belongs to another Project;
- Fragment is locked.

Validation SHALL complete before execution begins.

---

# 6. Execution Rules

Execution SHALL:

1. Load the Fragment Aggregate.
2. Validate the Voice Profile.
3. Assign the Voice Profile.
4. Update effective generation parameters.
5. Invalidate generated SpeechSegments when required.
6. Persist the Aggregate.
7. Publish lifecycle events.

Execution SHALL be atomic.

---

# 7. Assignment Rules

Assigning a Voice Profile SHALL NOT modify:

- Fragment text;
- Fragment ordering;
- assigned Role;
- User metadata.

The effective Voice Profile SHALL be determined according to the inheritance rules defined by the Domain Model.

Generated audio SHALL become invalid whenever the effective Voice Profile changes.

---

# 8. Result

Successful execution SHALL return:

AssignVoiceProfileResult

The result SHALL contain:

- FragmentId
- PreviousVoiceProfileId
- AssignedVoiceProfileId

---

# 9. Published Events

Successful execution SHALL publish:

- FragmentVoiceProfileAssigned

Additionally, the implementation MAY publish:

- FragmentGenerationInvalidated
- FragmentUpdated

---

# 10. Error Conditions

Execution MAY fail with:

- FragmentNotFound
- VoiceProfileNotFound
- InvalidVoiceProfile
- FragmentLocked
- ValidationFailed
- InternalError

---

# 11. Idempotency

Assigning the currently effective Voice Profile SHALL produce no state changes.

Repeated execution with identical parameters SHALL produce identical Fragment state.

---

# 12. Transaction Requirements

The assignment SHALL execute within a single Application transaction.

Rollback SHALL restore the previous Voice Profile.

---

# 13. Authorization

The caller SHALL possess permission to modify the owning Project.

---

# 14. Performance Requirements

Typical execution SHOULD complete within 20 milliseconds.

The command SHALL NOT perform speech generation.

---

# 15. Thread Safety

Concurrent Voice Profile assignments targeting the same Fragment SHALL be serialized.

---

# 16. AI Implementation Rules

AI-generated implementations SHALL:

- validate Voice Profile existence;
- preserve Fragment identity;
- preserve Fragment content;
- invalidate generated SpeechSegments only when the effective Voice Profile changes;
- publish events only after successful commit.

---

# 17. Sequence

```text
GUI
 │
 ▼
AssignVoiceProfileCommand
 │
 ▼
CommandBus
 │
 ▼
AssignVoiceProfileCommandHandler
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
FragmentVoiceProfileAssigned Event
```

---

# 18. Compliance Checklist

The implementation conforms to this specification only if it:

- validates the Voice Profile;
- preserves Fragment identity;
- updates only the Voice Profile assignment;
- invalidates generation state when required;
- executes atomically;
- publishes FragmentVoiceProfileAssigned after successful completion.

---

End of Document