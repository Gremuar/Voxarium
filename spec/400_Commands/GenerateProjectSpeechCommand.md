# Voxarium Software Architecture Specification

Document Path:
spec/400_Commands/GenerateProjectSpeechCommand.md

Document ID: CMD-035

Title: GenerateProjectSpeechCommand

Version: 1.0.0

Status: Accepted

Classification: Normative

Depends On

- Project
- Document
- Fragment
- SpeechSegment
- Generation_Service
- Queue_Service
- Command_Model
- Command_Bus

Referenced By

- Workflow_Engine
- Project_Service
- User_Interface_Architecture

---

# 1. Purpose

GenerateProjectSpeechCommand requests speech generation for all eligible Fragments within a Project.

The command SHALL coordinate generation across multiple Documents.

Speech synthesis SHALL execute asynchronously.

---

# 2. Responsibility

Execution SHALL be performed by GenerateProjectSpeechCommandHandler.

The handler SHALL create a Project Generation Job and schedule generation for every eligible Document.

---

# 3. Command Definition

## Name

GenerateProjectSpeechCommand

## Category

Generation Commands

## Layer

Application

---

# 4. Parameters

## Required

### ProjectId

Type

Identifier

Identifier of the Project.

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

### Scope

Type

Enumeration

Allowed values:

- EntireProject
- SelectedDocuments

Default:

EntireProject

---

### DocumentIds

Type

Collection<Identifier>

Required only when Scope is SelectedDocuments.

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

- Project does not exist;
- Project contains no eligible Documents;
- Project is locked;
- Generation Service is unavailable;
- selected Documents do not belong to the Project.

Validation SHALL complete before execution begins.

---

# 6. Execution Rules

Execution SHALL:

1. Load the Project Aggregate.
2. Identify eligible Documents.
3. Build a Project Generation Plan.
4. Create a Project Generation Job.
5. Schedule Document Generation Jobs.
6. Mark the Project as GenerationPending.
7. Publish lifecycle events.

Execution SHALL complete immediately after Job creation.

Speech synthesis SHALL execute asynchronously.

---

# 7. Scheduling Rules

Generation SHALL preserve Document independence.

Each Document MAY execute concurrently.

Each Fragment SHALL use its effective generation configuration.

The scheduler MAY reorder Jobs to maximize throughput.

The resulting audio SHALL be independent of execution order.

---

# 8. Result

Successful execution SHALL return:

GenerateProjectSpeechResult

The result SHALL contain:

- JobId
- ProjectId
- ScheduledDocuments
- ScheduledFragments

---

# 9. Published Events

Successful execution SHALL publish:

- ProjectGenerationStarted
- JobQueued

Background execution SHALL additionally publish:

- DocumentGenerationStarted
- DocumentGenerationCompleted
- FragmentGenerationStarted
- FragmentGenerationCompleted
- FragmentGenerationFailed

After completion:

- ProjectGenerationCompleted

Upon cancellation:

- ProjectGenerationCancelled

---

# 10. Error Conditions

Execution MAY fail with:

- ProjectNotFound
- EmptyProject
- NothingToGenerate
- QueueUnavailable
- ValidationFailed
- InternalError

---

# 11. Idempotency

Submitting an equivalent request while an active Project Generation Job already exists SHALL return the existing Job.

Duplicate Jobs SHALL NOT be created.

---

# 12. Transaction Requirements

The transaction SHALL include:

- Project Job creation;
- queue registration;
- Project state update.

Speech generation SHALL execute outside the transaction.

---

# 13. Authorization

The caller SHALL possess permission to generate speech for the Project.

---

# 14. Performance Requirements

Command execution SHOULD complete within 200 milliseconds.

Execution time SHALL NOT depend on the number of scheduled Fragments.

---

# 15. Thread Safety

Only one active Project Generation Job MAY exist for the same Project.

Independent Projects MAY execute concurrently.

---

# 16. AI Implementation Rules

AI-generated implementations SHALL:

- construct a Project Generation Plan;
- avoid duplicate Jobs;
- schedule Document Jobs rather than performing synthesis directly;
- preserve Project consistency;
- publish lifecycle events only after successful transaction completion.

---

# 17. Sequence

```text
GUI
 │
 ▼
GenerateProjectSpeechCommand
 │
 ▼
CommandBus
 │
 ▼
GenerateProjectSpeechCommandHandler
 │
 ▼
GenerationService
 │
 ├── Build Project Generation Plan
 │
 ├── Create Project Job
 │
 ├── Schedule Document Jobs
 │
 ▼
JobQueued Event
 │
 ▼
Background Workers
 │
 ▼
Document Generation
 │
 ▼
Fragment Generation
 │
 ▼
ProjectGenerationCompleted
```

---

# 18. Compliance Checklist

The implementation conforms to this specification only if it:

- builds a Project Generation Plan;
- creates exactly one Project Generation Job;
- schedules Document generation;
- performs no synchronous speech synthesis;
- updates Project generation state;
- publishes ProjectGenerationStarted after successful completion.

---

End of Document