# Voxarium Software Architecture Specification

Document Path:
spec/400_Commands/GenerateFragmentSpeechCommand.md

Document ID: CMD-033

Title: GenerateFragmentSpeechCommand

Version: 1.0.0

Status: Accepted

Classification: Normative

Depends On

- Fragment
- SpeechSegment
- VoiceProfile
- GenerationPreset
- Generation_Service
- Command_Model
- Command_Bus

Referenced By

- Workflow_Engine
- Queue_Service
- Fragment_Service
- User_Interface_Architecture

---

# 1. Purpose

GenerateFragmentSpeechCommand requests speech generation for a Fragment.

The command SHALL initiate speech generation.

The command SHALL NOT perform speech synthesis synchronously.

---

# 2. Responsibility

Execution SHALL be performed by GenerateFragmentSpeechCommandHandler.

The handler SHALL create a Generation Job and enqueue it for execution.

---

# 3. Command Definition

## Name

GenerateFragmentSpeechCommand

## Category

Generation Commands

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

### RegenerationMode

Type

Enumeration

Allowed values:

- MissingOnly
- RegenerateOutdated
- Force

Default:

RegenerateOutdated

---

### Priority

Type

Enumeration

Allowed values:

- Low
- Normal
- High

Default:

Normal

---

# 5. Validation Rules

Execution SHALL fail if:

- Fragment does not exist;
- Fragment contains no text;
- Fragment is locked;
- Voice Profile is missing;
- Generation Preset is missing;
- another exclusive generation job already exists.

Validation SHALL complete before the Job is created.

---

# 6. Execution Rules

Execution SHALL:

1. Load the Fragment Aggregate.
2. Validate generation prerequisites.
3. Determine the effective generation configuration.
4. Create a Generation Job.
5. Place the Job into the execution queue.
6. Mark the Fragment as GenerationPending.
7. Publish lifecycle events.

Execution SHALL finish immediately after successful Job creation.

Speech synthesis SHALL execute asynchronously.

---

# 7. Generation Rules

Generation SHALL use:

- effective Voice Profile;
- effective Emotion;
- effective Generation Preset;
- effective Pronunciation Dictionary.

The generated SpeechSegments SHALL replace obsolete ones only after successful completion.

---

# 8. Result

Successful execution SHALL return:

GenerateFragmentSpeechResult

The result SHALL contain:

- JobId
- FragmentId
- QueuePosition

---

# 9. Published Events

Successful execution SHALL publish:

- FragmentGenerationStarted
- JobQueued

Upon successful completion the background Job SHALL publish:

- FragmentGenerationCompleted

Upon failure:

- FragmentGenerationFailed

---

# 10. Error Conditions

Execution MAY fail with:

- FragmentNotFound
- MissingVoiceProfile
- MissingGenerationPreset
- EmptyFragment
- QueueUnavailable
- ValidationFailed
- InternalError

---

# 11. Idempotency

Submitting the command while an equivalent Generation Job is already pending SHALL return the existing Job.

No duplicate Jobs SHALL be created.

---

# 12. Transaction Requirements

The transaction SHALL include:

- Job creation;
- queue registration;
- Fragment state update.

Speech synthesis SHALL execute outside the transaction.

---

# 13. Authorization

The caller SHALL possess permission to generate speech for the owning Project.

---

# 14. Performance Requirements

Command execution SHOULD complete within 50 milliseconds.

The command SHALL NOT wait for speech synthesis.

---

# 15. Thread Safety

Only one active Generation Job MAY exist for the same Fragment unless explicitly allowed by the Generation Service.

---

# 16. AI Implementation Rules

AI-generated implementations SHALL:

- never perform speech synthesis inside the command handler;
- enqueue background Jobs;
- preserve Fragment consistency;
- avoid duplicate Jobs;
- publish lifecycle events only after successful transaction completion.

---

# 17. Sequence

```text
GUI
 │
 ▼
GenerateFragmentSpeechCommand
 │
 ▼
CommandBus
 │
 ▼
GenerateFragmentSpeechCommandHandler
 │
 ▼
GenerationService
 │
 ├── Create Job
 │
 ├── Queue Job
 │
 └── Update Fragment State
 │
 ▼
JobQueued Event
 │
 ▼
Background Worker
 │
 ▼
Speech Generation
 │
 ▼
FragmentGenerationCompleted
```

---

# 18. Compliance Checklist

The implementation conforms to this specification only if it:

- validates generation prerequisites;
- creates exactly one Generation Job;
- does not perform synchronous speech synthesis;
- updates Fragment generation state;
- executes atomically;
- publishes FragmentGenerationStarted and JobQueued after successful completion.

---

End of Document