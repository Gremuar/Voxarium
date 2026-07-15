# TimelineClip

**Document Path:**
`spec/100_Domain/TimelineClip.md`

**Document ID:** DOM-039

**Version:** 1.0.0

**Status:** Draft

**Classification:** Normative

---

# 1. Purpose

This document defines the **TimelineClip** domain entity of the Voxarium platform.

A TimelineClip represents a time-bounded placement of content within a Timeline. It defines **when** a resource appears on a Timeline without owning or modifying the referenced resource itself.

TimelineClip exists exclusively within the **Timeline Aggregate**.

---

# 2. Scope

This specification defines:

* responsibilities;
* ownership;
* lifecycle;
* aggregate boundaries;
* relationships;
* business invariants.

Playback engines, rendering, waveform visualization, media decoding, and editor behavior are outside the scope of this specification.

---

# 3. Definition

A **TimelineClip** is a domain entity representing a temporal placement of a resource inside a Timeline.

A TimelineClip describes scheduling information rather than the underlying content.

---

# 4. Responsibilities

TimelineClip SHALL be responsible for:

* defining clip position;
* defining clip duration;
* referencing Project resources;
* supporting synchronization;
* preserving temporal consistency.

TimelineClip SHALL NOT:

* own referenced resources;
* generate audio;
* perform playback;
* modify source content.

---

# 5. Identity

Every TimelineClip SHALL possess a unique identifier.

Its identity SHALL remain stable throughout its lifetime within the owning Timeline.

Identity uniqueness SHALL be guaranteed only inside the Timeline Aggregate.

---

# 6. Ownership

Every TimelineClip SHALL belong to exactly one Timeline.

TimelineClip SHALL NOT exist independently.

Creation, modification and deletion SHALL occur exclusively through the Timeline Aggregate Root.

---

# 7. Temporal Properties

A TimelineClip SHALL define:

* start position;
* duration.

A TimelineClip MAY additionally define:

* end position;
* playback offset;
* playback speed;
* gain;
* mute state;
* lock state.

Temporal values SHALL use the canonical Project time representation.

---

# 8. Referenced Resources

A TimelineClip MAY reference:

* AudioAsset;
* AudioSegment;
* Fragment;
* Character;
* Speaker;
* GenerationHistory.

Referenced resources SHALL remain external to the Timeline Aggregate.

---

# 9. Relationships

TimelineClip MAY reference:

* Timeline;
* TimelineTrack;
* AudioAsset;
* AudioSegment;
* Fragment;
* Speaker;
* Character.

TimelineClip SHALL NOT own referenced entities.

---

# 10. Metadata

TimelineClip SHOULD expose:

* identifier;
* display name;
* creation timestamp;
* modification timestamp;
* optional color;
* optional tags.

Metadata SHALL NOT affect temporal behavior.

---

# 11. Lifecycle

The lifecycle SHALL consist of:

1. creation;
2. insertion into a Timeline;
3. positioning;
4. modification;
5. removal.

Lifecycle management SHALL be coordinated exclusively by the Timeline Aggregate.

---

# 12. Business Rules

The following rules SHALL apply:

* every TimelineClip belongs to exactly one Timeline;
* every TimelineClip MAY belong to one TimelineTrack;
* clip duration SHALL be positive;
* clip position SHALL remain valid within the Timeline;
* referenced resources SHALL preserve referential integrity.

---

# 13. Aggregate Rules

TimelineClip is a member of the Timeline Aggregate.

External components SHALL NOT:

* create TimelineClip independently;
* delete TimelineClip independently;
* modify TimelineClip outside the Aggregate.

All state transitions SHALL be coordinated by the Timeline Aggregate Root.

---

# 14. Validation

Validation SHALL verify:

* existing parent Timeline;
* unique identifier;
* valid temporal values;
* valid referenced resources;
* aggregate consistency.

Validation failures SHALL be reported through the Validation subsystem.

---

# 15. Persistence

Persistence SHALL be managed through the Timeline Repository.

TimelineClip SHALL remain independent of:

* multimedia frameworks;
* serialization format;
* storage implementation.

---

# 16. Events

TimelineClip participates in Aggregate events including:

* TimelineClipAddedEvent;
* TimelineClipUpdatedEvent;
* TimelineClipMovedEvent;
* TimelineClipRemovedEvent.

The entity itself SHALL NOT publish events.

---

# 17. Compliance

All TimelineClip entities within Voxarium SHALL conform to this specification.

Implementations SHALL preserve aggregate boundaries, ownership integrity, temporal consistency, stable identity, and business invariants defined herein.

---

# 18. References

* Timeline.md
* TimelineTrack.md
* AudioAsset.md
* AudioSegment.md
* Fragment.md
* Speaker.md
* Character.md
* GenerationHistory.md
* ValidationIssue.md
* AddTimelineClipCommand.md
* MoveTimelineClipCommand.md
* RemoveTimelineClipCommand.md
* TimelineClipAddedEvent.md

---

**End of Document**
