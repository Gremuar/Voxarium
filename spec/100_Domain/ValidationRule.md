# ValidationRule

**Document Path:**
`spec/100_Domain/ValidationRule.md`

**Document ID:** DOM-062

**Version:** 1.0.0

**Status:** Draft

**Classification:** Normative

---

# 1. Purpose

This document defines the **ValidationRule** domain entity of the Voxarium platform.

A ValidationRule represents a reusable business rule that defines how Project entities are validated. It provides a declarative description of validation requirements independently of validation engines, execution mechanisms, or user interface implementation.

A ValidationRule describes **what must be validated**, not how validation is executed.

---

# 2. Scope

This specification defines:

* responsibilities;
* ownership;
* lifecycle;
* relationships;
* business invariants.

Rule execution engines, expression evaluators, diagnostics generation, scheduling, and infrastructure implementation are outside the scope of this specification.

---

# 3. Definition

A **ValidationRule** is a domain entity representing a reusable business validation rule.

It defines validation semantics without performing validation itself.

---

# 4. Responsibilities

ValidationRule SHALL be responsible for:

* describing validation requirements;
* identifying validation targets;
* defining validation severity;
* exposing validation metadata;
* supporting reusable validation policies.

ValidationRule SHALL NOT:

* execute validation;
* modify validated entities;
* create ValidationIssues directly;
* schedule validation operations.

---

# 5. Identity

Every ValidationRule SHALL possess a globally unique identifier.

Its identity SHALL remain stable regardless of:

* description updates;
* severity changes;
* implementation changes.

---

# 6. Ownership

Every ValidationRule SHALL belong to exactly one Project.

A ValidationJob MAY reference one or more ValidationRules.

The same ValidationRule MAY participate in multiple ValidationJobs.

---

# 7. Rule Definition

A ValidationRule SHALL define:

* rule identifier;
* rule name;
* validation target;
* severity level.

A ValidationRule MAY additionally define:

* category;
* description;
* recommendation;
* applicability conditions;
* optional tags.

The internal evaluation logic SHALL remain implementation independent.

---

# 8. Relationships

ValidationRule MAY reference:

* Project;
* ValidationJob;
* ValidationIssue;
* Document;
* Timeline;
* AudioAsset;
* TextAsset;
* Tag.

Referenced entities SHALL remain external to the ValidationRule.

---

# 9. Metadata

ValidationRule SHOULD expose:

* identifier;
* display name;
* category;
* severity;
* creation timestamp;
* modification timestamp.

Metadata SHALL NOT affect ValidationRule identity.

---

# 10. Lifecycle

The lifecycle SHALL consist of:

1. creation;
2. configuration;
3. validation;
4. usage by ValidationJobs;
5. modification;
6. archival or deletion.

Deleting a ValidationRule SHALL NOT invalidate completed ValidationJobs.

---

# 11. Business Rules

The following rules SHALL apply:

* every ValidationRule belongs to exactly one Project;
* rule identifiers SHALL be unique within a Project;
* validation severity SHALL always be defined;
* ValidationRules SHALL remain immutable during ValidationJob execution.

---

# 12. Validation

Validation SHALL verify:

* unique identifier;
* existing Project;
* valid validation target;
* defined severity;
* internally consistent metadata.

Validation failures SHALL be reported through the Validation subsystem.

---

# 13. Persistence

Persistence SHALL be performed through Repository abstractions.

ValidationRule SHALL remain independent of:

* validation engines;
* rule interpreters;
* storage implementation;
* serialization format.

---

# 14. Events

Business operations MAY produce events including:

* ValidationRuleCreatedEvent;
* ValidationRuleUpdatedEvent;
* ValidationRuleDeletedEvent.

The ValidationRule entity SHALL NOT publish events directly.

---

# 15. Compliance

All business validation rules within Voxarium SHALL conform to this specification.

Implementations SHALL preserve stable identity, ownership boundaries, rule consistency, and business invariants defined by this document.

---

# 16. References

* Project.md
* ValidationJob.md
* ValidationIssue.md
* Document.md
* Timeline.md
* AudioAsset.md
* TextAsset.md
* Tag.md
* CreateValidationRuleCommand.md
* UpdateValidationRuleCommand.md
* ValidationRuleCreatedEvent.md

---

**End of Document**
