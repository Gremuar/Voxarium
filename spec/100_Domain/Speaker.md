# Speaker

**Document Path:**
`spec/100_Domain/Speaker.md`

**Document ID:** DOM-036

**Version:** 1.0.0

**Status:** Draft

**Classification:** Normative

---

# 1. Purpose

This document defines the **Speaker** Aggregate Root of the Voxarium platform.

A Speaker represents a logical speaking entity responsible for narrating textual content within a Project. It defines the business identity of a narrator independently of any concrete voice synthesis provider, voice model, or runtime implementation.

A Speaker represents **who speaks**, while a VoiceProfile defines **how the Speaker sounds**.

---

# 2. Scope

This specification defines:

* responsibilities;
* ownership;
* aggregate boundaries;
* lifecycle;
* relationships;
* business invariants.

Speech synthesis engines, neural voice models, audio rendering, and provider-specific voice parameters are outside the scope of this specification.

---

# 3. Definition

A **Speaker** is the Aggregate Root representing a logical narrator within a Project.

The Speaker provides the canonical business identity used throughout narration, dialogue, and generation workflows.

---

# 4. Responsibilities

Speaker SHALL be responsible for:

* representing a logical narrator;
* maintaining speaker identity;
* coordinating speaker metadata;
* providing references for narration;
* preserving business consistency.

Speaker SHALL NOT:

* synthesize speech;
* generate audio;
* own voice models;
* communicate with speech providers.

---

# 5. Identity

Every Speaker SHALL possess a globally unique identifier.

Its identity SHALL remain stable regardless of:

* display name changes;
* assigned VoiceProfiles;
* metadata modifications.

Identity SHALL represent the logical narrator rather than any technical implementation.

---

# 6. Ownership

Every Speaker SHALL belong to exactly one Project.

A Speaker MAY be referenced by:

* Documents;
* Chapters;
* Fragments;
* GenerationPresets;
* AudioGenerationJobs;
* Timelines.

A Speaker SHALL NOT own these entities.

---

# 7. Aggregate Boundary

Speaker SHALL be the Aggregate Root.

Future Speaker-owned entities MAY include:

* SpeakerAliases;
* SpeakerMetadata;
* SpeakerTags.

All owned entities SHALL be modified exclusively through the Speaker Aggregate.

---

# 8. Relationships

Speaker MAY reference:

* Project;
* Character;
* VoiceProfile;
* Language;
* EmotionPreset;
* GenerationPreset.

A Speaker MAY have multiple VoiceProfiles.

Selection of the active VoiceProfile SHALL be governed by Application-layer policies.

---

# 9. Metadata

A Speaker SHOULD expose:

* identifier;
* display name;
* description;
* primary language;
* creation timestamp;
* modification timestamp;
* optional tags.

Metadata SHALL NOT affect Speaker identity.

---

# 10. Lifecycle

The lifecycle SHALL consist of:

1. creation;
2. configuration;
3. assignment to Project resources;
4. modification;
5. archival or deletion.

Deleting a Speaker SHALL NOT invalidate historical generation records.

---

# 11. Business Rules

The following rules SHALL apply:

* every Speaker belongs to exactly one Project;
* Speaker identity SHALL remain immutable;
* multiple Project entities MAY reference the same Speaker;
* completed GenerationHistory SHALL preserve the originally used Speaker.

---

# 12. Validation

Validation SHALL verify:

* unique identifier;
* existing Project;
* valid Language reference where applicable;
* valid VoiceProfile references;
* internally consistent metadata.

Validation failures SHALL be reported through the Validation subsystem.

---

# 13. Persistence

Persistence SHALL be performed through Repository abstractions.

Speaker SHALL remain independent of:

* storage implementation;
* serialization format;
* speech synthesis providers.

---

# 14. Events

Business operations MAY produce events including:

* SpeakerCreatedEvent;
* SpeakerUpdatedEvent;
* SpeakerArchivedEvent;
* SpeakerDeletedEvent.

Event publication SHALL occur outside the Aggregate.

---

# 15. Compliance

All logical narrators within Voxarium SHALL conform to this specification.

Implementations SHALL preserve stable identity, aggregate boundaries, ownership rules, and business invariants defined by this document.

---

# 16. References

* Project.md
* Character.md
* VoiceProfile.md
* Language.md
* EmotionPreset.md
* GenerationPreset.md
* GenerationHistory.md
* ValidationIssue.md
* CreateSpeakerCommand.md
* SpeakerCreatedEvent.md

---

**End of Document**
