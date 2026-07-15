# TimelineTrack

**Document Path:**
`spec/100_Domain/TimelineTrack.md`

**Document ID:** DOM-041

**Version:** 1.0.0

**Status:** Draft

**Classification:** Normative

---

# 1. Purpose

This document defines the **TimelineTrack** domain entity of the Voxarium platform.

A TimelineTrack represents an ordered logical lane within a Timeline. It provides organizational structure for TimelineClips while preserving temporal consistency and separation of independent content streams.

TimelineTrack exists exclusively within the **Timeline Aggregate**.

---

# 2. Scope

This specification defines:

* responsibilities;
* ownership;
* lifecycle;
* aggregate boundaries;
* relationships;
* business invariants.

Playback behavior, waveform rendering, UI layout, and editor implementation are outside the scope of this specification.

---

# 3. Definition

A **TimelineTrack** is a domain entity representing one logical track inside a Timeline.

A TimelineTrack organizes TimelineClips but does not own the media resources referenced by those clips.

---

# 4. Responsibilities

TimelineTrack SHALL be responsible for:

* organizing TimelineClips;
* preserving clip ordering;
* maintaining track metadata;
* supporting synchronization;
* participating in Timeline consistency.

TimelineTrack SHALL NOT:

* generate audio;
* execute playback;
* own media resources;
* modify referenced Project entities.

---

# 5. Identity

Every TimelineTrack SHALL possess a unique identifier.

Its identity SHALL remain stable throughout its lifetime within the owning Timeline.

Identity uniqueness SHALL be guaranteed only inside the Timeline Aggregate.

---

# 6. Ownership

Every TimelineTrack SHALL belong to exactly one Timeline.

TimelineTrack SHALL own the logical placement of TimelineClips assigned to it but SHALL NOT own the TimelineClip entities themselves.

TimelineClip lifecycle SHALL remain coordinated by the Timeline Aggregate Root.

---

# 7. Track Structure

A TimelineTrack MAY contain:

* zero or more TimelineClips;
* optional TimelineMarkers associated with the track.

Ordering of clips SHALL remain deterministic.

---

# 8. Relationships

TimelineTrack MAY reference:

* Timeline;
* TimelineClip;
* TimelineMarker;
* Speaker;
* Character;
* AudioAsset.

TimelineTrack SHALL NOT own referenced Project resources.

---

# 9. Metadata

TimelineTrack SHOULD expose:

* identifier;
* display name;
* track type;
* creation timestamp;
* modification timestamp;
* visibility state;
* mute state;
* solo state;
* lock state.

Metadata SHALL NOT affect track identity.

---

# 10. Lifecycle

The lifecycle SHALL consist of:

1. creation;
2. insertion into Timeline;
3. population with clips;
4. modification;
5. removal.

Lifecycle management SHALL be coordinated exclusively by the Timeline Aggregate.

---

# 11. Business Rules

The following rules SHALL apply:

* every TimelineTrack belongs to exactly one Timeline;
* clip ordering SHALL remain deterministic;
* a TimelineClip SHALL belong to at most one TimelineTrack at any given time;
* track identity SHALL remain immutable;
* aggregate consistency SHALL always be preserved.

---

# 12. Aggregate Rules

TimelineTrack is a member of the Timeline Aggregate.

External components SHALL NOT:

* create TimelineTrack independently;
* delete TimelineTrack independently;
* modify TimelineTrack outside the Aggregate.

All lifecycle operations SHALL be coordinated by the Timeline Aggregate Root.

---

# 13. Validation

Validation SHALL verify:

* existing parent Timeline;
* unique identifier;
* valid clip assignments;
* internally consistent metadata;
* aggregate integrity.

Validation failures SHALL be reported through the Validation subsystem.

---

# 14. Persistence

Persistence SHALL be managed through the Timeline Repository.

TimelineTrack SHALL remain independent of:

* serialization format;
* storage implementation;
* multimedia frameworks.

---

# 15. Events

TimelineTrack participates in Aggregate events including:

* TimelineTrackAddedEvent;
* TimelineTrackUpdatedEvent;
* TimelineTrackRemovedEvent;
* TimelineTrackReorderedEvent.

The entity itself SHALL NOT publish events.

---

# 16. Compliance

All TimelineTrack entities within Voxarium SHALL conform to this specification.

Implementations SHALL preserve aggregate boundaries, deterministic ordering, ownership integrity, stable identity, and business invariants defined herein.

---

# 17. References

* Timeline.md
* TimelineClip.md
* TimelineMarker.md
* Speaker.md
* Character.md
* AudioAsset.md
* ValidationIssue.md
* AddTimelineTrackCommand.md
* RemoveTimelineTrackCommand.md
* ReorderTimelineTrackCommand.md
* TimelineTrackAddedEvent.md

---

**End of Document**
