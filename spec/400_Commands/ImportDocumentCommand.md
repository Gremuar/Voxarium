# Voxarium Software Architecture Specification

Document Path:
spec/400_Commands/ImportDocumentCommand.md

Document ID: CMD-045

Title: ImportDocumentCommand

Version: 1.0.0

Status: Accepted

Classification: Normative

Depends On

- Project
- Document
- Import_Service
- Command_Model
- Command_Bus

Referenced By

- Import_Service
- Workflow_Engine
- Project_Service
- User_Interface_Architecture

---

# 1. Purpose

ImportDocumentCommand requests importing one or more Documents into an existing Project.

The command SHALL create new Document Aggregates from external sources.

The command SHALL NOT overwrite existing Documents unless explicitly requested.

---

# 2. Responsibility

Execution SHALL be performed by ImportDocumentCommandHandler.

The handler SHALL create an Import Job and schedule document import.

---

# 3. Command Definition

## Name

ImportDocumentCommand

## Category

Import Commands

## Layer

Application

---

# 4. Parameters

## Required

### ProjectId

Type

Identifier

Identifier of the destination Project.

---

### SourcePath

Type

Path

Path to the imported file or directory.

---

## Optional

### ImportFormat

Type

Enumeration

Allowed values:

- AutoDetect
- PlainText
- Markdown
- DOCX
- PDF
- EPUB

Default:

AutoDetect

---

### ConflictResolution

Type

Enumeration

Allowed values:

- Skip
- Rename
- Replace

Default:

Rename

---

### PreserveStructure

Type

Boolean

Default:

true

Preserves headings, chapters and logical document structure whenever supported.

---

# 5. Validation Rules

Execution SHALL fail if:

- Project does not exist;
- SourcePath does not exist;
- source format is unsupported;
- Import Service is unavailable;
- caller lacks sufficient permissions.

Validation SHALL complete before execution begins.

---

# 6. Execution Rules

Execution SHALL:

1. Load the Project Aggregate.
2. Validate the source.
3. Detect the document format.
4. Create an Import Job.
5. Register the Job with the Import Service.
6. Publish lifecycle events.

Execution SHALL complete immediately.

Document import SHALL execute asynchronously.

---

# 7. Import Rules

The import process SHALL:

- preserve textual content;
- preserve document ordering whenever available;
- preserve chapters and sections when supported;
- create new Document identifiers.

Existing Project objects SHALL NOT be modified unless ConflictResolution explicitly permits replacement.

Imported Documents SHALL initially contain no generated speech.

---

# 8. Result

Successful execution SHALL return:

ImportDocumentResult

The result SHALL contain:

- JobId
- ProjectId
- DetectedFormat
- ImportedDocuments

---

# 9. Published Events

Successful execution SHALL publish:

- DocumentImportStarted
- JobQueued

Background execution SHALL additionally publish:

- DocumentImported

After successful completion:

- DocumentImportCompleted

Upon failure:

- DocumentImportFailed

---

# 10. Error Conditions

Execution MAY fail with:

- ProjectNotFound
- SourceNotFound
- UnsupportedFormat
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

Parsing and Document creation SHALL execute outside the transaction.

---

# 13. Authorization

The caller SHALL possess permission to modify the destination Project.

---

# 14. Performance Requirements

Command execution SHOULD complete within 50 milliseconds.

The command SHALL NOT wait for document parsing.

---

# 15. Thread Safety

Concurrent imports into different Projects MAY execute simultaneously.

Concurrent imports into the same Project SHALL be serialized when conflicts are possible.

---

# 16. AI Implementation Rules

AI-generated implementations SHALL:

- create new Document identifiers;
- preserve document structure whenever possible;
- never overwrite existing Documents unless explicitly requested;
- execute asynchronously;
- publish lifecycle events only after successful transaction completion.

---

# 17. Sequence

```text
GUI
 │
 ▼
ImportDocumentCommand
 │
 ▼
CommandBus
 │
 ▼
ImportDocumentCommandHandler
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
Parse Document
 │
 ▼
Create Document Aggregate
 │
 ▼
DocumentImportCompleted
```

---

# 18. Compliance Checklist

The implementation conforms to this specification only if it:

- imports supported document formats;
- preserves document structure whenever possible;
- creates new Document identifiers;
- never overwrites existing Documents unless requested;
- executes asynchronously;
- publishes DocumentImportStarted after successful completion.

---

End of Document