# Voxarium Software Architecture Specification

Document Path:
spec/400_Commands/CancelGenerationCommand.md

Document ID: CMD-036

Title: CancelGenerationCommand

Version: 1.0.0

Status: Accepted

Classification: Normative

Depends On

- GenerationJob
- Queue_Service
- Generation_Service
- Command_Model
- Command_Bus

Referenced By

- Workflow_Engine
- User_Interface_Architecture

---

# 1. Purpose

CancelGenerationCommand requests cancellation of an active Generation Job.

The command SHALL request graceful termination.

The command SHALL NOT discard already completed generation results.

---

# 2. Responsibility

Execution SHALL be performed by CancelGenerationCommandHandler.

The handler SHALL locate the target Generation Job and request its cancellation.

---

# 3. Command Definition

## Name

CancelGenerationCommand

## Category

Generation Commands

## Layer

Application

---

# 4. Parameters

## Required

### JobId

Type

Identifier

Identifier of the Generation Job.

---

## Optional

### CancelMode

Type

Enumeration

Allowed values:

- Graceful
- Immediate

Default:

Graceful

Graceful cancellation SHALL allow the currently executing task to finish.

Immediate cancellation MAY interrupt execution as soon as possible.

---

# 5. Validation Rules

Execution SHALL fail if:

- Job does not exist;
- Job has already completed;
- Job has already been cancelled;
- Job cannot be cancelled.

Validation SHALL complete before execution begins.

---

# 6. Execution Rules

Execution SHALL:

1. Load the Generation Job.
2. Validate its current state.
3. Mark the Job as CancellationRequested.
4. Notify the Queue Service.
5. Notify active workers.
6. Publish lifecycle events.

Execution SHALL complete immediately.

Workers SHALL terminate execution asynchronously.

---

# 7. Cancellation Rules

Completed SpeechSegments SHALL remain available.

Completed Documents SHALL remain unchanged.

Only unfinished tasks SHALL be cancelled.

Already persisted Assets SHALL NOT be deleted.

---

# 8. Result

Successful execution SHALL return:

CancelGenerationResult

The result SHALL contain:

- JobId
- PreviousState
- CurrentState

---

# 9. Published Events

Successful execution SHALL publish:

- GenerationCancellationRequested

After workers terminate:

- GenerationCancelled

If cancellation fails:

- GenerationCancellationFailed

---

# 10. Error Conditions

Execution MAY fail with:

- JobNotFound
- JobAlreadyCompleted
- JobAlreadyCancelled
- QueueUnavailable
- ValidationFailed
- InternalError

---

# 11. Idempotency

Cancelling an already cancelled Job SHALL produce no state changes.

Repeated execution SHALL return the current Job state.

---

# 12. Transaction Requirements

The transaction SHALL include:

- Job state update;
- Queue notification.

Worker termination SHALL occur outside the transaction.

---

# 13. Authorization

The caller SHALL possess permission to manage generation within the owning Project.

---

# 14. Performance Requirements

Command execution SHOULD complete within 20 milliseconds.

The command SHALL NOT wait for worker termination.

---

# 15. Thread Safety

Cancellation requests for the same Job SHALL be serialized.

---

# 16. AI Implementation Rules

AI-generated implementations SHALL:

- never terminate worker threads directly;
- request cancellation through the Queue Service;
- preserve completed generation results;
- avoid partial state corruption;
- publish lifecycle events only after successful transaction completion.

---

# 17. Sequence

```text
GUI
 │
 ▼
CancelGenerationCommand
 │
 ▼
CommandBus
 │
 ▼
CancelGenerationCommandHandler
 │
 ▼
GenerationService
 │
 ├── Update Job State
 │
 ├── Notify Queue
 │
 └── Notify Workers
 │
 ▼
GenerationCancellationRequested
 │
 ▼
Background Workers
 │
 ▼
GenerationCancelled
```

---

# 18. Compliance Checklist

The implementation conforms to this specification only if it:

- requests cancellation without blocking;
- preserves completed generation results;
- updates Job state correctly;
- delegates termination to background workers;
- executes atomically;
- publishes GenerationCancellationRequested after successful completion.

---

End of Document