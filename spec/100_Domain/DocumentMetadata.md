# DocumentMetadata

**Document Path:**
`spec/100_Domain/DocumentMetadata.md`

**Document ID:** DOM-015

**Version:** 1.0.0

**Status:** Draft

**Classification:** Normative

---

# 1. Purpose

This document defines the **DocumentMetadata** domain entity of the Voxarium platform.

DocumentMetadata represents the descriptive business information associated with a Document. It contains information used for identification, classification, search, organization, and project management while remaining independent of the document's textual content.

DocumentMetadata is owned exclusively by the **Document** Aggregate Root.

---

# 2. Scope

This specification defines:

* responsibilities;
* ownership;
* lifecycle;
* aggregate boundaries;
* business invariants.

Storage representation and user interface presentation are outside the scope of this specification.

---

# 3. Definition

A **DocumentMetadata** is a domain entity representing descriptive information about a Document.

It contains metadata only and SHALL NOT contain document content.

---

# 4. Responsibilities

DocumentMetadata SHALL be responsible for:

* describing a Document;
* exposing searchable information;
* supporting document organization;
* storing business classification;
* maintaining descriptive attributes.

DocumentMetadata SHALL NOT:

* contain document text;
* modify document hierarchy;
* own other domain entities;
* execute business workflows.

---

# 5. Identity

DocumentMetadata SHALL inherit the identity boundary of its owning Document.

A Document SHALL own exactly one DocumentMetadata instance.

DocumentMetadata SHALL NOT exist independently.

---

# 6. Ownership

DocumentMetadata SHALL belong to exactly one Document.

Ownership SHALL NOT change during its lifetime.

Creation and deletion SHALL occur only through the owning Document Aggregate.

---

# 7. Metadata Fields

DocumentMetadata MAY include:

* title;
* subtitle;
* description;
* language;
* author;
* contributors;
* keywords;
* category;
* tags;
* creation date;
* modification date;
* publication status;
* custom metadata.

The concrete attribute set MAY evolve without changing the business responsibilities of the entity.

---

# 8. Relationships

DocumentMetadata MAY reference:

* Document;
* Language;
* Tag;
* Collection.

DocumentMetadata SHALL NOT own external entities.

---

# 9. Lifecycle

The lifecycle SHALL consist of:

1. creation together with the Document;
2. modification;
3. validation;
4. deletion together with the Document.

Independent lifecycle management SHALL NOT be permitted.

---

# 10. Business Rules

The following rules SHALL apply:

* every Document owns exactly one DocumentMetadata;
* metadata SHALL describe only its owning Document;
* metadata SHALL remain internally consistent;
* modifying metadata SHALL NOT change Document identity.

---

# 11. Aggregate Rules

DocumentMetadata is a member of the Document Aggregate.

External components SHALL NOT:

* create DocumentMetadata independently;
* delete DocumentMetadata independently;
* bypass the Document Aggregate when modifying metadata.

All modifications SHALL be coordinated by the Document Aggregate Root.

---

# 12. Validation

Validation SHALL verify:

* existing parent Document;
* required descriptive fields;
* valid language reference;
* internally consistent metadata;
* compliance with Project conventions.

Validation failures SHALL be reported through the Validation subsystem.

---

# 13. Persistence

Persistence SHALL be managed exclusively through the Document Repository.

DocumentMetadata SHALL remain independent of:

* serialization format;
* storage implementation;
* indexing technology.

---

# 14. Events

Business operations MAY produce events including:

* DocumentMetadataUpdatedEvent;
* DocumentMetadataValidatedEvent.

Event publication SHALL be coordinated by the Application layer.

---

# 15. Compliance

All document descriptive information within Voxarium SHALL conform to this specification.

Implementations SHALL preserve aggregate boundaries, ownership rules, and business invariants defined by this document.

---

# 16. References

* Document.md
* Project.md
* Language.md
* Tag.md
* Collection.md
* ValidationIssue.md
* UpdateDocumentMetadataCommand.md
* DocumentMetadataUpdatedEvent.md

---

**End of Document**
