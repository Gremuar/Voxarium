# Voxarium Software Architecture Specification

Document Path:
spec/400_Commands/RetryGenerationCommand.md

Document ID: CMD-037

Title: RetryGenerationCommand

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

RetryGenerationCommand requests rescheduling of failed generation tasks.

The command SHALL schedule only failed or cancelled generation tasks.

Previously completed generation results SHALL be preserved.

---

# 2. Responsibility

Execution SHALL be performed by RetryGenerationCommandHandler.

The handler SHALL analyze the previous Generation Job and create a retry plan.

---

# 3. Command Definition

## Name

RetryGenerationCommand

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

Identifier of the previously executed Generation Job.

---

## Optional

### RetryMode

Type

Enumeration

Allowed values:

- FailedOnly
- CancelledOnly
- FailedAndCancelled
- ForceAll

Default:

FailedOnly

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

- Job does not exist;
- Job is still running;
- Job contains no retryable tasks;
- Queue Service is unavailable.

Validation SHALL complete before execution begins.

---

# 6. Execution Rules

Execution SHALL:

1. Load the Generation Job.
2. Analyze completed tasks.
3. Identify retryable tasks.
4. Build a Retry Plan.
5. Create a new Generation Job.
6. Enqueue retry tasks.
7. Publish lifecycle events.

Execution SHALL complete immediately after Job creation.

Retry execution SHALL occur asynchronously.

---

# 7. Retry Rules

Completed SpeechSegments SHALL NOT be regenerated unless RetryMode is ForceAll.

Only selected tasks SHALL be scheduled.

The retry operation SHALL preserve generation configuration used by the original Job unless explicitly overridden by the Generation Service.

---

# 8. Result

Successful execution SHALL return:

RetryGenerationResult

The result SHALL contain:

- OriginalJobId
- RetryJobId
- ScheduledTasks

---

# 9. Published Events

Successful execution SHALL publish:

- GenerationRetryStarted
- JobQueued

Background execution SHALL additionally publish:

- FragmentGenerationStarted
- FragmentGenerationCompleted
- FragmentGenerationFailed

After completion:

- GenerationRetryCompleted

---

# 10. Error Conditions

Execution MAY fail with:

- JobNotFound
- JobStillRunning
- NothingToRetry
- QueueUnavailable
- ValidationFailed
- InternalError

---

# 11. Idempotency

Submitting an equivalent retry request while an identical Retry Job is already pending SHALL return the existing Retry Job.

Duplicate Retry Jobs SHALL NOT be created.

---

# 12. Transaction Requirements

The transaction SHALL include:

- Retry Job creation;
- queue registration.

Retry execution SHALL occur outside the transaction.

---

# 13. Authorization

The caller SHALL possess permission to generate speech for the owning Project.

---

# 14. Performance Requirements

Command execution SHOULD complete within 50 milliseconds.

The command SHALL NOT wait for retry execution.

---

# 15. Thread Safety

Retry requests targeting the same Generation Job SHALL be serialized.

---

# 16. AI Implementation Rules

AI-generated implementations SHALL:

- analyze the original Generation Job before scheduling retries;
- preserve completed generation results;
- avoid scheduling duplicate retry tasks;
- enqueue background Jobs rather than performing generation directly;
- publish lifecycle events only after successful transaction completion.

---

# 17. Sequence

```text
GUI
 │
 ▼
RetryGenerationCommand
 │
 ▼
CommandBus
 │
 ▼
RetryGenerationCommandHandler
 │
 ▼
GenerationService
 │
 ├── Analyze Previous Job
 │
 ├── Build Retry Plan
 │
 ├── Create Retry Job
 │
 ├── Queue Tasks
 │
 ▼
JobQueued Event
 │
 ▼
Background Workers
 │
 ▼
GenerationRetryCompleted
```

---

# 18. Compliance Checklist

The implementation conforms to this specification only if it:

- analyzes the previous Generation Job;
- schedules only eligible retry tasks;
- preserves completed generation results;
- creates exactly one Retry Job;
- executes asynchronously;
- publishes GenerationRetryStarted after successful completion.

---

End of Document