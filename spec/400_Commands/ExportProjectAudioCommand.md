# Voxarium Software Architecture Specification

Document Path:
spec/400_Commands/ExportProjectAudioCommand.md

Document ID: CMD-041

Title: ExportProjectAudioCommand

Version: 1.0.0

Status: Accepted

Classification: Normative

Depends On

- Project
- Document
- Fragment
- SpeechSegment
- Export_Service
- Command_Model
- Command_Bus

Referenced By

- Export_Service
- Workflow_Engine
- Project_Service
- User_Interface_Architecture

---

# 1. Purpose

ExportProjectAudioCommand requests exporting generated speech for an entire Project.

The command SHALL export existing generated speech.

The command SHALL NOT initiate speech generation.

---

# 2. Responsibility

Execution SHALL be performed by ExportProjectAudioCommandHandler.

The handler SHALL create an Export Job for all eligible Documents within the Project.

---

# 3. Command Definition

## Name

ExportProjectAudioCommand

## Category

Export Commands

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

### OutputPath

Type

Path

Destination directory for exported content.

---

## Optional

### ExportMode

Type

Enumeration

Allowed values:

- SingleArchive
- SeparateDocuments
- SeparateFragments

Default:

SeparateDocuments

---

### AudioFormat

Type

Enumeration

Allowed values:

- WAV
- FLAC
- MP3
- OGG

Default:

WAV

---

### IncludeMetadata

Type

Boolean

Default:

true

Determines whether metadata files SHALL accompany exported audio.

---

### OverwriteExisting

Type

Boolean

Default:

false

---

# 5. Validation Rules

Execution SHALL fail if:

- Project does not exist;
- Project contains no generated speech;
- OutputPath is invalid;
- destination already exists and overwrite is disabled;
- Export Service is unavailable.

Validation SHALL complete before execution begins.

---

# 6. Execution Rules

Execution SHALL:

1. Load the Project Aggregate.
2. Identify eligible Documents.
3. Build an Export Plan.
4. Create an Export Job.
5. Register the Job with the Export Service.
6. Publish lifecycle events.

Execution SHALL complete immediately.

Export SHALL execute asynchronously.

---

# 7. Export Rules

When ExportMode is SingleArchive:

- one archive SHALL contain all exported audio.

When ExportMode is SeparateDocuments:

- one directory SHALL be created for each Document.

When ExportMode is SeparateFragments:

- audio SHALL be exported individually for every Fragment.

Document ordering SHALL be preserved.

Fragment ordering within every Document SHALL be preserved.

The command SHALL NOT modify Project data.

---

# 8. Result

Successful execution SHALL return:

ExportProjectAudioResult

The result SHALL contain:

- JobId
- ProjectId
- OutputPath
- ExportMode
- ExportedDocuments

---

# 9. Published Events

Successful execution SHALL publish:

- ProjectExportStarted
- JobQueued

Background execution SHALL additionally publish:

- DocumentExportStarted
- DocumentExportCompleted
- ProjectExportCompleted

Upon failure:

- ProjectExportFailed

---

# 10. Error Conditions

Execution MAY fail with:

- ProjectNotFound
- GeneratedSpeechNotFound
- InvalidOutputPath
- ExportServiceUnavailable
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

Physical file creation SHALL execute outside the transaction.

---

# 13. Authorization

The caller SHALL possess permission to export the Project.

---

# 14. Performance Requirements

Command execution SHOULD complete within 100 milliseconds.

The command SHALL NOT wait for archive or file creation.

---

# 15. Thread Safety

Concurrent export operations targeting different Projects MAY execute simultaneously.

Concurrent exports targeting the same destination SHALL be serialized.

---

# 16. AI Implementation Rules

AI-generated implementations SHALL:

- export only previously generated speech;
- preserve Document and Fragment ordering;
- never initiate speech generation;
- execute export asynchronously;
- avoid overwriting existing files unless explicitly requested;
- publish lifecycle events only after successful transaction completion.

---

# 17. Sequence

```text
GUI
 │
 ▼
ExportProjectAudioCommand
 │
 ▼
CommandBus
 │
 ▼
ExportProjectAudioCommandHandler
 │
 ▼
ExportService
 │
 ├── Build Export Plan
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
Export Project Audio
 │
 ▼
ProjectExportCompleted
```

---

# 18. Compliance Checklist

The implementation conforms to this specification only if it:

- exports only existing generated speech;
- preserves Project, Document and Fragment ordering;
- creates exactly one Export Job;
- executes asynchronously;
- never performs speech generation;
- publishes ProjectExportStarted after successful completion.

---

End of Document