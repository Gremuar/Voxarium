# FragmentGroup

**Document Path:**
`spec/100_Domain/FragmentGroup.md`

**Document ID:** DOM-021

**Version:** 1.0.0

**Status:** Draft

**Classification:** Normative

---

# 1. Purpose

This document defines the **FragmentGroup** domain entity of the Voxarium platform.

A FragmentGroup represents a logical grouping of Fragments within a Project. It enables semantic organization of related textual content without changing the ownership or hierarchical structure of the Document Aggregate.

---

# 2. Scope

This specification defines:

* responsibilities;
* ownership;
* lifecycle;
* relationships;
* business invariants.

Document editing, rendering, and speech generation are outside the scope of this specification.

---

# 3. Definition

A **FragmentGroup** is a domain entity representing a reusable logical collection of Fragments.

A FragmentGroup expresses semantic relationships between Fragments rather than document hierarchy.

---

# 4. Responsibilities

FragmentGroup SHALL be responsible for:

* grouping related Fragments;
* preserving semantic associations;
* exposing group metadata;
* supporting workflow organization;
* maintaining membership integrity.

FragmentGroup SHALL NOT:

* own Fragments;
* modify Fragment content;
* affect Document hierarchy;
* execute business workflows.

---

# 5. Identity

Every FragmentGroup SHALL possess a globally unique identifier.

Its identity SHALL remain stable regardless of:

* name changes;
* membership changes;
* metadata modifications.

---

# 6. Ownership

Every FragmentGroup SHALL belong to exactly one Project.

FragmentGroups SHALL NOT span multiple Projects.

A Fragment MAY belong to multiple FragmentGroups unless restricted by application policy.

---

# 7. Membership

A FragmentGroup SHALL contain zero or more Fragment references.

Membership SHALL be reference-based.

Removing a Fragment from a FragmentGroup SHALL NOT affect the Fragment itself.

Deleting a FragmentGroup SHALL NOT affect its members.

---

# 8. Relationships

FragmentGroup MAY reference:

* Project;
* Fragment;
* Chapter;
* Character;
* Speaker;
* Collection;
* Tag.

FragmentGroup SHALL NOT own referenced entities.

---

# 9. Metadata

FragmentGroup SHOULD expose:

* identifier;
* name;
* description;
* creation timestamp;
* modification timestamp;
* optional category;
* optional tags.

Metadata SHALL NOT alter business semantics.

---

# 10. Lifecycle

The lifecycle SHALL consist of:

1. creation;
2. population with Fragment references;
3. modification;
4. usage;
5. archival or deletion.

Deletion SHALL remove only the group itself.

---

# 11. Business Rules

The following rules SHALL apply:

* every FragmentGroup belongs to exactly one Project;
* membership SHALL be reference-based;
* duplicate Fragment references within the same FragmentGroup SHALL NOT be permitted;
* membership SHALL preserve referential integrity.

---

# 12. Validation

Validation SHALL verify:

* unique identifier;
* existing Project;
* valid Fragment references;
* absence of duplicate members;
* internally consistent metadata.

Validation failures SHALL be reported through the Validation subsystem.

---

# 13. Persistence

Persistence SHALL be performed through Repository abstractions.

FragmentGroup SHALL remain independent of:

* serialization format;
* storage implementation;
* document editor implementation.

---

# 14. Events

Business operations MAY produce events including:

* FragmentGroupCreatedEvent;
* FragmentGroupUpdatedEvent;
* FragmentGroupDeletedEvent;
* FragmentAddedToGroupEvent;
* FragmentRemovedFromGroupEvent.

Event publication SHALL occur outside the entity.

---

# 15. Compliance

All logical Fragment collections within Voxarium SHALL conform to this specification.

Implementations SHALL preserve stable identity, reference integrity, and ownership boundaries defined by this document.

---

# 16. References

* Project.md
* Fragment.md
* Chapter.md
* Character.md
* Speaker.md
* Collection.md
* Tag.md
* ValidationIssue.md
* CreateFragmentGroupCommand.md
* AddFragmentToGroupCommand.md
* RemoveFragmentFromGroupCommand.md
* FragmentGroupCreatedEvent.md

---

**End of Document**
