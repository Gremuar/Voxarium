# Scene

**Document Path:**
`spec/100_Domain/Scene.md`

**Document ID:** DOM-055

**Version:** 1.0.0

**Status:** Draft

**Classification:** Normative

---

# 1. Purpose

This document defines the **Scene** domain entity of the Voxarium platform.

A Scene represents a logical subdivision of a Project that groups Fragments, Timeline elements, and related assets into a coherent narrative or structural unit. It provides organizational boundaries for editing, generation, playback, and export without owning the underlying media resources.

---

# 2. Scope

This specification defines:

* responsibilities;
* ownership;
* lifecycle;
* relationships;
* business invariants.

Editor presentation, rendering, playback implementation, and UI navigation are outside the scope of this specification.

---

# 3. Definition

A **Scene** is a domain entity representing a logical section of a Project.

A Scene groups related content while remaining independent of document formatting and playback implementation.

---

# 4. Responsibilities

Scene SHALL be responsible for:

* grouping related content;
* defining structural boundaries;
* exposing scene metadata;
* supporting editing workflows;
* supporting export and generation workflows.

Scene SHALL NOT:

* own media assets;
* execute playback;
* perform speech generation;
* modify referenced entities directly.

---

# 5. Identity

Every Scene SHALL possess a globally unique identifier.

Its identity SHALL remain stable regardless of:

* title changes;
* ordering changes;
* metadata modifications.

---

# 6. Ownership

Every Scene SHALL belong to exactly one Project.

A Project MAY contain zero or more Scenes.

Lifecycle management SHALL be coordinated by the owning Project Aggregate.

---

# 7. Structure

A Scene MAY contain references to:

* Chapters;
* Fragments;
* TimelineClips;
* TimelineMarkers;
* AudioAssets;
* Characters;
* Speakers.

A Scene SHALL organize content but SHALL NOT own the referenced entities.

---

# 8. Relationships

Scene MAY reference:

* Project;
* Chapter;
* Fragment;
* Timeline;
* TimelineClip;
* TimelineMarker;
* AudioAsset;
* Character;
* Speaker;
* Tag.

Referenced entities SHALL remain external to the Scene.

---

# 9. Metadata

Scene SHOULD expose:

* identifier;
* title;
* description;
* display order;
* creation timestamp;
* modification timestamp;
* optional tags.

Metadata SHALL NOT affect Scene identity.

---

# 10. Lifecycle

The lifecycle SHALL consist of:

1. creation;
2. population;
3. modification;
4. reordering;
5. archival or deletion.

Deleting a Scene SHALL NOT delete referenced entities.

---

# 11. Business Rules

The following rules SHALL apply:

* every Scene belongs to exactly one Project;
* Scene ordering SHALL remain deterministic;
* Scene identity SHALL remain immutable;
* referenced entities SHALL preserve referential integrity.

---

# 12. Validation

Validation SHALL verify:

* unique identifier;
* existing Project;
* valid references;
* deterministic ordering;
* internally consistent metadata.

Validation failures SHALL be reported through the Validation subsystem.

---

# 13. Persistence

Persistence SHALL be performed through Repository abstractions.

Scene SHALL remain independent of:

* storage implementation;
* serialization format;
* editor implementation.

---

# 14. Events

Business operations MAY produce events including:

* SceneCreatedEvent;
* SceneUpdatedEvent;
* SceneMovedEvent;
* SceneDeletedEvent.

The Scene entity SHALL NOT publish events directly.

---

# 15. Compliance

All Scenes within Voxarium SHALL conform to this specification.

Implementations SHALL preserve stable identity, ownership boundaries, structural consistency, and business invariants defined by this document.

---

# 16. References

* Project.md
* Chapter.md
* Fragment.md
* Timeline.md
* TimelineClip.md
* TimelineMarker.md
* AudioAsset.md
* Character.md
* Speaker.md
* Tag.md
* ValidationIssue.md
* CreateSceneCommand.md
* UpdateSceneCommand.md
* DeleteSceneCommand.md
* SceneCreatedEvent.md

---

**End of Document**
