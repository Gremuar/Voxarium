# Voxarium Software Architecture Specification

Document Path:
spec/400_Commands/ImportPronunciationDictionaryCommand.md

Document ID: CMD-049

Title: ImportPronunciationDictionaryCommand

Version: 1.0.0

Status: Accepted

Classification: Normative

Depends On

- PronunciationDictionary
- DictionaryEntry
- Import_Service
- Dictionary_Service
- Command_Model
- Command_Bus

Referenced By

- Import_Service
- Dictionary_Service
- Workflow_Engine
- User_Interface_Architecture

---

# 1. Purpose

ImportPronunciationDictionaryCommand requests importing pronunciation dictionary entries into an existing Pronunciation Dictionary.

The command SHALL import dictionary entries from an external source.

The command SHALL NOT modify unrelated dictionaries.

---

# 2. Responsibility

Execution SHALL be performed by ImportPronunciationDictionaryCommandHandler.

The handler SHALL create an Import Job and schedule dictionary processing.

---

# 3. Command Definition

## Name

ImportPronunciationDictionaryCommand

## Category

Import Commands

## Layer

Application

---

# 4. Parameters

## Required

### DictionaryId

Type

Identifier

Identifier of the destination Pronunciation Dictionary.

---

### SourcePath

Type

Path

Path to the dictionary file.

---

## Optional

### DictionaryFormat

Type

Enumeration

Allowed values:

- AutoDetect
- JSON
- YAML
- CSV
- XML

Default:

AutoDetect

---

### ImportMode

Type

Enumeration

Allowed values:

- Merge
- Replace
- SkipExisting

Default:

Merge

---

### NormalizeEntries

Type

Boolean

Default:

true

Normalizes imported entries before validation.

---

### ValidatePronunciations

Type

Boolean

Default:

true

Validates imported pronunciation values before persistence.

---

# 5. Validation Rules

Execution SHALL fail if:

- the dictionary does not exist;
- SourcePath does not exist;
- the dictionary format is unsupported;
- imported data cannot be parsed;
- Import Service is unavailable.

Validation SHALL complete before execution begins.

---

# 6. Execution Rules

Execution SHALL:

1. Load the Pronunciation Dictionary Aggregate.
2. Validate the import source.
3. Detect the dictionary format.
4. Parse dictionary entries.
5. Normalize imported data.
6. Create an Import Job.
7. Register the Job with the Import Service.
8. Publish lifecycle events.

Execution SHALL complete immediately.

Dictionary import SHALL execute asynchronously.

---

# 7. Import Rules

Each imported entry SHALL be validated before persistence.

Duplicate entries SHALL be processed according to ImportMode.

Normalization MAY include:

- whitespace normalization;
- Unicode normalization;
- duplicate removal;
- key canonicalization.

The command SHALL NOT modify:

- Projects;
- Documents;
- Fragments;
- Voice Profiles;
- Generation Presets.

Dictionary identifiers SHALL remain unchanged.

---

# 8. Result

Successful execution SHALL return:

ImportPronunciationDictionaryResult

The result SHALL contain:

- JobId
- DictionaryId
- DetectedFormat
- ImportedEntries
- SkippedEntries
- UpdatedEntries

---

# 9. Published Events

Successful execution SHALL publish:

- DictionaryImportStarted
- JobQueued

Background execution SHALL additionally publish:

- DictionaryEntriesImported

After successful completion:

- DictionaryImportCompleted

Upon failure:

- DictionaryImportFailed

---

# 10. Error Conditions

Execution MAY fail with:

- DictionaryNotFound
- SourceNotFound
- UnsupportedDictionaryFormat
- DictionaryParsingFailed
- DuplicateEntryConflict
- ImportServiceUnavailable
- ValidationFailed
- InternalError

---

# 11. Idempotency

Submitting an identical import request while an equivalent Import Job is active SHALL return the existing Job.

Duplicate Import Jobs SHALL NOT be created.

Repeated imports with ImportMode set to SkipExisting SHALL NOT modify existing entries.

---

# 12. Transaction Requirements

The transaction SHALL include:

- Import Job creation;
- queue registration.

Dictionary parsing and entry persistence SHALL execute outside the transaction.

---

# 13. Authorization

The caller SHALL possess permission to modify the destination Pronunciation Dictionary.

---

# 14. Performance Requirements

Command execution SHOULD complete within 50 milliseconds.

The command SHALL NOT wait for dictionary parsing or persistence.

---

# 15. Thread Safety

Concurrent imports into different dictionaries MAY execute simultaneously.

Concurrent imports targeting the same dictionary SHALL be serialized.

---

# 16. AI Implementation Rules

AI-generated implementations SHALL:

- validate every imported dictionary entry;
- normalize imported data before persistence;
- preserve dictionary identity;
- execute asynchronously;
- publish lifecycle events only after successful transaction completion.

---

# 17. Sequence

```text
GUI
 │
 ▼
ImportPronunciationDictionaryCommand
 │
 ▼
CommandBus
 │
 ▼
ImportPronunciationDictionaryCommandHandler
 │
 ▼
ImportService
 │
 ├── Detect Format
 │
 ├── Parse Dictionary
 │
 ├── Normalize Entries
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
Validate Entries
 │
 ▼
Persist Dictionary Entries
 │
 ▼
DictionaryImportCompleted
```

---

# 18. Compliance Checklist

The implementation conforms to this specification only if it:

- imports supported dictionary formats;
- validates every imported entry;
- processes duplicates according to ImportMode;
- preserves dictionary identity;
- executes asynchronously;
- publishes DictionaryImportStarted after successful completion.

---

End of Document