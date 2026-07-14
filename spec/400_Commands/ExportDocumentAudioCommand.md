# Voxarium Software Architecture Specification

Document Path:
spec/400_Commands/ExportDocumentAudioCommand.md

Document ID: CMD-040

Title: ExportDocumentAudioCommand

Version: 1.0.0

Status: Accepted

Classification: Normative

Depends On

- Document
- Fragment
- SpeechSegment
- Export_Service
- Command_Model
- Command_Bus

Referenced By

- Export_Service
- Workflow_Engine
- User_Interface_Architecture

---

# 1. Purpose

ExportDocumentAudioCommand requests exporting generated speech for an entire Document.

The command SHALL export existing generated speech.

The command SHALL NOT initiate speech generation.

---

# 2. Responsibility

Execution SHALL be performed by ExportDocumentAudioCommandHandler.

The handler SHALL prepare an Export Job for the requested Document.

---

# 3. Command Definition

## Name

ExportDocumentAudioCommand

## Category

Export Commands

## Layer

Application

---

# 4. Parameters

## Required

### DocumentId

Type

Identifier

Identifier of the Document.

---

### OutputPath

Type

Path

Destination path for exported audio.

---

## Optional

### ExportMode

Type

Enumeration

Allowed values:

- SingleFile
- SeparateFragments

Default:

SingleFile

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

### IncludeSilence

Type

Boolean

Default:

true

Determines whether pauses between Fragments SHALL be included.

---

### OverwriteExisting

Type

Boolean

Default:

false

---

# 5. Validation Rules

Execution SHALL fail if:

- Document does not exist;
- Document contains no generated speech;
- OutputPath is invalid;
- destination already exists and overwrite is disabled;
- Export Service is unavailable.

Validation SHALL complete before execution begins.

---

# 6. Execution Rules

Execution SHALL:

1. Load the Document Aggregate.
2. Verify generated SpeechSegments.
3. Determine the export strategy.
4. Create an Export Job.
5. Register the Job with the Export Service.
6. Publish lifecycle events.

Execution SHALL complete immediately.

Audio export SHALL execute asynchronously.

---

# 7. Export Rules

When ExportMode is SingleFile:

- all generated SpeechSegments SHALL be concatenated in Document order.

When ExportMode is SeparateFragments:

- one audio file SHALL be produced for each Fragment.

The export process SHALL preserve Fragment ordering.

The command SHALL NOT modify Project data.

---

# 8. Result

Successful execution SHALL return:

ExportDocumentAudioResult

The result SHALL contain:

- JobId
- DocumentId
- OutputPath
- ExportMode

---

# 9. Published Events

Successful execution SHALL publish:

- DocumentExportStarted
- JobQueued

Background execution SHALL additionally publish:

- DocumentExportCompleted

Upon failure:

- DocumentExportFailed

---

# 10. Error Conditions

Execution MAY fail with:

- DocumentNotFound
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

File creation SHALL execute outside the transaction.

---

# 13. Authorization

The caller SHALL possess permission to export the Document.

---

# 14. Performance Requirements

Command execution SHOULD complete within 50 milliseconds.

The command SHALL NOT wait for export completion.

---

# 15. Thread Safety

Concurrent exports of different Documents MAY execute simultaneously.

Concurrent exports targeting the same destination SHALL be serialized.

---

# 16. AI Implementation Rules

AI-generated implementations SHALL:

- export only existing generated speech;
- preserve Fragment ordering;
- never initiate speech generation;
- execute asynchronously;
- publish lifecycle events only after successful transaction completion.

---

# 17. Sequence

```text
GUI
 │
 ▼
ExportDocumentAudioCommand
 │
 ▼
CommandBus
 │
 ▼
ExportDocumentAudioCommandHandler
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
Write Audio File(s)
 │
 ▼
DocumentExportCompleted
```

---

# 18. Compliance Checklist

The implementation conforms to this specification only if it:

- exports only generated speech;
- preserves Document ordering;
- creates exactly one Export Job;
- executes asynchronously;
- never performs speech generation;
- publishes DocumentExportStarted after successful completion.

---

End of Document