# ImportService

**Document Path:**
`spec/200_Application/ImportService.md`

**Document ID:** APP-044

**Version:** 1.0.0

**Status:** Draft

**Classification:** Normative

---

# 1. Purpose

This document defines the **ImportService** of the Voxarium Application Layer.

ImportService coordinates application workflows responsible for importing external resources into Voxarium projects. The service validates import requests, orchestrates import providers, registers imported resources, and ensures transactional consistency while remaining independent of file formats and storage technologies.

The service SHALL coordinate import workflows but SHALL NOT implement document parsing, media decoding, archive extraction, or storage mechanisms.

---

# 2. Scope

This specification defines:

* responsibilities;
* supported import operations;
* dependencies;
* import lifecycle;
* transactional behavior.

Document parsers, archive libraries, codecs, OCR engines, storage providers, and Infrastructure implementations are outside the scope of this specification.

---

# 3. Definition

ImportService is an Application Service responsible for coordinating import operations for Voxarium projects.

The service SHALL orchestrate import workflows using Domain objects, Repository contracts, and Infrastructure abstractions.

---

# 4. Responsibilities

ImportService SHALL be responsible for:

* validating import requests;
* coordinating import providers;
* creating imported resources;
* registering imported assets;
* detecting duplicate imports where applicable;
* tracking import progress;
* publishing resulting Domain Events.

The service SHALL NOT:

* parse imported files;
* decode media;
* perform OCR;
* access storage implementations directly;
* implement format-specific logic.

---

# 5. Dependencies

ImportService MAY depend upon:

* RepositoryContract;
* UnitOfWork;
* TransactionCoordinator;
* EventBus;
* ApplicationValidator;
* ApplicationMapper;
* OperationResult.

The service SHALL depend only upon import abstraction contracts.

---

# 6. Supported Operations

Typical operations include:

* ImportDocument;
* ImportAudio;
* ImportVoiceProfile;
* ImportProject;
* ImportDictionary;
* CancelImport;
* ValidateImport;
* GetImportStatus.

Additional operations MAY be introduced provided they remain consistent with Application Layer responsibilities.

---

# 7. Import Workflow

A typical import workflow SHOULD consist of:

1. validation of the import request;
2. preparation of import parameters;
3. selection of an appropriate import provider;
4. execution of the import operation;
5. validation of imported resources;
6. registration of imported objects;
7. publication of resulting Domain Events.

The workflow SHALL preserve project consistency throughout execution.

---

# 8. Transaction Management

Operations affecting Domain state SHALL execute within a transaction coordinated by TransactionCoordinator.

Long-running import operations MAY execute asynchronously.

Imported resources SHALL become visible only after successful transaction completion.

---

# 9. Validation

Before import begins, the service SHALL validate:

* project existence;
* supported resource type;
* import configuration;
* compatibility constraints;
* application invariants.

Validation failures SHALL prevent import execution.

---

# 10. Error Handling

Failures SHALL be represented using OperationResult or standardized Application exceptions.

Infrastructure-specific import failures SHALL be translated into Application-level failures before leaving the Application Layer.

Failed imports SHALL NOT leave partially registered resources.

---

# 11. Thread Safety

ImportService SHOULD remain stateless.

Concurrent import operations SHALL execute independently using isolated execution contexts.

Application consistency SHALL be preserved through transactional coordination.

---

# 12. Compliance

All import workflows within Voxarium SHALL be coordinated through ImportService or an equivalent Application Service conforming to this specification.

Implementations SHALL preserve deterministic orchestration, dependency inversion, architectural isolation, transactional consistency, and complete separation between Application workflow coordination and Infrastructure import technologies.

---

# 13. References

* ApplicationService.md
* ApplicationContext.md
* EventBus.md
* RepositoryContract.md
* UnitOfWork.md
* TransactionCoordinator.md
* ApplicationValidator.md
* ApplicationMapper.md
* OperationResult.md
* DocumentService.md
* FileStorageService.md
* ProjectService.md

---

**End of Document**
