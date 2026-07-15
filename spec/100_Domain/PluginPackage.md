# PluginPackage

**Document Path:**
`spec/100_Domain/PluginPackage.md`

**Document ID:** DOM-033

**Version:** 1.0.0

**Status:** Draft

**Classification:** Normative

---

# 1. Purpose

This document defines the **PluginPackage** Aggregate Root of the Voxarium platform.

A PluginPackage represents a distributable Plugin artifact together with all business information required for installation, validation, lifecycle management, and compatibility verification.

PluginPackage is the Aggregate Root responsible for the integrity of Plugin-related metadata.

---

# 2. Scope

This specification defines:

* responsibilities;
* ownership;
* aggregate boundaries;
* lifecycle;
* relationships;
* business invariants.

Archive formats, compression algorithms, package installation, and runtime loading are outside the scope of this specification.

---

# 3. Definition

A **PluginPackage** is the Aggregate Root representing a distributable Plugin package.

It defines the consistency boundary for all Plugin package metadata.

---

# 4. Responsibilities

PluginPackage SHALL be responsible for:

* representing a distributable Plugin;
* maintaining package integrity;
* coordinating package metadata;
* exposing package information;
* supporting installation workflows.

PluginPackage SHALL NOT:

* execute Plugin code;
* load assemblies;
* resolve dependencies;
* manage runtime execution.

---

# 5. Identity

Every PluginPackage SHALL possess a globally unique identifier.

Its identity SHALL remain stable regardless of:

* metadata updates;
* package relocation;
* installation state.

Package identity SHALL remain immutable.

---

# 6. Ownership

A PluginPackage SHALL own:

* one PluginManifest.

A PluginPackage MAY additionally own package-specific metadata defined by future specifications.

Owned entities SHALL NOT exist independently.

---

# 7. Aggregate Boundary

PluginPackage SHALL be the Aggregate Root.

All modifications to PluginManifest SHALL occur through the PluginPackage Aggregate.

External components SHALL NOT modify aggregate members directly.

---

# 8. Package Information

A PluginPackage MAY define:

* package identifier;
* package version;
* package format version;
* package size;
* checksum;
* digital signature reference;
* publication metadata.

These attributes describe the package itself rather than the Plugin runtime.

---

# 9. Relationships

PluginPackage MAY reference:

* PluginManifest;
* PluginRepository;
* PluginInstallation;
* Project.

PluginPackage SHALL NOT own runtime Plugin instances.

---

# 10. Metadata

PluginPackage SHOULD expose:

* identifier;
* creation timestamp;
* publication timestamp;
* version;
* package format version;
* integrity information.

Metadata SHALL NOT modify package identity.

---

# 11. Lifecycle

The lifecycle SHALL consist of:

1. package creation;
2. validation;
3. publication;
4. installation;
5. update;
6. removal.

Published packages SHALL remain immutable.

---

# 12. Business Rules

The following rules SHALL apply:

* every PluginPackage SHALL contain exactly one PluginManifest;
* package identity SHALL remain immutable;
* package integrity SHALL be verifiable;
* published packages SHALL NOT be modified.

---

# 13. Validation

Validation SHALL verify:

* unique package identifier;
* existing PluginManifest;
* valid version information;
* package integrity;
* internal consistency.

Validation failures SHALL be reported through the Validation subsystem.

---

# 14. Persistence

Persistence SHALL be performed through Repository abstractions.

PluginPackage SHALL remain independent of:

* archive formats;
* storage implementation;
* package distribution mechanisms.

---

# 15. Events

Business operations MAY produce events including:

* PluginPackageCreatedEvent;
* PluginPackageValidatedEvent;
* PluginPackagePublishedEvent;
* PluginPackageRemovedEvent.

Event publication SHALL occur outside the Aggregate.

---

# 16. Compliance

All distributable Plugin packages within Voxarium SHALL conform to this specification.

Implementations SHALL preserve aggregate integrity, immutable package identity, ownership boundaries, and business invariants defined by this document.

---

# 17. References

* PluginManifest.md
* Project.md
* ValidationIssue.md
* CreatePluginPackageCommand.md
* PublishPluginPackageCommand.md
* PluginPackageCreatedEvent.md

---

**End of Document**
