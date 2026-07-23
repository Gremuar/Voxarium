# ProjectService

**Document Path:**
`spec/200_Application/ProjectService.md`

**Document ID:** APP-061

**Version:** 1.0.0

**Status:** Draft

**Classification:** Normative

---

# 1. Purpose

This document defines the **ProjectService** of the Voxarium Application Layer.

ProjectService coordinates the complete lifecycle of Voxarium projects. The service provides a unified Application interface for creating, opening, modifying, validating, saving, closing, and deleting projects while remaining independent of storage formats and Infrastructure implementations.

The service SHALL coordinate project management workflows but SHALL NOT implement project persistence, serialization, or file system operations.

---

# 2. Scope

This specification defines:

* responsibilities;
* supported project operations;
* project lifecycle;
* dependencies;
* transactional behavior.

Project file formats, storage providers, databases, synchronization mechanisms, and Infrastructure implementations are outside the scope of this specification.

---

# 3. Definition

ProjectService is an Application Service responsible for coordinating all operations related to Voxarium projects.

A Project SHALL be considered the primary aggregate managed by the Application Layer.

---

# 4. Responsibilities

ProjectService SHALL be responsible for:

* creating projects;
* opening existing projects;
* saving projects;
* closing projects;
* validating project integrity;
* deleting projects;
* coordinating project metadata updates;
* publishing project-related Domain Events.

The service SHALL NOT:

* manipulate project files directly;
* serialize project data;
* access storage implementations;
* implement backup mechanisms.

---

# 5. Dependencies

ProjectService MAY depend upon:

* RepositoryContract;
* UnitOfWork;
* TransactionCoordinator;
* EventBus;
* ApplicationValidator;
* ApplicationMapper;
* OperationResult;
* MetadataService.

The service SHALL depend only upon Application abstractions.

---

# 6. Supported Operations

Typical operations include:

* CreateProject;
* OpenProject;
* SaveProject;
* SaveProjectAs;
* CloseProject;
* DeleteProject;
* RenameProject;
* ValidateProject;
* GetProject;
* GetCurrentProject;
* ListProjects.

Additional operations MAY be introduced provided they remain consistent with this specification.

---

# 7. Project Lifecycle

A project SHOULD follow the lifecycle:

1. creation;
2. initialization;
3. opening;
4. modification;
5. validation;
6. saving;
7. closing;
8. reopening or deletion.

The lifecycle SHALL preserve project consistency at every stage.

---

# 8. Transaction Management

Operations modifying project state SHALL execute within a transaction coordinated by TransactionCoordinator.

Projects SHALL become visible to other Application components only after successful transaction completion.

Rollback SHALL restore the previous project state.

---

# 9. Validation

Before modifying project state, the service SHALL validate:

* project identifier;
* project integrity;
* required metadata;
* referenced resources;
* application constraints.

Validation failures SHALL prevent the requested operation.

---

# 10. Error Handling

Failures SHALL be represented using OperationResult or standardized Application exceptions.

Infrastructure-specific failures SHALL be translated into Application-level failures before leaving the Application Layer.

Project failures SHALL NOT leave partially committed project state.

---

# 11. Thread Safety

ProjectService SHOULD remain stateless.

Concurrent project operations SHALL execute using isolated execution contexts.

Conflicting operations targeting the same project SHALL be serialized or rejected according to Application policy.

---

# 12. Compliance

All project management workflows within Voxarium SHALL be coordinated through ProjectService or an equivalent Application Service conforming to this specification.

Implementations SHALL preserve deterministic project behavior, dependency inversion, architectural isolation, transactional consistency, project integrity, and complete separation between Application coordination and Infrastructure storage technologies.

---

# 13. References

* ApplicationService.md
* ApplicationContext.md
* RepositoryContract.md
* UnitOfWork.md
* TransactionCoordinator.md
* EventBus.md
* ApplicationValidator.md
* ApplicationMapper.md
* OperationResult.md
* MetadataService.md
* HistoryService.md

---

**End of Document**
