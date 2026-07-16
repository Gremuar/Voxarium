# Subtitle

**Document Path:**
`spec/100_Domain/Subtitle.md`

**Document ID:** DOM-057

**Version:** 1.0.0

**Status:** Draft

**Classification:** Normative

---

# 1. Purpose

This document defines the **Subtitle** domain entity of the Voxarium platform.

A Subtitle represents a time-bound textual element synchronized with audio or timeline content. It provides the business representation of subtitle information independently of subtitle file formats, rendering engines, or playback implementations.

Subtitle exists to synchronize textual content with media rather than to define visual presentation.

---

# 2. Scope

This specification defines:

* responsibilities;
* ownership;
* lifecycle;
* relationships;
* business invariants.

Subtitle rendering, typography, animation, subtitle codecs, and media playback are outside the scope of this specification.

---

# 3. Definition

A **Subtitle** is a domain entity representing a synchronized text segment associated with media content.

A Subtitle SHALL represent timing and textual information only.

---

# 4. Responsibilities

Subtitle SHALL be responsible for:

* representing synchronized text;
* preserving timing information;
* maintaining subtitle ordering;
* exposing subtitle metadata;
* supporting import and export workflows.

Subtitle SHALL NOT:

* render subtitles;
* modify media;
* perform playback;
* generate speech.

---

# 5. Identity

Every Subtitle SHALL possess a globally unique identifier.

Its identity SHALL remain stable regardless of:

* text edits;
* timing adjustments;
* metadata updates.

---

# 6. Ownership

Every Subtitle SHALL belong to exactly one Project.

A Subtitle MAY be associated with:

* one Timeline;
* one TimelineClip;
* one AudioAsset.

Ownership SHALL remain coordinated by the Project Aggregate.

---

# 7. Subtitle Structure

A Subtitle SHALL contain:

* subtitle text;
* start position;
* end position.

A Subtitle MAY additionally define:

* language;
* speaker reference;
* style reference;
* confidence information;
* generation source.

---

# 8. Relationships

Subtitle MAY reference:

* Project;
* Timeline;
* TimelineClip;
* AudioAsset;
* Speaker;
* Language;
* StylePreset.

Referenced entities SHALL remain external to the Subtitle.

---

# 9. Metadata

Subtitle SHOULD expose:

* identifier;
* creation timestamp;
* modification timestamp;
* subtitle index;
* optional tags.

Metadata SHALL NOT affect Subtitle identity.

---

# 10. Lifecycle

The lifecycle SHALL consist of:

1. creation;
2. synchronization;
3. validation;
4. modification;
5. export;
6. deletion.

Deleting a Subtitle SHALL NOT affect the associated media.

---

# 11. Business Rules

The following rules SHALL apply:

* every Subtitle belongs to exactly one Project;
* start position SHALL precede end position;
* subtitle ordering SHALL remain deterministic;
* Subtitle identity SHALL remain immutable.

---

# 12. Validation

Validation SHALL verify:

* unique identifier;
* existing Project;
* valid timing information;
* valid referenced entities;
* internally consistent subtitle content.

Validation failures SHALL be reported through the Validation subsystem.

---

# 13. Persistence

Persistence SHALL be performed through Repository abstractions.

Subtitle SHALL remain independent of:

* subtitle formats;
* rendering engines;
* storage implementation;
* serialization format.

---

# 14. Events

Business operations MAY produce events including:

* SubtitleCreatedEvent;
* SubtitleUpdatedEvent;
* SubtitleDeletedEvent;
* SubtitleSynchronizedEvent.

The Subtitle entity SHALL NOT publish events directly.

---

# 15. Compliance

All subtitles within Voxarium SHALL conform to this specification.

Implementations SHALL preserve stable identity, timing consistency, ownership boundaries, referential integrity, and business invariants defined by this document.

---

# 16. References

* Project.md
* Timeline.md
* TimelineClip.md
* AudioAsset.md
* Speaker.md
* Language.md
* StylePreset.md
* ValidationIssue.md
* CreateSubtitleCommand.md
* UpdateSubtitleCommand.md
* DeleteSubtitleCommand.md
* SubtitleCreatedEvent.md

---

**End of Document**
