# Voxarium Software Architecture Specification

Document Path:
spec/400_Commands/UpdateFragmentCommand.md

Document ID: CMD-021

Title: UpdateFragmentCommand

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
- Timeline_Service
- User_Interface_Architecture

---

# 1. Purpose

UpdateFragmentCommand requests modification of an existing Fragment.

The command SHALL modify only the specified Fragment.

The command SHALL preserve the identity of the Fragment.

---

# 2. Responsibility

Execution SHALL be performed by UpdateFragmentCommandHandler.

The handler SHALL validate and apply the requested modifications.

---

# 3. Command Definition

## Name

UpdateFragmentCommand

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

### Changes

Type

FragmentChangeSet

Contains only the properties that shall be modified.

---

## Optional

### ValidateOnly

Type

Boolean

Default:

false

When enabled, validation SHALL be performed without modifying the Fragment.

---

# 5. Validation Rules

Execution SHALL fail if:

- Fragment does not exist;
- Fragment is locked;
- ChangeSet is empty;
- one or more values are invalid;
- referenced Role does not exist;
- referenced VoiceProfile does not exist.

Validation SHALL complete before execution begins.

---

# 6. Execution Rules

Execution SHALL:

1. Load the Fragment Aggregate.
2. Validate the ChangeSet.
3. Apply modifications.
4. Update derived properties.
5. Mark affected SpeechSegments as outdated if required.
6. Persist the Aggregate.
7. Publish lifecycle events.

Execution SHALL be atomic.

---

# 7. Supported Changes

The ChangeSet MAY modify:

- Text
- Role
- VoiceProfile
- Emotion
- GenerationPreset
- PronunciationDictionary
- Notes
- Tags
- User Metadata

The ChangeSet SHALL NOT modify:

- FragmentId
- Owner Document
- Creation Timestamp

---

# 8. Result

Successful execution SHALL return:

UpdateFragmentResult

The result SHALL contain:

- FragmentId
- UpdatedProperties
- Version
- Timestamp

---

# 9. Published Events

Successful execution SHALL publish:

- FragmentUpdated

Additionally, one or more of the following events MAY be published:

- FragmentVoiceChanged
- FragmentRoleChanged
- FragmentEmotionChanged
- FragmentGenerationPresetChanged

If regeneration becomes necessary:

- FragmentGenerationInvalidated

---

# 10. Error Conditions

Execution MAY fail with:

- FragmentNotFound
- ValidationFailed
- InvalidRole
- InvalidVoiceProfile
- InvalidGenerationPreset
- VersionConflict
- InternalError

---

# 11. Idempotency

Applying the same ChangeSet multiple times SHALL produce the same Fragment state.

---

# 12. Transaction Requirements

The update SHALL execute within a single Application transaction.

Rollback SHALL restore the previous Fragment state.

---

# 13. Authorization

The caller SHALL possess permission to modify the owning Project.

---

# 14. Performance Requirements

Typical execution SHOULD complete within 20 milliseconds.

Updates SHALL NOT trigger synchronous speech generation.

---

# 15. Thread Safety

Concurrent updates targeting the same Fragment SHALL be serialized.

Independent Fragments MAY be updated concurrently.

---

# 16. AI Implementation Rules

AI-generated implementations SHALL:

- update only explicitly specified properties;
- preserve Fragment identity;
- preserve ordering inside the owning Document;
- invalidate generated artifacts only when necessary;
- avoid regeneration during command execution;
- publish events only after successful commit.

---

# 17. Sequence

```text
GUI
 │
 ▼
UpdateFragmentCommand
 │
 ▼
CommandBus
 │
 ▼
UpdateFragmentCommandHandler
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
FragmentUpdated Event
```

---

# 18. Compliance Checklist

The implementation conforms to this specification only if it:

- modifies only the requested properties;
- preserves Fragment identity;
- validates all references;
- invalidates generation state when necessary;
- executes atomically;
- publishes FragmentUpdated after successful completion.

---

End of Document