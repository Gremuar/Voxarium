# GenerationScheduler

**Document Path:**
`spec/200_Application/GenerationScheduler.md`

**Document ID:** APP-041

**Version:** 1.0.0

**Status:** Draft

**Classification:** Normative

---

# 1. Purpose

This document defines the **GenerationScheduler** of the Voxarium Application Layer.

GenerationScheduler coordinates the scheduling of speech generation jobs created by Application workflows. The scheduler determines execution order, allocates generation requests to execution providers, and manages scheduling policies while remaining independent of Infrastructure execution engines.

The scheduler SHALL coordinate scheduling decisions but SHALL NOT execute speech generation.

---

# 2. Scope

This specification defines:

* responsibilities;
* scheduling lifecycle;
* supported scheduling operations;
* dependencies;
* scheduling constraints.

Worker implementations, execution engines, Infrastructure queues, thread pools, and operating system schedulers are outside the scope of this specification.

---

# 3. Definition

GenerationScheduler is an Application Service responsible for coordinating the execution order of generation jobs.

The scheduler SHALL provide deterministic scheduling behavior for equivalent queue states and scheduling policies.

---

# 4. Responsibilities

GenerationScheduler SHALL be responsible for:

* selecting executable generation jobs;
* determining execution priority;
* coordinating job dispatch;
* delaying scheduled execution when required;
* supporting pause and resume operations;
* coordinating retry scheduling;
* tracking scheduling state;
* publishing scheduling-related events.

The scheduler SHALL NOT:

* synthesize speech;
* execute AI models;
* manipulate Infrastructure worker threads;
* access execution providers directly.

---

# 5. Dependencies

GenerationScheduler MAY depend upon:

* GenerationQueueService;
* RepositoryContract;
* UnitOfWork;
* TransactionCoordinator;
* EventBus;
* ApplicationValidator;
* OperationResult.

The scheduler SHALL depend only upon scheduling abstraction contracts.

---

# 6. Supported Operations

Typical operations include:

* ScheduleNextJob;
* PauseScheduling;
* ResumeScheduling;
* RescheduleJob;
* DelayJob;
* CancelScheduledJob;
* GetSchedulingState;
* UpdateSchedulingPolicy.

Additional operations MAY be introduced provided they remain consistent with Application Layer responsibilities.

---

# 7. Scheduling Lifecycle

A generation job SHOULD follow this scheduling lifecycle:

1. acceptance by GenerationQueueService;
2. eligibility validation;
3. priority evaluation;
4. scheduling decision;
5. dispatch to an execution provider;
6. completion, cancellation, or retry scheduling.

Scheduling SHALL remain deterministic for equivalent queue contents and policies.

---

# 8. Transaction Management

Scheduling decisions affecting Domain state SHALL execute within a transaction coordinated by TransactionCoordinator.

Dispatch SHALL occur only after successful transaction completion.

Failed scheduling operations SHALL roll back all Application state changes.

---

# 9. Validation

Before scheduling a job, the scheduler SHALL validate:

* job existence;
* queue consistency;
* project availability;
* generation configuration;
* scheduling policy;
* execution constraints.

Validation failures SHALL prevent scheduling.

---

# 10. Error Handling

Failures SHALL be represented using OperationResult or standardized Application exceptions.

Infrastructure-specific scheduling failures SHALL be translated into Application-level failures before leaving the Application Layer.

Scheduling failures SHALL NOT leave inconsistent queue state.

---

# 11. Thread Safety

GenerationScheduler SHOULD remain stateless.

Concurrent scheduling requests SHALL execute using isolated execution contexts.

Scheduling consistency SHALL be preserved through transactional coordination and deterministic scheduling policies.

---

# 12. Compliance

All scheduling of speech generation workflows within Voxarium SHALL be coordinated through GenerationScheduler or an equivalent Application Service conforming to this specification.

Implementations SHALL preserve deterministic scheduling, dependency inversion, architectural isolation, transactional consistency, and complete separation between scheduling logic and execution infrastructure.

---

# 13. References

* ApplicationService.md
* ApplicationContext.md
* GenerationQueueService.md
* EventBus.md
* RepositoryContract.md
* UnitOfWork.md
* TransactionCoordinator.md
* ApplicationValidator.md
* OperationResult.md
* SpeechSynthesisService.md

---

**End of Document**
