# Voxarium Software Architecture Specification

Document Path:
spec/400_Commands/ImportAudioCommand.md

Document ID: CMD-048

Title: ImportAudioCommand

Version: 1.0.0

Status: Accepted

Classification: Normative

Depends On

- Project
- Document
- Fragment
- SpeechSegment
- AudioAsset
- Import_Service
- Command_Model
- Command_Bus

Referenced By

- Import_Service
- Audio_Service
- Workflow_Engine
- User_Interface_Architecture

---

# 1. Purpose

ImportAudioCommand requests importing externally produced audio into an existing Project.

The command SHALL associate imported audio with one or more Fragments.

The command SHALL NOT perform speech generation.

---

# 2. Responsibility

Execution SHALL be performed by ImportAudioCommandHandler.

The handler SHALL create an Import Job and schedule audio processing.

---

# 3. Command Definition

## Name

ImportAudioCommand

## Category

Import Commands

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

### SourcePath

Type

Path

Path to the imported audio file or directory.

---

## Optional

### AudioFormat

Type

Enumeration

Allowed values:

- AutoDetect
- WAV
- FLAC
- MP3
- OGG

Default:

AutoDetect

---

### ImportMode

Type

Enumeration

Allowed values:

- ReplaceAudio
- MergeAudio
- AppendAudio

Default:

ReplaceAudio

---

### PreserveExistingTiming

Type

Boolean

Default:

true

---

### ValidateDuration

Type

Boolean

Default:

true

Verifies that imported audio duration is compatible with the target scope.

---

# 5. Validation Rules

Execution SHALL fail if:

- the target object does not exist;
- SourcePath does not exist;
- audio format is unsupported;
- audio cannot be decoded;
- the target is locked;
- Import Service is unavailable.

Validation SHALL complete before execution begins.

---

# 6. Execution Rules

Execution SHALL:

1. Load the target Aggregate.
2. Validate the audio source.
3. Detect the audio format.
4. Analyze imported audio.
5. Create an Import Job.
6. Register the Job with the Import Service.
7. Publish lifecycle events.

Execution SHALL complete immediately.

Audio import SHALL execute asynchronously.

---

# 7. Import Rules

Imported audio SHALL become managed Project Assets.

When ImportMode is ReplaceAudio:

- existing imported audio SHALL be replaced.

When ImportMode is MergeAudio:

- compatible audio Assets SHALL be preserved.

When ImportMode is AppendAudio:

- imported audio SHALL be appended according to the selected Scope.

The command SHALL NOT modify:

- Fragment text;
- Voice Profiles;
- Roles;
- Emotions;
- Generation Presets;
- Pronunciation Dictionaries.

Imported audio SHALL NOT be treated as generated speech unless explicitly approved by the Generation Service.

---

# 8. Result

Successful execution SHALL return:

ImportAudioResult

The result SHALL contain:

- JobId
- Scope
- TargetId
- DetectedFormat
- ImportedAssets

---

# 9. Published Events

Successful execution SHALL publish:

- AudioImportStarted
- JobQueued

Background execution SHALL additionally publish:

- AudioImported

After successful completion:

- AudioImportCompleted

Upon failure:

- AudioImportFailed

---

# 10. Error Conditions

Execution MAY fail with:

- TargetNotFound
- SourceNotFound
- UnsupportedAudioFormat
- AudioDecodingFailed
- DurationMismatch
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

Audio decoding and Asset creation SHALL execute outside the transaction.

---

# 13. Authorization

The caller SHALL possess permission to modify the selected Project object.

---

# 14. Performance Requirements

Command execution SHOULD complete within 50 milliseconds.

The command SHALL NOT wait for audio analysis or import completion.

---

# 15. Thread Safety

Concurrent imports targeting different objects MAY execute simultaneously.

Concurrent imports targeting the same object SHALL be serialized.

---

# 16. AI Implementation Rules

AI-generated implementations SHALL:

- validate imported audio before registration;
- preserve Project structure;
- never modify generation configuration;
- execute asynchronously;
- publish lifecycle events only after successful transaction completion.

---

# 17. Sequence

```text
GUI
 │
 ▼
ImportAudioCommand
 │
 ▼
CommandBus
 │
 ▼
ImportAudioCommandHandler
 │
 ▼
ImportService
 │
 ├── Detect Audio Format
 │
 ├── Analyze Audio
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
Create Audio Assets
 │
 ▼
AudioImportCompleted
```

---

# 18. Compliance Checklist

The implementation conforms to this specification only if it:

- imports supported audio formats;
- validates imported audio;
- preserves Project structure;
- creates exactly one Import Job;
- executes asynchronously;
- publishes AudioImportStarted after successful completion.

---

End of Document