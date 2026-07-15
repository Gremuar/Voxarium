# Marker

**Document Path:**
`spec/100_Domain/Marker.md`

**Document ID:** DOM-028

**Version:** 1.0.0

**Status:** Draft

**Classification:** Normative

---

# 1. Purpose

This document defines the **Marker** domain entity of the Voxarium platform.

A Marker represents a persistent logical annotation attached to a position within Project content. Markers identify meaningful locations used for navigation, editing, validation, synchronization, review, or automation without modifying the underlying business data.

---

# 2. Scope

This specification defines:

* responsibilities;
* ownership;
* lifecycle;
* relationships;
* business invariants.

Visualization, rendering, and editor behavior are outside the scope of this specification.

---

# 3. Definition

A **Marker** is a domain entity representing a logical annotation associated with a specific location within a Project.

A Marker describes the significance of a location rather than the behavior of the application.

---

# 4. Responsibilities

Marker SHALL be responsible for:

* identifying meaningful locations;
* storing annotation metadata;
* supporting navigation;
* supporting validation workflows;
* preserving positional references.

Marker SHALL NOT:

* modify project content;
* execute commands;
* control playback;
* implement presentation behavior.

---

# 5. Identity

Every Marker SHALL possess a globally unique identifier.

Its identity SHALL remain stable regardless of:

* name changes;
* position updates;
* metadata modifications.

---

# 6. Ownership

Every Marker SHALL belong to exactly one Project.

A Marker SHALL reference exactly one primary target within the Project.

---

# 7. Target

A Marker MAY reference:

* Document;
* Chapter;
* Fragment;
* Timeline;
* TimelineClip;
* TimelineMarker;
* AudioSegment;
* AudioFragment;
* ValidationIssue.

The referenced target SHALL remain valid throughout the lifetime of the Marker.

---

# 8. Classification

A Marker MAY define one or more business classifications, including:

* review;
* synchronization;
* validation;
* navigation;
* export;
* automation;
* custom categories.

The application MAY extend the available categories without changing the domain model.

---

# 9. Relationships

Marker MAY reference:

* Project;
* Document;
* Chapter;
* Fragment;
* Timeline;
* AudioSegment;
* Bookmark;
* Tag;
* ValidationIssue.

Marker SHALL NOT own referenced entities.

---

# 10. Metadata

Marker SHOULD expose:

* identifier;
* name;
* description;
* category;
* creation timestamp;
* modification timestamp;
* optional color;
* optional tags.

Metadata SHALL NOT affect business semantics.

---

# 11. Lifecycle

The lifecycle SHALL consist of:

1. creation;
2. association with a target;
3. modification;
4. usage;
5. archival or deletion.

Deleting a Marker SHALL NOT modify its referenced entity.

---

# 12. Business Rules

The following rules SHALL apply:

* every Marker belongs to exactly one Project;
* every Marker references at most one primary target;
* Marker identity SHALL remain immutable;
* referenced entities SHALL preserve referential integrity.

---

# 13. Validation

Validation SHALL verify:

* unique identifier;
* existing Project;
* valid target reference;
* internally consistent metadata;
* valid business classification.

Validation failures SHALL be reported through the Validation subsystem.

---

# 14. Persistence

Persistence SHALL be performed through Repository abstractions.

Marker SHALL remain independent of:

* serialization format;
* storage implementation;
* editor implementation.

---

# 15. Events

Business operations MAY produce events including:

* MarkerCreatedEvent;
* MarkerUpdatedEvent;
* MarkerDeletedEvent.

Event publication SHALL occur outside the entity.

---

# 16. Compliance

All persistent logical annotations within Voxarium SHALL conform to this specification.

Implementations SHALL preserve stable identity, ownership boundaries, referential integrity, and business invariants defined by this document.

---

# 17. References

* Project.md
* Document.md
* Chapter.md
* Fragment.md
* Timeline.md
* TimelineMarker.md
* AudioSegment.md
* AudioFragment.md
* Bookmark.md
* Tag.md
* ValidationIssue.md
* CreateMarkerCommand.md
* MarkerCreatedEvent.md

---

**End of Document**
