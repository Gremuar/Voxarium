# Tag

**Document Path:**
`spec/100_Domain/Tag.md`

**Document ID:** DOM-037

**Version:** 1.0.0

**Status:** Draft

**Classification:** Normative

---

# 1. Purpose

This document defines the **Tag** domain entity of the Voxarium platform.

A Tag represents a reusable semantic label used to classify, organize, search, and group Project resources. Tags provide a flexible classification mechanism without affecting ownership, hierarchy, or business behavior of the tagged entities.

---

# 2. Scope

This specification defines:

* responsibilities;
* ownership;
* lifecycle;
* relationships;
* business invariants.

Search indexing, user interface presentation, filtering algorithms, and recommendation systems are outside the scope of this specification.

---

# 3. Definition

A **Tag** is a reusable domain entity representing a semantic classification label.

A Tag provides descriptive categorization only and SHALL NOT define business logic.

---

# 4. Responsibilities

Tag SHALL be responsible for:

* classifying Project resources;
* supporting search;
* supporting filtering;
* supporting grouping;
* exposing semantic metadata.

Tag SHALL NOT:

* modify tagged entities;
* define ownership;
* control workflows;
* affect business semantics.

---

# 5. Identity

Every Tag SHALL possess a globally unique identifier.

Its identity SHALL remain stable regardless of:

* display name changes;
* metadata modifications;
* assignment changes.

---

# 6. Ownership

Every Tag SHALL belong to exactly one Project.

Tags SHALL NOT be shared directly between Projects.

A Tag MAY be assigned to zero or more Project entities.

---

# 7. Assignment

A Tag MAY be assigned to:

* Project;
* Folder;
* Document;
* Chapter;
* Fragment;
* Character;
* Speaker;
* VoiceProfile;
* Timeline;
* AudioAsset;
* Collection;
* Dictionary;
* Lexicon;
* Note;
* Bookmark;
* Marker.

Assignments SHALL be reference-based.

Tag assignment SHALL NOT modify the tagged entity.

---

# 8. Relationships

Tag MAY reference:

* Project;
* Collection;
* Folder.

Multiple entities MAY reference the same Tag.

Tag SHALL NOT own referenced entities.

---

# 9. Metadata

Tag SHOULD expose:

* identifier;
* name;
* description;
* color where applicable;
* creation timestamp;
* modification timestamp.

Metadata SHALL NOT alter the semantic meaning of the Tag.

---

# 10. Lifecycle

The lifecycle SHALL consist of:

1. creation;
2. assignment;
3. modification;
4. removal from entities;
5. archival or deletion.

Deleting a Tag SHALL remove only tag assignments.

Tagged entities SHALL remain unchanged.

---

# 11. Business Rules

The following rules SHALL apply:

* every Tag belongs to exactly one Project;
* duplicate Tag names SHOULD NOT exist within the same Project;
* Tag assignment SHALL preserve referential integrity;
* removing a Tag SHALL NOT delete tagged entities.

---

# 12. Validation

Validation SHALL verify:

* unique identifier;
* existing Project;
* valid assignments;
* internally consistent metadata;
* absence of duplicate assignments.

Validation failures SHALL be reported through the Validation subsystem.

---

# 13. Persistence

Persistence SHALL be performed through Repository abstractions.

Tag SHALL remain independent of:

* search engine implementation;
* indexing technology;
* serialization format;
* storage implementation.

---

# 14. Events

Business operations MAY produce events including:

* TagCreatedEvent;
* TagUpdatedEvent;
* TagDeletedEvent;
* TagAssignedEvent;
* TagRemovedEvent.

The Tag entity SHALL NOT publish events directly.

---

# 15. Compliance

All semantic classification labels within Voxarium SHALL conform to this specification.

Implementations SHALL preserve stable identity, ownership boundaries, assignment integrity, and business invariants defined by this document.

---

# 16. References

* Project.md
* Folder.md
* Document.md
* Chapter.md
* Fragment.md
* Character.md
* Speaker.md
* VoiceProfile.md
* Timeline.md
* AudioAsset.md
* Collection.md
* Dictionary.md
* Lexicon.md
* Note.md
* Bookmark.md
* Marker.md
* ValidationIssue.md
* CreateTagCommand.md
* TagCreatedEvent.md

---

**End of Document**
