# Dictionary

**Document Path:**
`spec/100_Domain/Dictionary.md`

**Document ID:** DOM-012

**Version:** 1.0.0

**Status:** Draft

**Classification:** Normative

---

# 1. Purpose

This document defines the **Dictionary** domain entity of the Voxarium platform.

A Dictionary represents a reusable collection of lexical rules that influence pronunciation, normalization, token transformation, and speech generation. It provides a business-level abstraction independent of any specific speech synthesis engine.

---

# 2. Scope

This specification defines:

* responsibilities;
* ownership;
* lifecycle;
* relationships;
* business invariants.

The internal storage format and engine-specific dictionary implementations are outside the scope of this specification.

---

# 3. Definition

A **Dictionary** is a domain entity representing a managed collection of lexical entries used during text processing and speech generation.

A Dictionary defines *what* lexical knowledge is available to the Project rather than *how* that knowledge is applied by a particular engine.

---

# 4. Responsibilities

Dictionary SHALL be responsible for:

* grouping lexical entries;
* providing reusable pronunciation resources;
* exposing dictionary metadata;
* maintaining lexical consistency;
* participating in validation.

Dictionary SHALL NOT:

* synthesize speech;
* execute text normalization;
* modify project content directly;
* communicate with speech providers.

---

# 5. Identity

Every Dictionary SHALL possess a globally unique identifier.

Its identity SHALL remain stable regardless of:

* name changes;
* entry modifications;
* metadata updates.

---

# 6. Ownership

Every Dictionary SHALL belong to exactly one Project.

Dictionaries SHALL NOT be shared directly between Projects.

Cross-project reuse SHALL occur only through explicit import or duplication.

---

# 7. Contents

A Dictionary SHALL contain zero or more DictionaryEntry entities.

The Dictionary SHALL be the aggregate root responsible for managing the lifecycle of its entries.

Entries SHALL NOT exist independently of a Dictionary.

---

# 8. Relationships

Dictionary MAY reference:

* Project;
* Language;
* PronunciationDictionary;
* Lexicon;
* AudioGenerationPreset;
* GenerationPreset;
* VoiceProfile.

Dictionary SHALL own only its DictionaryEntry entities.

---

# 9. Metadata

A Dictionary SHOULD expose:

* identifier;
* name;
* description;
* primary language;
* version;
* creation timestamp;
* modification timestamp.

Metadata SHALL NOT alter the semantic meaning of lexical entries.

---

# 10. Lifecycle

The lifecycle SHALL consist of:

1. creation;
2. population with entries;
3. modification;
4. usage;
5. archival or deletion.

Deleting a Dictionary SHALL delete all contained DictionaryEntry entities.

---

# 11. Business Rules

The following rules SHALL apply:

* every Dictionary belongs to exactly one Project;
* every DictionaryEntry belongs to exactly one Dictionary;
* entry identifiers SHALL be unique within the Dictionary;
* duplicate lexical entries MAY be restricted by application policy;
* dictionary integrity SHALL be preserved after every modification.

---

# 12. Aggregate Rules

Dictionary is the Aggregate Root.

All modifications to DictionaryEntry SHALL occur through Dictionary.

External components SHALL NOT modify DictionaryEntry entities directly.

---

# 13. Validation

Validation SHALL verify:

* unique identifier;
* existing parent Project;
* valid Language reference;
* unique entry identifiers;
* internal consistency of lexical data.

Validation failures SHALL be reported through the Validation subsystem.

---

# 14. Persistence

Persistence SHALL be performed through Repository abstractions.

Dictionary SHALL remain independent of:

* serialization format;
* storage implementation;
* speech engine dictionary formats.

---

# 15. Events

Business operations MAY produce events including:

* DictionaryCreatedEvent;
* DictionaryUpdatedEvent;
* DictionaryDeletedEvent;
* DictionaryEntryAddedEvent;
* DictionaryEntryRemovedEvent.

Events SHALL be published by the Application layer.

---

# 16. Compliance

All managed lexical collections within Voxarium SHALL conform to this specification.

Implementations SHALL preserve aggregate boundaries, ownership rules, and business invariants defined by this document.

---

# 17. References

* Project.md
* DictionaryEntry.md
* Language.md
* Lexicon.md
* PronunciationDictionary.md
* GenerationPreset.md
* AudioGenerationPreset.md
* VoiceProfile.md
* ValidationIssue.md
* CreateDictionaryCommand.md
* DictionaryCreatedEvent.md

---

**End of Document**
