# Voxarium Software Architecture Specification

Document Path:
spec/400_Commands/ClearGeneratedSpeechCommand.md

Document ID: CMD-038

Title: ClearGeneratedSpeechCommand

Version: 1.0.0

Status: Accepted

Classification: Normative

Depends On

- Project
- Document
- Fragment
- SpeechSegment
- GeneratedAsset
- Generation_Service
- Command_Model
- Command_Bus

Referenced By

- Workflow_Engine
- Fragment_Service
- Project_Service
- User_Interface_Architecture

---

# 1. Purpose

ClearGeneratedSpeechCommand requests removal of previously generated speech artifacts.

The command SHALL remove generated runtime artifacts only.

The command SHALL preserve all user-authored data.

---

# 2. Responsibility

Execution SHALL be performed by ClearGeneratedSpeechCommandHandler.

The handler SHALL remove generated speech artifacts according to the selected scope.

---

# 3. Command Definition

## Name

ClearGeneratedSpeechCommand

## Category

Generation Commands

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

## Optional

### RemoveCachedAudio

Type

Boolean

Default:

true

---

### RemoveWaveforms

Type

Boolean

Default:

true

---

### RemoveTimingData

Type

Boolean

Default:

true

---

# 5. Validation Rules

Execution SHALL fail if:

- the target object does not exist;
- generation is currently running for the target;
- the target is locked;
- caller lacks required permissions.

Validation SHALL complete before execution begins.

---

# 6. Execution Rules

Execution SHALL:

1. Load the target Aggregate.
2. Validate the requested Scope.
3. Remove generated SpeechSegments.
4. Remove generated audio Assets.
5. Remove waveform caches.
6. Remove timing caches.
7. Mark affected Fragments as GenerationRequired.
8. Publish lifecycle events.

Execution SHALL be atomic.

---

# 7. Removal Rules

The command SHALL remove only generated artifacts, including:

- generated audio;
- waveform cache;
- timing cache;
- generation metadata;
- provider-specific temporary files.

The command SHALL NOT remove:

- Documents;
- Fragments;
- Roles;
- Voice Profiles;
- Generation Presets;
- Pronunciation Dictionaries;
- user annotations.

---

# 8. Result

Successful execution SHALL return:

ClearGeneratedSpeechResult

The result SHALL contain:

- Scope
- TargetId
- RemovedSpeechSegments
- RemovedAssets

---

# 9. Published Events

Successful execution SHALL publish:

- GeneratedSpeechCleared

Additionally, the implementation MAY publish:

- FragmentGenerationInvalidated
- DocumentModified
- ProjectModified

---

# 10. Error Conditions

Execution MAY fail with:

- TargetNotFound
- GenerationRunning
- TargetLocked
- ValidationFailed
- StorageFailure
- InternalError

---

# 11. Idempotency

Executing the command when no generated artifacts exist SHALL produce no state changes.

Repeated execution SHALL produce identical results.

---

# 12. Transaction Requirements

Removal of generated artifacts SHALL execute within a single Application transaction.

Rollback SHALL restore the previous state.

---

# 13. Authorization

The caller SHALL possess permission to modify the owning Project.

---

# 14. Performance Requirements

Typical execution SHOULD complete within:

- 20 milliseconds for a Fragment;
- 100 milliseconds for a Document;
- 500 milliseconds for a Project.

Removal of physical files MAY continue asynchronously after transaction completion.

---

# 15. Thread Safety

Concurrent cleanup operations targeting the same Aggregate SHALL be serialized.

Independent cleanup operations MAY execute concurrently.

---

# 16. AI Implementation Rules

AI-generated implementations SHALL:

- remove only generated artifacts;
- preserve all user-authored data;
- invalidate generation state;
- avoid orphaned files;
- publish lifecycle events only after successful transaction completion.

---

# 17. Sequence

```text
GUI
 │
 ▼
ClearGeneratedSpeechCommand
 │
 ▼
CommandBus
 │
 ▼
ClearGeneratedSpeechCommandHandler
 │
 ▼
GenerationService
 │
 ├── Remove SpeechSegments
 │
 ├── Remove Audio Assets
 │
 ├── Remove Caches
 │
 ▼
Repository
 │
 ▼
GeneratedSpeechCleared Event
```

---

# 18. Compliance Checklist

The implementation conforms to this specification only if it:

- removes only generated artifacts;
- preserves all user-authored data;
- invalidates generation state;
- executes atomically;
- publishes GeneratedSpeechCleared after successful completion.

---

End of Document