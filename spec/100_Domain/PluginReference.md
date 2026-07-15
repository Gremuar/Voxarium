# PluginReference

**Document Path:**
`spec/100_Domain/PluginReference.md`

**Document ID:** DOM-051

**Version:** 1.0.0

**Status:** Draft

**Classification:** Normative

---

# 1. Purpose

This document defines the **PluginReference** domain entity of the Voxarium platform.

A PluginReference represents a stable reference from a Project to an externally available Plugin. It identifies which Plugin is used by the Project without embedding the Plugin itself into the Project domain model.

PluginReference establishes a business relationship rather than representing a Plugin implementation.

---

# 2. Scope

This specification defines:

* responsibilities;
* ownership;
* lifecycle;
* relationships;
* business invariants.

Plugin installation, discovery, dependency resolution, loading, execution, and sandboxing are outside the scope of this specification.

---

# 3. Definition

A **PluginReference** is a domain entity representing a reference to an external Plugin.

It records the Project's dependency on a Plugin independently of how that Plugin is installed or executed.

---

# 4. Responsibilities

PluginReference SHALL be responsible for:

* identifying a referenced Plugin;
* maintaining Plugin version requirements;
* exposing Plugin metadata;
* supporting compatibility validation;
* preserving reference integrity.

PluginReference SHALL NOT:

* install Plugins;
* execute Plugin code;
* resolve dependencies;
* manage Plugin lifecycle.

---

# 5. Identity

Every PluginReference SHALL possess a globally unique identifier.

Its identity SHALL remain stable regardless of:

* version constraint updates;
* metadata modifications;
* Plugin installation state.

---

# 6. Ownership

Every PluginReference SHALL belong to exactly one Project.

A Project MAY contain zero or more PluginReferences.

A PluginReference SHALL reference exactly one Plugin.

---

# 7. Reference Information

A PluginReference MAY define:

* Plugin identifier;
* version constraint;
* optional minimum version;
* optional maximum version;
* compatibility policy;
* optional description.

The reference SHALL remain independent of Plugin implementation details.

---

# 8. Relationships

PluginReference MAY reference:

* Project;
* PluginRepository;
* Plugin;
* Workspace.

Referenced entities SHALL remain external to the Project.

---

# 9. Metadata

PluginReference SHOULD expose:

* identifier;
* Plugin identifier;
* display name;
* creation timestamp;
* modification timestamp;
* optional tags.

Metadata SHALL NOT affect reference identity.

---

# 10. Lifecycle

The lifecycle SHALL consist of:

1. creation;
2. Plugin association;
3. validation;
4. version update;
5. removal.

Removing a PluginReference SHALL NOT uninstall the referenced Plugin.

---

# 11. Business Rules

The following rules SHALL apply:

* every PluginReference belongs to exactly one Project;
* every PluginReference SHALL reference exactly one Plugin;
* duplicate Plugin references within a Project SHOULD NOT exist;
* version constraints SHALL remain internally consistent.

---

# 12. Validation

Validation SHALL verify:

* unique identifier;
* existing Project;
* valid Plugin identifier;
* valid version constraint;
* internally consistent metadata.

Validation failures SHALL be reported through the Validation subsystem.

---

# 13. Persistence

Persistence SHALL be performed through Repository abstractions.

PluginReference SHALL remain independent of:

* Plugin runtime implementation;
* storage implementation;
* serialization format.

---

# 14. Events

Business operations MAY produce events including:

* PluginReferenceCreatedEvent;
* PluginReferenceUpdatedEvent;
* PluginReferenceRemovedEvent.

The PluginReference entity SHALL NOT publish events directly.

---

# 15. Compliance

All Project Plugin references within Voxarium SHALL conform to this specification.

Implementations SHALL preserve stable identity, ownership boundaries, compatibility integrity, and business invariants defined by this document.

---

# 16. References

* Project.md
* Plugin.md
* PluginRepository.md
* Workspace.md
* ValidationIssue.md
* AddPluginReferenceCommand.md
* RemovePluginReferenceCommand.md
* PluginReferenceCreatedEvent.md

---

**End of Document**
