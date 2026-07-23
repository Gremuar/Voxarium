# RecentFilesService

**Document Path:**
`spec/200_Application/RecentFilesService.md`

**Document ID:** APP-064

**Version:** 1.0.0

**Status:** Draft

**Classification:** Normative

---

# 1. Purpose

This document defines the **RecentFilesService** of the Voxarium Application Layer.

RecentFilesService coordinates the management of the list of recently opened projects and documents. The service maintains a consistent, validated, and ordered history of recently accessed resources while remaining independent of storage mechanisms, user interface implementations, and Infrastructure technologies.

The service SHALL coordinate recent-file management workflows but SHALL NOT implement persistence, operating system integration, or user interface presentation.

---

# 2. Scope

This specification defines:

* responsibilities;
* supported operations;
* lifecycle of recent entries;
* dependencies;
* transactional behavior.

Configuration files, databases, operating system recent-document APIs, and Infrastructure implementations are outside the scope of this specification.

---

# 3. Definition

RecentFilesService is an Application Service responsible for maintaining the collection of recently accessed resources.

The service SHALL expose a deterministic and validated view of recently opened resources for use by the Application.

---

# 4. Responsibilities

RecentFilesService SHALL be responsible for:

* registering recently opened resources;
* updating access order;
* removing obsolete entries;
* validating resource references;
* limiting history size according to Application policy;
* clearing recent history;
* publishing recent-file related Domain Events where applicable.

The service SHALL NOT:

* open files;
* validate file contents;
* access file systems directly;
* display recent items in the user interface.

---

# 5. Dependencies

RecentFilesService MAY depend upon:

* RepositoryContract;
* UnitOfWork;
* TransactionCoordinator;
* EventBus;
* ApplicationValidator;
* ApplicationMapper;
* OperationResult.

The service SHALL depend only upon Application abstractions.

---

# 6. Supported Operations

Typical operations include:

* RegisterRecentFile;
* RemoveRecentFile;
* UpdateRecentFile;
* GetRecentFiles;
* ClearRecentFiles;
* ValidateRecentEntries;
* SetMaximumHistorySize;
* TrimHistory.

Additional operations MAY be introduced provided they remain consistent with this specification.

---

# 7. Recent File Lifecycle

A recent file entry SHOULD follow this lifecycle:

1. registration after successful resource access;
2. validation;
3. insertion or update within the recent list;
4. ordering by most recent access;
5. automatic removal when exceeding retention limits;
6. removal upon explicit user request.

Duplicate entries SHALL be consolidated into a single record.

---

# 8. Ordering Rules

Recent entries SHALL be ordered according to the latest successful access time.

Whenever an existing resource is reopened:

* the existing entry SHALL be updated;
* duplicate entries SHALL NOT be created;
* the updated entry SHALL become the first item in the list.

Ordering SHALL remain deterministic.

---

# 9. Transaction Management

Operations modifying recent history SHALL execute within a transaction coordinated by TransactionCoordinator.

History updates SHALL become visible only after successful transaction completion.

Rollback SHALL restore the previous history state.

---

# 10. Validation

Before accepting a recent entry, the service SHALL validate:

* resource identifier;
* supported resource type;
* required metadata;
* application constraints.

Invalid or inaccessible resources MAY be removed during validation according to Application policy.

---

# 11. Error Handling

Failures SHALL be represented using OperationResult or standardized Application exceptions.

Infrastructure-specific failures SHALL be translated into Application-level failures before leaving the Application Layer.

Recent history failures SHALL NOT affect the successful completion of unrelated Application workflows.

---

# 12. Thread Safety

RecentFilesService SHOULD remain stateless.

Concurrent history operations SHALL execute using isolated execution contexts.

Conflicting updates SHALL be serialized or rejected according to Application policy.

---

# 13. Compliance

All recent resource history within Voxarium SHALL be coordinated through RecentFilesService or an equivalent Application Service conforming to this specification.

Implementations SHALL preserve deterministic history ordering, dependency inversion, architectural isolation, transactional consistency, history integrity, and complete separation between Application coordination and Infrastructure storage technologies.

---

# 14. References

* ApplicationService.md
* ProjectService.md
* RepositoryContract.md
* UnitOfWork.md
* TransactionCoordinator.md
* EventBus.md
* ApplicationValidator.md
* ApplicationMapper.md
* OperationResult.md

---

**End of Document**
