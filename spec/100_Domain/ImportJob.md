# ImportJob

**Document Path:**
`spec/100_Domain/ImportJob.md`

**Document ID:** DOM-024

**Version:** 1.0.0

**Status:** Draft

**Classification:** Normative

---

# 1. Purpose

This document defines the **ImportJob** domain entity of the Voxarium platform.

An ImportJob represents a business process responsible for importing external resources into a Project. It models the complete lifecycle of an import operation, including its configuration, execution state, traceability, and resulting domain objects, independently of the underlying import implementation.

---

# 2. Scope

This specification defines:

* responsibilities;
* ownership;
* lifecycle;
* state model;
* relationships;
* business invariants.

Parsing algorithms, file formats, storage mechanisms, and external integrations are outside the scope of this specification.

---

# 3. Definition

An **ImportJob** is a domain entity representing a single import operation initiated for a Project.

The entity models the business process rather than the technical implementation of data import.

---

# 4. Responsibilities

ImportJob SHALL be responsible for:

* representing an import request;
* tracking execution progress;
* maintaining import metadata;
* preserving import traceability;
* exposing execution status.

ImportJob SHALL NOT:

* parse external formats;
* modify imported files;
* perform persistence directly;
* communicate with external storage providers.

---

# 5. Identity

Every ImportJob SHALL possess a globally unique identifier.

Its identity SHALL remain stable throughout the lifetime of the Project.

---

# 6. Ownership

Every ImportJob SHALL belong to exactly one Project.

All imported resources SHALL preserve traceability to the originating ImportJob.

---

# 7. Lifecycle

The lifecycle SHALL consist of:

1. creation;
2. scheduling;
3. validation;
4. execution;
5. completion or failure;
6. archival.

Completed ImportJobs SHALL remain available for audit purposes unless explicitly removed according to Project policy.

---

# 8. State Model

An ImportJob SHALL occupy exactly one of the following states:

* Created;
* Queued;
* Running;
* Completed;
* Failed;
* Cancelled.

State transitions SHALL be deterministic.

Invalid transitions SHALL be rejected.

---

# 9. Input

An ImportJob MAY reference:

* external documents;
* audio resources;
* subtitle resources;
* dictionaries;
* timelines;
* project packages;
* import configuration.

Input resources SHALL remain immutable during execution.

---

# 10. Output

Successful execution MAY create:

* Documents;
* AudioAssets;
* Dictionaries;
* Timelines;
* Collections;
* other supported domain entities.

Created entities SHALL preserve traceability to the ImportJob.

---

# 11. Relationships

ImportJob MAY reference:

* Project;
* Document;
* AudioAsset;
* Dictionary;
* Timeline;
* Collection;
* ImportPreset.

ImportJob SHALL NOT own imported domain entities after successful creation.

---

# 12. Metadata

ImportJob SHOULD expose:

* identifier;
* creation timestamp;
* execution timestamp;
* completion timestamp;
* execution duration;
* initiating actor where applicable;
* execution status.

Metadata SHALL remain independent of the import implementation.

---

# 13. Business Rules

The following rules SHALL apply:

* every ImportJob belongs to exactly one Project;
* every ImportJob SHALL have exactly one execution state;
* completed ImportJobs SHALL remain immutable except administrative metadata;
* imported entities SHALL preserve import provenance.

---

# 14. Validation

Validation SHALL verify:

* unique identifier;
* existing Project;
* valid execution state;
* internally consistent timestamps;
* valid configuration.

Validation failures SHALL be reported through the Validation subsystem.

---

# 15. Failure Handling

Failed ImportJobs SHALL preserve:

* execution history;
* diagnostic information;
* failure state.

Failure SHALL NOT leave the Project in an inconsistent state.

Partial imports SHALL follow transactional rules defined by the Application layer.

---

# 16. Persistence

Persistence SHALL be performed through Repository abstractions.

ImportJob SHALL remain independent of:

* storage technology;
* serialization format;
* parser implementation.

---

# 17. Events

Business operations MAY produce events including:

* ImportStartedEvent;
* ImportCompletedEvent;
* ImportFailedEvent;
* ImportCancelledEvent.

The ImportJob entity SHALL NOT publish events directly.

---

# 18. Compliance

All import operations within Voxarium SHALL conform to this specification.

Implementations SHALL preserve identity, lifecycle integrity, traceability, and business invariants defined by this document.

---

# 19. References

* Project.md
* Document.md
* AudioAsset.md
* Dictionary.md
* Timeline.md
* Collection.md
* ValidationIssue.md
* ImportProjectCommand.md
* ImportCompletedEvent.md

---

**End of Document**
