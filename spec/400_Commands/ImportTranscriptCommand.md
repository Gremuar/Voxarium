# Voxarium Software Architecture Specification

Document Path:
spec/400_Commands/ImportTranscriptCommand.md

Document ID: CMD-046

Title: ImportTranscriptCommand

Version: 1.0.0

Status: Accepted

Classification: Normative

Depends On

- Project
- Document
- Fragment
- Transcript
- Import_Service
- Command_Model
- Command_Bus

Referenced By

- Import_Service
- Fragment_Service
- Workflow_Engine
- User_Interface_Architecture

---

# 1. Purpose

ImportTranscriptCommand requests importing transcript data into an existing Document.

The command SHALL create or update Fragments based on imported transcript content.

The command SHALL NOT initiate speech generation.

---

# 2. Responsibility

Execution SHALL be performed by ImportTranscriptCommandHandler.

The handler SHALL create an Import Job and schedule transcript processing.

---

# 3. Command Definition

## Name

ImportTranscriptCommand

## Category

Import Commands

## Layer

Application

---

# 4. Parameters

## Required

### DocumentId

Type

Identifier

Identifier of the destination Document.

---

### SourcePath

Type

Path

Path to the transcript file.

---

## Optional

### TranscriptFormat

Type

Enumeration

Allowed values:

- AutoDetect
- TXT
- Markdown
- HTML
- DOCX
- PDF

Default:

AutoDetect

---

### ImportMode

Type

Enumeration

Allowed values:

- ReplaceFragments
- AppendFragments
- MergeFragments

Default:

ReplaceFragments

---

### PreserveExistingMetadata

Type

Boolean

Default:

true

---

### DetectSpeakers

Type

Boolean

Default:

true

Attempts to recognize speaker information from the imported transcript.

---

# 5. Validation Rules

Execution SHALL fail if:

- Document does not exist;
- SourcePath does not exist;
- transcript format is unsupported;
- Document is locked;
- Import Service is unavailable.

Validation SHALL complete before execution begins.

---

# 6. Execution Rules

Execution SHALL:

1. Load the Document Aggregate.
2. Validate the source.
3. Detect the transcript format.
4. Create an Import Job.
5. Register the Job with the Import Service.
6. Publish lifecycle events.

Execution SHALL complete immediately.

Transcript import SHALL execute asynchronously.

---

# 7. Import Rules

The import process SHALL:

- preserve transcript ordering;
- preserve paragraph boundaries whenever available;
- create or update Fragments according to ImportMode;
- preserve existing metadata when requested.

Imported Fragments SHALL initially have no generated SpeechSegments.

The command SHALL NOT overwrite generated audio.

---

# 8. Result

Successful execution SHALL return:

ImportTranscriptResult

The result SHALL contain:

- JobId
- DocumentId
- DetectedFormat
- ImportedFragments

---

# 9. Published Events

Successful execution SHALL publish:

- TranscriptImportStarted
- JobQueued

Background execution SHALL additionally publish:

- TranscriptImported

After successful completion:

- TranscriptImportCompleted

Upon failure:

- TranscriptImportFailed

---

# 10. Error Conditions

Execution MAY fail with:

- DocumentNotFound
- SourceNotFound
- UnsupportedFormat
- DocumentLocked
- ImportServiceUnavailable
- ValidationFailed
- InternalError

---

# 11. Idempotency

Submitting an identical import request while an equivalent Import Job is active SHALL return the existing Job.

Duplicate Import Jobs SHALL NOT be created.

---

# 12. Transaction Requirements

The transaction SHALL include:

- Import Job creation;
- queue registration.

Transcript parsing and Fragment creation SHALL execute outside the transaction.

---

# 13. Authorization

The caller SHALL possess permission to modify the destination Document.

---

# 14. Performance Requirements

Command execution SHOULD complete within 50 milliseconds.

The command SHALL NOT wait for transcript parsing.

---

# 15. Thread Safety

Concurrent imports into different Documents MAY execute simultaneously.

Concurrent imports into the same Document SHALL be serialized.

---

# 16. AI Implementation Rules

AI-generated implementations SHALL:

- preserve transcript ordering;
- preserve metadata when requested;
- never overwrite generated speech;
- execute asynchronously;
- publish lifecycle events only after successful transaction completion.

---

# 17. Sequence

```text
GUI
 │
 ▼
ImportTranscriptCommand
 │
 ▼
CommandBus
 │
 ▼
ImportTranscriptCommandHandler
 │
 ▼
ImportService
 │
 ├── Detect Format
 │
 ├── Create Import Job
 │
 ├── Queue Import
 │
 ▼
JobQueued Event
 │
 ▼
Background Worker
 │
 ▼
Parse Transcript
 │
 ▼
Create or Update Fragments
 │
 ▼
TranscriptImportCompleted
```

---

# 18. Compliance Checklist

The implementation conforms to this specification only if it:

- imports supported transcript formats;
- preserves transcript ordering;
- updates Fragments according to ImportMode;
- never overwrites generated speech;
- executes asynchronously;
- publishes TranscriptImportStarted after successful completion.

---

End of Document