# TextAsset

**Document Path:**
`spec/100_Domain/TextAsset.md`

**Document ID:** DOM-059

**Version:** 1.0.0

**Status:** Draft

**Classification:** Normative

---

# 1. Purpose

This document defines the **TextAsset** domain entity of the Voxarium platform.

A TextAsset represents a reusable textual resource within a Project. It provides a unified business abstraction for textual content regardless of its origin, storage format, or intended use in narration, subtitle generation, translation, or document processing.

A TextAsset represents the textual content itself rather than the document that contains it.

---

# 2. Scope

This specification defines:

* responsibilities;
* ownership;
* lifecycle;
* relationships;
* business invariants.

Document parsing, file formats, OCR, translation engines, language models, and rendering are outside the scope of this specification.

---

# 3. Definition

A **TextAsset** is a domain entity representing reusable textual content belonging to a Project.

It serves as the canonical business representation of text used by other domain entities.

---

# 4. Responsibilities

TextAsset SHALL be responsible for:

* representing textual content;
* preserving text integrity;
* exposing text metadata;
* supporting reuse across Project workflows;
* maintaining language information.

TextAsset SHALL NOT:

* parse documents;
* generate speech;
* perform translation;
* execute text processing algorithms.

---

# 5. Identity

Every TextAsset SHALL possess a globally unique identifier.

Its identity SHALL remain stable regardless of:

* text revisions;
* metadata modifications;
* relationship changes.

---

# 6. Ownership

Every TextAsset SHALL belong to exactly one Project.

A Project MAY contain zero or more TextAssets.

Lifecycle management SHALL be coordinated by the owning Project Aggregate.

---

# 7. Content

A TextAsset SHALL contain textual content.

A TextAsset MAY additionally define:

* title;
* summary;
* source information;
* language;
* encoding metadata;
* revision information.

The business meaning of the text SHALL remain independent of its original file format.

---

# 8. Relationships

TextAsset MAY reference:

* Project;
* Document;
* Chapter;
* Fragment;
* Subtitle;
* Language;
* Dictionary;
* Lexicon;
* Tag.

Referenced entities SHALL remain external to the TextAsset.

---

# 9. Metadata

TextAsset SHOULD expose:

* identifier;
* display name;
* creation timestamp;
* modification timestamp;
* text length;
* optional checksum;
* optional tags.

Metadata SHALL NOT affect TextAsset identity.

---

# 10. Lifecycle

The lifecycle SHALL consist of:

1. creation;
2. content assignment;
3. validation;
4. modification;
5. archival or deletion.

Deleting a TextAsset SHALL NOT automatically delete referencing entities.

---

# 11. Business Rules

The following rules SHALL apply:

* every TextAsset belongs to exactly one Project;
* textual content SHALL always exist;
* language SHALL be identifiable where applicable;
* references SHALL preserve referential integrity;
* identity SHALL remain immutable.

---

# 12. Validation

Validation SHALL verify:

* unique identifier;
* existing Project;
* non-empty textual content;
* valid language reference where applicable;
* internally consistent metadata.

Validation failures SHALL be reported through the Validation subsystem.

---

# 13. Persistence

Persistence SHALL be performed through Repository abstractions.

TextAsset SHALL remain independent of:

* document formats;
* storage implementation;
* serialization format;
* text processing engines.

---

# 14. Events

Business operations MAY produce events including:

* TextAssetCreatedEvent;
* TextAssetUpdatedEvent;
* TextAssetDeletedEvent.

Event publication SHALL occur outside the Aggregate.

---

# 15. Compliance

All textual resources within Voxarium SHALL conform to this specification.

Implementations SHALL preserve stable identity, ownership boundaries, referential integrity, and business invariants defined by this document.

---

# 16. References

* Project.md
* Document.md
* Chapter.md
* Fragment.md
* Subtitle.md
* Language.md
* Dictionary.md
* Lexicon.md
* Tag.md
* ValidationIssue.md
* CreateTextAssetCommand.md
* UpdateTextAssetCommand.md
* DeleteTextAssetCommand.md
* TextAssetCreatedEvent.md

---

**End of Document**
