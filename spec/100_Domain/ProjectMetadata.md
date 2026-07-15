# ProjectMetadata

**Document Path:**
`spec/100_Domain/ProjectMetadata.md`

**Document ID:** DOM-052

**Version:** 1.0.0

**Status:** Draft

**Classification:** Normative

---

# 1. Purpose

This document defines the **ProjectMetadata** domain entity of the Voxarium platform.

ProjectMetadata represents descriptive information associated with a Project. It stores identification, descriptive, and informational attributes that support organization, discovery, versioning, and documentation without affecting the business behavior or identity of the Project itself.

---

# 2. Scope

This specification defines:

* responsibilities;
* ownership;
* lifecycle;
* relationships;
* business invariants.

Persistence implementation, user interface presentation, search indexing, and synchronization mechanisms are outside the scope of this specification.

---

# 3. Definition

A **ProjectMetadata** is a domain entity representing descriptive information owned by a Project.

It contains informational attributes that describe a Project but SHALL NOT define its business semantics.

---

# 4. Responsibilities

ProjectMetadata SHALL be responsible for:

* describing a Project;
* exposing informational attributes;
* supporting Project discovery;
* supporting Project documentation;
* preserving metadata consistency.

ProjectMetadata SHALL NOT:

* modify Project behavior;
* own Project resources;
* execute business logic;
* manage Project lifecycle.

---

# 5. Identity

ProjectMetadata SHALL inherit the identity of its owning Project.

It SHALL NOT exist independently.

Exactly one ProjectMetadata entity SHALL exist for each Project.

---

# 6. Ownership

ProjectMetadata SHALL belong to exactly one Project.

Ownership SHALL remain immutable throughout its lifecycle.

Lifecycle management SHALL be coordinated by the owning Project Aggregate.

---

# 7. Metadata Contents

ProjectMetadata MAY define:

* display name;
* description;
* author;
* organization;
* copyright;
* version;
* keywords;
* category;
* documentation links;
* custom metadata.

Metadata SHALL remain descriptive only.

---

# 8. Relationships

ProjectMetadata MAY reference:

* Project;
* Workspace;
* Tag;
* Language.

Referenced entities SHALL remain external to ProjectMetadata.

---

# 9. Versioning

ProjectMetadata MAY maintain:

* metadata version;
* creation timestamp;
* modification timestamp;
* optional revision information.

Metadata versioning SHALL NOT modify Project identity.

---

# 10. Lifecycle

The lifecycle SHALL consist of:

1. creation with the Project;
2. configuration;
3. validation;
4. modification;
5. deletion together with the Project.

Independent lifecycle management SHALL NOT be permitted.

---

# 11. Business Rules

The following rules SHALL apply:

* every Project SHALL own exactly one ProjectMetadata;
* ProjectMetadata SHALL have exactly one owner;
* metadata SHALL remain internally consistent;
* descriptive information SHALL NOT alter Project semantics.

---

# 12. Validation

Validation SHALL verify:

* existing Project;
* internally consistent metadata;
* valid references;
* compliance with naming and documentation conventions.

Validation failures SHALL be reported through the Validation subsystem.

---

# 13. Persistence

Persistence SHALL be performed through the Repository of the owning Project.

ProjectMetadata SHALL remain independent of:

* storage implementation;
* serialization format;
* indexing technology.

---

# 14. Events

Business operations MAY produce events including:

* ProjectMetadataUpdatedEvent;
* ProjectMetadataValidatedEvent.

Event publication SHALL occur through the owning Project Aggregate.

---

# 15. Compliance

All Project descriptive metadata within Voxarium SHALL conform to this specification.

Implementations SHALL preserve ownership boundaries, metadata consistency, and business invariants defined by this document.

---

# 16. References

* Project.md
* Workspace.md
* Tag.md
* Language.md
* ValidationIssue.md
* UpdateProjectMetadataCommand.md
* ProjectMetadataUpdatedEvent.md

---

**End of Document**
