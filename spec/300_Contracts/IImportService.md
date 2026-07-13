# Voxarium Software Architecture Specification

Document Path:
spec/300_Contracts/IImportService.md

Document ID: CTR-007

Title: IImportService

Version: 1.0.0

Status: Accepted

Classification: Normative

Depends On

- CTR-000 IService
- Project
- Source
- Document
- ImportProfile
- Job

Referenced By

- Import_Service
- Workflow_Engine
- User_Interface_Architecture

---

# 1. Purpose

IImportService defines the public contract for importing external data into Voxarium.

The contract provides a unified interface for all supported import formats while remaining independent of specific parser implementations.

Import operations SHALL preserve Domain Model consistency.

---

# 2. Responsibilities

The contract SHALL provide operations for:

- importing projects;
- importing source files;
- importing documents;
- importing metadata;
- validating imported data;
- previewing import results.

---

# 3. Non-Responsibilities

The contract SHALL NOT:

- generate speech;
- export data;
- modify Timeline directly;
- execute Workflow;
- access GUI components.

---

# 4. Lifecycle Operations

## 4.1 ImportProject

### Signature

ImportProject(SourceUri, ImportProfileId)

### Purpose

Imports an external project.

### Parameters

- SourceUri
- ImportProfileId

### Returns

- Job

### Preconditions

- Source exists.
- ImportProfile exists.

### Postconditions

- Import Job created.

### Published Events

- ImportRequested

### Exceptions

- SourceNotFound
- UnsupportedFormat
- InvalidImportProfile

---

## 4.2 ImportDocument

### Signature

ImportDocument(SourceUri, TargetProjectId)

### Purpose

Imports a document into an existing project.

### Returns

- Job

### Published Events

- ImportRequested

---

## 4.3 ImportSource

### Signature

ImportSource(SourceUri)

### Purpose

Imports a Source object.

### Returns

- Job

---

## 4.4 CancelImport

### Signature

CancelImport(JobId)

### Purpose

Cancels an active import operation.

### Published Events

- ImportCancellationRequested

---

# 5. Validation Operations

The contract SHALL provide:

- ValidateImportSource
- ValidateImportProfile
- PreviewImport

Validation SHALL NOT modify the Project.

Preview SHALL return an immutable description of the expected import result.

---

# 6. Query Operations

The contract SHALL provide:

- GetImportJob
- GetImportStatus
- GetImportProgress
- GetImportResult
- ListImportJobs

Queries SHALL NOT modify system state.

---

# 7. Import Profiles

Every import SHALL use exactly one ImportProfile.

ImportProfile determines:

- parser configuration;
- text normalization rules;
- encoding policy;
- conflict resolution policy;
- duplicate handling policy;
- metadata import policy.

---

# 8. Result Model

Successful import SHALL produce:

- created Project, or
- modified Project,
- diagnostics,
- warnings,
- imported object statistics.

---

# 9. Transaction Rules

Creation of an Import Job SHALL be atomic.

Modification of Domain Model SHALL occur only after successful validation.

Partial import SHALL NOT leave the Domain Model in an inconsistent state.

---

# 10. Thread Safety

Multiple independent imports MAY execute concurrently.

Import into the same Project SHALL be serialized.

---

# 11. Dependencies

The contract SHALL depend only on:

- Domain Model;
- IService.

The contract SHALL NOT depend on:

- GUI;
- parser implementations;
- Infrastructure.

---

# 12. AI Implementation Rules

Implementations SHALL:

- validate input before modifying Domain Model;
- isolate parser implementations behind plugin interfaces;
- support asynchronous execution;
- publish lifecycle events.

---

# 13. Test Requirements

Tests SHALL verify:

- successful project import;
- successful document import;
- invalid format handling;
- preview generation;
- cancellation;
- concurrent imports.

---

# 14. Compliance Checklist

The contract conforms to this specification only if it:

- supports asynchronous execution;
- validates imported data;
- supports preview mode;
- isolates parser implementations;
- preserves Domain consistency;
- conforms to IService.

---

End of Document