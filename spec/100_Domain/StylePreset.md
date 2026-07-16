# StylePreset

**Document Path:**
`spec/100_Domain/StylePreset.md`

**Document ID:** DOM-056

**Version:** 1.0.0

**Status:** Draft

**Classification:** Normative

---

# 1. Purpose

This document defines the **StylePreset** Aggregate Root of the Voxarium platform.

A StylePreset represents a reusable collection of stylistic parameters that may be applied during text processing, speech generation, subtitle generation, or export workflows. It provides a reusable business abstraction for stylistic configuration while remaining independent of any particular TTS engine, rendering engine, or export implementation.

---

# 2. Scope

This specification defines:

* responsibilities;
* ownership;
* aggregate boundaries;
* lifecycle;
* relationships;
* business invariants.

Speech synthesis algorithms, rendering pipelines, prompt generation, and user interface presentation are outside the scope of this specification.

---

# 3. Definition

A **StylePreset** is the Aggregate Root representing a reusable style configuration within a Project.

It defines the consistency boundary for stylistic parameters used by multiple application workflows.

---

# 4. Responsibilities

StylePreset SHALL be responsible for:

* defining reusable stylistic configuration;
* maintaining presentation preferences;
* supporting generation workflows;
* supporting export workflows;
* preserving configuration consistency.

StylePreset SHALL NOT:

* generate speech;
* modify source text;
* perform rendering;
* execute business workflows.

---

# 5. Identity

Every StylePreset SHALL possess a globally unique identifier.

Its identity SHALL remain stable regardless of:

* parameter modifications;
* metadata updates;
* assignment changes.

---

# 6. Ownership

Every StylePreset SHALL belong to exactly one Project.

Multiple workflows MAY reference the same StylePreset.

---

# 7. Aggregate Boundary

StylePreset SHALL be the Aggregate Root.

Future owned entities MAY include:

* StyleParameterSet;
* TypographyConfiguration;
* NarrationStyleConfiguration;
* SubtitleStyleConfiguration.

All owned entities SHALL be modified exclusively through the StylePreset Aggregate.

---

# 8. Configuration

A StylePreset MAY define:

* narration style;
* reading intensity;
* pause behavior;
* emphasis preferences;
* subtitle presentation defaults;
* typography preferences;
* formatting options;
* custom stylistic parameters.

Configuration SHALL remain independent of specific rendering or synthesis implementations.

---

# 9. Relationships

StylePreset MAY reference:

* Project;
* VoiceProfile;
* AudioProfile;
* PlaybackProfile;
* GenerationPreset;
* Subtitle;
* ExportProfile.

Referenced entities SHALL remain external to the Aggregate.

---

# 10. Metadata

StylePreset SHOULD expose:

* identifier;
* name;
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
4. assignment to workflows;
5. modification;
6. archival or deletion.

Deleting a StylePreset SHALL NOT invalidate historical Project outputs.

---

# 12. Business Rules

The following rules SHALL apply:

* every StylePreset belongs to exactly one Project;
* configuration SHALL remain internally consistent;
* multiple workflows MAY reference the same StylePreset;
* aggregate integrity SHALL always be preserved.

---

# 13. Validation

Validation SHALL verify:

* unique identifier;
* existing Project;
* internally consistent configuration;
* valid referenced entities;
* compliance with Project policies.

Validation failures SHALL be reported through the Validation subsystem.

---

# 14. Persistence

Persistence SHALL be performed through Repository abstractions.

StylePreset SHALL remain independent of:

* rendering engines;
* TTS providers;
* storage implementation;
* serialization format.

---

# 15. Events

Business operations MAY produce events including:

* StylePresetCreatedEvent;
* StylePresetUpdatedEvent;
* StylePresetDeletedEvent.

Event publication SHALL occur outside the Aggregate.

---

# 16. Compliance

All reusable stylistic configurations within Voxarium SHALL conform to this specification.

Implementations SHALL preserve aggregate boundaries, ownership integrity, stable identity, and business invariants defined by this document.

---

# 17. References

* Project.md
* VoiceProfile.md
* AudioProfile.md
* PlaybackProfile.md
* GenerationPreset.md
* Subtitle.md
* ExportProfile.md
* ValidationIssue.md
* CreateStylePresetCommand.md
* UpdateStylePresetCommand.md
* StylePresetCreatedEvent.md

---

**End of Document**
