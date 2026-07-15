# AudioGenerationPreset

**Document Path:**
`spec/100_Domain/AudioGenerationPreset.md`

**Document ID:** DOM-004

**Version:** 1.0.0

**Status:** Draft

**Classification:** Normative

---

# 1. Purpose

This document defines the **AudioGenerationPreset** domain entity of the Voxarium platform.

An AudioGenerationPreset represents a reusable collection of business-level generation parameters that can be applied to one or more AudioGenerationJobs.

Its purpose is to provide consistency, repeatability, and standardization of audio generation workflows.

---

# 2. Scope

This specification defines:

* responsibilities;
* ownership;
* lifecycle;
* relationships;
* business invariants.

Implementation-specific speech engine parameters are outside the scope of this document.

---

# 3. Definition

An **AudioGenerationPreset** is a reusable domain entity encapsulating a predefined set of audio generation options.

It represents business intent rather than engine-specific configuration.

---

# 4. Responsibilities

AudioGenerationPreset SHALL be responsible for:

* storing reusable generation parameters;
* providing a consistent generation profile;
* supporting multiple generation jobs;
* exposing business metadata.

AudioGenerationPreset SHALL NOT:

* execute generation;
* communicate with speech providers;
* store generated audio;
* perform validation of generated output.

---

# 5. Identity

Every AudioGenerationPreset SHALL possess a globally unique identifier.

Its identity SHALL remain stable regardless of modifications to preset parameters.

---

# 6. Ownership

An AudioGenerationPreset SHALL belong to exactly one Project.

Presets MAY be duplicated between Projects through import or copy operations.

Direct sharing between Projects SHALL NOT occur.

---

# 7. Lifecycle

The lifecycle SHALL consist of:

1. creation;
2. modification;
3. application;
4. duplication;
5. archival or deletion.

Deleting a preset SHALL NOT invalidate previously completed AudioGenerationJobs.

---

# 8. Preset Contents

A preset MAY define business-level defaults including:

* default Voice;
* default Speaker;
* Language;
* pronunciation resources;
* playback preferences;
* generation strategy;
* output organization.

Engine-specific parameters SHALL be encapsulated separately.

---

# 9. Relationships

AudioGenerationPreset MAY reference:

* Project;
* Voice;
* Speaker;
* Language;
* Dictionary;
* PronunciationDictionary;
* AudioGenerationJob.

The preset SHALL NOT own these entities.

---

# 10. Metadata

The preset SHOULD expose:

* identifier;
* name;
* description;
* creation timestamp;
* modification timestamp;
* author where applicable.

Metadata SHALL NOT alter business behavior.

---

# 11. Business Rules

The following rules SHALL apply:

* every preset belongs to one Project;
* preset names SHOULD be unique within a Project;
* presets SHALL remain reusable;
* modifications SHALL affect only future generation jobs.

Completed jobs SHALL preserve the configuration used during execution.

---

# 12. Validation

Validation SHALL verify:

* unique identifier;
* valid references;
* internally consistent configuration;
* required parameters are present.

Validation failures SHALL be reported through the Validation subsystem.

---

# 13. Usage

An AudioGenerationPreset MAY be applied by:

* AudioGenerationJob;
* user workflows;
* automation;
* plugins through documented APIs.

Application of a preset SHALL create an immutable execution configuration for the corresponding job.

---

# 14. Persistence

Persistence SHALL be performed through Repository abstractions.

The entity SHALL remain independent of:

* serialization format;
* storage implementation;
* speech engine APIs.

---

# 15. Events

Business operations involving AudioGenerationPreset MAY produce events including:

* AudioGenerationPresetCreatedEvent;
* AudioGenerationPresetUpdatedEvent;
* AudioGenerationPresetDeletedEvent.

The entity itself SHALL NOT publish events.

---

# 16. Compliance

All reusable generation profiles SHALL conform to this specification.

No implementation SHALL introduce behavior inconsistent with the lifecycle and business rules defined herein.

---

# 17. References

* Project.md
* AudioGenerationJob.md
* GenerationPreset.md
* Voice.md
* Speaker.md
* Language.md
* Dictionary.md
* PronunciationDictionary.md
* ValidationIssue.md
* CreateAudioGenerationPresetCommand.md

---

**End of Document**
