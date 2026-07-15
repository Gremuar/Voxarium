# Lexicon

**Document Path:**
`spec/100_Domain/Lexicon.md`

**Document ID:** DOM-026

**Version:** 1.0.0

**Status:** Draft

**Classification:** Normative

---

# 1. Purpose

This document defines the **Lexicon** Aggregate Root of the Voxarium platform.

A Lexicon represents a managed collection of lexical knowledge used by the Project for pronunciation, normalization, linguistic analysis, and speech generation. Unlike a Dictionary, which primarily defines replacement and pronunciation rules, a Lexicon represents structured linguistic knowledge.

---

# 2. Scope

This specification defines:

* responsibilities;
* ownership;
* aggregate boundaries;
* lifecycle;
* relationships;
* business invariants.

Linguistic processing algorithms and speech engine implementations are outside the scope of this specification.

---

# 3. Definition

A **Lexicon** is the Aggregate Root representing a managed collection of lexical entries.

It provides the consistency boundary for all LexiconEntry entities.

---

# 4. Responsibilities

Lexicon SHALL be responsible for:

* managing lexical entries;
* preserving lexical consistency;
* exposing lexical metadata;
* supporting linguistic validation;
* coordinating aggregate integrity.

Lexicon SHALL NOT:

* execute text processing;
* perform pronunciation;
* generate speech;
* communicate with external linguistic services.

---

# 5. Identity

Every Lexicon SHALL possess a globally unique identifier.

Its identity SHALL remain stable regardless of:

* name changes;
* entry modifications;
* metadata updates.

---

# 6. Ownership

Every Lexicon SHALL belong to exactly one Project.

A Lexicon SHALL own:

* LexiconEntry entities.

LexiconEntry SHALL NOT exist independently.

---

# 7. Aggregate Boundary

Lexicon SHALL be the Aggregate Root.

All lifecycle operations affecting LexiconEntry SHALL be coordinated through the Lexicon Aggregate.

External components SHALL NOT directly modify LexiconEntry.

---

# 8. Contents

A Lexicon SHALL contain zero or more LexiconEntry entities.

Entries MAY describe:

* lexical forms;
* canonical forms;
* pronunciation information;
* grammatical information;
* language-specific metadata.

---

# 9. Relationships

Lexicon MAY reference:

* Project;
* Language;
* Dictionary;
* PronunciationDictionary;
* VoiceProfile.

Lexicon SHALL own only its LexiconEntry entities.

---

# 10. Metadata

A Lexicon SHOULD expose:

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
2. population with entries;
3. modification;
4. validation;
5. archival or deletion.

Deleting a Lexicon SHALL delete all owned LexiconEntry entities.

---

# 12. Business Rules

The following rules SHALL apply:

* every Lexicon belongs to exactly one Project;
* every LexiconEntry belongs to exactly one Lexicon;
* aggregate consistency SHALL always be preserved;
* duplicate entry identifiers SHALL NOT exist within the same Lexicon.

---

# 13. Validation

Validation SHALL verify:

* unique identifier;
* existing Project;
* valid Language reference;
* internally consistent entries;
* aggregate integrity.

Validation failures SHALL be reported through the Validation subsystem.

---

# 14. Persistence

Persistence SHALL be performed through Repository abstractions.

Lexicon SHALL remain independent of:

* storage implementation;
* serialization format;
* linguistic engines.

---

# 15. Events

Business operations MAY produce events including:

* LexiconCreatedEvent;
* LexiconUpdatedEvent;
* LexiconDeletedEvent;
* LexiconEntryAddedEvent;
* LexiconEntryRemovedEvent.

Event publication SHALL occur outside the Aggregate.

---

# 16. Compliance

All managed lexical collections within Voxarium SHALL conform to this specification.

Implementations SHALL preserve aggregate boundaries, ownership rules, stable identity, and business invariants defined by this document.

---

# 17. References

* Project.md
* LexiconEntry.md
* Language.md
* Dictionary.md
* PronunciationDictionary.md
* VoiceProfile.md
* ValidationIssue.md
* CreateLexiconCommand.md
* LexiconCreatedEvent.md

---

**End of Document**
