# AudioFragment

**Document Path:**
`spec/100_Domain/AudioFragment.md`

**Document ID:** DOM-002

**Version:** 1.0.0

**Status:** Draft

**Classification:** Normative

---

# 1. Purpose

This document defines the **AudioFragment** domain entity of the Voxarium platform.

An AudioFragment represents a logical segment of an AudioAsset that participates in playback, editing, timeline composition, export, and speech generation workflows.

It allows the system to reference meaningful portions of audio without duplicating the underlying audio resource.

---

# 2. Scope

This specification defines:

* the responsibilities of AudioFragment;
* ownership;
* lifecycle;
* relationships with other domain entities;
* business invariants.

Signal processing algorithms are outside the scope of this document.

---

# 3. Definition

An **AudioFragment** is a domain entity representing a bounded interval within an AudioAsset.

The entity models logical audio content rather than physical waveform storage.

---

# 4. Responsibilities

AudioFragment SHALL be responsible for:

* identifying an audio segment;
* defining its temporal boundaries;
* participating in timeline composition;
* maintaining references to its source AudioAsset;
* exposing business metadata.

AudioFragment SHALL NOT:

* modify audio samples;
* decode audio;
* encode audio;
* access the filesystem.

---

# 5. Identity

Every AudioFragment SHALL possess a unique identifier.

Its identity SHALL remain stable regardless of changes to metadata or timeline placement.

---

# 6. Ownership

Every AudioFragment SHALL belong to exactly one AudioAsset.

An AudioFragment SHALL NOT reference multiple AudioAssets.

---

# 7. Temporal Boundaries

An AudioFragment SHALL define:

* start position;
* end position;
* duration.

The following invariant SHALL always hold:

* start position < end position;
* duration > 0.

Temporal values SHALL be expressed using the canonical project time representation.

---

# 8. Relationships

AudioFragment MAY be referenced by:

* TimelineClip;
* GenerationHistory;
* ExportJob;
* Preview operations.

AudioFragment SHALL reference exactly one AudioAsset.

---

# 9. Metadata

AudioFragment MAY expose:

* identifier;
* display name;
* description;
* language;
* associated speaker;
* creation timestamp;
* source information.

Additional metadata MAY be introduced without changing the entity's responsibilities.

---

# 10. Lifecycle

The lifecycle consists of:

1. creation;
2. registration;
3. editing of metadata;
4. usage;
5. archival or deletion.

Deleting an AudioFragment SHALL NOT necessarily delete its parent AudioAsset.

---

# 11. Business Rules

The following rules SHALL apply:

* every AudioFragment belongs to one AudioAsset;
* temporal boundaries SHALL remain valid;
* overlapping fragments are permitted unless restricted by higher-level workflows;
* references SHALL remain valid throughout the fragment lifecycle.

---

# 12. Validation

Validation SHALL verify:

* unique identifier;
* valid temporal boundaries;
* existing parent AudioAsset;
* consistent metadata;
* referential integrity.

Validation failures SHALL be reported through the validation subsystem.

---

# 13. Timeline Integration

AudioFragments MAY be reused by multiple TimelineClips.

Timeline placement SHALL NOT modify the identity of an AudioFragment.

Timeline-specific information SHALL reside outside this entity.

---

# 14. Speech Generation

AudioFragments MAY originate from:

* generated speech;
* imported recordings;
* externally supplied media;
* plugin-generated content.

The generation mechanism SHALL NOT alter the business semantics of the entity.

---

# 15. Persistence

Persistence SHALL be performed through Repository abstractions.

AudioFragment SHALL remain independent of:

* storage format;
* serialization;
* filesystem organization.

---

# 16. Events

Operations involving AudioFragment MAY produce events including:

* AudioGenerationCompletedEvent;
* TimelineClipCreatedEvent;
* TimelineClipUpdatedEvent.

The entity itself SHALL NOT publish events directly.

---

# 17. Compliance

All implementations representing logical audio segments SHALL conform to this specification.

No implementation SHALL violate the invariants defined in this document.

---

# 18. References

* AudioAsset.md
* TimelineClip.md
* Timeline.md
* ExportJob.md
* ValidationIssue.md
* AudioAssetDto.md
* AudioGenerationCompletedEvent.md

---

**End of Document**
