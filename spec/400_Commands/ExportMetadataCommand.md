# Voxarium Software Architecture Specification

Document Path:
spec/400_Commands/ExportMetadataCommand.md

Document ID: CMD-044

Title: ExportMetadataCommand

Version: 1.0.0

Status: Accepted

Classification: Normative

Depends On

- Project
- Document
- Fragment
- Metadata
- Export_Service
- Command_Model
- Command_Bus

Referenced By

- Export_Service
- Project_Service
- Workflow_Engine
- User_Interface_Architecture

---

# 1. Purpose

ExportMetadataCommand requests exporting metadata describing a Project, Document or Fragment.

The command SHALL export metadata only.

The command SHALL NOT export generated audio or textual content unless explicitly represented as metadata.

---

# 2. Responsibility

Execution SHALL be performed by ExportMetadataCommandHandler.

The handler SHALL collect metadata and schedule an Export Job.

---

# 3. Command Definition

## Name

ExportMetadataCommand

## Category

Export Commands

## Layer

Application

---

# 4. Parameters

## Required

### Scope

Type

Enumeration

Allowed values:

- Fragment
- Document
- Project

---

### TargetId

Type

Identifier

Identifier corresponding to the selected Scope.

---

### OutputPath

Type

Path

Destination path for exported metadata.

---

## Optional

### MetadataFormat

Type

Enumeration

Allowed values:

- JSON
- XML
- YAML

Default:

JSON

---

### IncludeStatistics

Type

Boolean

Default:

true

---

### IncludeGenerationConfiguration

Type

Boolean

Default:

true

---

### IncludeCustomProperties

Type

Boolean

Default:

true

---

### IncludeRuntimeState

Type

Boolean

Default:

false

---

### OverwriteExisting

Type

Boolean

Default:

false

---

# 5. Validation Rules

Execution SHALL fail if:

- target object does not exist;
- OutputPath is invalid;
- destination already exists and overwrite is disabled;
- Export Service is unavailable.

Validation SHALL complete before execution begins.

---

# 6. Execution Rules

Execution SHALL:

1. Load the target Aggregate.
2. Collect exportable metadata.
3. Apply export filters.
4. Serialize metadata.
5. Create an Export Job.
6. Register the Job with the Export Service.
7. Publish lifecycle events.

Execution SHALL complete immediately.

Metadata export SHALL execute asynchronously.

---

# 7. Export Rules

The exported metadata MAY include:

- identifiers;
- names;
- hierarchy;
- ordering;
- Roles;
- Voice Profiles;
- Emotions;
- Generation Presets;
- Pronunciation Dictionaries;
- statistics;
- timestamps;
- user-defined properties.

Runtime-only state SHALL NOT be exported unless IncludeRuntimeState is enabled.

The export SHALL preserve the hierarchy of the selected Scope.

The command SHALL NOT modify Project data.

---

# 8. Result

Successful execution SHALL return:

ExportMetadataResult

The result SHALL contain:

- JobId
- Scope
- TargetId
- MetadataFormat
- OutputPath

---

# 9. Published Events

Successful execution SHALL publish:

- MetadataExportStarted
- JobQueued

Background execution SHALL additionally publish:

- MetadataExportCompleted

Upon failure:

- MetadataExportFailed

---

# 10. Error Conditions

Execution MAY fail with:

- TargetNotFound
- InvalidOutputPath
- ExportServiceUnavailable
- SerializationFailed
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

Metadata serialization and file writing SHALL execute outside the transaction.

---

# 13. Authorization

The caller SHALL possess permission to export the selected object.

---

# 14. Performance Requirements

Command execution SHOULD complete within 50 milliseconds.

The command SHALL NOT wait for metadata export completion.

---

# 15. Thread Safety

Concurrent metadata exports targeting different destinations MAY execute simultaneously.

Concurrent exports targeting the same destination SHALL be serialized.

---

# 16. AI Implementation Rules

AI-generated implementations SHALL:

- export metadata only;
- preserve hierarchy and object relationships;
- avoid exporting runtime state unless explicitly requested;
- execute asynchronously;
- publish lifecycle events only after successful transaction completion.

---

# 17. Sequence

```text
GUI
 │
 ▼
ExportMetadataCommand
 │
 ▼
CommandBus
 │
 ▼
ExportMetadataCommandHandler
 │
 ▼
ExportService
 │
 ├── Collect Metadata
 │
 ├── Serialize
 │
 ├── Create Export Job
 │
 ├── Queue Export
 │
 ▼
JobQueued Event
 │
 ▼
Background Worker
 │
 ▼
Write Metadata File
 │
 ▼
MetadataExportCompleted
```

---

# 18. Compliance Checklist

The implementation conforms to this specification only if it:

- exports only metadata;
- preserves hierarchy and relationships;
- creates exactly one Export Job;
- executes asynchronously;
- does not modify Project data;
- publishes MetadataExportStarted after successful completion.

---

End of Document