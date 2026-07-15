# Project

**Document Path:**
`spec/100_Domain/Project.md`

**Document ID:** DOM-034

**Version:** 1.0.0

**Status:** Draft

**Classification:** Normative

---

# 1. Purpose

This document defines the **Project** Aggregate Root of the Voxarium platform.

A Project is the top-level business entity representing an isolated workspace. It defines the ownership boundary for all user-created resources and provides the primary consistency boundary of the entire domain model.

Every business object within Voxarium ultimately belongs to exactly one Project unless explicitly defined as a global reference entity.

---

# 2. Scope

This specification defines:

* responsibilities;
* ownership;
* aggregate boundaries;
* lifecycle;
* relationships;
* business invariants.

User interface behavior, storage implementation, synchronization protocols, and deployment concerns are outside the scope of this specification.

---

# 3. Definition

A **Project** is the root business entity representing an independent Voxarium workspace.

A Project defines the highest ownership boundary for domain resources.

---

# 4. Responsibilities

Project SHALL be responsible for:

* owning Project resources;
* maintaining Project identity;
* coordinating Project metadata;
* preserving ownership integrity;
* defining the scope of business operations.

Project SHALL NOT:

* execute speech generation;
* perform import/export directly;
* implement persistence;
* execute plugin code.

---

# 5. Identity

Every Project SHALL possess a globally unique identifier.

Its identity SHALL remain stable regardless of:

* name changes;
* metadata modifications;
* content changes;
* structural changes.

---

# 6. Ownership

Project SHALL own all Project-scoped entities including, but not limited to:

* Documents;
* Folders;
* Collections;
* Dictionaries;
* Lexicons;
* Characters;
* Speakers;
* VoiceProfiles;
* GenerationPresets;
* AudioGenerationPresets;
* EmotionPresets;
* AudioAssets;
* Timelines;
* ExportJobs;
* ImportJobs;
* GenerationHistory;
* Notes;
* Bookmarks;
* Markers;
* PluginPackages.

Entities SHALL NOT belong to multiple Projects simultaneously.

---

# 7. Aggregate Boundary

Project is the highest Aggregate Root within the Domain model.

Lower-level Aggregates SHALL remain internally independent while preserving Project ownership.

Project SHALL coordinate ownership but SHALL NOT directly manage internal consistency of subordinate Aggregates.

---

# 8. Relationships

Project MAY reference global reference entities including:

* Language;
* Voice;
* PluginRepository;
* SystemConfiguration.

Project SHALL own Project-specific entities rather than merely reference them.

---

# 9. Metadata

Project SHOULD expose:

* identifier;
* name;
* description;
* version;
* creation timestamp;
* modification timestamp;
* author where applicable.

Metadata SHALL NOT affect Project identity.

---

# 10. Lifecycle

The lifecycle SHALL consist of:

1. creation;
2. initialization;
3. normal operation;
4. archival;
5. deletion.

Deleting a Project SHALL delete all owned Project-scoped entities according to application retention policy.

---

# 11. Business Rules

The following rules SHALL apply:

* every Project SHALL possess exactly one unique identifier;
* every Project-scoped entity SHALL belong to exactly one Project;
* Project ownership SHALL remain immutable;
* cross-project references SHALL be explicitly defined by dedicated specifications;
* ownership cycles SHALL NOT exist.

---

# 12. Validation

Validation SHALL verify:

* unique identifier;
* internal ownership consistency;
* valid aggregate references;
* metadata consistency;
* absence of orphan Project entities.

Validation failures SHALL be reported through the Validation subsystem.

---

# 13. Persistence

Persistence SHALL be performed through the Project Repository.

Project SHALL remain independent of:

* storage technology;
* serialization format;
* synchronization mechanisms.

---

# 14. Events

Business operations MAY produce events including:

* ProjectCreatedEvent;
* ProjectOpenedEvent;
* ProjectUpdatedEvent;
* ProjectClosedEvent;
* ProjectDeletedEvent.

The Project entity SHALL NOT publish events directly.

---

# 15. Compliance

Every Voxarium workspace SHALL conform to this specification.

Implementations SHALL preserve ownership boundaries, aggregate independence, stable identity, and business invariants defined by this document.

---

# 16. References

* Document.md
* Folder.md
* Collection.md
* Dictionary.md
* Lexicon.md
* Character.md
* Speaker.md
* VoiceProfile.md
* AudioGenerationPreset.md
* GenerationPreset.md
* EmotionPreset.md
* AudioAsset.md
* Timeline.md
* ExportJob.md
* ImportJob.md
* GenerationHistory.md
* ValidationIssue.md
* CreateProjectCommand.md
* ProjectCreatedEvent.md

---

**End of Document**
