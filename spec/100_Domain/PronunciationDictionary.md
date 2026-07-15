# PronunciationDictionary

**Document Path:**
`spec/100_Domain/PronunciationDictionary.md`

**Document ID:** DOM-035

**Version:** 1.0.0

**Status:** Draft

**Classification:** Normative

---

# 1. Purpose

This document defines the **PronunciationDictionary** Aggregate Root of the Voxarium platform.

A PronunciationDictionary represents a managed collection of pronunciation rules and lexical pronunciation entries used during speech generation. It provides a consistent business abstraction for pronunciation management independently of any specific speech synthesis provider.

---

# 2. Scope

This specification defines:

* responsibilities;
* ownership;
* aggregate boundaries;
* lifecycle;
* relationships;
* business invariants.

Phoneme conversion algorithms, grapheme-to-phoneme engines, and provider-specific pronunciation formats are outside the scope of this specification.

---

# 3. Definition

A **PronunciationDictionary** is the Aggregate Root representing a managed pronunciation dictionary.

It defines the consistency boundary for pronunciation entries and pronunciation rules.

---

# 4. Responsibilities

PronunciationDictionary SHALL be responsible for:

* managing pronunciation entries;
* maintaining pronunciation consistency;
* coordinating pronunciation rules;
* exposing pronunciation metadata;
* supporting pronunciation validation.

PronunciationDictionary SHALL NOT:

* synthesize speech;
* execute pronunciation algorithms;
* perform text normalization;
* communicate with speech providers.

---

# 5. Identity

Every PronunciationDictionary SHALL possess a globally unique identifier.

Its identity SHALL remain stable regardless of:

* name changes;
* entry modifications;
* metadata updates.

---

# 6. Ownership

Every PronunciationDictionary SHALL belong to exactly one Project.

A PronunciationDictionary SHALL own:

* pronunciation entries;
* pronunciation rules.

Owned entities SHALL NOT exist independently.

---

# 7. Aggregate Boundary

PronunciationDictionary SHALL be the Aggregate Root.

All modifications affecting owned entities SHALL occur through the Aggregate Root.

External components SHALL NOT modify aggregate members directly.

---

# 8. Contents

A PronunciationDictionary MAY contain:

* pronunciation entries;
* phoneme mappings;
* pronunciation exceptions;
* language-specific pronunciation rules;
* provider-independent phonetic representations.

The exact internal structure MAY evolve without changing aggregate responsibilities.

---

# 9. Relationships

PronunciationDictionary MAY reference:

* Project;
* Language;
* Dictionary;
* Lexicon;
* VoiceProfile;
* PhonemeRule.

PronunciationDictionary SHALL own only its internal pronunciation entities.

---

# 10. Metadata

PronunciationDictionary SHOULD expose:

* identifier;
* name;
* description;
* primary language;
* version;
* creation timestamp;
* modification timestamp.

Metadata SHALL NOT affect aggregate identity.

---

# 11. Lifecycle

The lifecycle SHALL consist of:

1. creation;
2. population with pronunciation data;
3. validation;
4. modification;
5. archival or deletion.

Deleting a PronunciationDictionary SHALL delete all owned pronunciation entities.

---

# 12. Business Rules

The following rules SHALL apply:

* every PronunciationDictionary belongs to exactly one Project;
* owned pronunciation entities SHALL belong to exactly one PronunciationDictionary;
* pronunciation information SHALL remain internally consistent;
* aggregate integrity SHALL always be preserved.

---

# 13. Validation

Validation SHALL verify:

* unique identifier;
* existing Project;
* valid Language reference;
* internally consistent pronunciation data;
* aggregate integrity.

Validation failures SHALL be reported through the Validation subsystem.

---

# 14. Persistence

Persistence SHALL be performed through Repository abstractions.

PronunciationDictionary SHALL remain independent of:

* storage implementation;
* serialization format;
* speech synthesis providers.

---

# 15. Events

Business operations MAY produce events including:

* PronunciationDictionaryCreatedEvent;
* PronunciationDictionaryUpdatedEvent;
* PronunciationDictionaryDeletedEvent;
* PronunciationEntryAddedEvent;
* PronunciationEntryRemovedEvent.

Event publication SHALL occur outside the Aggregate.

---

# 16. Compliance

All managed pronunciation dictionaries within Voxarium SHALL conform to this specification.

Implementations SHALL preserve aggregate boundaries, ownership rules, stable identity, and business invariants defined by this document.

---

# 17. References

* Project.md
* Language.md
* Dictionary.md
* Lexicon.md
* VoiceProfile.md
* PhonemeRule.md
* ValidationIssue.md
* CreatePronunciationDictionaryCommand.md
* PronunciationDictionaryCreatedEvent.md

---

**End of Document**
