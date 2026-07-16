# ValidationJob

**Document Path:**
`spec/100_Domain/ValidationJob.md`

**Document ID:** DOM-061

**Version:** 1.0.0

**Status:** Draft

**Classification:** Normative

---

# 1. Purpose

This document defines the **ValidationJob** Aggregate Root of the Voxarium platform.

A ValidationJob represents a business operation responsible for validating one or more Project entities against business rules. It provides a reusable abstraction for validation workflows independently of validation engines, execution infrastructure, or user interface.

A ValidationJob models **the validation process**, not the validation rules themselves.

---

# 2. Scope

This specification defines:

* responsibilities;
* ownership;
* aggregate boundaries;
* lifecycle;
* relationships;
* business invariants.

Validation algorithms, execution scheduling, threading, diagnostics formatting, and infrastructure concerns are outside the scope of this specification.

---

# 3. Definition

A **ValidationJob** is the Aggregate Root representing a validation operation within a Project.

It defines the consistency boundary for validation execution and its resulting ValidationIssues.

---

# 4. Responsibilities

ValidationJob SHALL be responsible for:

* representing a validation operation;
* tracking validation progress;
* maintaining validation status;
* collecting ValidationIssues;
* preserving validation history.

ValidationJob SHALL NOT:

* define validation rules;
* modify validated entities;
* automatically resolve detected issues;
* execute infrastructure-specific validation logic.

---

# 5. Identity

Every ValidationJob SHALL possess a globally unique identifier.

Its identity SHALL remain stable regardless of:

* execution progress;
* status changes;
* collected ValidationIssues.

---

# 6. Ownership

Every ValidationJob SHALL belong to exactly one Project.

A Project MAY contain zero or more ValidationJobs.

---

# 7. Aggregate Boundary

ValidationJob SHALL be the Aggregate Root.

Owned entities MAY include:

* ValidationIssue references;
* Validation statistics;
* Validation summary;
* Validation execution metadata.

All modifications SHALL occur through the ValidationJob Aggregate.

---

# 8. Validation State

A ValidationJob SHALL maintain one execution state.

Recommended states include:

* Created;
* Queued;
* Running;
* Completed;
* Failed;
* Cancelled.

Only one current state SHALL exist at any given time.

---

# 9. Relationships

ValidationJob MAY reference:

* Project;
* ValidationRule;
* ValidationIssue;
* Document;
* Timeline;
* AudioAsset;
* TextAsset;
* Task.

Referenced entities SHALL remain external to the Aggregate.

---

# 10. Metadata

ValidationJob SHOULD expose:

* identifier;
* validation scope;
* execution state;
* progress;
* creation timestamp;
* start timestamp;
* completion timestamp;
* summary information.

Metadata SHALL NOT affect aggregate identity.

---

# 11. Lifecycle

The lifecycle SHALL consist of:

1. creation;
2. scheduling;
3. execution;
4. ValidationIssue collection;
5. completion or failure;
6. archival.

Completed ValidationJobs MAY remain available for audit purposes.

---

# 12. Business Rules

The following rules SHALL apply:

* every ValidationJob belongs to exactly one Project;
* ValidationIssues SHALL remain associated with the ValidationJob that produced them;
* execution state SHALL always be internally consistent;
* validation SHALL NOT modify validated entities.

---

# 13. Validation

Validation SHALL verify:

* unique identifier;
* existing Project;
* valid execution state;
* valid ValidationIssue references;
* internally consistent timestamps.

Validation failures SHALL be reported through the Validation subsystem.

---

# 14. Persistence

Persistence SHALL be performed through Repository abstractions.

ValidationJob SHALL remain independent of:

* validation engines;
* execution infrastructure;
* storage implementation;
* serialization format.

---

# 15. Events

Business operations MAY produce events including:

* ValidationJobCreatedEvent;
* ValidationJobStartedEvent;
* ValidationJobCompletedEvent;
* ValidationJobFailedEvent;
* ValidationIssueDetectedEvent.

Event publication SHALL occur outside the Aggregate.

---

# 16. Compliance

All validation operations within Voxarium SHALL conform to this specification.

Implementations SHALL preserve aggregate boundaries, execution consistency, stable identity, and business invariants defined by this document.

---

# 17. References

* Project.md
* ValidationRule.md
* ValidationIssue.md
* Document.md
* Timeline.md
* AudioAsset.md
* TextAsset.md
* Task.md
* CreateValidationJobCommand.md
* RunValidationCommand.md
* ValidationJobCreatedEvent.md

---

**End of Document**
