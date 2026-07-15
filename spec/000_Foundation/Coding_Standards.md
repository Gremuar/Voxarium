# Coding Standards

**Document Path:**
`spec/000_Foundation/Coding_Standards.md`

**Document ID:** FOUND-004

**Version:** 1.0.0

**Status:** Draft

**Classification:** Normative

---

# 1. Purpose

This document defines the mandatory coding standards for the Voxarium project.

Its purpose is to ensure that all source code remains consistent, readable, maintainable, and suitable for long-term development.

These standards apply equally to handwritten and AI-generated code.

---

# 2. Scope

These rules apply to:

* application source code;
* plugins;
* libraries;
* test code;
* build scripts where applicable.

Generated third-party code is excluded unless modified within the project.

---

# 3. General Principles

Source code SHALL prioritize:

* readability;
* simplicity;
* determinism;
* maintainability;
* explicitness.

Code SHALL always be written for human readers first.

---

# 4. Naming Conventions

Identifiers SHALL use descriptive names.

Abbreviations SHOULD be avoided unless universally recognized.

Examples:

Good:

* `ProjectService`
* `VoiceProfile`
* `GenerationJob`

Bad:

* `PS`
* `Tmp`
* `Obj`
* `Data1`

---

# 5. File Organization

Each source file SHALL have a single primary responsibility.

Files SHOULD remain reasonably small.

A file SHALL contain one primary public type unless language conventions dictate otherwise.

---

# 6. Class Design

Classes SHALL have a single responsibility.

Large "God Objects" are prohibited.

Composition SHALL be preferred over inheritance.

Inheritance SHALL represent true specialization.

---

# 7. Function Design

Functions SHALL:

* perform one logical task;
* have descriptive names;
* minimize side effects;
* return predictable results.

Deep nesting SHOULD be avoided.

Early returns are preferred where they improve readability.

---

# 8. Dependency Management

Dependencies SHALL be explicit.

Hidden global dependencies are prohibited.

Dependency Injection SHALL be preferred over service locators.

---

# 9. Error Handling

Recoverable errors SHALL be handled.

Unexpected errors SHALL propagate with sufficient diagnostic information.

Empty exception handlers are prohibited.

---

# 10. Logging

Logging SHALL provide operational value.

Logs SHALL be:

* meaningful;
* structured where practical;
* free of sensitive information.

Debug logging SHALL NOT replace proper error handling.

---

# 11. Comments

Comments SHALL explain:

* intent;
* rationale;
* non-obvious decisions.

Comments SHALL NOT merely restate the code.

Outdated comments SHALL be corrected or removed.

---

# 12. Documentation

Every public component SHALL be documented.

Public APIs SHALL describe:

* purpose;
* parameters;
* return values;
* possible failures.

---

# 13. Immutability

Immutable data structures SHOULD be preferred whenever practical.

Mutable shared state SHALL be minimized.

---

# 14. Constants

Magic numbers are prohibited.

Named constants SHALL be used for all reusable values.

---

# 15. Formatting

Formatting SHALL remain consistent throughout the repository.

Automatic formatting tools SHOULD be used where available.

Manual formatting SHALL follow project conventions.

---

# 16. Testing

New functionality SHALL include corresponding automated tests whenever practical.

Bug fixes SHOULD include regression tests.

---

# 17. AI-Generated Code

AI-generated code SHALL satisfy the same quality requirements as manually written code.

Generated code SHALL be reviewed before integration.

The origin of code SHALL NOT affect review standards.

---

# 18. Prohibited Practices

The following are prohibited:

* duplicated business logic;
* cyclic dependencies;
* dead code;
* commented-out implementations;
* unexplained workarounds;
* hidden side effects.

---

# 19. Compliance

All source code SHALL comply with this document.

Architecture reviews and code reviews SHALL verify compliance.

---

# 20. References

* Documentation_Index.md
* Architecture_Principles.md
* Architecture_Overview.md
* Naming_Conventions.md
* Dependency_Rules.md

---

**End of Document**
