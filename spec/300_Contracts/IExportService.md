# Voxarium Software Architecture Specification

Document Path:
spec/300_Contracts/IExportService.md

Document ID: CTR-006

Title: IExportService

Version: 1.0.0

Status: Accepted

Classification: Normative

Depends On

- CTR-000 IService
- Project
- Production
- ExportProfile
- Job

Referenced By

- Export_Service
- Workflow_Engine
- Job_Orchestrator
- User_Interface_Architecture

---

# 1. Purpose

IExportService defines the public contract for exporting application data into external representations.

The contract provides a unified API for all export operations regardless of the target format.

The contract SHALL NOT expose implementation details of export providers.

---

# 2. Responsibilities

The contract SHALL provide operations for:

- exporting Project;
- exporting Production;
- exporting generated audio;
- exporting metadata;
- exporting reports;
- monitoring export progress.

---

# 3. Non-Responsibilities

The contract SHALL NOT:

- generate speech;
- modify Project;
- modify Production;
- perform audio synthesis;
- manage storage backends.

---

# 4. Lifecycle Operations

## 4.1 ExportProject

### Signature

ExportProject(ProjectId, ExportProfileId)

### Purpose

Exports the complete project.

### Parameters

- ProjectId
- ExportProfileId

### Returns

- Job

### Preconditions

- Project exists.
- ExportProfile exists.

### Postconditions

- Export Job created.

### Published Events

- ExportRequested

### Exceptions

- ProjectNotFound
- ExportProfileNotFound

---

## 4.2 ExportProduction

### Signature

ExportProduction(ProductionId, ExportProfileId)

### Purpose

Exports a Production.

### Returns

- Job

### Published Events

- ExportRequested

---

## 4.3 ExportAudio

### Signature

ExportAudio(AudioTrackIds, ExportProfileId)

### Purpose

Exports one or more AudioTrack objects.

### Returns

- Job

---

## 4.4 CancelExport

### Signature

CancelExport(JobId)

### Purpose

Cancels an active export operation.

### Published Events

- ExportCancellationRequested

---

# 5. Query Operations

The contract SHALL provide:

- GetExportJob
- GetExportStatus
- GetExportProgress
- GetExportResult
- ListExportJobs

Queries SHALL NOT modify system state.

---

# 6. Export Profiles

Every export operation SHALL use exactly one ExportProfile.

The ExportProfile determines:

- output format;
- codec;
- sample rate;
- channel configuration;
- metadata policy;
- file naming policy;
- output directory policy.

---

# 7. Result Model

Successful export SHALL produce an Export Result containing:

- Job identifier;
- exported artifacts;
- export duration;
- diagnostic information.

---

# 8. Transaction Rules

Creating an export job SHALL be atomic.

Actual export execution MAY occur asynchronously.

---

# 9. Thread Safety

Multiple independent export jobs MAY execute concurrently.

---

# 10. Dependencies

The contract SHALL depend only on:

- Domain Model;
- IService.

The contract SHALL NOT depend on:

- GUI;
- Infrastructure;
- Export libraries.

---

# 11. AI Implementation Rules

Implementations SHALL:

- create a Job for every export operation;
- separate job creation from execution;
- support cancellation;
- publish lifecycle events.

---

# 12. Test Requirements

Tests SHALL verify:

- project export;
- production export;
- cancellation;
- invalid export profile;
- concurrent exports;
- progress reporting.

---

# 13. Compliance Checklist

The contract conforms to this specification only if it:

- provides asynchronous export;
- supports ExportProfile;
- exposes progress reporting;
- supports cancellation;
- is independent of export implementation;
- conforms to IService.

---

End of Document