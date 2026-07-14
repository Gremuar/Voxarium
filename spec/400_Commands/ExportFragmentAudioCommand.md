# Voxarium Software Architecture Specification

Document Path:
spec/400_Commands/ExportFragmentAudioCommand.md

Document ID: CMD-039

Title: ExportFragmentAudioCommand

Version: 1.0.0

Status: Accepted

Classification: Normative

Depends On

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

ExportFragmentAudioCommand requests exporting generated speech associated with a Fragment.

The command SHALL export previously generated speech.

The command SHALL NOT initiate speech generation.

---

# 2. Responsibility

Execution SHALL be performed by ExportFragmentAudioCommandHandler.

The handler SHALL prepare and schedule an Export Job.

---

# 3. Command Definition

## Name

ExportFragmentAudioCommand

## Category

Export Commands

## Layer

Application

---

# 4. Parameters

## Required

### FragmentId

Type

Identifier

Identifier of the Fragment.

---

### OutputPath

Type

Path

Destination path for exported audio.

---

## Optional

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

### OverwriteExisting

Type

Boolean

Default:

false

---

# 5. Validation Rules

Execution SHALL fail if:

- Fragment does not exist;
- generated speech is unavailable;
- OutputPath is invalid;
- destination already exists and overwrite is disabled;
- Export Service is unavailable.

Validation SHALL complete before execution begins.

---

# 6. Execution Rules

Execution SHALL:

1. Load the Fragment Aggregate.
2. Validate generated speech availability.
3. Create an Export Job.
4. Register the Job with the Export Service.
5. Publish lifecycle events.

Execution SHALL complete immediately.

Export SHALL execute asynchronously.

---

# 7. Export Rules

The exported file SHALL contain only generated speech belonging to the specified Fragment.

The command SHALL NOT modify Project data.

The command SHALL NOT regenerate speech.

---

# 8. Result

Successful execution SHALL return:

ExportFragmentAudioResult

The result SHALL contain:

- JobId
- FragmentId
- OutputPath

---

# 9. Published Events

Successful execution SHALL publish:

- FragmentExportStarted
- JobQueued

Background execution SHALL additionally publish:

- FragmentExportCompleted

Upon failure:

- FragmentExportFailed

---

# 10. Error Conditions

Execution MAY fail with:

- FragmentNotFound
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

File export SHALL execute outside the transaction.

---

# 13. Authorization

The caller SHALL possess permission to export Project assets.

---

# 14. Performance Requirements

Command execution SHOULD complete within 20 milliseconds.

The command SHALL NOT wait for file creation.

---

# 15. Thread Safety

Concurrent export operations targeting different Fragments MAY execute simultaneously.

Concurrent export operations targeting the same output file SHALL be serialized.

---

# 16. AI Implementation Rules

AI-generated implementations SHALL:

- export existing generated speech only;
- never trigger speech generation;
- execute export asynchronously;
- avoid overwriting existing files unless explicitly requested;
- publish lifecycle events only after successful transaction completion.

---

# 17. Sequence

```text
GUI
 │
 ▼
ExportFragmentAudioCommand
 │
 ▼
CommandBus
 │
 ▼
ExportFragmentAudioCommandHandler
 │
 ▼
ExportService
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
Write Audio File
 │
 ▼
FragmentExportCompleted
```

---

# 18. Compliance Checklist

The implementation conforms to this specification only if it:

- exports only existing generated speech;
- never performs speech generation;
- creates exactly one Export Job;
- executes asynchronously;
- publishes FragmentExportStarted after successful completion.

---

End of Document