# LexiconEntry

**Document Path:**
`spec/100_Domain/LexiconEntry.md`

**Document ID:** DOM-027

**Version:** 1.0.0

**Status:** Draft

**Classification:** Normative

---

# 1. Purpose

This document defines the **LexiconEntry** domain entity of the Voxarium platform.

A LexiconEntry represents a single linguistic entry within a Lexicon. It describes the canonical lexical characteristics of a word, phrase, or linguistic construct and serves as the smallest managed unit of lexical knowledge.

LexiconEntry exists exclusively within the **Lexicon** Aggregate.

---

# 2. Scope

This specification defines:

* responsibilities;
* ownership;
* lifecycle;
* aggregate boundaries;
* business invariants.

Morphological analysis, pronunciation engines, and linguistic processing algorithms are outside the scope of this specification.

---

# 3. Definition

A **LexiconEntry** is a domain entity representing one managed lexical record belonging to a Lexicon.

It models structured linguistic information rather than speech engine configuration.

---

# 4. Responsibilities

LexiconEntry SHALL be responsible for:

* representing a lexical unit;
* storing canonical linguistic information;
* exposing lexical metadata;
* supporting validation;
* participating in linguistic workflows.

LexiconEntry SHALL NOT:

* execute linguistic analysis;
* perform pronunciation;
* modify its parent Lexicon;
* communicate with external services.

---

# 5. Identity

Every LexiconEntry SHALL possess a unique identifier.

Its identity SHALL remain stable within the lifetime of its parent Lexicon.

Identity uniqueness SHALL be guaranteed only inside the owning Aggregate.

---

# 6. Ownership

Every LexiconEntry SHALL belong to exactly one Lexicon.

LexiconEntry SHALL NOT exist independently.

Creation, modification, and deletion SHALL occur only through the Lexicon Aggregate Root.

---

# 7. Linguistic Information

A LexiconEntry MAY contain:

* canonical text;
* normalized form;
* pronunciation;
* phonetic transcription;
* part of speech;
* grammatical attributes;
* language;
* usage notes;
* custom metadata.

The representation SHALL remain independent of any specific linguistic engine.

---

# 8. Relationships

LexiconEntry MAY reference:

* Lexicon;
* Language;
* DictionaryEntry;
* PronunciationDictionary.

LexiconEntry SHALL NOT own external entities.

---

# 9. Metadata

LexiconEntry SHOULD expose:

* identifier;
* creation timestamp;
* modification timestamp;
* version;
* author where applicable.

Metadata SHALL NOT alter lexical meaning.

---

# 10. Lifecycle

The lifecycle SHALL consist of:

1. creation;
2. insertion into Lexicon;
3. modification;
4. usage;
5. removal.

Lifecycle management SHALL be coordinated exclusively by the Lexicon Aggregate.

---

# 11. Business Rules

The following rules SHALL apply:

* every LexiconEntry belongs to exactly one Lexicon;
* duplicate identifiers SHALL NOT exist within the same Lexicon;
* lexical information SHALL remain internally consistent;
* orphan LexiconEntry entities SHALL NOT exist.

---

# 12. Aggregate Rules

LexiconEntry is a member of the Lexicon Aggregate.

External components SHALL NOT:

* create LexiconEntry independently;
* delete LexiconEntry independently;
* modify LexiconEntry outside the Aggregate.

All state transitions SHALL be coordinated by the Lexicon Aggregate Root.

---

# 13. Validation

Validation SHALL verify:

* existing parent Lexicon;
* unique identifier;
* valid language reference;
* internally consistent linguistic information;
* compliance with aggregate invariants.

Validation failures SHALL be reported through the Validation subsystem.

---

# 14. Persistence

Persistence SHALL be managed exclusively through the Lexicon Repository.

LexiconEntry SHALL remain independent of:

* serialization format;
* storage technology;
* linguistic processing engines.

---

# 15. Events

LexiconEntry participates in Aggregate events including:

* LexiconEntryAddedEvent;
* LexiconEntryUpdatedEvent;
* LexiconEntryRemovedEvent.

The entity itself SHALL NOT publish events.

---

# 16. Compliance

All managed lexical records within Voxarium SHALL conform to this specification.

Implementations SHALL preserve aggregate boundaries, ownership rules, stable identity, and business invariants defined herein.

---

# 17. References

* Lexicon.md
* Language.md
* DictionaryEntry.md
* PronunciationDictionary.md
* ValidationIssue.md
* AddLexiconEntryCommand.md
* UpdateLexiconEntryCommand.md
* RemoveLexiconEntryCommand.md
* LexiconEntryAddedEvent.md

---

**End of Document**
