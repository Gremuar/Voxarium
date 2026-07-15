# ValidationIssue

**Document Path:**
`spec/100_Domain/ValidationIssue.md`

**Document ID:** DOM-042

**Version:** 1.0.0

**Status:** Draft

**Classification:** Normative

---

# 1. Purpose

This document defines the **ValidationIssue** domain entity of the Voxarium platform.

A ValidationIssue represents a business-level validation finding produced during verification of Project resources. It records violations of domain rules, consistency constraints, or business policies while remaining independent of user interface presentation and validation engine implementation.

---

# 2. Scope

This specification defines:

* responsibilities;
* ownership;
* lifecycle;
* relationships;
* business invariants.

Validation algorithms, diagnostics formatting, IDE integration, and UI presentation are outside the scope of this specification.

---

# 3. Definition

A **ValidationIssue** is a domain entity representing a single validation finding.

It describes a detected business problem without prescribing how it should be displayed or resolved.

---

# 4. Responsibilities

ValidationIssue SHALL be responsible for:

* representing validation findings;
* identifying affected domain objects;
* exposing severity information;
* preserving diagnostic metadata;
* supporting validation workflows.

ValidationIssue SHALL NOT:

* perform validation;
* modify Project resources;
* automatically resolve violations;
* execute business logic.

---

# 5. Identity

Every ValidationIssue SHALL possess a globally unique identifier.

Its identity SHALL remain stable throughout its lifetime regardless of:

* description changes;
* severity changes;
* metadata updates.

---

# 6. Ownership

Every ValidationIssue SHALL belong to exactly one Project.

A ValidationIssue SHALL reference one primary affected domain entity.

Historical validation records MAY be preserved after the referenced entity changes.

---

# 7. Classification

A ValidationIssue SHALL define a severity.

Supported severities MAY include:

* Information;
* Warning;
* Error;
* Critical.

Projects MAY introduce additional classifications provided the existing severity semantics remain compatible.

---

# 8. Relationships

ValidationIssue MAY reference:

* Project;
* Document;
* Chapter;
* Fragment;
* Timeline;
* TimelineClip;
* TimelineMarker;
* Dictionary;
* DictionaryEntry;
* Lexicon;
* LexiconEntry;
* AudioAsset;
* Character;
* Speaker.

ValidationIssue SHALL NOT own referenced entities.

---

# 9. Metadata

ValidationIssue SHOULD expose:

* identifier;
* validation rule identifier;
* severity;
* message;
* creation timestamp;
* resolution timestamp where applicable;
* optional category.

Metadata SHALL NOT affect issue identity.

---

# 10. Lifecycle

The lifecycle SHALL consist of:

1. creation;
2. reporting;
3. review;
4. optional resolution;
5. archival or deletion.

Resolved ValidationIssues MAY remain available for auditing.

---

# 11. Business Rules

The following rules SHALL apply:

* every ValidationIssue belongs to exactly one Project;
* every ValidationIssue SHALL reference at least one affected entity;
* issue identity SHALL remain immutable;
* issue severity SHALL always be explicitly defined.

---

# 12. Validation

Validation SHALL verify:

* unique identifier;
* existing Project;
* valid referenced entities;
* valid severity classification;
* internally consistent diagnostic information.

Validation failures SHALL themselves be reported through the Validation subsystem.

---

# 13. Persistence

Persistence SHALL be performed through Repository abstractions.

ValidationIssue SHALL remain independent of:

* validation engine implementation;
* storage technology;
* serialization format.

---

# 14. Events

Business operations MAY produce events including:

* ValidationIssueCreatedEvent;
* ValidationIssueResolvedEvent;
* ValidationIssueDeletedEvent.

The ValidationIssue entity SHALL NOT publish events directly.

---

# 15. Compliance

All validation findings within Voxarium SHALL conform to this specification.

Implementations SHALL preserve stable identity, ownership boundaries, diagnostic consistency, and business invariants defined by this document.

---

# 16. References

* Project.md
* Document.md
* Chapter.md
* Fragment.md
* Timeline.md
* TimelineClip.md
* TimelineMarker.md
* Dictionary.md
* DictionaryEntry.md
* Lexicon.md
* LexiconEntry.md
* AudioAsset.md
* Character.md
* Speaker.md
* CreateValidationIssueCommand.md
* ResolveValidationIssueCommand.md
* ValidationIssueCreatedEvent.md

---

**End of Document**
