# VoicePreset

**Document Path:**
`spec/100_Domain/VoicePreset.md`

**Document ID:** DOM-064

**Version:** 1.0.0

**Status:** Draft

**Classification:** Normative

---

# 1. Purpose

This document defines the **VoicePreset** Aggregate Root of the Voxarium platform.

A VoicePreset represents a reusable configuration of speech synthesis parameters that can be applied to one or more VoiceModels. It encapsulates synthesis settings independently of any specific TTS engine or machine learning implementation.

A VoicePreset defines **how a voice should be used**, rather than the voice model itself.

---

# 2. Scope

This specification defines:

* responsibilities;
* ownership;
* aggregate boundaries;
* lifecycle;
* relationships;
* business invariants.

Speech synthesis, inference, runtime parameter translation, and provider-specific APIs are outside the scope of this specification.

---

# 3. Definition

A **VoicePreset** is the Aggregate Root representing a reusable speech synthesis configuration.

It defines the consistency boundary for voice generation parameters.

---

# 4. Responsibilities

VoicePreset SHALL be responsible for:

* storing reusable synthesis parameters;
* maintaining voice generation preferences;
* supporting generation workflows;
* supporting profile reuse;
* preserving configuration consistency.

VoicePreset SHALL NOT:

* perform speech synthesis;
* load VoiceModels;
* manage runtime execution;
* own generated audio.

---

# 5. Identity

Every VoicePreset SHALL possess a globally unique identifier.

Its identity SHALL remain stable regardless of:

* parameter modifications;
* metadata updates;
* assignment changes.

---

# 6. Ownership

Every VoicePreset SHALL belong to exactly one Project.

Multiple VoiceProfiles MAY reference the same VoicePreset.

---

# 7. Aggregate Boundary

VoicePreset SHALL be the Aggregate Root.

Future owned entities MAY include:

* SynthesisParameters;
* EngineOverrides;
* PresetMetadata;
* ProviderConfiguration.

All owned entities SHALL be modified exclusively through the VoicePreset Aggregate.

---

# 8. Configuration

A VoicePreset MAY define:

* speech rate;
* pitch;
* volume;
* temperature;
* stability;
* expressiveness;
* pronunciation preferences;
* provider-specific optional parameters.

Configuration SHALL remain independent of any particular synthesis engine.

---

# 9. Relationships

VoicePreset MAY reference:

* Project;
* VoiceModel;
* VoiceProfile;
* VoiceStyle;
* Speaker;
* Language.

Referenced entities SHALL remain external to the Aggregate.

---

# 10. Metadata

VoicePreset SHOULD expose:

* identifier;
* display name;
* description;
* version;
* creation timestamp;
* modification timestamp.

Metadata SHALL NOT affect aggregate identity.

---

# 11. Lifecycle

The lifecycle SHALL consist of:

1. creation;
2. configuration;
3. validation;
4. assignment;
5. modification;
6. archival or deletion.

Deleting a VoicePreset SHALL NOT invalidate previously generated audio.

---

# 12. Business Rules

The following rules SHALL apply:

* every VoicePreset belongs to exactly one Project;
* configuration SHALL remain internally consistent;
* multiple VoiceProfiles MAY reuse the same VoicePreset;
* aggregate integrity SHALL always be preserved.

---

# 13. Validation

Validation SHALL verify:

* unique identifier;
* existing Project;
* internally consistent configuration;
* valid referenced entities;
* supported parameter ranges.

Validation failures SHALL be reported through the Validation subsystem.

---

# 14. Persistence

Persistence SHALL be performed through Repository abstractions.

VoicePreset SHALL remain independent of:

* TTS engines;
* machine learning frameworks;
* storage implementation;
* serialization format.

---

# 15. Events

Business operations MAY produce events including:

* VoicePresetCreatedEvent;
* VoicePresetUpdatedEvent;
* VoicePresetDeletedEvent.

Event publication SHALL occur outside the Aggregate.

---

# 16. Compliance

All reusable speech synthesis presets within Voxarium SHALL conform to this specification.

Implementations SHALL preserve aggregate boundaries, stable identity, configuration consistency, and business invariants defined by this document.

---

# 17. References

* Project.md
* VoiceModel.md
* VoiceProfile.md
* VoiceStyle.md
* Speaker.md
* Language.md
* ValidationIssue.md
* CreateVoicePresetCommand.md
* UpdateVoicePresetCommand.md
* VoicePresetCreatedEvent.md

---

**End of Document**
