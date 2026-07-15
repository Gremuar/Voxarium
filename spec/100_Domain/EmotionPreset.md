# EmotionPreset

**Document Path:**
`spec/100_Domain/EmotionPreset.md`

**Document ID:** DOM-017

**Version:** 1.0.0

**Status:** Draft

**Classification:** Normative

---

# 1. Purpose

This document defines the **EmotionPreset** domain entity of the Voxarium platform.

An EmotionPreset represents a reusable business-level description of emotional speech characteristics. It allows Projects to consistently apply expressive behavior during speech generation while remaining independent of any specific speech synthesis engine.

EmotionPreset captures **intent**, not implementation.

---

# 2. Scope

This specification defines:

* responsibilities;
* ownership;
* lifecycle;
* relationships;
* business invariants.

Speech engine parameters, DSP algorithms, and runtime synthesis implementation are outside the scope of this specification.

---

# 3. Definition

An **EmotionPreset** is a reusable domain entity representing a predefined emotional speech profile.

It describes the desired expressive characteristics that MAY be interpreted by one or more synthesis providers.

---

# 4. Responsibilities

EmotionPreset SHALL be responsible for:

* defining reusable emotional behavior;
* providing consistent expressive profiles;
* supporting generation workflows;
* exposing business metadata;
* remaining independent of synthesis providers.

EmotionPreset SHALL NOT:

* synthesize speech;
* execute generation;
* contain provider-specific configuration;
* modify generated audio.

---

# 5. Identity

Every EmotionPreset SHALL possess a globally unique identifier.

Its identity SHALL remain stable regardless of:

* display name changes;
* parameter modifications;
* metadata updates.

---

# 6. Ownership

Every EmotionPreset SHALL belong to exactly one Project.

EmotionPresets SHALL NOT be shared directly between Projects.

Cross-project reuse SHALL occur only through explicit import or duplication.

---

# 7. Emotional Characteristics

An EmotionPreset MAY define business-level characteristics including:

* emotional category;
* emotional intensity;
* expressiveness level;
* speaking energy;
* stability;
* narrative style;
* emphasis profile.

These characteristics SHALL represent business intent only.

Provider-specific mappings SHALL be defined outside the Domain layer.

---

# 8. Relationships

EmotionPreset MAY reference:

* Project;
* AudioGenerationPreset;
* GenerationPreset;
* VoiceProfile;
* Speaker;
* Character.

EmotionPreset SHALL NOT own these entities.

---

# 9. Metadata

EmotionPreset SHOULD expose:

* identifier;
* name;
* description;
* creation timestamp;
* modification timestamp;
* version.

Metadata SHALL NOT affect business identity.

---

# 10. Lifecycle

The lifecycle SHALL consist of:

1. creation;
2. configuration;
3. usage;
4. modification;
5. archival or deletion.

Deleting an EmotionPreset SHALL NOT invalidate completed generation history.

---

# 11. Business Rules

The following rules SHALL apply:

* every EmotionPreset belongs to exactly one Project;
* preset names SHOULD be unique within a Project;
* modifications SHALL affect only future generation operations;
* completed jobs SHALL preserve the applied emotional configuration.

---

# 12. Validation

Validation SHALL verify:

* unique identifier;
* existing parent Project;
* internally consistent configuration;
* valid references;
* required business attributes.

Validation failures SHALL be reported through the Validation subsystem.

---

# 13. Usage

EmotionPreset MAY be applied by:

* AudioGenerationJob;
* AudioGenerationPreset;
* GenerationPreset;
* automation workflows;
* plugins through documented APIs.

Consumers SHALL treat the preset as immutable during execution.

---

# 14. Persistence

Persistence SHALL be performed through Repository abstractions.

EmotionPreset SHALL remain independent of:

* serialization format;
* storage implementation;
* speech synthesis providers.

---

# 15. Events

Business operations MAY produce events including:

* EmotionPresetCreatedEvent;
* EmotionPresetUpdatedEvent;
* EmotionPresetDeletedEvent.

The entity itself SHALL NOT publish events directly.

---

# 16. Compliance

All reusable emotional speech profiles within Voxarium SHALL conform to this specification.

Implementations SHALL preserve business intent, ownership, and identity independently of provider-specific implementations.

---

# 17. References

* Project.md
* Character.md
* Speaker.md
* VoiceProfile.md
* AudioGenerationPreset.md
* GenerationPreset.md
* ValidationIssue.md
* CreateEmotionPresetCommand.md
* EmotionPresetCreatedEvent.md

---

**End of Document**
