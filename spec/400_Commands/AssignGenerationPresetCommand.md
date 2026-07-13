# Voxarium Software Architecture Specification

Document Path:
spec/400_Commands/AssignGenerationPresetCommand.md

Document ID: CMD-031

Title: AssignGenerationPresetCommand

Version: 1.0.0

Status: Accepted

Classification: Normative

Depends On

- Fragment
- GenerationPreset
- VoiceProfile
- Command_Model
- Command_Bus

Referenced By

- Fragment_Service
- Generation_Service
- Workflow_Engine
- User_Interface_Architecture

---

# 1. Purpose

AssignGenerationPresetCommand requests assignment or replacement of the Generation Preset associated with a Fragment.

The command SHALL modify only generation configuration.

The command SHALL preserve Fragment identity and textual content.

---

# 2. Responsibility

Execution SHALL be performed by AssignGenerationPresetCommandHandler.

The handler SHALL validate the requested Generation Preset and update the Fragment.

---

# 3. Command Definition

## Name

AssignGenerationPresetCommand

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

### GenerationPresetId

Type

Identifier

Identifier of the Generation Preset.

---

## Optional

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
- Generation Preset does not exist;
- Generation Preset is incompatible with the effective Voice Provider;
- Fragment is locked.

Validation SHALL complete before execution begins.

---

# 6. Execution Rules

Execution SHALL:

1. Load the Fragment Aggregate.
2. Validate the Generation Preset.
3. Verify compatibility with the active Voice Provider.
4. Assign the Generation Preset.
5. Recalculate effective generation parameters.
6. Invalidate generated SpeechSegments when required.
7. Persist the Aggregate.
8. Publish lifecycle events.

Execution SHALL be atomic.

---

# 7. Assignment Rules

Assigning a Generation Preset SHALL NOT modify:

- Fragment text;
- Fragment ordering;
- assigned Role;
- assigned Voice Profile;
- assigned Emotion;
- User metadata.

Only generation parameters SHALL change.

---

# 8. Result

Successful execution SHALL return:

AssignGenerationPresetResult

The result SHALL contain:

- FragmentId
- PreviousGenerationPresetId
- AssignedGenerationPresetId

---

# 9. Published Events

Successful execution SHALL publish:

- FragmentGenerationPresetAssigned

Additionally, the implementation MAY publish:

- FragmentGenerationInvalidated
- FragmentUpdated

---

# 10. Error Conditions

Execution MAY fail with:

- FragmentNotFound
- GenerationPresetNotFound
- UnsupportedGenerationPreset
- FragmentLocked
- ValidationFailed
- InternalError

---

# 11. Idempotency

Assigning the currently active Generation Preset SHALL produce no state changes.

Repeated execution with identical parameters SHALL produce identical Fragment state.

---

# 12. Transaction Requirements

The assignment SHALL execute within a single Application transaction.

Rollback SHALL restore the previous Generation Preset.

---

# 13. Authorization

The caller SHALL possess permission to modify the owning Project.

---

# 14. Performance Requirements

Typical execution SHOULD complete within 20 milliseconds.

The command SHALL NOT perform speech generation.

---

# 15. Thread Safety

Concurrent Generation Preset assignments targeting the same Fragment SHALL be serialized.

---

# 16. AI Implementation Rules

AI-generated implementations SHALL:

- validate Generation Preset compatibility;
- preserve Fragment identity;
- preserve Fragment content;
- invalidate generated SpeechSegments only when generation parameters change;
- publish events only after successful commit.

---

# 17. Sequence

```text
GUI
 │
 ▼
AssignGenerationPresetCommand
 │
 ▼
CommandBus
 │
 ▼
AssignGenerationPresetCommandHandler
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
FragmentGenerationPresetAssigned Event
```

---

# 18. Compliance Checklist

The implementation conforms to this specification only if it:

- validates the Generation Preset;
- preserves Fragment identity;
- updates only generation parameters;
- invalidates generation state when required;
- executes atomically;
- publishes FragmentGenerationPresetAssigned after successful completion.

---

End of Document