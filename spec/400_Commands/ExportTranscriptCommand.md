# Voxarium Software Architecture Specification

Document Path:
spec/400_Commands/ExportTranscriptCommand.md

Document ID: CMD-043

Title: ExportTranscriptCommand

Version: 1.0.0

Status: Accepted

Classification: Normative

Depends On

- Project
- Document
- Fragment
- Transcript
- Export_Service
- Command_Model
- Command_Bus

Referenced By

- Export_Service
- Workflow_Engine
- User_Interface_Architecture

---

# 1. Purpose

ExportTranscriptCommand requests exporting textual transcripts from a Project, Document, or Fragment.

The command SHALL export existing textual content.

The command SHALL NOT modify Project data.

---

# 2. Responsibility

Execution SHALL be performed by ExportTranscriptCommandHandler.

The handler SHALL prepare transcript data and schedule an Export Job.

---

# 3. Command Definition

## Name

ExportTranscriptCommand

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

Destination path for exported transcript.

---

## Optional

### TranscriptFormat

Type

Enumeration

Allowed values:

- TXT
- Markdown
- HTML
- DOCX
- PDF

Default:

Markdown

---

### IncludeSpeakerNames

Type

Boolean

Default:

true

---

### IncludeFragmentIdentifiers

Type

Boolean

Default:

false

---

### IncludeGenerationMetadata

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
- no textual content exists;
- OutputPath is invalid;
- destination already exists and overwrite is disabled;
- Export Service is unavailable.

Validation SHALL complete before execution begins.

---

# 6. Execution Rules

Execution SHALL:

1. Load the target Aggregate.
2. Collect transcript data.
3. Format the transcript.
4. Create an Export Job.
5. Register the Job with the Export Service.
6. Publish lifecycle events.

Execution SHALL complete immediately.

Transcript export SHALL execute asynchronously.

---

# 7. Export Rules

The exported transcript SHALL preserve:

- Project ordering;
- Document ordering;
- Fragment ordering.

When IncludeSpeakerNames is enabled, each Fragment SHALL include its effective speaker.

When IncludeGenerationMetadata is enabled, only non-runtime metadata SHALL be exported.

The command SHALL NOT export generated audio.

The command SHALL NOT regenerate any content.

---

# 8. Result

Successful execution SHALL return:

ExportTranscriptResult

The result SHALL contain:

- JobId
- Scope
- TargetId
- TranscriptFormat
- OutputPath

---

# 9. Published Events

Successful execution SHALL publish:

- TranscriptExportStarted
- JobQueued

Background execution SHALL additionally publish:

- TranscriptExportCompleted

Upon failure:

- TranscriptExportFailed

---

# 10. Error Conditions

Execution MAY fail with:

- TargetNotFound
- EmptyTranscript
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

Transcript generation SHALL execute outside the transaction.

---

# 13. Authorization

The caller SHALL possess permission to export Project data.

---

# 14. Performance Requirements

Command execution SHOULD complete within 50 milliseconds.

The command SHALL NOT wait for transcript creation.

---

# 15. Thread Safety

Concurrent transcript exports targeting different destinations MAY execute simultaneously.

Concurrent exports targeting the same destination SHALL be serialized.

---

# 16. AI Implementation Rules

AI-generated implementations SHALL:

- export only existing textual content;
- preserve Project, Document and Fragment ordering;
- never modify the Project;
- execute asynchronously;
- publish lifecycle events only after successful transaction completion.

---

# 17. Sequence

```text
GUI
 │
 ▼
ExportTranscriptCommand
 │
 ▼
CommandBus
 │
 ▼
ExportTranscriptCommandHandler
 │
 ▼
ExportService
 │
 ├── Collect Transcript
 │
 ├── Format Output
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
Write Transcript
 │
 ▼
TranscriptExportCompleted
```

---

# 18. Compliance Checklist

The implementation conforms to this specification only if it:

- exports only existing textual content;
- preserves Project, Document and Fragment ordering;
- creates exactly one Export Job;
- executes asynchronously;
- does not modify Project data;
- publishes TranscriptExportStarted after successful completion.

---

End of Document