# Bookmark

**Document Path:**
`spec/100_Domain/Bookmark.md`

**Document ID:** DOM-007

**Version:** 1.0.0

**Status:** Draft

**Classification:** Normative

---

# 1. Purpose

This document defines the **Bookmark** domain entity of the Voxarium platform.

A Bookmark represents a persistent user-defined reference to a significant location within a Project. It enables quick navigation without modifying the business content of the Project.

---

# 2. Scope

This specification defines:

* responsibilities;
* ownership;
* lifecycle;
* relationships;
* business invariants.

User interface presentation is outside the scope of this document.

---

# 3. Definition

A **Bookmark** is a domain entity representing a named reference to a logical location within a Project.

A Bookmark identifies *where* to return, not *how* the location is displayed.

---

# 4. Responsibilities

Bookmark SHALL be responsible for:

* identifying a navigation target;
* storing user-defined metadata;
* supporting persistent navigation;
* maintaining referential integrity.

Bookmark SHALL NOT:

* modify project content;
* alter timeline state;
* execute application commands;
* perform presentation logic.

---

# 5. Identity

Every Bookmark SHALL possess a globally unique identifier.

Its identity SHALL remain stable throughout its lifetime.

---

# 6. Ownership

Every Bookmark SHALL belong to exactly one Project.

Bookmarks SHALL NOT be shared directly between Projects.

---

# 7. Bookmark Target

A Bookmark SHALL reference exactly one logical target.

A target MAY be:

* Project;
* Folder;
* Document;
* Chapter;
* Scene;
* Fragment;
* Timeline;
* TimelineMarker;
* ValidationIssue;
* another domain object explicitly supporting bookmarks.

The referenced target SHALL exist while the Bookmark remains valid.

---

# 8. Metadata

A Bookmark SHOULD expose:

* identifier;
* title;
* optional description;
* creation timestamp;
* modification timestamp;
* optional color or category;
* optional tags.

Metadata SHALL NOT influence business behavior.

---

# 9. Relationships

Bookmark MAY reference:

* Project;
* Folder;
* Document;
* Chapter;
* Scene;
* Fragment;
* Timeline;
* TimelineMarker;
* ValidationIssue.

Bookmark SHALL NOT own referenced entities.

---

# 10. Lifecycle

The lifecycle SHALL consist of:

1. creation;
2. association with a target;
3. modification;
4. usage;
5. deletion.

Deletion of a Bookmark SHALL NOT modify its target.

---

# 11. Business Rules

The following rules SHALL apply:

* every Bookmark belongs to one Project;
* every Bookmark references exactly one valid target;
* bookmark titles SHOULD be unique within the same Project;
* removing a referenced object SHALL invalidate or remove dependent Bookmarks according to application policy.

---

# 12. Validation

Validation SHALL verify:

* unique identifier;
* existing Project;
* valid referenced target;
* internally consistent metadata.

Validation failures SHALL be reported through the Validation subsystem.

---

# 13. Navigation

Bookmarks provide logical navigation only.

Navigation behavior SHALL be implemented by the Application layer and User Interface.

The Bookmark entity SHALL remain independent of presentation logic.

---

# 14. Persistence

Persistence SHALL be performed through Repository abstractions.

Bookmark SHALL remain independent of:

* serialization format;
* storage implementation;
* user interface state.

---

# 15. Events

Business operations MAY produce events including:

* BookmarkCreatedEvent;
* BookmarkUpdatedEvent;
* BookmarkDeletedEvent.

The entity itself SHALL NOT publish events.

---

# 16. Compliance

All persistent navigation references within Voxarium SHALL conform to this specification.

Implementations SHALL preserve the identity, ownership, and referential integrity defined herein.

---

# 17. References

* Project.md
* Folder.md
* Document.md
* Chapter.md
* Scene.md
* Fragment.md
* Timeline.md
* TimelineMarker.md
* ValidationIssue.md
* CreateBookmarkCommand.md
* BookmarkCreatedEvent.md

---

**End of Document**
