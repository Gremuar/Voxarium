# Voxarium Software Architecture Specification

Document Path:
spec/400_Commands/AnalyzeDocumentCommand.md

Document ID: CMD-050

Title: AnalyzeDocumentCommand

Version: 1.0.0

Status: Accepted

Classification: Normative

Depends On

- Document
- Fragment
- Analysis_Service
- AnalysisJob
- Command_Model
- Command_Bus

Referenced By

- Workflow_Engine
- Analysis_Service
- User_Interface_Architecture

---

# 1. Purpose

AnalyzeDocumentCommand requests semantic and structural analysis of a Document.

The command SHALL analyze existing Document content.

The command SHALL NOT modify the Document directly.

---

# 2. Responsibility

Execution SHALL be performed by AnalyzeDocumentCommandHandler.

The handler SHALL prepare an Analysis Job and submit it to the Analysis Service.

---

# 3. Command Definition

## Name

AnalyzeDocumentCommand

## Category

Analysis Commands

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

## Optional

### AnalysisScope

Type

Enumeration

Allowed values:

- Structure
- Text
- Speakers
- Pronunciation
- Full

Default:

Full

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

### ForceReanalysis

Type

Boolean

Default:

false

When enabled, previously cached analysis results SHALL be ignored.

---

# 5. Validation Rules

Execution SHALL fail if:

- Document does not exist;
- Document contains no Fragments;
- Analysis Service is unavailable;
- another equivalent Analysis Job is already running.

Validation SHALL complete before execution begins.

---

# 6. Execution Rules

Execution SHALL:

1. Load the Document Aggregate.
2. Validate analysis eligibility.
3. Build an Analysis Plan.
4. Create an Analysis Job.
5. Register the Job with the Analysis Service.
6. Publish lifecycle events.

Execution SHALL complete immediately.

Analysis SHALL execute asynchronously.

---

# 7. Analysis Rules

The analysis MAY include:

- document structure;
- chapter hierarchy;
- fragment boundaries;
- speaker consistency;
- pronunciation candidates;
- unsupported symbols;
- formatting anomalies;
- language detection.

Analysis SHALL NOT modify persisted Project data.

Analysis results SHALL be stored separately from the Document Aggregate.

---

# 8. Result

Successful execution SHALL return:

AnalyzeDocumentResult

The result SHALL contain:

- JobId
- DocumentId
- AnalysisScope

---

# 9. Published Events

Successful execution SHALL publish:

- DocumentAnalysisStarted
- JobQueued

Background execution SHALL additionally publish:

- DocumentAnalysisCompleted

Upon failure:

- DocumentAnalysisFailed

---

# 10. Error Conditions

Execution MAY fail with:

- DocumentNotFound
- EmptyDocument
- AnalysisServiceUnavailable
- AnalysisAlreadyRunning
- ValidationFailed
- InternalError

---

# 11. Idempotency

Submitting an identical analysis request while an equivalent Analysis Job is active SHALL return the existing Job.

Duplicate Analysis Jobs SHALL NOT be created.

---

# 12. Transaction Requirements

The transaction SHALL include:

- Analysis Job creation;
- queue registration.

Analysis SHALL execute outside the transaction.

---

# 13. Authorization

The caller SHALL possess permission to analyze the Document.

---

# 14. Performance Requirements

Command execution SHOULD complete within 30 milliseconds.

The command SHALL NOT wait for analysis completion.

---

# 15. Thread Safety

Only one active Analysis Job MAY exist for the same Document.

Independent Documents MAY be analyzed concurrently.

---

# 16. AI Implementation Rules

AI-generated implementations SHALL:

- create an Analysis Job before processing;
- never modify Document data during analysis;
- store analysis results independently;
- execute asynchronously;
- publish lifecycle events only after successful transaction completion.

---

# 17. Sequence

```text
GUI
 │
 ▼
AnalyzeDocumentCommand
 │
 ▼
CommandBus
 │
 ▼
AnalyzeDocumentCommandHandler
 │
 ▼
AnalysisService
 │
 ├── Build Analysis Plan
 │
 ├── Create Analysis Job
 │
 ├── Queue Analysis
 │
 ▼
JobQueued Event
 │
 ▼
Background Worker
 │
 ▼
Analyze Document
 │
 ▼
DocumentAnalysisCompleted
```

---

# 18. Compliance Checklist

The implementation conforms to this specification only if it:

- creates exactly one Analysis Job;
- performs analysis asynchronously;
- never modifies the Document;
- stores analysis results separately;
- prevents duplicate analysis jobs;
- publishes DocumentAnalysisStarted after successful completion.

---

End of Document