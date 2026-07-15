# GenerationPreset

**Document Path:**
`spec/100_Domain/GenerationPreset.md`

**Document ID:** DOM-023

**Version:** 1.0.0

**Status:** Draft

**Classification:** Normative

---

# 1. Purpose

This document defines the **GenerationPreset** domain entity of the Voxarium platform.

A GenerationPreset represents a reusable business-level configuration describing how generation operations should be performed. It encapsulates generation intent independently of any specific speech synthesis provider or execution engine.

---

# 2. Scope

This specification defines:

* responsibilities;
* ownership;
* lifecycle;
* relationships;
* business invariants.

Provider-specific parameters and execution algorithms are outside the scope of this specification.

---

# 3. Definition

A **GenerationPreset** is a reusable domain entity representing a predefined configuration for generation workflows.

The preset defines **what generation behavior is desired**, not **how it is technically implemented**.

---

# 4. Responsibilities

GenerationPreset SHALL be responsible for:

* defining reusable generation configurations;
* providing consistent generation behavior;
* exposing business-level generation parameters;
* supporting automation workflows;
* remaining independent of implementation details.

GenerationPreset SHALL NOT:

* execute generation;
* communicate with speech providers;
* modify generated resources;
* contain provider-specific runtime state.

---

# 5. Identity

Every GenerationPreset SHALL possess a globally unique identifier.

Its identity SHALL remain stable regardless of:

* name changes;
* parameter modifications;
* metadata updates.

---

# 6. Ownership

Every GenerationPreset SHALL belong to exactly one Project.

GenerationPresets SHALL NOT be shared directly between Projects.

Cross-project reuse SHALL occur only through explicit import or duplication.

---

# 7. Configuration

A GenerationPreset MAY define business-level configuration including:

* generation strategy;
* language preferences;
* voice selection policy;
* pronunciation policy;
* emotion profile;
* quality profile;
* validation policy;
* output preferences.

Concrete provider mappings SHALL be implemented outside the Domain layer.

---

# 8. Relationships

GenerationPreset MAY reference:

* Project;
* AudioGenerationPreset;
* VoiceProfile;
* EmotionPreset;
* Dictionary;
* Language;
* Character;
* Speaker.

GenerationPreset SHALL NOT own these entities.

---

# 9. Metadata

GenerationPreset SHOULD expose:

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

Deleting a GenerationPreset SHALL NOT invalidate completed GenerationHistory records.

---

# 11. Business Rules

The following rules SHALL apply:

* every GenerationPreset belongs to exactly one Project;
* preset names SHOULD be unique within a Project;
* modifications SHALL affect only future generation operations;
* completed jobs SHALL preserve the configuration that was originally applied.

---

# 12. Validation

Validation SHALL verify:

* unique identifier;
* existing parent Project;
* internally consistent configuration;
* valid referenced entities;
* required business attributes.

Validation failures SHALL be reported through the Validation subsystem.

---

# 13. Usage

GenerationPreset MAY be used by:

* AudioGenerationJob;
* ExportJob;
* automation workflows;
* plugins;
* batch processing operations.

Consumers SHALL treat the preset as immutable during execution.

---

# 14. Persistence

Persistence SHALL be performed through Repository abstractions.

GenerationPreset SHALL remain independent of:

* serialization format;
* storage implementation;
* provider-specific APIs.

---

# 15. Events

Business operations MAY produce events including:

* GenerationPresetCreatedEvent;
* GenerationPresetUpdatedEvent;
* GenerationPresetDeletedEvent.

The entity itself SHALL NOT publish events directly.

---

# 16. Compliance

All reusable generation configurations within Voxarium SHALL conform to this specification.

Implementations SHALL preserve stable identity, business intent, ownership boundaries, and implementation independence.

---

# 17. References

* Project.md
* AudioGenerationPreset.md
* VoiceProfile.md
* EmotionPreset.md
* Dictionary.md
* Language.md
* Character.md
* Speaker.md
* AudioGenerationJob.md
* GenerationHistory.md
* ValidationIssue.md
* CreateGenerationPresetCommand.md
* GenerationPresetCreatedEvent.md

---

**End of Document**
