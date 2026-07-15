# PluginManifest

**Document Path:**
`spec/100_Domain/PluginManifest.md`

**Document ID:** DOM-032

**Version:** 1.0.0

**Status:** Draft

**Classification:** Normative

---

# 1. Purpose

This document defines the **PluginManifest** domain entity of the Voxarium platform.

A PluginManifest represents the business description of a Plugin package. It provides immutable identification, compatibility information, capabilities, dependencies, and metadata required for plugin discovery and lifecycle management.

The PluginManifest describes **what a Plugin is**, not **how it is executed**.

---

# 2. Scope

This specification defines:

* responsibilities;
* ownership;
* lifecycle;
* relationships;
* business invariants.

Plugin loading, dependency resolution algorithms, sandbox execution, and package formats are outside the scope of this specification.

---

# 3. Definition

A **PluginManifest** is a domain entity representing the declarative metadata of a Plugin.

It serves as the authoritative source of Plugin identity and compatibility.

---

# 4. Responsibilities

PluginManifest SHALL be responsible for:

* identifying a Plugin;
* describing Plugin metadata;
* declaring Plugin capabilities;
* declaring compatibility requirements;
* declaring Plugin dependencies.

PluginManifest SHALL NOT:

* execute Plugin code;
* manage Plugin lifecycle;
* load assemblies;
* perform dependency resolution.

---

# 5. Identity

Every PluginManifest SHALL possess a globally unique identifier.

Its identity SHALL remain stable regardless of:

* display name changes;
* description updates;
* metadata modifications.

The Plugin identifier SHALL remain immutable.

---

# 6. Ownership

Every PluginManifest SHALL belong to exactly one Plugin package.

A Plugin package SHALL contain exactly one PluginManifest.

---

# 7. Manifest Information

A PluginManifest MAY define:

* plugin identifier;
* display name;
* description;
* author;
* publisher;
* version;
* license;
* homepage;
* repository;
* documentation reference.

The manifest SHALL remain independent of runtime implementation.

---

# 8. Compatibility

A PluginManifest MAY declare:

* minimum Voxarium version;
* maximum supported version;
* supported operating systems;
* supported architectures;
* required runtime capabilities;
* optional capabilities.

Compatibility declarations SHALL be evaluated by the Application layer.

---

# 9. Dependencies

A PluginManifest MAY declare:

* required Plugins;
* optional Plugins;
* minimum dependency versions;
* compatible dependency ranges.

Dependency resolution SHALL occur outside the Domain layer.

---

# 10. Relationships

PluginManifest MAY reference:

* PluginPackage;
* PluginCapability;
* PluginDependency;
* PluginPermission.

PluginManifest SHALL NOT own runtime objects.

---

# 11. Metadata

PluginManifest SHOULD expose:

* identifier;
* version;
* publication date;
* manifest schema version;
* digital signature reference where applicable.

Metadata SHALL NOT alter Plugin identity.

---

# 12. Lifecycle

The lifecycle SHALL consist of:

1. creation;
2. packaging;
3. validation;
4. installation;
5. update;
6. removal.

Manifest information SHALL remain immutable for a published Plugin version.

---

# 13. Business Rules

The following rules SHALL apply:

* every Plugin package SHALL contain exactly one PluginManifest;
* Plugin identifiers SHALL be globally unique;
* version identifiers SHALL comply with Project versioning policy;
* declared dependencies SHALL reference valid Plugin identifiers;
* compatibility information SHALL remain internally consistent.

---

# 14. Validation

Validation SHALL verify:

* unique Plugin identifier;
* valid version information;
* valid dependency declarations;
* internally consistent compatibility information;
* required manifest fields.

Validation failures SHALL be reported through the Validation subsystem.

---

# 15. Persistence

Persistence SHALL be performed through Repository abstractions.

PluginManifest SHALL remain independent of:

* package formats;
* storage implementation;
* runtime Plugin loader.

---

# 16. Events

Business operations MAY produce events including:

* PluginManifestCreatedEvent;
* PluginManifestValidatedEvent;
* PluginManifestUpdatedEvent.

The PluginManifest entity SHALL NOT publish events directly.

---

# 17. Compliance

All Plugin manifests within Voxarium SHALL conform to this specification.

Implementations SHALL preserve stable identity, declarative behavior, compatibility integrity, and business invariants defined by this document.

---

# 18. References

* PluginPackage.md
* PluginCapability.md
* PluginDependency.md
* PluginPermission.md
* Project.md
* ValidationIssue.md
* RegisterPluginCommand.md
* PluginManifestCreatedEvent.md

---

**End of Document**
