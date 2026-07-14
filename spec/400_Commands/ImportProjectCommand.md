# Voxarium Software Architecture Specification

Document Path:

spec/400_Commands/ImportProjectCommand.md

Document ID: CMD-067

Title: ImportProjectCommand

Version: 1.0.0

Status: Accepted

Classification: Normative

Depends On

- Project
- Import_Service
- Storage_Service
- Validation_Service
- Command_Model
- Command_Bus

Referenced By

- Import_Service
- Workflow_Engine
- User_Interface_Architecture

---

# 1. Purpose

ImportProjectCommand requests importing a Project from an external representation.

The command SHALL create or update a Project from validated imported data.

The import process SHALL preserve repository consistency.

---

# 2. Responsibility

Execution SHALL be performed by ImportProjectCommandHandler.

The handler SHALL create an Import Job and submit it to the Import Service.

---

# 3. Command Definition

## Name

ImportProjectCommand

## Category

Administration Commands

## Layer

Application

---

# 4. Parameters

## Required

### Source

Type

Path

Location of the import package.

---

### ImportFormat

Type

Enumeration

Allowed values:

- Native
- JSON
- XML
- YAML
- ZIP

---

## Optional

### ImportMode

Type

Enumeration

Allowed values:

- Create
- Replace
- Merge

Default:

Create

---

### ValidateBeforeImport

Type

Boolean

Default:

true

---

### ValidateAfterImport

Type

Boolean

Default:

true

---

### ImportGeneratedAudio

Type

Boolean

Default:

true

---

### ImportPronunciationDictionaries

Type

Boolean

Default:

true

---

### Priority

Type

Enumeration

Allowed values:

- Low
- Normal
- High

Default:

Normal

---

# 5. Validation Rules

Execution SHALL fail if:

- import package does not exist;
- package format is unsupported;
- package validation fails;
- Import Service is unavailable;
- another Import Job is already active for the same target.

Validation SHALL complete before execution begins.

---

# 6. Execution Rules

Execution SHALL:

1. Validate the import package.
2. Build an Import Plan.
3. Create an Import Job.
4. Register the Job with the Import Service.
5. Publish lifecycle events.

Execution SHALL complete immediately.

Import SHALL execute asynchronously.

---

# 7. Import Rules

The import process SHALL restore:

- Project metadata;
- Documents;
- Fragments;
- Roles;
- Voice Profiles;
- Generation Presets;
- Pronunciation Dictionaries;
- Timeline;
- Project configuration.

Generated audio SHALL be imported only when requested.

Temporary files SHALL NOT be imported.

Imported identifiers SHALL remain stable whenever possible.

Repository consistency SHALL be preserved throughout the import process.

---

# 8. Result

Successful execution SHALL return:

ImportProjectResult

The result SHALL contain:

- JobId
- ImportedProjectId
- ImportMode
- ImportedObjects

---

# 9. Published Events

Successful execution SHALL publish:

- ProjectImportStarted
- JobQueued

Background execution SHALL additionally publish:

- ProjectImportCompleted

If validation is enabled:

- ProjectValidationStarted

Upon failure:

- ProjectImportFailed

---

# 10. Error Conditions

Execution MAY fail with:

- ImportPackageNotFound
- InvalidImportPackage
- UnsupportedImportFormat
- ImportServiceUnavailable
- ImportAlreadyRunning
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

Import SHALL execute outside the transaction.

Imported data SHALL become visible atomically.

---

# 13. Authorization

The caller SHALL possess permission to import Projects.

---

# 14. Performance Requirements

Command execution SHOULD complete within 30 milliseconds.

The command SHALL NOT wait for import completion.

---

# 15. Thread Safety

Only one Import Job MAY exist for the same target Project.

Different Projects MAY be imported concurrently.

---

# 16. AI Implementation Rules

AI-generated implementations SHALL:

- validate imported data before persistence;
- preserve repository consistency;
- never expose partially imported Projects;
- execute asynchronously;
- publish lifecycle events only after successful transaction completion.

---

# 17. Sequence

```text
GUI
 │
 ▼
ImportProjectCommand
 │
 ▼
CommandBus
 │
 ▼
ImportProjectCommandHandler
 │
 ▼
ImportService
 │
 ├── Validate Package
 │
 ├── Build Import Plan
 │
 ├── Create Import Job
 │
 ├── Queue Job
 │
 ▼
JobQueued Event
 │
 ▼
Background Worker
 │
 ▼
Import Project
 │
 │
 ├── Validate Project
 │
 ▼
ProjectImportCompleted
```

---

# 18. Compliance Checklist

The implementation conforms to this specification only if it:

- validates imported packages before persistence;
- preserves repository consistency;
- never exposes partially imported data;
- optionally validates the imported Project;
- creates exactly one Import Job;
- executes asynchronously;
- publishes ProjectImportStarted after successful completion.

---

End of Document