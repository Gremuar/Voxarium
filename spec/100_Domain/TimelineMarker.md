# TimelineMarker

**Document Path:**
`spec/100_Domain/TimelineMarker.md`

**Document ID:** DOM-040

**Version:** 1.0.0

**Status:** Draft

**Classification:** Normative

---

# 1. Purpose

This document defines the **TimelineMarker** domain entity of the Voxarium platform.

A TimelineMarker represents a persistent temporal annotation within a Timeline. It identifies significant time positions used for navigation, synchronization, editing, validation, automation, and export without modifying the Timeline content itself.

TimelineMarker exists exclusively within the **Timeline Aggregate**.

---

# 2. Scope

This specification defines:

* responsibilities;
* ownership;
* lifecycle;
* aggregate boundaries;
* relationships;
* business invariants.

Playback, rendering, waveform visualization, and editor implementation are outside the scope of this specification.

---

# 3. Definition

A **TimelineMarker** is a domain entity representing a meaningful position on a Timeline.

It describes **where something is significant in time**, rather than the media itself.

---

# 4. Responsibilities

TimelineMarker SHALL be responsible for:

* marking temporal positions;
* supporting navigation;
* supporting synchronization workflows;
* supporting editing operations;
* exposing marker metadata.

TimelineMarker SHALL NOT:

* modify Timeline content;
* own media resources;
* execute playback;
* perform synchronization logic.

---

# 5. Identity

Every TimelineMarker SHALL possess a unique identifier.

Its identity SHALL remain stable throughout its lifetime within the owning Timeline.

Identity uniqueness SHALL be guaranteed only inside the Timeline Aggregate.

---

# 6. Ownership

Every TimelineMarker SHALL belong to exactly one Timeline.

TimelineMarker SHALL NOT exist independently.

Creation, modification, and deletion SHALL occur exclusively through the Timeline Aggregate Root.

---

# 7. Temporal Position

A TimelineMarker SHALL define exactly one temporal position.

A TimelineMarker MAY additionally define:

* duration;
* marker type;
* priority;
* visibility state;
* lock state.

Temporal values SHALL use the canonical Project time representation.

---

# 8. Relationships

TimelineMarker MAY reference:

* Timeline;
* TimelineClip;
* TimelineTrack;
* AudioSegment;
* AudioAsset;
* Fragment;
* Speaker;
* Character;
* GenerationHistory;
* ValidationIssue.

TimelineMarker SHALL NOT own referenced entities.

---

# 9. Classification

A TimelineMarker MAY belong to one or more business categories including:

* synchronization;
* chapter boundary;
* cue point;
* review;
* validation;
* export;
* automation;
* custom category.

Category semantics SHALL remain independent of editor implementation.

---

# 10. Metadata

TimelineMarker SHOULD expose:

* identifier;
* name;
* description;
* creation timestamp;
* modification timestamp;
* optional color;
* optional tags.

Metadata SHALL NOT affect marker identity.

---

# 11. Lifecycle

The lifecycle SHALL consist of:

1. creation;
2. placement on Timeline;
3. modification;
4. usage;
5. removal.

Lifecycle management SHALL be coordinated exclusively by the Timeline Aggregate.

---

# 12. Business Rules

The following rules SHALL apply:

* every TimelineMarker belongs to exactly one Timeline;
* marker position SHALL remain valid within the Timeline;
* marker identity SHALL remain immutable;
* referenced entities SHALL preserve referential integrity.

---

# 13. Aggregate Rules

TimelineMarker is a member of the Timeline Aggregate.

External components SHALL NOT:

* create TimelineMarker independently;
* delete TimelineMarker independently;
* modify TimelineMarker outside the Aggregate.

All lifecycle operations SHALL be coordinated by the Timeline Aggregate Root.

---

# 14. Validation

Validation SHALL verify:

* existing parent Timeline;
* unique identifier;
* valid temporal position;
* valid referenced entities;
* aggregate consistency.

Validation failures SHALL be reported through the Validation subsystem.

---

# 15. Persistence

Persistence SHALL be managed through the Timeline Repository.

TimelineMarker SHALL remain independent of:

* serialization format;
* multimedia frameworks;
* storage implementation.

---

# 16. Events

TimelineMarker participates in Aggregate events including:

* TimelineMarkerAddedEvent;
* TimelineMarkerUpdatedEvent;
* TimelineMarkerMovedEvent;
* TimelineMarkerRemovedEvent.

The entity itself SHALL NOT publish events.

---

# 17. Compliance

All TimelineMarker entities within Voxarium SHALL conform to this specification.

Implementations SHALL preserve aggregate boundaries, ownership integrity, temporal consistency, stable identity, and business invariants defined herein.

---

# 18. References

* Timeline.md
* TimelineTrack.md
* TimelineClip.md
* AudioAsset.md
* AudioSegment.md
* Fragment.md
* Speaker.md
* Character.md
* GenerationHistory.md
* ValidationIssue.md
* AddTimelineMarkerCommand.md
* MoveTimelineMarkerCommand.md
* RemoveTimelineMarkerCommand.md
* TimelineMarkerAddedEvent.md

---

**End of Document**
