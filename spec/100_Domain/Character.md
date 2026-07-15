# Character

**Document Path:**
`spec/100_Domain/Character.md`

**Document ID:** DOM-009

**Version:** 1.0.0

**Status:** Draft

**Classification:** Normative

---

# 1. Purpose

This document defines the **Character** domain entity of the Voxarium platform.

A Character represents a logical persona participating in a Project. It encapsulates the narrative identity of a speaker independently of the concrete voice synthesis technology used during audio generation.

---

# 2. Scope

This specification defines:

* responsibilities;
* ownership;
* lifecycle;
* relationships;
* business invariants.

Voice synthesis implementation and rendering behavior are outside the scope of this specification.

---

# 3. Definition

A **Character** is a domain entity representing a logical participant in a Project.

A Character models *who* is speaking from the perspective of the project content, independently of *how* the speech is synthesized.

---

# 4. Responsibilities

Character SHALL be responsible for:

* representing a narrative persona;
* maintaining character metadata;
* serving as the logical owner of speech assignments;
* participating in generation workflows;
* preserving identity across the lifetime of a Project.

Character SHALL NOT:

* perform speech synthesis;
* manage audio resources;
* execute generation jobs;
* contain presentation logic.

---

# 5. Identity

Every Character SHALL possess a globally unique identifier.

Its identity SHALL remain stable regardless of:

* display name changes;
* assigned voices;
* assigned speakers;
* metadata modifications.

---

# 6. Ownership

Every Character SHALL belong to exactly one Project.

Characters SHALL NOT be shared directly between Projects.

Cross-project reuse SHALL occur only through explicit import or duplication.

---

# 7. Relationships

A Character MAY reference:

* Speaker;
* Voice;
* VoiceProfile;
* Fragment;
* Scene;
* Chapter;
* GenerationPreset.

A Character SHALL NOT own these entities.

---

# 8. Assignments

One Character MAY be associated with multiple Fragments.

One Fragment SHOULD reference at most one Character.

Assignment rules SHALL be enforced by the Application layer.

---

# 9. Metadata

A Character SHOULD expose:

* identifier;
* display name;
* optional description;
* creation timestamp;
* modification timestamp;
* optional tags;
* optional visual attributes.

Metadata SHALL NOT affect business identity.

---

# 10. Lifecycle

The lifecycle SHALL consist of:

1. creation;
2. configuration;
3. assignment to project content;
4. modification;
5. archival or deletion.

Deleting a Character SHALL follow the Project's referential integrity rules.

---

# 11. Business Rules

The following rules SHALL apply:

* every Character belongs to exactly one Project;
* Character identity SHALL remain immutable;
* Character names SHOULD be unique within a Project;
* removing a Character SHALL NOT leave invalid references.

---

# 12. Validation

Validation SHALL verify:

* unique identifier;
* existing parent Project;
* valid references;
* consistent metadata;
* referential integrity.

Validation failures SHALL be reported through the Validation subsystem.

---

# 13. Persistence

Persistence SHALL be performed through Repository abstractions.

Character SHALL remain independent of:

* serialization format;
* storage implementation;
* speech synthesis providers.

---

# 14. Events

Business operations MAY produce events including:

* CharacterCreatedEvent;
* CharacterUpdatedEvent;
* CharacterDeletedEvent;
* CharacterAssignedEvent.

The Character entity SHALL NOT publish events directly.

---

# 15. Compliance

All logical project personas SHALL conform to this specification.

Implementations SHALL preserve Character identity, ownership, and business invariants throughout the Project lifecycle.

---

# 16. References

* Project.md
* Speaker.md
* Voice.md
* VoiceProfile.md
* Fragment.md
* Scene.md
* Chapter.md
* GenerationPreset.md
* ValidationIssue.md
* CreateCharacterCommand.md
* CharacterCreatedEvent.md

---

**End of Document**
