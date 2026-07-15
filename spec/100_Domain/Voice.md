# Voice

**Document Path:**
`spec/100_Domain/Voice.md`

**Document ID:** DOM-043

**Version:** 1.0.0

**Status:** Draft

**Classification:** Normative

---

# 1. Purpose

This document defines the **Voice** reference domain entity of the Voxarium platform.

A Voice represents a globally available voice definition that can be referenced by Projects and VoiceProfiles. It identifies a speech synthesis voice independently of any Project-specific configuration or runtime implementation.

A Voice defines **which voice is available**, while a VoiceProfile defines **how that voice is configured for a specific Project**.

---

# 2. Scope

This specification defines:

* responsibilities;
* ownership;
* lifecycle;
* relationships;
* business invariants.

Speech synthesis providers, runtime voice loading, neural inference, and audio generation are outside the scope of this specification.

---

# 3. Definition

A **Voice** is a global reference entity representing an available speech synthesis voice.

It provides a stable business identifier independent of provider implementation.

---

# 4. Responsibilities

Voice SHALL be responsible for:

* identifying available voices;
* exposing voice metadata;
* declaring supported languages;
* declaring supported capabilities;
* serving as a reusable Project reference.

Voice SHALL NOT:

* synthesize speech;
* store Project-specific settings;
* execute generation;
* own generated audio.

---

# 5. Identity

Every Voice SHALL possess a globally unique identifier.

Its identity SHALL remain stable regardless of:

* display name changes;
* provider updates;
* metadata modifications.

---

# 6. Ownership

Voice is a global reference entity.

Voice SHALL NOT belong to a specific Project.

Projects MAY reference the same Voice simultaneously.

---

# 7. Voice Information

A Voice MAY define:

* provider identifier;
* provider voice identifier;
* display name;
* supported languages;
* gender where applicable;
* age category where applicable;
* available capabilities;
* provider metadata.

Voice information SHALL remain implementation-independent whenever possible.

---

# 8. Relationships

Voice MAY be referenced by:

* VoiceProfile;
* Speaker;
* Language;
* GenerationPreset;
* AudioGenerationPreset.

Voice SHALL NOT own Project resources.

---

# 9. Metadata

Voice SHOULD expose:

* identifier;
* display name;
* provider;
* version;
* creation timestamp;
* optional provider metadata.

Metadata SHALL NOT alter Voice identity.

---

# 10. Lifecycle

The lifecycle SHALL consist of:

1. registration;
2. availability;
3. metadata updates;
4. deprecation where applicable.

Deprecated Voices MAY remain available for compatibility with historical Projects.

---

# 11. Business Rules

The following rules SHALL apply:

* every Voice SHALL possess a globally unique identifier;
* Voice identifiers SHALL remain immutable;
* multiple Projects MAY reference the same Voice;
* Voice SHALL remain independent of Project configuration.

---

# 12. Validation

Validation SHALL verify:

* unique identifier;
* valid provider identifier;
* valid language references;
* internally consistent metadata;
* supported capability declarations.

Validation failures SHALL be reported through the Validation subsystem.

---

# 13. Persistence

Persistence SHALL be performed through Repository abstractions.

Voice SHALL remain independent of:

* provider SDKs;
* storage implementation;
* serialization format.

---

# 14. Events

Business operations MAY produce events including:

* VoiceRegisteredEvent;
* VoiceUpdatedEvent;
* VoiceDeprecatedEvent.

The Voice entity SHALL NOT publish events directly.

---

# 15. Compliance

All globally available voices within Voxarium SHALL conform to this specification.

Implementations SHALL preserve stable identity, provider independence, referential integrity, and business invariants defined by this document.

---

# 16. References

* VoiceProfile.md
* Speaker.md
* Language.md
* GenerationPreset.md
* AudioGenerationPreset.md
* ValidationIssue.md
* RegisterVoiceCommand.md
* VoiceRegisteredEvent.md

---

**End of Document**
