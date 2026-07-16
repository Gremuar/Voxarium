# Task

**Document Path:**
`spec/100_Domain/Task.md`

**Document ID:** DOM-058

**Version:** 1.0.0

**Status:** Draft

**Classification:** Normative

---

# 1. Purpose

This document defines the **Task** Aggregate Root of the Voxarium platform.

A Task represents a business operation scheduled or executed within a Project. It provides a unified domain model for long-running and asynchronous operations such as document import, speech generation, validation, export, audio processing, and plugin execution.

A Task models **what work is performed**, independently of how that work is executed.

---

# 2. Scope

This specification defines:

* responsibilities;
* ownership;
* aggregate boundaries;
* lifecycle;
* relationships;
* business invariants.

Schedulers, worker processes, message queues, operating system threads, and execution infrastructure are outside the scope of this specification.

---

# 3. Definition

A **Task** is the Aggregate Root representing a business operation within a Project.

It defines the consistency boundary for execution state and business progress.

---

# 4. Responsibilities

Task SHALL be responsible for:

* representing a business operation;
* tracking execution state;
* exposing execution progress;
* maintaining execution metadata;
* preserving execution history.

Task SHALL NOT:

* execute business logic directly;
* manage worker processes;
* perform scheduling;
* own business entities unrelated to execution.

---

# 5. Identity

Every Task SHALL possess a globally unique identifier.

Its identity SHALL remain stable regardless of:

* execution state changes;
* progress updates;
* metadata modifications.

---

# 6. Ownership

Every Task SHALL belong to exactly one Project.

A Project MAY contain zero or more Tasks.

Lifecycle management SHALL be coordinated by the owning Project Aggregate.

---

# 7. Aggregate Boundary

Task SHALL be the Aggregate Root.

Future owned entities MAY include:

* TaskProgress;
* TaskLog;
* TaskCheckpoint;
* TaskResultReference.

All owned entities SHALL be modified exclusively through the Task Aggregate.

---

# 8. Task State

A Task SHALL maintain one execution state.

Supported states SHOULD include:

* Created;
* Queued;
* Running;
* Paused;
* Completed;
* Failed;
* Cancelled.

State transitions SHALL follow business rules defined by the Application layer.

---

# 9. Relationships

Task MAY reference:

* Project;
* Document;
* Timeline;
* AudioAsset;
* ExportProfile;
* ImportProfile;
* PluginReference;
* ValidationJob.

Referenced entities SHALL remain external to the Aggregate.

---

# 10. Metadata

Task SHOULD expose:

* identifier;
* task type;
* current state;
* progress value;
* creation timestamp;
* start timestamp;
* completion timestamp;
* optional status message.

Metadata SHALL NOT affect aggregate identity.

---

# 11. Lifecycle

The lifecycle SHALL consist of:

1. creation;
2. queuing;
3. execution;
4. completion, cancellation, or failure;
5. archival.

Completed Tasks MAY remain available for auditing and history purposes.

---

# 12. Business Rules

The following rules SHALL apply:

* every Task belongs to exactly one Project;
* a Task SHALL have exactly one current state;
* progress SHALL remain within valid bounds;
* terminal states SHALL be immutable unless explicitly reopened by business rules.

---

# 13. Validation

Validation SHALL verify:

* unique identifier;
* existing Project;
* valid execution state;
* valid progress value;
* internally consistent timestamps;
* valid references.

Validation failures SHALL be reported through the Validation subsystem.

---

# 14. Persistence

Persistence SHALL be performed through Repository abstractions.

Task SHALL remain independent of:

* execution engines;
* schedulers;
* storage implementation;
* serialization format.

---

# 15. Events

Business operations MAY produce events including:

* TaskCreatedEvent;
* TaskQueuedEvent;
* TaskStartedEvent;
* TaskProgressChangedEvent;
* TaskCompletedEvent;
* TaskFailedEvent;
* TaskCancelledEvent.

Event publication SHALL occur outside the Aggregate.

---

# 16. Compliance

All business operations within Voxarium SHALL conform to this specification.

Implementations SHALL preserve aggregate boundaries, execution consistency, stable identity, and business invariants defined by this document.

---

# 17. References

* Project.md
* Document.md
* Timeline.md
* AudioAsset.md
* ExportProfile.md
* ImportProfile.md
* PluginReference.md
* ValidationJob.md
* ValidationIssue.md
* CreateTaskCommand.md
* CancelTaskCommand.md
* TaskCreatedEvent.md

---

**End of Document**
