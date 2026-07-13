# Voxarium Software Architecture Specification

Document Path:
spec/400_Commands/AssignEmotionCommand.md

Document ID: CMD-030

Title: AssignEmotionCommand

Version: 1.0.0

Status: Accepted

Classification: Normative

Depends On

- Fragment
- Emotion
- VoiceProfile
- Command_Model
- Command_Bus

Referenced By

- Fragment_Service
- Voice_Service
- Workflow_Engine
- User_Interface_Architecture

---

# 1. Purpose

AssignEmotionCommand requests assignment or replacement of the Emotion associated with a Fragment.

The command SHALL modify only the emotional rendering parameters of the Fragment.

The command SHALL preserve Fragment identity and textual content.

---

# 2. Responsibility

Execution SHALL be performed by AssignEmotionCommandHandler.

The handler SHALL validate the requested Emotion and update the Fragment.

---

# 3. Command Definition

## Name

AssignEmotionCommand

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

### EmotionId

Type

Identifier

Identifier of the Emotion.

---

## Optional

### Intensity

Type

Decimal

Range

0.0–1.0

Default:

1.0

---

### ForceRegeneration

Type

Boolean

Default:

false

If enabled, generated SpeechSegments SHALL immediately become obsolete.

---

# 5. Validation Rules

Execution SHALL fail if:

- Fragment does not exist;
- Emotion does not exist;
- Emotion is not supported by the assigned Voice Profile;
- Intensity is outside the permitted range;
- Fragment is locked.

Validation SHALL complete before execution begins.

---

# 6. Execution Rules

Execution SHALL:

1. Load the Fragment Aggregate.
2. Validate the Emotion.
3. Validate compatibility with the effective Voice Profile.
4. Assign the Emotion.
5. Store the Intensity.
6. Invalidate generated SpeechSegments when required.
7. Persist the Aggregate.
8. Publish lifecycle events.

Execution SHALL be atomic.

---

# 7. Assignment Rules

Assigning an Emotion SHALL NOT modify:

- Fragment text;
- Fragment ordering;
- assigned Role;
- assigned Voice Profile;
- User metadata.

Changing Emotion SHALL invalidate generated audio whenever emotional rendering affects speech synthesis.

---

# 8. Result

Successful execution SHALL return:

AssignEmotionResult

The result SHALL contain:

- FragmentId
- PreviousEmotionId
- AssignedEmotionId
- Intensity

---

# 9. Published Events

Successful execution SHALL publish:

- FragmentEmotionAssigned

Additionally, the implementation MAY publish:

- FragmentGenerationInvalidated
- FragmentUpdated

---

# 10. Error Conditions

Execution MAY fail with:

- FragmentNotFound
- EmotionNotFound
- UnsupportedEmotion
- InvalidIntensity
- FragmentLocked
- ValidationFailed
- InternalError

---

# 11. Idempotency

Assigning the same Emotion with the same Intensity SHALL produce no state changes.

Repeated execution with identical parameters SHALL produce identical Fragment state.

---

# 12. Transaction Requirements

The assignment SHALL execute within a single Application transaction.

Rollback SHALL restore the previous Emotion configuration.

---

# 13. Authorization

The caller SHALL possess permission to modify the owning Project.

---

# 14. Performance Requirements

Typical execution SHOULD complete within 20 milliseconds.

The command SHALL NOT trigger synchronous speech synthesis.

---

# 15. Thread Safety

Concurrent Emotion assignments targeting the same Fragment SHALL be serialized.

---

# 16. AI Implementation Rules

AI-generated implementations SHALL:

- validate Emotion compatibility with the effective Voice Profile;
- preserve Fragment identity;
- preserve Fragment content;
- invalidate generated SpeechSegments only when rendering parameters change;
- publish events only after successful commit.

---

# 17. Sequence

```text
GUI
 │
 ▼
AssignEmotionCommand
 │
 ▼
CommandBus
 │
 ▼
AssignEmotionCommandHandler
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
FragmentEmotionAssigned Event
```

---

# 18. Compliance Checklist

The implementation conforms to this specification only if it:

- validates Emotion compatibility;
- preserves Fragment identity;
- updates only Emotion-related properties;
- invalidates generation state when required;
- executes atomically;
- publishes FragmentEmotionAssigned after successful completion.

---

End of Document