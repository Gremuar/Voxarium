# DictionaryEntry

**Document Path:**
`spec/100_Domain/DictionaryEntry.md`

**Document ID:** DOM-013

**Version:** 1.0.0

**Status:** Draft

**Classification:** Normative

---

# 1. Purpose

This document defines the **DictionaryEntry** domain entity of the Voxarium platform.

A DictionaryEntry represents a single lexical rule within a Dictionary. It defines how a lexical item is interpreted, normalized, or pronounced during speech generation and related text-processing workflows.

DictionaryEntry exists exclusively within the Aggregate Root **Dictionary**.

---

# 2. Scope

This specification defines:

* responsibilities;
* ownership;
* lifecycle;
* business invariants;
* aggregate rules.

Storage formats and speech engine implementations are outside the scope of this specification.

---

# 3. Definition

A **DictionaryEntry** is a domain entity representing one managed lexical record belonging to a Dictionary.

It models business knowledge rather than implementation-specific pronunciation rules.

---

# 4. Responsibilities

DictionaryEntry SHALL be responsible for:

* representing a single lexical item;
* storing lexical metadata;
* exposing pronunciation information;
* supporting validation;
* participating in dictionary management.

DictionaryEntry SHALL NOT:

* execute pronunciation;
* perform speech synthesis;
* modify its parent Dictionary directly;
* communicate with external systems.

---

# 5. Identity

Every DictionaryEntry SHALL possess a unique identifier.

Its identity SHALL remain stable within the lifetime of its parent Dictionary.

Identity uniqueness SHALL be guaranteed only inside the owning Dictionary Aggregate.

---

# 6. Ownership

Every DictionaryEntry SHALL belong to exactly one Dictionary.

DictionaryEntry SHALL NOT exist independently.

Ownership SHALL NOT change after creation.

---

# 7. Lexical Information

A DictionaryEntry MAY contain:

* source text;
* normalized form;
* pronunciation;
* phonetic representation;
* language;
* notes;
* optional tags.

The exact representation SHALL remain independent of speech engine implementations.

---

# 8. Relationships

DictionaryEntry MAY reference:

* Dictionary;
* Language;
* PronunciationDictionary;
* LexiconEntry.

DictionaryEntry SHALL NOT own external entities.

---

# 9. Metadata

DictionaryEntry SHOULD expose:

* identifier;
* creation timestamp;
* modification timestamp;
* author where applicable;
* version.

Metadata SHALL NOT change lexical meaning.

---

# 10. Lifecycle

The lifecycle SHALL consist of:

1. creation;
2. insertion into Dictionary;
3. modification;
4. usage;
5. removal.

Creation and deletion SHALL occur only through the owning Dictionary Aggregate.

---

# 11. Business Rules

The following rules SHALL apply:

* every DictionaryEntry belongs to one Dictionary;
* duplicate identifiers SHALL NOT exist within the same Dictionary;
* lexical information SHALL remain internally consistent;
* orphan DictionaryEntry entities SHALL NOT exist.

---

# 12. Aggregate Rules

DictionaryEntry is part of the Dictionary Aggregate.

External components SHALL NOT:

* create DictionaryEntry independently;
* delete DictionaryEntry independently;
* modify DictionaryEntry bypassing Dictionary.

All state changes SHALL be coordinated by the Aggregate Root.

---

# 13. Validation

Validation SHALL verify:

* existing parent Dictionary;
* unique identifier;
* valid lexical data;
* valid language reference;
* internally consistent metadata.

Validation failures SHALL be reported through the Validation subsystem.

---

# 14. Persistence

Persistence SHALL be managed exclusively by the Dictionary Repository.

DictionaryEntry SHALL remain independent of:

* serialization format;
* storage technology;
* speech synthesis engines.

---

# 15. Events

DictionaryEntry participates in Aggregate events including:

* DictionaryEntryAddedEvent;
* DictionaryEntryUpdatedEvent;
* DictionaryEntryRemovedEvent.

The entity itself SHALL NOT publish events.

---

# 16. Compliance

All managed lexical records SHALL conform to this specification.

Implementations SHALL preserve aggregate boundaries, ownership rules, and business invariants defined herein.

---

# 17. References

* Dictionary.md
* Language.md
* LexiconEntry.md
* PronunciationDictionary.md
* ValidationIssue.md
* AddDictionaryEntryCommand.md
* UpdateDictionaryEntryCommand.md
* RemoveDictionaryEntryCommand.md
* DictionaryEntryAddedEvent.md

---

**End of Document**
