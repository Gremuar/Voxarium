# Metadata

**Document Path:**
`spec/100_Domain/Metadata.md`

**Document ID:** DOM-029

**Version:** 1.0.0

**Status:** Draft

**Classification:** Normative

---

# 1. Purpose

This document defines the **Metadata** domain entity of the Voxarium platform.

Metadata represents a reusable collection of descriptive business attributes associated with a domain entity. It provides extensible descriptive information without altering the business identity or behavior of the owning entity.

Metadata is intended as a generic abstraction reused throughout the domain model.

---

# 2. Scope

This specification defines:

* responsibilities;
* ownership;
* lifecycle;
* relationships;
* business invariants.

Serialization formats, indexing engines, and user interface presentation are outside the scope of this specification.

---

# 3. Definition

A **Metadata** is a domain entity representing structured descriptive information attached to another domain entity.

Metadata SHALL describe an entity but SHALL NOT define its business identity.

---

# 4. Responsibilities

Metadata SHALL be responsible for:

* storing descriptive attributes;
* supporting search and classification;
* providing extensibility;
* preserving semantic consistency;
* exposing descriptive information.

Metadata SHALL NOT:

* modify business behavior;
* define entity identity;
* own business entities;
* execute business logic.

---

# 5. Identity

Metadata SHALL inherit the identity boundary of its owning entity.

Metadata SHALL NOT exist independently.

Each owning entity MAY own at most one Metadata instance unless explicitly defined otherwise by its specification.

---

# 6. Ownership

Metadata SHALL belong to exactly one domain entity.

Ownership SHALL remain immutable throughout its lifecycle.

Creation and deletion SHALL be coordinated by the owning Aggregate Root.

---

# 7. Metadata Structure

Metadata MAY contain:

* title;
* description;
* keywords;
* tags;
* author information;
* version information;
* creation timestamp;
* modification timestamp;
* custom business attributes.

The schema MAY be extended without affecting existing business semantics.

---

# 8. Relationships

Metadata MAY reference:

* Project;
* Document;
* Chapter;
* Fragment;
* Collection;
* Folder;
* Tag;
* Language.

Metadata SHALL NOT own external entities.

---

# 9. Lifecycle

The lifecycle SHALL consist of:

1. creation together with the owning entity;
2. modification;
3. validation;
4. deletion together with the owning entity.

Independent lifecycle management SHALL NOT be permitted.

---

# 10. Business Rules

The following rules SHALL apply:

* Metadata SHALL always have exactly one owner;
* Metadata SHALL NOT redefine business identity;
* Metadata SHALL remain internally consistent;
* modifications SHALL NOT invalidate the owning entity.

---

# 11. Validation

Validation SHALL verify:

* existing owner;
* internally consistent attributes;
* valid references;
* compliance with Project conventions.

Validation failures SHALL be reported through the Validation subsystem.

---

# 12. Persistence

Persistence SHALL be performed through the Repository of the owning Aggregate.

Metadata SHALL remain independent of:

* storage implementation;
* serialization format;
* indexing technology.

---

# 13. Events

Business operations MAY produce events including:

* MetadataUpdatedEvent;
* MetadataValidatedEvent.

Event publication SHALL occur through the owning Aggregate rather than the Metadata entity itself.

---

# 14. Compliance

All reusable descriptive metadata within Voxarium SHALL conform to this specification.

Implementations SHALL preserve ownership boundaries, descriptive semantics, and business invariants defined by this document.

---

# 15. References

* Project.md
* Document.md
* Chapter.md
* Fragment.md
* Collection.md
* Folder.md
* Tag.md
* Language.md
* ValidationIssue.md
* UpdateMetadataCommand.md
* MetadataUpdatedEvent.md

---

**End of Document**
