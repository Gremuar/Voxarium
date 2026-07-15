# Terminology

**Document Path:**
`spec/000_Foundation/Terminology.md`

**Document ID:** FOUND-012

**Version:** 1.0.0

**Status:** Draft

**Classification:** Normative

---

# 1. Purpose

This document defines the canonical terminology used throughout the Voxarium Architecture Specification.

Its purpose is to establish a single vocabulary for architects, developers, plugin authors, testers, technical writers, and AI assistants working on the project.

Every architectural term SHALL have exactly one canonical meaning.

---

# 2. Scope

This document applies to:

* architecture documentation;
* source code;
* public APIs;
* project format;
* plugins;
* graphical user interface;
* testing documentation.

---

# 3. General Rules

The following principles SHALL apply:

* one concept SHALL have one canonical name;
* one term SHALL represent one concept only;
* synonyms SHALL be avoided;
* abbreviations SHALL be minimized;
* terminology SHALL remain stable across releases.

---

# 4. Core Architectural Terms

## Application

The orchestration layer responsible for executing use cases and coordinating interactions between the User Interface, Domain, and Infrastructure.

---

## Architecture

The complete logical structure governing the organization, behavior, and evolution of the Voxarium platform.

---

## Aggregate

A consistency boundary containing one Aggregate Root and the entities and value objects it controls.

External components SHALL communicate with an Aggregate only through its Aggregate Root.

---

## Aggregate Root

The primary entry point to an Aggregate.

Only Aggregate Roots may be referenced from outside the Aggregate.

---

## Entity

An object possessing a stable identity throughout its lifetime.

Entity equality SHALL be identity-based.

---

## Value Object

An immutable object identified entirely by its value.

Value Objects SHALL NOT possess independent identity.

---

## Domain

The layer containing business rules, invariants, entities, aggregates, value objects, and domain services.

---

## Infrastructure

The layer implementing technical concerns such as persistence, networking, filesystem access, speech engines, logging, and plugin loading.

---

## User Interface

The presentation layer responsible for visualization and user interaction.

The User Interface SHALL NOT implement business logic.

---

# 5. Application Terms

## Command

A request expressing the intention to change application state.

Commands are executed by the Application layer.

---

## Query

A request for information that SHALL NOT modify system state.

---

## Event

An immutable representation of a completed fact.

Events describe what has already happened.

---

## Event Handler

A component responsible for reacting to published events.

---

## Application Service

A component coordinating one or more business use cases.

Application Services SHALL NOT own business rules.

---

# 6. Domain Terms

## Project

The highest-level business object representing a Voxarium workspace artifact.

A Project contains all information necessary for speech production.

---

## Document

A structured textual resource contained within a Project.

---

## Fragment

The smallest editable unit of textual content managed by the application.

---

## Timeline

An ordered arrangement of content used for playback and speech generation sequencing.

---

## Voice

A speech synthesis profile capable of producing spoken audio.

---

## Speaker

A logical actor assigned to one or more textual fragments.

A Speaker references a Voice but is not itself a speech engine.

---

## Dictionary

A collection of pronunciation and normalization rules.

---

# 7. Plugin Terms

## Plugin

An independently deployable software extension executed by the Plugin Host.

Plugins extend functionality without modifying the application core.

---

## Extension Point

A documented interface through which plugins integrate with the application.

---

## Plugin Host

The subsystem responsible for discovering, loading, isolating, and managing plugins.

---

# 8. Persistence Terms

## Repository

An abstraction responsible for loading and storing Aggregate Roots.

Repositories hide persistence implementation details.

---

## Serialization

The transformation of runtime objects into persistent representations and vice versa.

---

## Project Format

The canonical persistent representation of a Voxarium project.

---

# 9. Testing Terms

## Unit Test

A test verifying a single unit of behavior in isolation.

---

## Integration Test

A test verifying interactions between multiple architectural components.

---

## System Test

A test validating the behavior of the complete application.

---

## Regression Test

A test ensuring that previously corrected defects do not reappear.

---

# 10. Error Terms

## Error

A structured representation of an abnormal condition.

Errors SHALL conform to the Error Model specification.

---

## Validation Issue

A diagnostic indicating that application data violates one or more validation rules.

---

## Warning

A non-fatal condition that may require user attention.

Warnings SHALL NOT prevent continued execution unless explicitly documented.

---

# 11. Forbidden Terminology

The following generic terms SHALL NOT be used in architectural documentation unless further qualified:

* Data
* Object
* Item
* Manager
* Handler
* Processor
* Helper
* Utility
* Module
* Thing

These names are insufficiently descriptive.

---

# 12. Synonyms

The following synonymous terms SHALL NOT be mixed:

| Preferred | Avoid          |
| --------- | -------------- |
| Project   | Workspace File |
| Fragment  | Text Block     |
| Voice     | Engine Voice   |
| Event     | Notification   |
| Command   | Action         |
| Query     | Request        |

The preferred terminology SHALL be used consistently.

---

# 13. Future Terms

New architectural terms SHALL be added to this document before being introduced elsewhere in the specification.

Each new term SHALL have:

* a definition;
* architectural context;
* ownership;
* relationship to existing terminology.

---

# 14. Compliance

Every document within the Voxarium Architecture Specification SHALL use the terminology defined by this document.

Architectural reviews SHALL verify terminology consistency across the repository.

---

# 15. References

* Documentation_Index.md
* Architecture_Principles.md
* Naming_Conventions.md
* Component_Model.md
* Bounded_Contexts.md
* Event_Model.md
* Error_Model.md

---

**End of Document**
