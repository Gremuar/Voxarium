# Dependency Rules

**Document Path:**
`spec/000_Foundation/Dependency_Rules.md`

**Document ID:** FOUND-006

**Version:** 1.0.0

**Status:** Draft

**Classification:** Normative

---

# 1. Purpose

This document defines the dependency rules governing the Voxarium architecture.

Its purpose is to ensure that the software remains modular, maintainable, testable, and resistant to architectural degradation over time.

All architectural dependencies SHALL comply with the rules defined herein.

---

# 2. Scope

This document applies to:

* architecture layers;
* architectural components;
* source code modules;
* plugins;
* services;
* contracts;
* tests.

---

# 3. Architectural Principle

Dependencies SHALL always point toward more stable architectural elements.

Business rules SHALL remain independent of implementation details.

Infrastructure SHALL depend upon the Domain, never the reverse.

---

# 4. Layer Dependency Model

The permitted dependency hierarchy is:

```text
User Interface
        │
        ▼
Application
        │
        ▼
Domain
        ▲
        │
Infrastructure
```

The Domain layer SHALL NOT reference any outer layer.

---

# 5. Allowed Dependencies

The following dependencies are permitted.

| From           | To                    |
| -------------- | --------------------- |
| User Interface | Application           |
| User Interface | Contracts             |
| Application    | Domain                |
| Application    | Contracts             |
| Infrastructure | Domain                |
| Infrastructure | Application Contracts |
| Plugins        | Public Contracts      |

---

# 6. Forbidden Dependencies

The following dependencies are prohibited.

| From        | Forbidden Target    |
| ----------- | ------------------- |
| Domain      | User Interface      |
| Domain      | Infrastructure      |
| Domain      | Plugin Host         |
| Domain      | Storage             |
| Application | GUI Components      |
| GUI         | Infrastructure      |
| Plugins     | Internal Components |

---

# 7. Domain Independence

The Domain layer SHALL remain independent from:

* operating system;
* file system;
* serialization;
* databases;
* network protocols;
* graphical interface;
* plugin implementation.

The Domain SHALL only contain business concepts.

---

# 8. Component Dependencies

Component dependencies SHALL satisfy the following constraints:

* acyclic;
* explicit;
* minimal;
* documented.

Circular dependencies are prohibited.

---

# 9. Public Interfaces

Components SHALL communicate only through public interfaces.

Internal implementation details SHALL remain inaccessible to external components.

Public interfaces SHALL be stable.

---

# 10. Dependency Injection

Dependencies SHALL be supplied explicitly.

Service Locator patterns are prohibited unless formally approved through an ADR.

Constructor injection SHOULD be preferred.

---

# 11. Runtime Dependencies

Runtime interactions MAY differ from compile-time dependencies.

Examples include:

* event publication;
* plugin discovery;
* dependency injection;
* reflection.

These mechanisms SHALL NOT violate architectural boundaries.

---

# 12. Event Dependencies

Events establish logical communication only.

Publishing an event SHALL NOT require knowledge of its subscribers.

Subscribers SHALL remain optional.

---

# 13. Command Dependencies

Commands SHALL depend only upon:

* public contracts;
* application interfaces.

Commands SHALL NOT directly manipulate persistence or user interface components.

---

# 14. Plugin Dependencies

Plugins SHALL depend exclusively upon documented extension APIs.

Plugins SHALL NOT reference:

* internal services;
* private classes;
* implementation-specific modules.

Plugin compatibility SHALL rely on published contracts.

---

# 15. Test Dependencies

Test projects MAY depend upon:

* public APIs;
* testing utilities;
* mock implementations.

Production code SHALL NEVER depend upon testing libraries.

---

# 16. Dependency Stability

Stable components SHOULD change less frequently than components depending upon them.

Lower architectural layers SHOULD remain more stable than upper layers.

---

# 17. Cyclic Dependency Prevention

The architecture SHALL remain a Directed Acyclic Graph (DAG).

Any detected dependency cycle SHALL be treated as an architectural defect.

Dependency cycles SHALL be eliminated before release.

---

# 18. Dependency Review

Every newly introduced dependency SHALL satisfy the following questions:

* Is it necessary?
* Is it directed inward?
* Does it violate layering?
* Can it be inverted?
* Can it be removed?

---

# 19. Architectural Evolution

Changes affecting dependency relationships SHALL require architectural review.

Breaking dependency rules SHALL require an Architecture Decision Record (ADR).

---

# 20. Compliance

Architecture validation SHALL verify:

* absence of circular dependencies;
* layer compliance;
* component isolation;
* plugin isolation;
* domain independence.

Violations SHALL be treated as architecture defects.

---

# 21. References

* Documentation_Index.md
* Architecture_Principles.md
* Architecture_Overview.md
* Component_Model.md
* Layered_Architecture.md
* Bounded_Contexts.md
* System_Context.md

---

**End of Document**
