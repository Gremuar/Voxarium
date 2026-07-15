# AudioAsset

**Document Path:**
`spec/100_Domain/AudioAsset.md`

**Document ID:** DOM-001

**Version:** 1.0.0

**Status:** Draft

**Classification:** Normative

---

# 1. Purpose

This document defines the **AudioAsset** domain entity of the Voxarium platform.

An AudioAsset represents a managed audio resource belonging to a Project. It serves as the canonical domain representation of generated, imported, or externally referenced audio while remaining independent of its physical storage implementation.

---

# 2. Scope

This specification defines:

* the responsibilities of AudioAsset;
* its lifecycle;
* ownership;
* relationships with other domain objects;
* business invariants.

Storage formats and serialization are defined elsewhere.

---

# 3. Definition

An **AudioAsset** is a domain entity representing an audio resource that is managed by a Project.

The entity describes the business identity and metadata of an audio resource rather than its physical file representation.

---

# 4. Responsibilities

AudioAsset SHALL be responsible for:

* identifying an audio resource;
* describing its origin;
* exposing business metadata;
* maintaining logical relationships;
* participating in project validation.

AudioAsset SHALL NOT perform:

* audio playback;
* waveform analysis;
* encoding;
* decoding;
* filesystem operations.

---

# 5. Identity

Every AudioAsset SHALL possess a globally unique identifier.

The identifier SHALL remain stable throughout the lifetime of the Project.

Identity SHALL NOT depend upon:

* filename;
* storage path;
* checksum;
* display name.

---

# 6. Ownership

An AudioAsset SHALL belong to exactly one Project.

It SHALL NOT be shared directly between multiple Projects.

Cross-project reuse SHALL occur only through import mechanisms.

---

# 7. Lifecycle

The lifecycle of an AudioAsset consists of:

1. creation;
2. registration;
3. usage;
4. modification of metadata;
5. archival or deletion.

Deletion SHALL remove the AudioAsset from the domain model.

---

# 8. Sources

AudioAssets MAY originate from:

* speech generation;
* audio import;
* project migration;
* plugin-generated content;
* future extension mechanisms.

The source SHALL be recorded as metadata.

---

# 9. Relationships

AudioAsset MAY be referenced by:

* AudioFragment;
* TimelineClip;
* GenerationHistory;
* ExportJob.

AudioAsset SHALL NOT directly own these entities.

---

# 10. Metadata

AudioAsset SHOULD expose metadata including:

* identifier;
* display name;
* duration;
* language;
* creation timestamp;
* origin;
* associated speaker where applicable.

Implementation-specific metadata MAY be stored separately.

---

# 11. Immutability Rules

The identity of an AudioAsset SHALL be immutable.

Metadata MAY change where permitted by business rules.

Changes SHALL preserve referential integrity.

---

# 12. Validation

An AudioAsset SHALL satisfy the following invariants:

* identifier is unique;
* associated Project exists;
* referenced resources are valid;
* metadata is internally consistent.

Invalid AudioAssets SHALL be reported through the validation subsystem.

---

# 13. Domain Behavior

AudioAsset participates in business workflows including:

* speech generation;
* timeline editing;
* export;
* validation;
* preview.

Behavior SHALL be coordinated by Application Services.

---

# 14. Persistence

Persistence SHALL be performed through Repository abstractions.

AudioAsset SHALL remain unaware of:

* filesystem layout;
* serialization format;
* storage technology.

---

# 15. Events

Operations involving AudioAsset MAY produce events including:

* AudioImportedEvent;
* AudioGenerationCompletedEvent;
* AudioExportCompletedEvent.

Event definitions are specified separately.

---

# 16. Commands

AudioAsset MAY participate in commands including:

* GenerateAudioCommand;
* ImportAudioCommand;
* ExportProjectCommand.

Command behavior is defined independently of this entity.

---

# 17. Business Rules

The following rules SHALL apply:

* every AudioAsset belongs to exactly one Project;
* every AudioAsset has a stable identity;
* business references SHALL use identifiers rather than storage paths;
* deletion SHALL preserve project consistency.

---

# 18. Compliance

All implementations representing managed audio resources SHALL conform to this specification.

No implementation SHALL introduce business behavior that violates the invariants defined herein.

---

# 19. References

* Project.md
* AudioFragment.md
* TimelineClip.md
* GenerationHistory.md
* ExportJob.md
* ValidationIssue.md
* AudioAssetDto.md
* GenerateAudioCommand.md
* AudioGenerationCompletedEvent.md

---

**End of Document**
