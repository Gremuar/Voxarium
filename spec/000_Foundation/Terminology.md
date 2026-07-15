# Terminology

**Document Path:**
`spec/000_Foundation/Terminology.md`

**Document ID:** FOUND-015

**Version:** 1.0.0

**Status:** Draft

**Classification:** Normative

---

# 1. Purpose

This document defines the canonical architectural terminology used throughout the Voxarium specification.

Its purpose is to establish a precise and consistent vocabulary for all architecture documents, source code, APIs, project formats, plugins, and testing artifacts.

Unlike **Glossary.md**, which provides concise reference definitions, this document specifies the **normative meaning and usage rules** of architectural terms.

---

# 2. Scope

This specification applies to:

* architecture documentation;
* domain model;
* application layer;
* public contracts;
* project format;
* plugins;
* user interface;
* source code documentation.

---

# 3. Terminology Principles

The terminology of Voxarium SHALL satisfy the following principles:

* every concept SHALL have one canonical term;
* every canonical term SHALL represent one concept only;
* synonymous architectural terms SHALL NOT be introduced;
* terminology SHALL remain stable across releases;
* English SHALL be the canonical language for all architectural terms.

---

# 4. Canonical Terms

The following terms are normative throughout the specification.

| Term       | Canonical Meaning                                                 |
| ---------- | ----------------------------------------------------------------- |
| Project    | The root business object representing an entire Voxarium project. |
| Document   | A structured textual document belonging to a Project.             |
| Fragment   | The smallest editable text unit within a Document.                |
| Timeline   | An ordered sequence controlling playback and generation.          |
| Track      | A logical lane within a Timeline.                                 |
| Clip       | A timeline element referencing project content.                   |
| Speaker    | A logical performer assigned to fragments.                        |
| Voice      | A speech synthesis profile used by a Speaker.                     |
| Dictionary | A collection of pronunciation rules and lexical overrides.        |

---

# 5. Architectural Terms

The following architectural concepts SHALL be used consistently.

## Component

A cohesive architectural unit with clearly defined responsibilities and public contracts.

---

## Layer

A logical architectural level defining dependency direction and responsibility boundaries.

---

## Bounded Context

A business boundary within which terminology and business rules remain internally consistent.

---

## Aggregate

A consistency boundary containing one Aggregate Root and its associated entities and value objects.

---

## Aggregate Root

The sole externally accessible entity of an Aggregate.

---

## Entity

An object possessing persistent identity.

---

## Value Object

An immutable object defined entirely by its value.

---

## Repository

An abstraction responsible for loading and storing Aggregate Roots.

---

## Domain Service

A stateless business service implementing domain behavior that does not naturally belong to an Entity or Aggregate.

---

# 6. Application Terms

## Command

A request expressing the intention to modify application state.

---

## Query

A request that retrieves information without changing application state.

---

## Event

An immutable representation of a completed fact.

---

## Application Service

A service coordinating one or more application use cases.

---

# 7. Infrastructure Terms

## Adapter

A component translating between Voxarium abstractions and external systems.

---

## Provider

An implementation supplying technical capabilities through a defined abstraction.

Examples include speech synthesis providers and storage providers.

---

## Serializer

A component converting runtime objects to and from persistent representations.

---

# 8. Plugin Terms

## Plugin

An independently deployable software extension loaded by the Plugin Host.

---

## Extension Point

A documented integration point exposed by the application.

---

## Plugin Host

The subsystem responsible for plugin discovery, loading, isolation, and lifecycle management.

---

# 9. User Interface Terms

## View

A visual representation of application state.

---

## ViewModel

An object exposing presentation-oriented state to the User Interface.

---

## Workspace

The active application environment in which one or more Projects are managed.

---

# 10. Reserved Terminology

The following terms have reserved architectural meanings and SHALL NOT be redefined:

* Aggregate
* Aggregate Root
* Entity
* Value Object
* Repository
* Command
* Query
* Event
* Component
* Context
* Layer
* Plugin
* Contract

---

# 11. Prohibited Terminology

The following generic names SHALL NOT be used as architectural concepts unless explicitly qualified:

* Manager
* Helper
* Utility
* Object
* Item
* Data
* Module
* Processor
* Handler
* Thing

These names do not adequately communicate architectural intent.

---

# 12. Evolution

New architectural terms SHALL be introduced only after:

1. defining the concept;
2. documenting its relationship to existing terminology;
3. updating this document.

Existing canonical terms SHALL NOT change meaning without an Architecture Decision Record.

---

# 13. Compliance

All specification documents SHALL use the terminology defined by this document.

Architectural reviews SHALL verify terminology consistency across the repository.

---

# 14. References

* Documentation_Index.md
* Glossary.md
* Naming_Conventions.md
* Architecture_Principles.md
* Component_Model.md
* Bounded_Contexts.md

---

**End of Document**
