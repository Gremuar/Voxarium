# JobManager

**Document Path:**
`spec/200_Application/JobManager.md`

**Document ID:** APP-046

**Version:** 1.0.0

**Status:** Draft

**Classification:** Normative

---

# 1. Purpose

This document defines the **JobManager** of the Voxarium Application Layer.

JobManager coordinates the lifecycle of long-running Application jobs. It provides a unified mechanism for creating, tracking, updating, suspending, cancelling, and completing jobs while remaining independent of execution engines, worker implementations, and Infrastructure technologies.

The JobManager SHALL coordinate job lifecycle management but SHALL NOT execute jobs directly.

---

# 2. Scope

This specification defines:

* responsibilities;
* supported job operations;
* job lifecycle;
* dependencies;
* transactional behavior.

Worker processes, operating system schedulers, Infrastructure task queues, distributed execution platforms, and execution engines are outside the scope of this specification.

---

# 3. Definition

JobManager is an Application Service responsible for coordinating long-running operations represented as Jobs.

A Job SHALL represent an executable unit of work whose execution extends beyond a single synchronous Application request.

---

# 4. Responsibilities

JobManager SHALL be responsible for:

* creating jobs;
* registering jobs;
* tracking job status;
* updating job progress;
* suspending jobs;
* resuming jobs;
* cancelling jobs;
* completing jobs;
* removing obsolete jobs;
* publishing resulting Domain Events.

The JobManager SHALL NOT:

* execute job logic;
* allocate worker threads;
* implement scheduling algorithms;
* communicate directly with execution providers.

---

# 5. Dependencies

JobManager MAY depend upon:

* RepositoryContract;
* UnitOfWork;
* TransactionCoordinator;
* EventBus;
* ApplicationValidator;
* ApplicationMapper;
* OperationResult.

The service SHALL depend only upon abstraction contracts.

---

# 6. Supported Operations

Typical operations include:

* CreateJob;
* RegisterJob;
* StartJob;
* SuspendJob;
* ResumeJob;
* CancelJob;
* CompleteJob;
* FailJob;
* GetJobStatus;
* GetJobProgress;
* ListJobs;
* RemoveCompletedJobs.

Additional operations MAY be introduced provided they remain consistent with Application Layer responsibilities.

---

# 7. Job Lifecycle

A Job SHOULD follow this lifecycle:

1. creation;
2. validation;
3. registration;
4. queued state;
5. running state;
6. completion, cancellation, or failure;
7. archival or removal according to retention policy.

State transitions SHALL be deterministic and SHALL NOT skip mandatory lifecycle stages.

---

# 8. Transaction Management

Operations affecting Job state SHALL execute within a transaction coordinated by TransactionCoordinator.

Job state SHALL become visible only after successful transaction completion.

Failed transactions SHALL NOT produce partially updated job information.

---

# 9. Validation

Before modifying a Job, the service SHALL validate:

* job existence;
* valid lifecycle transition;
* project association where applicable;
* execution constraints;
* application invariants.

Validation failures SHALL prevent state transitions.

---

# 10. Error Handling

Failures SHALL be represented using OperationResult or standardized Application exceptions.

Infrastructure-specific failures SHALL be translated into Application-level failures before leaving the Application Layer.

Job failures SHALL NOT corrupt Application state.

---

# 11. Thread Safety

JobManager SHOULD remain stateless.

Concurrent Job operations SHALL execute using isolated execution contexts.

Consistency of Job state SHALL be maintained through transactional coordination.

---

# 12. Compliance

All long-running Application operations within Voxarium SHALL be coordinated through JobManager or an equivalent Application Service conforming to this specification.

Implementations SHALL preserve deterministic lifecycle management, dependency inversion, architectural isolation, transactional consistency, and complete separation between Application orchestration and Infrastructure execution technologies.

---

# 13. References

* ApplicationService.md
* ApplicationContext.md
* EventBus.md
* RepositoryContract.md
* UnitOfWork.md
* TransactionCoordinator.md
* ApplicationValidator.md
* ApplicationMapper.md
* OperationResult.md
* GenerationQueueService.md
* GenerationScheduler.md
* JobScheduler.md

---

**End of Document**
