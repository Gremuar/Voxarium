# Document

**Document Path:**
`spec/100_Domain/Document.md`

**Document ID:** DOM-014

**Version:** 1.0.0

**Status:** Draft

**Classification:** Normative

---

# 1. Purpose

This document defines the **Document** Aggregate Root of the Voxarium platform.

A Document represents the primary textual content container within a Project. It is responsible for organizing hierarchical content, preserving document integrity, and managing the lifecycle of its owned entities.

---

# 2. Scope

This specification defines:

* responsibilities;
* ownership;
* aggregate boundaries;
* lifecycle;
* relationships;
* business invariants.

Rendering, editing implementation, serialization, and speech synthesis are outside the scope of this specification.

---

# 3. Definition

A **Document** is the Aggregate Root representing a structured textual resource within a Project.

It provides the consistency boundary for all document content and related metadata.

---

# 4. Responsibilities

Document SHALL be responsible for:

* maintaining document structure;
* owning document content;
* preserving hierarchical consistency;
* coordinating document-level validation;
* exposing document metadata.

Document SHALL NOT:

* perform speech synthesis;
* manage audio resources;
* execute export operations;
* implement presentation behavior.

---

# 5. Identity

Every Document SHALL possess a globally unique identifier.

Its identity SHALL remain stable regardless of:

* title changes;
* content modifications;
* hierarchy changes;
* metadata updates.

---

# 6. Ownership

Every Document SHALL belong to exactly one Project.

A Document SHALL own:

* Chapters;
* Fragments;
* DocumentMetadata;
* DocumentStatistics.

Owned entities SHALL NOT exist independently.

---

# 7. Aggregate Boundary

Document SHALL be the Aggregate Root.

All modifications to owned entities SHALL occur through the Document Aggregate.

External components SHALL NOT directly modify aggregate members.

---

# 8. Structure

A Document MAY contain:

* Chapters;
* Fragments;
* Notes;
* Bookmarks;
* Metadata.

The exact hierarchy SHALL remain internally consistent.

---

# 9. Relationships

Document MAY reference:

* Project;
* Folder;
* Character;
* Speaker;
* Dictionary;
* Timeline;
* Collection;
* ValidationIssue.

Document SHALL NOT own entities outside its aggregate.

---

# 10. Metadata

A Document SHOULD expose:

* identifier;
* title;
* description;
* language;
* creation timestamp;
* modification timestamp;
* version.

Metadata SHALL remain independent of document identity.

---

# 11. Lifecycle

The lifecycle SHALL consist of:

1. creation;
2. population with content;
3. modification;
4. validation;
5. archival or deletion.

Deleting a Document SHALL delete all entities belonging to its aggregate.

---

# 12. Business Rules

The following rules SHALL apply:

* every Document belongs to one Project;
* every owned entity belongs to exactly one Document;
* aggregate consistency SHALL be preserved after every modification;
* orphan aggregate members SHALL NOT exist.

---

# 13. Aggregate Rules

Document SHALL coordinate:

* Chapter lifecycle;
* Fragment lifecycle;
* metadata consistency;
* statistics updates;
* validation.

Aggregate members SHALL NOT modify aggregate state independently.

---

# 14. Validation

Validation SHALL verify:

* unique identifier;
* existing parent Project;
* valid hierarchy;
* consistent metadata;
* aggregate integrity.

Validation failures SHALL be reported through the Validation subsystem.

---

# 15. Persistence

Persistence SHALL be performed through Repository abstractions.

Document SHALL remain independent of:

* serialization format;
* storage implementation;
* editor implementation.

---

# 16. Events

Business operations MAY produce events including:

* DocumentCreatedEvent;
* DocumentUpdatedEvent;
* DocumentDeletedEvent;
* DocumentValidatedEvent.

Events SHALL be published by the Application layer.

---

# 17. Compliance

All structured textual resources within Voxarium SHALL conform to this specification.

Implementations SHALL preserve aggregate boundaries, ownership rules, referential integrity, and business invariants defined by this document.

---

# 18. References

* Project.md
* Chapter.md
* Fragment.md
* DocumentMetadata.md
* DocumentStatistics.md
* Folder.md
* Collection.md
* ValidationIssue.md
* CreateDocumentCommand.md
* DocumentCreatedEvent.md

---

**End of Document**
