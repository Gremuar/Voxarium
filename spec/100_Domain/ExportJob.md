# ExportJob

**Document Path:**
`spec/100_Domain/ExportJob.md`

**Document ID:** DOM-018

**Version:** 1.0.0

**Status:** Draft

**Classification:** Normative

---

# 1. Purpose

This document defines the **ExportJob** domain entity of the Voxarium platform.

An ExportJob represents a business process responsible for exporting Project resources into one or more external representations. It captures the business intent, execution state, configuration, and resulting artifacts independently of the export implementation.

---

# 2. Scope

This specification defines:

* responsibilities;
* ownership;
* lifecycle;
* state model;
* relationships;
* business invariants.

Export engines, serialization formats, and filesystem operations are outside the scope of this specification.

---

# 3. Definition

An **ExportJob** is a domain entity representing a single export operation initiated within a Project.

The entity models the business process rather than the export implementation.

---

# 4. Responsibilities

ExportJob SHALL be responsible for:

* representing an export request;
* tracking execution progress;
* maintaining export metadata;
* referencing exported artifacts;
* exposing execution status.

ExportJob SHALL NOT:

* serialize project data;
* write files;
* communicate with external storage;
* perform format conversion.

---

# 5. Identity

Every ExportJob SHALL possess a globally unique identifier.

Its identity SHALL remain stable throughout the lifetime of the Project.

---

# 6. Ownership

Every ExportJob SHALL belong to exactly one Project.

Generated export artifacts SHALL preserve traceability to the originating ExportJob.

---

# 7. Lifecycle

The lifecycle SHALL consist of:

1. creation;
2. scheduling;
3. execution;
4. completion or failure;
5. archival.

Completed ExportJobs SHALL remain available for project history unless explicitly removed.

---

# 8. State Model

An ExportJob SHALL occupy exactly one of the following states:

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

An ExportJob MAY reference:

* Project;
* Documents;
* AudioAssets;
* Timelines;
* Collections;
* GenerationHistory;
* export configuration.

All referenced entities SHALL exist before execution begins.

---

# 10. Output

Successful execution MAY produce:

* exported packages;
* exported documents;
* exported audio resources;
* export reports;
* execution diagnostics.

The resulting artifacts SHALL remain associated with the ExportJob.

---

# 11. Relationships

ExportJob MAY reference:

* Project;
* Document;
* AudioAsset;
* Timeline;
* Collection;
* ExportPreset;
* GenerationHistory.

ExportJob SHALL NOT own these entities.

---

# 12. Metadata

ExportJob SHOULD expose:

* identifier;
* creation timestamp;
* execution timestamp;
* completion timestamp;
* execution duration;
* initiating actor where applicable;
* current status.

Metadata SHALL remain independent of export implementation.

---

# 13. Business Rules

The following rules SHALL apply:

* every ExportJob belongs to exactly one Project;
* every ExportJob SHALL have exactly one execution state;
* completed jobs SHALL be immutable except administrative metadata;
* exported artifacts SHALL preserve traceability.

---

# 14. Validation

Validation SHALL verify:

* unique identifier;
* existing Project;
* valid references;
* valid execution state;
* internally consistent timestamps.

Validation failures SHALL be reported through the Validation subsystem.

---

# 15. Failure Handling

Failed ExportJobs SHALL preserve:

* failure state;
* execution history;
* diagnostic information.

Failure SHALL NOT modify authoritative Project data.

---

# 16. Persistence

Persistence SHALL be performed through Repository abstractions.

ExportJob SHALL remain independent of:

* serialization technologies;
* storage providers;
* export engines.

---

# 17. Events

Business operations MAY produce events including:

* ExportStartedEvent;
* ExportCompletedEvent;
* ExportFailedEvent;
* ExportCancelledEvent.

Event publication SHALL occur outside the entity.

---

# 18. Compliance

All export operations within Voxarium SHALL conform to this specification.

Implementations SHALL preserve identity, traceability, lifecycle integrity, and business invariants defined herein.

---

# 19. References

* Project.md
* Document.md
* AudioAsset.md
* Timeline.md
* Collection.md
* GenerationHistory.md
* ValidationIssue.md
* ExportProjectCommand.md
* ExportCompletedEvent.md

---

**End of Document**
