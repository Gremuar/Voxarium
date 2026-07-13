# Voxarium Software Architecture Specification

Document Path:
spec/400_Commands/AssignPronunciationDictionaryCommand.md

Document ID: CMD-032

Title: AssignPronunciationDictionaryCommand

Version: 1.0.0

Status: Accepted

Classification: Normative

Depends On

- Fragment
- PronunciationDictionary
- Command_Model
- Command_Bus

Referenced By

- Fragment_Service
- Pronunciation_Service
- Generation_Service
- Workflow_Engine
- User_Interface_Architecture

---

# 1. Purpose

AssignPronunciationDictionaryCommand requests assignment or replacement of the Pronunciation Dictionary associated with a Fragment.

The command SHALL modify only pronunciation configuration.

The command SHALL preserve Fragment identity and textual content.

---

# 2. Responsibility

Execution SHALL be performed by AssignPronunciationDictionaryCommandHandler.

The handler SHALL validate the requested Pronunciation Dictionary and update the Fragment.

---

# 3. Command Definition

## Name

AssignPronunciationDictionaryCommand

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

### PronunciationDictionaryId

Type

Identifier

Identifier of the Pronunciation Dictionary.

---

## Optional

### MergeMode

Type

Enumeration

Allowed values:

- Replace
- Merge

Default:

Replace

Replace SHALL completely replace the current dictionary.

Merge SHALL extend the current effective pronunciation rules.

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
- Pronunciation Dictionary does not exist;
- Pronunciation Dictionary belongs to another Project;
- Fragment is locked.

Validation SHALL complete before execution begins.

---

# 6. Execution Rules

Execution SHALL:

1. Load the Fragment Aggregate.
2. Validate the Pronunciation Dictionary.
3. Apply the selected MergeMode.
4. Recalculate effective pronunciation rules.
5. Invalidate generated SpeechSegments when required.
6. Persist the Aggregate.
7. Publish lifecycle events.

Execution SHALL be atomic.

---

# 7. Assignment Rules

Assigning a Pronunciation Dictionary SHALL NOT modify:

- Fragment text;
- Fragment ordering;
- assigned Role;
- assigned Voice Profile;
- assigned Emotion;
- assigned Generation Preset;
- User metadata.

Only pronunciation rules SHALL change.

---

# 8. Result

Successful execution SHALL return:

AssignPronunciationDictionaryResult

The result SHALL contain:

- FragmentId
- PreviousPronunciationDictionaryId
- AssignedPronunciationDictionaryId
- MergeMode

---

# 9. Published Events

Successful execution SHALL publish:

- FragmentPronunciationDictionaryAssigned

Additionally, the implementation MAY publish:

- FragmentGenerationInvalidated
- FragmentUpdated

---

# 10. Error Conditions

Execution MAY fail with:

- FragmentNotFound
- PronunciationDictionaryNotFound
- InvalidPronunciationDictionary
- FragmentLocked
- ValidationFailed
- InternalError

---

# 11. Idempotency

Assigning the currently effective Pronunciation Dictionary using the same MergeMode SHALL produce no state changes.

Repeated execution with identical parameters SHALL produce identical Fragment state.

---

# 12. Transaction Requirements

The assignment SHALL execute within a single Application transaction.

Rollback SHALL restore the previous pronunciation configuration.

---

# 13. Authorization

The caller SHALL possess permission to modify the owning Project.

---

# 14. Performance Requirements

Typical execution SHOULD complete within 20 milliseconds.

The command SHALL NOT perform speech generation.

---

# 15. Thread Safety

Concurrent pronunciation updates targeting the same Fragment SHALL be serialized.

---

# 16. AI Implementation Rules

AI-generated implementations SHALL:

- validate Pronunciation Dictionary existence;
- preserve Fragment identity;
- preserve Fragment content;
- recalculate only pronunciation-related parameters;
- invalidate generated SpeechSegments only when effective pronunciation changes;
- publish events only after successful commit.

---

# 17. Sequence

```text
GUI
 │
 ▼
AssignPronunciationDictionaryCommand
 │
 ▼
CommandBus
 │
 ▼
AssignPronunciationDictionaryCommandHandler
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
FragmentPronunciationDictionaryAssigned Event
```

---

# 18. Compliance Checklist

The implementation conforms to this specification only if it:

- validates the Pronunciation Dictionary;
- preserves Fragment identity;
- updates only pronunciation configuration;
- invalidates generation state when required;
- executes atomically;
- publishes FragmentPronunciationDictionaryAssigned after successful completion.

---

End of Document
```