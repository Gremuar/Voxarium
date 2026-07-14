# Voxarium Software Architecture Specification

Document Path:
spec/400_Commands/ExportSubtitleCommand.md

Document ID: CMD-042

Title: ExportSubtitleCommand

Version: 1.0.0

Status: Accepted

Classification: Normative

Depends On

- Project
- Document
- Fragment
- SpeechSegment
- Timeline
- Export_Service
- Command_Model
- Command_Bus

Referenced By

- Export_Service
- Timeline_Service
- Workflow_Engine
- User_Interface_Architecture

---

# 1. Purpose

ExportSubtitleCommand requests exporting subtitle files derived from generated speech.

The command SHALL export subtitle data based on existing timing information.

The command SHALL NOT initiate speech generation.

---

# 2. Responsibility

Execution SHALL be performed by ExportSubtitleCommandHandler.

The handler SHALL prepare subtitle data and schedule an Export Job.

---

# 3. Command Definition

## Name

ExportSubtitleCommand

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

Destination path for exported subtitles.

---

## Optional

### SubtitleFormat

Type

Enumeration

Allowed values:

- SRT
- VTT
- ASS
- TTML

Default:

SRT

---

### IncludeSpeakerNames

Type

Boolean

Default:

true

---

### IncludeEmptyFragments

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
- timing information is unavailable;
- OutputPath is invalid;
- destination already exists and overwrite is disabled;
- Export Service is unavailable.

Validation SHALL complete before execution begins.

---

# 6. Execution Rules

Execution SHALL:

1. Load the target Aggregate.
2. Validate subtitle availability.
3. Build subtitle entries.
4. Create an Export Job.
5. Register the Job with the Export Service.
6. Publish lifecycle events.

Execution SHALL complete immediately.

Subtitle export SHALL execute asynchronously.

---

# 7. Export Rules

Subtitle timestamps SHALL be derived exclusively from existing SpeechSegments.

The exported subtitles SHALL preserve:

- Project ordering;
- Document ordering;
- Fragment ordering.

Speaker names SHALL be exported only when requested and available.

The command SHALL NOT modify Project data.

The command SHALL NOT regenerate timing information.

---

# 8. Result

Successful execution SHALL return:

ExportSubtitleResult

The result SHALL contain:

- JobId
- Scope
- TargetId
- SubtitleFormat
- OutputPath

---

# 9. Published Events

Successful execution SHALL publish:

- SubtitleExportStarted
- JobQueued

Background execution SHALL additionally publish:

- SubtitleExportCompleted

Upon failure:

- SubtitleExportFailed

---

# 10. Error Conditions

Execution MAY fail with:

- TargetNotFound
- TimingInformationUnavailable
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

Subtitle file generation SHALL execute outside the transaction.

---

# 13. Authorization

The caller SHALL possess permission to export Project assets.

---

# 14. Performance Requirements

Command execution SHOULD complete within 50 milliseconds.

The command SHALL NOT wait for subtitle file creation.

---

# 15. Thread Safety

Concurrent subtitle exports targeting different destinations MAY execute simultaneously.

Concurrent exports targeting the same destination SHALL be serialized.

---

# 16. AI Implementation Rules

AI-generated implementations SHALL:

- export subtitles only from existing timing information;
- never regenerate timestamps;
- preserve Project, Document and Fragment ordering;
- execute asynchronously;
- publish lifecycle events only after successful transaction completion.

---

# 17. Sequence

```text
GUI
 │
 ▼
ExportSubtitleCommand
 │
 ▼
CommandBus
 │
 ▼
ExportSubtitleCommandHandler
 │
 ▼
ExportService
 │
 ├── Build Subtitle Data
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
Write Subtitle File
 │
 ▼
SubtitleExportCompleted
```

---

# 18. Compliance Checklist

The implementation conforms to this specification only if it:

- exports subtitles only from existing timing information;
- preserves ordering of exported content;
- creates exactly one Export Job;
- executes asynchronously;
- never performs speech generation;
- publishes SubtitleExportStarted after successful completion.

---

End of Document