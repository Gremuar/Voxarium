# Folder

**Document Path:**
`spec/100_Domain/Folder.md`

**Document ID:** DOM-019

**Version:** 1.0.0

**Status:** Draft

**Classification:** Normative

---

# 1. Purpose

This document defines the **Folder** Aggregate Root of the Voxarium platform.

A Folder represents a hierarchical organizational container within a Project. It is used to organize Project resources into a tree structure without affecting the business semantics or ownership of the contained entities.

---

# 2. Scope

This specification defines:

* responsibilities;
* ownership;
* hierarchy rules;
* lifecycle;
* relationships;
* business invariants.

User interface presentation and filesystem mapping are outside the scope of this specification.

---

# 3. Definition

A **Folder** is a domain entity representing a logical container for organizing Project resources.

A Folder provides hierarchical organization only and SHALL NOT define ownership of contained resources.

---

# 4. Responsibilities

Folder SHALL be responsible for:

* organizing Project resources;
* maintaining hierarchical structure;
* exposing organizational metadata;
* preserving deterministic ordering;
* supporting navigation.

Folder SHALL NOT:

* own contained resources;
* modify business entities;
* implement access control;
* perform filesystem operations.

---

# 5. Identity

Every Folder SHALL possess a globally unique identifier.

Its identity SHALL remain stable regardless of:

* name changes;
* movement within the hierarchy;
* membership changes.

---

# 6. Ownership

Every Folder SHALL belong to exactly one Project.

Folders SHALL NOT be shared between Projects.

A Folder MAY contain references to domain entities, but SHALL NOT become their owner.

---

# 7. Hierarchy

Folders SHALL form a rooted tree.

Each Folder SHALL have:

* zero or one parent Folder;
* zero or more child Folders.

The hierarchy SHALL NOT contain cycles.

---

# 8. Contents

A Folder MAY reference:

* Documents;
* Collections;
* Dictionaries;
* AudioAssets;
* TextAssets;
* Timelines;
* other Folder-supported entities.

Membership SHALL be reference-based.

Moving a resource between Folders SHALL NOT change its identity.

---

# 9. Relationships

Folder MAY reference:

* Project;
* Folder;
* Document;
* Collection;
* Dictionary;
* AudioAsset;
* TextAsset;
* Timeline.

Folder SHALL NOT own external entities.

---

# 10. Metadata

A Folder SHOULD expose:

* identifier;
* name;
* description;
* creation timestamp;
* modification timestamp;
* ordering information.

Metadata SHALL NOT affect business behavior.

---

# 11. Lifecycle

The lifecycle SHALL consist of:

1. creation;
2. insertion into hierarchy;
3. population with references;
4. modification;
5. deletion.

Deleting a Folder SHALL NOT delete referenced resources.

Application policy SHALL determine how child Folders are handled during deletion.

---

# 12. Business Rules

The following rules SHALL apply:

* every Folder belongs to one Project;
* hierarchy SHALL remain acyclic;
* sibling ordering SHALL be deterministic;
* resources MAY exist outside any Folder;
* Folder membership SHALL NOT define ownership.

---

# 13. Validation

Validation SHALL verify:

* unique identifier;
* existing Project;
* valid parent reference;
* absence of hierarchy cycles;
* valid referenced resources.

Validation failures SHALL be reported through the Validation subsystem.

---

# 14. Persistence

Persistence SHALL be performed through Repository abstractions.

Folder SHALL remain independent of:

* filesystem layout;
* serialization format;
* storage implementation.

---

# 15. Events

Business operations MAY produce events including:

* FolderCreatedEvent;
* FolderMovedEvent;
* FolderUpdatedEvent;
* FolderDeletedEvent.

The Folder entity SHALL NOT publish events directly.

---

# 16. Compliance

All hierarchical organizational containers within Voxarium SHALL conform to this specification.

Implementations SHALL preserve hierarchy integrity, stable identity, deterministic ordering, and ownership boundaries.

---

# 17. References

* Project.md
* Document.md
* Collection.md
* Dictionary.md
* AudioAsset.md
* TextAsset.md
* Timeline.md
* ValidationIssue.md
* CreateFolderCommand.md
* MoveFolderCommand.md
* FolderCreatedEvent.md

---

**End of Document**
