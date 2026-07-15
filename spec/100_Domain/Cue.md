# Cue

**Document Path:**
`spec/100_Domain/Cue.md`

**Document ID:** DOM-011

**Version:** 1.0.0

**Status:** Draft

**Classification:** Normative

---

# 1. Purpose

This document defines the **Cue** domain entity of the Voxarium platform.

A Cue represents a logical control point associated with project content or timeline execution. It is used to indicate meaningful synchronization positions for playback, speech generation, export, automation, and plugin integration.

---

# 2. Scope

This specification defines:

* responsibilities;
* ownership;
* lifecycle;
* relationships;
* business invariants.

Playback implementation and execution scheduling are outside the scope of this specification.

---

# 3. Definition

A **Cue** is a domain entity representing a named synchronization point within a Project.

A Cue identifies *where* a significant event occurs without defining *how* that event is processed.

---

# 4. Responsibilities

Cue SHALL be responsible for:

* representing synchronization points;
* identifying logical execution positions;
* exposing synchronization metadata;
* supporting automation and integration workflows.

Cue SHALL NOT:

* execute actions;
* modify project content;
* perform playback;
* control speech synthesis.

---

# 5. Identity

Every Cue SHALL possess a globally unique identifier.

Its identity SHALL remain stable regardless of:

* name changes;
* timing adjustments;
* metadata modifications.

---

# 6. Ownership

Every Cue SHALL belong to exactly one Project.

A Cue MAY be associated with one primary target entity.

---

# 7. Target

A Cue MAY reference:

* Timeline;
* TimelineClip;
* TimelineMarker;
* Chapter;
* Scene;
* Fragment;
* AudioSegment;
* AudioFragment;
* Document;
* other cue-enabled entities.

Referenced entities SHALL remain valid throughout the lifetime of the Cue.

---

# 8. Timing

A Cue MAY define:

* timeline position;
* document position;
* playback position;
* generation position.

The exact interpretation depends upon the referenced target.

Timing values SHALL use the canonical project time representation where applicable.

---

# 9. Relationships

Cue MAY reference:

* Project;
* Timeline;
* TimelineClip;
* TimelineMarker;
* Scene;
* Chapter;
* Fragment;
* AudioSegment;
* AudioFragment;
* Bookmark.

Cue SHALL NOT own referenced entities.

---

# 10. Metadata

A Cue SHOULD expose:

* identifier;
* name;
* description;
* category;
* creation timestamp;
* modification timestamp;
* optional tags.

Metadata SHALL NOT alter business semantics.

---

# 11. Lifecycle

The lifecycle SHALL consist of:

1. creation;
2. association with a target;
3. modification;
4. usage;
5. archival or deletion.

Deleting a Cue SHALL NOT modify the referenced entity.

---

# 12. Business Rules

The following rules SHALL apply:

* every Cue belongs to one Project;
* a Cue SHALL reference at most one primary target;
* timing information SHALL remain valid;
* deleting a referenced entity SHALL be handled according to Project integrity rules.

---

# 13. Validation

Validation SHALL verify:

* unique identifier;
* existing Project;
* valid target reference;
* consistent timing information;
* internally consistent metadata.

Validation failures SHALL be reported through the Validation subsystem.

---

# 14. Persistence

Persistence SHALL be performed through Repository abstractions.

Cue SHALL remain independent of:

* serialization format;
* storage implementation;
* runtime execution engine.

---

# 15. Events

Business operations MAY produce events including:

* CueCreatedEvent;
* CueUpdatedEvent;
* CueDeletedEvent.

Cue-related events SHALL be published by the Application layer rather than the entity itself.

---

# 16. Compliance

All synchronization points within Voxarium SHALL conform to this specification.

Implementations SHALL preserve Cue identity, timing consistency, and referential integrity.

---

# 17. References

* Project.md
* Timeline.md
* TimelineClip.md
* TimelineMarker.md
* Chapter.md
* Scene.md
* Fragment.md
* AudioSegment.md
* AudioFragment.md
* Bookmark.md
* ValidationIssue.md
* CreateCueCommand.md
* CueCreatedEvent.md

---

**End of Document**
