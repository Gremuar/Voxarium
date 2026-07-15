# Note

**Document Path:**
`spec/100_Domain/Note.md`

**Document ID:** DOM-030

**Version:** 1.0.0

**Status:** Draft

**Classification:** Normative

---

# 1. Purpose

This document defines the **Note** domain entity of the Voxarium platform.

A Note represents a persistent textual annotation associated with one or more Project entities. It provides contextual information intended for authors, editors, reviewers, and automation workflows without becoming part of the primary project content.

---

# 2. Scope

This specification defines:

* responsibilities;
* ownership;
* lifecycle;
* relationships;
* business invariants.

Rendering, collaboration interfaces, and notification mechanisms are outside the scope of this specification.

---

# 3. Definition

A **Note** is a domain entity representing supplementary textual information attached to a Project entity.

A Note provides contextual information and SHALL NOT modify the semantic meaning of the referenced entity.

---

# 4. Responsibilities

Note SHALL be responsible for:

* storing annotation text;
* preserving contextual information;
* supporting review workflows;
* supporting collaboration;
* exposing descriptive metadata.

Note SHALL NOT:

* modify business entities;
* participate in speech generation;
* execute workflows;
* alter document structure.

---

# 5. Identity

Every Note SHALL possess a globally unique identifier.

Its identity SHALL remain stable regardless of:

* text modifications;
* metadata updates;
* target changes permitted by application policy.

---

# 6. Ownership

Every Note SHALL belong to exactly one Project.

A Note SHALL reference one primary target entity.

Ownership of the referenced entity SHALL remain unchanged.

---

# 7. Target

A Note MAY reference:

* Project;
* Folder;
* Document;
* Chapter;
* Fragment;
* Character;
* Speaker;
* Timeline;
* TimelineMarker;
* ValidationIssue;
* Bookmark.

Referenced entities SHALL remain valid while the Note exists.

---

# 8. Content

A Note SHALL contain textual information.

A Note MAY additionally contain:

* title;
* category;
* author;
* creation timestamp;
* modification timestamp;
* tags;
* custom metadata.

The content SHALL remain independent of presentation.

---

# 9. Relationships

Note MAY reference:

* Project;
* Document;
* Chapter;
* Fragment;
* Character;
* Timeline;
* Bookmark;
* Tag;
* ValidationIssue.

Note SHALL NOT own referenced entities.

---

# 10. Lifecycle

The lifecycle SHALL consist of:

1. creation;
2. association with a target;
3. modification;
4. review;
5. archival or deletion.

Deleting a Note SHALL NOT affect the referenced entity.

---

# 11. Business Rules

The following rules SHALL apply:

* every Note belongs to exactly one Project;
* every Note SHALL reference at most one primary target;
* Note identity SHALL remain immutable;
* Notes SHALL preserve referential integrity.

---

# 12. Validation

Validation SHALL verify:

* unique identifier;
* existing Project;
* valid target reference;
* non-empty textual content where required;
* internally consistent metadata.

Validation failures SHALL be reported through the Validation subsystem.

---

# 13. Persistence

Persistence SHALL be performed through Repository abstractions.

Note SHALL remain independent of:

* serialization format;
* storage implementation;
* collaboration infrastructure.

---

# 14. Events

Business operations MAY produce events including:

* NoteCreatedEvent;
* NoteUpdatedEvent;
* NoteDeletedEvent.

The Note entity SHALL NOT publish events directly.

---

# 15. Compliance

All persistent annotations within Voxarium SHALL conform to this specification.

Implementations SHALL preserve stable identity, ownership boundaries, contextual semantics, and referential integrity defined by this document.

---

# 16. References

* Project.md
* Folder.md
* Document.md
* Chapter.md
* Fragment.md
* Character.md
* Speaker.md
* Timeline.md
* TimelineMarker.md
* Bookmark.md
* Tag.md
* ValidationIssue.md
* CreateNoteCommand.md
* NoteCreatedEvent.md

---

**End of Document**
