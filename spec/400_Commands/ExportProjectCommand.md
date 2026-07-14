# Voxarium Software Architecture Specification

Document Path:

spec/400_Commands/ExportProjectCommand.md

Document ID: CMD-066

Title: ExportProjectCommand

Version: 1.0.0

Status: Accepted

Classification: Normative

Depends On

- Project
- Export_Service
- Storage_Service
- Command_Model
- Command_Bus

Referenced By

- Export_Service
- Workflow_Engine
- User_Interface_Architecture

---

# 1. Purpose

ExportProjectCommand requests export of a Project into an external representation.

The command SHALL produce a portable export package without modifying the Project.

---

# 2. Responsibility

Execution SHALL be performed by ExportProjectCommandHandler.

The handler SHALL create an Export Job and submit it to the Export Service.

---

# 3. Command Definition

## Name

ExportProjectCommand

## Category

Administration Commands

## Layer

Application

---

# 4. Parameters

## Required

### ProjectId

Type

Identifier

Identifier of the Project.

---

### Destination

Type

Path

Destination for exported artifacts.

---

## Optional

### ExportFormat

Type

Enumeration

Allowed values:

- Native
- JSON
- XML
- YAML
- ZIP

Default:

Native

---

### IncludeGeneratedAudio

Type

Boolean

Default:

true

---

### IncludePronunciationDictionaries

Type

Boolean

Default:

true

---

### IncludeMetadata

Type

Boolean

Default:

true

---

### IncludeStatistics

Type

Boolean

Default:

false

---

### Compression

Type

Enumeration

Allowed values:

- None
- Fast
- Normal
- Maximum

Default:

Normal

---

### Priority

Type

Enumeration

Allowed values:

- Low
- Normal
- High

Default:

Normal

---

# 5. Validation Rules

Execution SHALL fail if:

- Project does not exist;
- Destination is unavailable;
- Export Service is unavailable;
- Storage Service is unavailable;
- an equivalent Export Job is already active.

Validation SHALL complete before execution begins.

---

# 6. Execution Rules

Execution SHALL:

1. Load the Project Aggregate.
2. Build an Export Plan.
3. Create an Export Job.
4. Register the Job with the Export Service.
5. Publish lifecycle events.

Execution SHALL complete immediately.

Export SHALL execute asynchronously.

---

# 7. Export Rules

The export SHALL include:

- Project metadata;
- Documents;
- Fragments;
- Roles;
- Voice Profiles;
- Generation Presets;
- Pronunciation Dictionaries;
- Timeline;
- Project configuration.

Generated audio SHALL be exported only when requested.

Temporary resources SHALL NOT be exported.

The export SHALL represent a consistent Project snapshot.

The Project SHALL remain unchanged.

---

# 8. Result

Successful execution SHALL return:

ExportProjectResult

The result SHALL contain:

- JobId
- ProjectId
- ExportFormat
- ExportLocation
- ExportSize

---

# 9. Published Events

Successful execution SHALL publish:

- ProjectExportStarted
- JobQueued

Background execution SHALL additionally publish:

- ProjectExportCompleted

Upon failure:

- ProjectExportFailed

---

# 10. Error Conditions

Execution MAY fail with:

- ProjectNotFound
- DestinationUnavailable
- ExportServiceUnavailable
- StorageServiceUnavailable
- ExportAlreadyRunning
- ValidationFailed
- InternalError

---

# 11. Idempotency

Submitting an identical export request while an equivalent Export Job is active SHALL return the existing Job.

Duplicate Export Jobs SHALL NOT be created.

---

# 12. Transaction Requirements

The transaction SHALL include:

- Export Job creation;
- queue registration.

Export SHALL execute outside the transaction.

---

# 13. Authorization

The caller SHALL possess permission to export Projects.

---

# 14. Performance Requirements

Command execution SHOULD complete within 30 milliseconds.

The command SHALL NOT wait for export completion.

---

# 15. Thread Safety

Only one Export Job MAY exist for the same Project.

Different Projects MAY be exported concurrently.

---

# 16. AI Implementation Rules

AI-generated implementations SHALL:

- export only persisted Project state;
- never modify Project data;
- produce deterministic export packages;
- execute asynchronously;
- publish lifecycle events only after successful transaction completion.

---

# 17. Sequence

```text
GUI
 │
 ▼
ExportProjectCommand
 │
 ▼
CommandBus
 │
 ▼
ExportProjectCommandHandler
 │
 ▼
ExportService
 │
 ├── Build Export Plan
 │
 ├── Create Export Job
 │
 ├── Queue Job
 │
 ▼
JobQueued Event
 │
 ▼
Background Worker
 │
 ▼
Collect Project Data
 │
 ▼
Generate Export Package
 │
 ▼
ProjectExportCompleted
```

---

# 18. Compliance Checklist

The implementation conforms to this specification only if it:

- exports a consistent Project snapshot;
- never modifies Project data;
- excludes temporary resources;
- creates exactly one Export Job;
- executes asynchronously;
- publishes ProjectExportStarted after successful completion.

---

End of Document