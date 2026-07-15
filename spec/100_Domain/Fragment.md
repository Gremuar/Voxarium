# Fragment

**Document Path:**
`spec/100_Domain/Fragment.md`

**Document ID:** DOM-020

**Version:** 1.0.0

**Status:** Draft

**Classification:** Normative

---

# 1. Purpose

This document defines the **Fragment** domain entity of the Voxarium platform.

A Fragment represents the smallest independently editable semantic unit of textual content within a Document. It serves as the primary source entity for speech generation, validation, synchronization, and timeline composition.

---

# 2. Scope

This specification defines:

* responsibilities;
* ownership;
* lifecycle;
* relationships;
* business invariants.

Text editor behavior, rendering, and speech synthesis are outside the scope of this specification.

---

# 3. Definition

A **Fragment** is a domain entity representing a logical piece of document content.

A Fragment is the canonical source of textual information used by downstream business processes.

---

# 4. Responsibilities

Fragment SHALL be responsible for:

* storing textual content;
* preserving semantic integrity;
* serving as the source for speech generation;
* supporting validation;
* participating in document structure.

Fragment SHALL NOT:

* generate speech;
* own audio resources;
* execute commands;
* implement presentation logic.

---

# 5. Identity

Every Fragment SHALL possess a globally unique identifier.

Its identity SHALL remain stable regardless of:

* text modifications;
* movement within the document;
* metadata changes.

---

# 6. Ownership

Every Fragment SHALL belong to exactly one Document.

A Fragment MAY belong to one Chapter.

Ownership SHALL NOT change independently of the owning Document Aggregate.

---

# 7. Content

A Fragment SHALL contain textual content.

A Fragment MAY additionally define:

* language;
* speaking character;
* speaker;
* notes;
* tags;
* custom metadata.

The textual content SHALL remain the authoritative source for downstream generation.

---

# 8. Relationships

Fragment MAY reference:

* Document;
* Chapter;
* Character;
* Speaker;
* VoiceProfile;
* Dictionary;
* Bookmark;
* Note;
* AudioSegment;
* ValidationIssue.

Fragment SHALL NOT own external entities.

---

# 9. Metadata

A Fragment SHOULD expose:

* identifier;
* sequence position;
* creation timestamp;
* modification timestamp;
* language;
* version.

Metadata SHALL NOT affect Fragment identity.

---

# 10. Lifecycle

The lifecycle SHALL consist of:

1. creation;
2. insertion into a Document;
3. modification;
4. validation;
5. archival or deletion.

Deleting a Fragment SHALL occur only through the owning Document Aggregate.

---

# 11. Business Rules

The following rules SHALL apply:

* every Fragment belongs to exactly one Document;
* Fragment ordering SHALL be deterministic;
* Fragment content SHALL remain internally consistent;
* references SHALL preserve referential integrity;
* Fragment identity SHALL remain immutable.

---

# 12. Aggregate Rules

Fragment is a member of the Document Aggregate.

External components SHALL NOT:

* create Fragment independently;
* delete Fragment independently;
* modify Fragment outside the Document Aggregate.

All lifecycle operations SHALL be coordinated by the Document Aggregate Root.

---

# 13. Validation

Validation SHALL verify:

* existing parent Document;
* valid Chapter reference;
* internally consistent content;
* valid language reference;
* valid metadata.

Validation failures SHALL be reported through the Validation subsystem.

---

# 14. Persistence

Persistence SHALL be managed through the Document Repository.

Fragment SHALL remain independent of:

* storage technology;
* serialization format;
* editor implementation.

---

# 15. Events

Business operations MAY produce events including:

* FragmentCreatedEvent;
* FragmentUpdatedEvent;
* FragmentDeletedEvent;
* FragmentMovedEvent.

Event publication SHALL occur outside the entity.

---

# 16. Compliance

All editable textual units within Voxarium SHALL conform to this specification.

Implementations SHALL preserve aggregate boundaries, stable identity, deterministic ordering, and business invariants defined herein.

---

# 17. References

* Document.md
* Chapter.md
* Character.md
* Speaker.md
* VoiceProfile.md
* Dictionary.md
* Bookmark.md
* Note.md
* AudioSegment.md
* ValidationIssue.md
* CreateFragmentCommand.md
* UpdateFragmentCommand.md
* FragmentCreatedEvent.md

---

**End of Document**
