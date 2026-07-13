# Voxarium Software Architecture Specification

Document Path:
spec/400_Commands/GenerateDocumentSpeechCommand.md

Document ID: CMD-034

Title: GenerateDocumentSpeechCommand

Version: 1.0.0

Status: Accepted

Classification: Normative

Depends On

- Document
- Fragment
- SpeechSegment
- Generation_Service
- Queue_Service
- Command_Model
- Command_Bus

Referenced By

- Workflow_Engine
- Document_Service
- User_Interface_Architecture

---

# 1. Purpose

GenerateDocumentSpeechCommand requests speech generation for every eligible Fragment within a Document.

The command SHALL create a coordinated generation Job.

Speech synthesis SHALL execute asynchronously.

---

# 2. Responsibility

Execution SHALL be performed by GenerateDocumentSpeechCommandHandler.

The handler SHALL identify eligible Fragments, construct a generation plan and submit it to the Generation Service.

---

# 3. Command Definition

## Name

GenerateDocumentSpeechCommand

## Category

Generation Commands

## Layer

Application

---

# 4. Parameters

## Required

### DocumentId

Type

Identifier

Identifier of the Document.

---

## Optional

### GenerationMode

Type

Enumeration

Allowed values:

- MissingOnly
- RegenerateOutdated
- RegenerateAll

Default:

RegenerateOutdated

---

### Parallelism

Type

Integer

Default:

Automatic

Specifies the preferred number of concurrent generation workers.

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

- Document does not exist;
- Document contains no Fragments;
- Document is locked;
- no eligible Fragments are found;
- Generation Service is unavailable.

Validation SHALL complete before execution begins.

---

# 6. Execution Rules

Execution SHALL:

1. Load the Document Aggregate.
2. Identify eligible Fragments.
3. Build a Generation Plan.
4. Create a Document Generation Job.
5. Enqueue Fragment generation tasks.
6. Mark the Document as GenerationPending.
7. Publish lifecycle events.

Execution SHALL complete immediately after Job creation.

Speech synthesis SHALL execute asynchronously.

---

# 7. Generation Rules

The Generation Plan SHALL include only Fragments matching the selected GenerationMode.

Each Fragment SHALL use its effective:

- Voice Profile;
- Emotion;
- Generation Preset;
- Pronunciation Dictionary.

Fragments MAY execute concurrently.

The execution order SHALL NOT affect the resulting audio.

---

# 8. Result

Successful execution SHALL return:

GenerateDocumentSpeechResult

The result SHALL contain:

- JobId
- DocumentId
- ScheduledFragments
- QueuePosition

---

# 9. Published Events

Successful execution SHALL publish:

- DocumentGenerationStarted
- JobQueued

Background execution SHALL additionally publish:

- FragmentGenerationStarted
- FragmentGenerationCompleted
- FragmentGenerationFailed

After all Fragments have completed:

- DocumentGenerationCompleted

If execution is interrupted:

- DocumentGenerationCancelled

---

# 10. Error Conditions

Execution MAY fail with:

- DocumentNotFound
- EmptyDocument
- NothingToGenerate
- QueueUnavailable
- ValidationFailed
- InternalError

---

# 11. Idempotency

Submitting an equivalent request while an active Document Generation Job already exists SHALL return the existing Job.

Duplicate Jobs SHALL NOT be created.

---

# 12. Transaction Requirements

The transaction SHALL include:

- Generation Job creation;
- queue registration;
- Document state update.

Speech generation SHALL execute outside the transaction.

---

# 13. Authorization

The caller SHALL possess permission to generate speech for the owning Project.

---

# 14. Performance Requirements

Command execution SHOULD complete within 100 milliseconds.

The execution time SHALL NOT depend on the number of Fragments requiring generation.

---

# 15. Thread Safety

Only one active Document Generation Job MAY exist for the same Document.

Independent Documents MAY be generated concurrently.

---

# 16. AI Implementation Rules

AI-generated implementations SHALL:

- construct a Generation Plan before queue submission;
- avoid duplicate Jobs;
- enqueue Fragment tasks instead of performing synthesis directly;
- preserve Document consistency;
- publish lifecycle events only after successful transaction completion.

---

# 17. Sequence

```text
GUI
 │
 ▼
GenerateDocumentSpeechCommand
 │
 ▼
CommandBus
 │
 ▼
GenerateDocumentSpeechCommandHandler
 │
 ▼
GenerationService
 │
 ├── Build Generation Plan
 │
 ├── Create Job
 │
 ├── Queue Fragment Tasks
 │
 ▼
JobQueued Event
 │
 ▼
Background Workers
 │
 ▼
Fragment Generation
 │
 ▼
DocumentGenerationCompleted
```

---

# 18. Compliance Checklist

The implementation conforms to this specification only if it:

- builds a Generation Plan;
- creates exactly one Document Generation Job;
- schedules eligible Fragments;
- does not perform synchronous speech synthesis;
- updates Document generation state;
- publishes DocumentGenerationStarted and JobQueued after successful completion.

---

End of Document