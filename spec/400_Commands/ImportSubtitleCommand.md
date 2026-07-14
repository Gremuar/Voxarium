# Voxarium Software Architecture Specification

Document Path:
spec/400_Commands/ImportSubtitleCommand.md

Document ID: CMD-047

Title: ImportSubtitleCommand

Version: 1.0.0

Status: Accepted

Classification: Normative

Depends On

- Document
- Fragment
- Timeline
- Subtitle
- Import_Service
- Command_Model
- Command_Bus

Referenced By

- Import_Service
- Timeline_Service
- Fragment_Service
- Workflow_Engine
- User_Interface_Architecture

---

# 1. Purpose

ImportSubtitleCommand requests importing subtitle data into an existing Document.

The command SHALL import subtitle text together with timing information.

The command SHALL NOT initiate speech generation.

---

# 2. Responsibility

Execution SHALL be performed by ImportSubtitleCommandHandler.

The handler SHALL create an Import Job and schedule subtitle processing.

---

# 3. Command Definition

## Name

ImportSubtitleCommand

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

Path to the subtitle file.

---

## Optional

### SubtitleFormat

Type

Enumeration

Allowed values:

- AutoDetect
- SRT
- VTT
- ASS
- TTML

Default:

AutoDetect

---

### ImportMode

Type

Enumeration

Allowed values:

- ReplaceTimeline
- MergeTimeline
- UpdateTimingOnly

Default:

MergeTimeline

---

### PreserveExistingText

Type

Boolean

Default:

true

When enabled, existing Fragment text SHALL be preserved and only timing information SHALL be updated where possible.

---

### DetectSpeakers

Type

Boolean

Default:

false

Attempts to derive speaker assignments from subtitle metadata when supported.

---

# 5. Validation Rules

Execution SHALL fail if:

- Document does not exist;
- SourcePath does not exist;
- subtitle format is unsupported;
- subtitle timing data is invalid;
- Document is locked;
- Import Service is unavailable.

Validation SHALL complete before execution begins.

---

# 6. Execution Rules

Execution SHALL:

1. Load the Document Aggregate.
2. Validate the source.
3. Detect the subtitle format.
4. Parse subtitle entries.
5. Create an Import Job.
6. Register the Job with the Import Service.
7. Publish lifecycle events.

Execution SHALL complete immediately.

Subtitle import SHALL execute asynchronously.

---

# 7. Import Rules

The import process SHALL:

- preserve subtitle ordering;
- preserve timing precision supported by the source format;
- update Fragment timing according to ImportMode;
- preserve existing Fragment text when PreserveExistingText is enabled.

The command SHALL NOT import generated audio.

The command SHALL NOT modify Voice Profiles, Roles, Emotions or Generation Presets.

Imported timing information SHALL invalidate existing speech timing metadata when applicable.

---

# 8. Result

Successful execution SHALL return:

ImportSubtitleResult

The result SHALL contain:

- JobId
- DocumentId
- DetectedFormat
- ImportedSubtitleEntries
- UpdatedFragments

---

# 9. Published Events

Successful execution SHALL publish:

- SubtitleImportStarted
- JobQueued

Background execution SHALL additionally publish:

- SubtitleImported

After successful completion:

- SubtitleImportCompleted

Upon failure:

- SubtitleImportFailed

---

# 10. Error Conditions

Execution MAY fail with:

- DocumentNotFound
- SourceNotFound
- UnsupportedFormat
- InvalidSubtitleFormat
- InvalidTimingData
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

Subtitle parsing and timeline updates SHALL execute outside the transaction.

---

# 13. Authorization

The caller SHALL possess permission to modify the destination Document.

---

# 14. Performance Requirements

Command execution SHOULD complete within 50 milliseconds.

The command SHALL NOT wait for subtitle parsing.

---

# 15. Thread Safety

Concurrent imports into different Documents MAY execute simultaneously.

Concurrent imports targeting the same Document SHALL be serialized.

---

# 16. AI Implementation Rules

AI-generated implementations SHALL:

- preserve subtitle ordering;
- preserve timing precision whenever possible;
- never overwrite Fragment text unless explicitly requested;
- never modify generation configuration;
- execute asynchronously;
- publish lifecycle events only after successful transaction completion.

---

# 17. Sequence

```text
GUI
 │
 ▼
ImportSubtitleCommand
 │
 ▼
CommandBus
 │
 ▼
ImportSubtitleCommandHandler
 │
 ▼
ImportService
 │
 ├── Detect Format
 │
 ├── Parse Subtitle
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
Update Timeline
 │
 ▼
SubtitleImportCompleted
```

---

# 18. Compliance Checklist

The implementation conforms to this specification only if it:

- imports supported subtitle formats;
- preserves subtitle ordering;
- updates timeline according to ImportMode;
- preserves Fragment text when requested;
- executes asynchronously;
- publishes SubtitleImportStarted after successful completion.

---

End of Document