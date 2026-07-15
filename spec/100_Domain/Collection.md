# Collection

**Document Path:**
`spec/100_Domain/Collection.md`

**Document ID:** DOM-010

**Version:** 1.0.0

**Status:** Draft

**Classification:** Normative

---

# 1. Purpose

This document defines the **Collection** domain entity of the Voxarium platform.

A Collection represents a named logical grouping of domain objects within a Project. It enables users to organize related resources independently of the physical project hierarchy.

---

# 2. Scope

This specification defines:

* responsibilities;
* ownership;
* lifecycle;
* relationships;
* business invariants.

Presentation, visualization, and storage implementation are outside the scope of this specification.

---

# 3. Definition

A **Collection** is a domain entity representing a reusable logical grouping of Project resources.

A Collection expresses semantic organization rather than ownership.

---

# 4. Responsibilities

Collection SHALL be responsible for:

* grouping related domain objects;
* providing reusable logical organization;
* exposing collection metadata;
* maintaining membership integrity.

Collection SHALL NOT:

* own member entities;
* duplicate project content;
* modify member objects;
* affect business identity of contained entities.

---

# 5. Identity

Every Collection SHALL possess a globally unique identifier.

Its identity SHALL remain stable regardless of:

* name changes;
* membership changes;
* metadata updates.

---

# 6. Ownership

Every Collection SHALL belong to exactly one Project.

Collections SHALL NOT span multiple Projects.

Cross-project transfer SHALL occur only through import or duplication workflows.

---

# 7. Membership

A Collection MAY contain references to supported domain entities, including:

* Document;
* Chapter;
* Scene;
* Fragment;
* Character;
* Speaker;
* Voice;
* Dictionary;
* AudioAsset;
* TextAsset;
* other collection-enabled entities.

Membership SHALL be reference-based.

The Collection SHALL NOT become the owner of its members.

---

# 8. Relationships

Collection MAY reference:

* Project;
* Folder;
* Document;
* Character;
* Speaker;
* Voice;
* Dictionary;
* AudioAsset;
* TextAsset;
* Tag.

Collection SHALL NOT introduce cyclic ownership relationships.

---

# 9. Metadata

A Collection SHOULD expose:

* identifier;
* name;
* description;
* creation timestamp;
* modification timestamp;
* optional category;
* optional tags.

Metadata SHALL NOT influence business behavior.

---

# 10. Lifecycle

The lifecycle SHALL consist of:

1. creation;
2. population;
3. modification;
4. usage;
5. archival or deletion.

Deleting a Collection SHALL NOT delete its members.

---

# 11. Business Rules

The following rules SHALL apply:

* every Collection belongs to exactly one Project;
* members SHALL remain independently managed;
* duplicate membership MAY be permitted according to collection policy;
* removal of a member from a Collection SHALL NOT delete the underlying entity.

---

# 12. Validation

Validation SHALL verify:

* unique identifier;
* existing Project;
* valid member references;
* consistent metadata;
* absence of ownership violations.

Validation failures SHALL be reported through the Validation subsystem.

---

# 13. Persistence

Persistence SHALL be performed through Repository abstractions.

Collection SHALL remain independent of:

* serialization format;
* storage technology;
* presentation layer.

---

# 14. Events

Business operations MAY produce events including:

* CollectionCreatedEvent;
* CollectionUpdatedEvent;
* CollectionDeletedEvent;
* CollectionMemberAddedEvent;
* CollectionMemberRemovedEvent.

The Collection entity SHALL NOT publish events directly.

---

# 15. Compliance

All reusable logical groupings within Voxarium SHALL conform to this specification.

Implementations SHALL preserve reference integrity, ownership boundaries, and business invariants defined by this document.

---

# 16. References

* Project.md
* Folder.md
* Document.md
* Chapter.md
* Scene.md
* Fragment.md
* Character.md
* Speaker.md
* Voice.md
* Dictionary.md
* AudioAsset.md
* TextAsset.md
* Tag.md
* ValidationIssue.md
* CreateCollectionCommand.md
* CollectionCreatedEvent.md

---

**End of Document**
