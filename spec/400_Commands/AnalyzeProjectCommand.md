# Voxarium Software Architecture Specification

Document Path:
spec/400_Commands/AnalyzeProjectCommand.md

Document ID: CMD-051

Title: AnalyzeProjectCommand

Version: 1.0.0

Status: Accepted

Classification: Normative

Depends On

- Project
- Document
- Fragment
- Analysis_Service
- AnalysisJob
- Command_Model
- Command_Bus

Referenced By

- Workflow_Engine
- Analysis_Service
- Project_Service
- User_Interface_Architecture

---

# 1. Purpose

AnalyzeProjectCommand requests comprehensive analysis of an entire Project.

The command SHALL analyze all eligible Documents within the Project.

The command SHALL NOT modify Project data.

---

# 2. Responsibility

Execution SHALL be performed by AnalyzeProjectCommandHandler.

The handler SHALL prepare an Analysis Job covering the requested Project.

---

# 3. Command Definition

## Name

AnalyzeProjectCommand

## Category

Analysis Commands

## Layer

Application

---

# 4. Parameters

## Required

### ProjectId

Type

Identifier

Identifier of the Project.

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
- Consistency
- Full

Default:

Full

---

### IncludeStatistics

Type

Boolean

Default:

true

---

### ForceReanalysis

Type

Boolean

Default:

false

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

- Project does not exist;
- Project contains no Documents;
- Analysis Service is unavailable;
- an equivalent Analysis Job is already active.

Validation SHALL complete before execution begins.

---

# 6. Execution Rules

Execution SHALL:

1. Load the Project Aggregate.
2. Discover eligible Documents.
3. Build an Analysis Plan.
4. Create an Analysis Job.
5. Register the Job with the Analysis Service.
6. Publish lifecycle events.

Execution SHALL complete immediately.

Analysis SHALL execute asynchronously.

---

# 7. Analysis Rules

Project analysis MAY include:

- Project structure;
- Document consistency;
- Fragment consistency;
- speaker consistency;
- pronunciation coverage;
- language consistency;
- duplicate content;
- missing assignments;
- generation readiness.

The analysis SHALL NOT modify Project data.

Analysis results SHALL be stored independently from Project Aggregates.

---

# 8. Result

Successful execution SHALL return:

AnalyzeProjectResult

The result SHALL contain:

- JobId
- ProjectId
- DocumentsAnalyzed
- AnalysisScope

---

# 9. Published Events

Successful execution SHALL publish:

- ProjectAnalysisStarted
- JobQueued

Background execution SHALL additionally publish:

- ProjectAnalysisProgressChanged
- ProjectAnalysisCompleted

Upon failure:

- ProjectAnalysisFailed

---

# 10. Error Conditions

Execution MAY fail with:

- ProjectNotFound
- EmptyProject
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

The caller SHALL possess permission to analyze the Project.

---

# 14. Performance Requirements

Command execution SHOULD complete within 50 milliseconds.

The command SHALL NOT wait for analysis completion.

---

# 15. Thread Safety

Only one active Analysis Job MAY exist for the same Project.

Independent Projects MAY be analyzed concurrently.

---

# 16. AI Implementation Rules

AI-generated implementations SHALL:

- analyze only persisted Project data;
- never modify Project state during analysis;
- create exactly one Analysis Job;
- execute asynchronously;
- publish lifecycle events only after successful transaction completion.

---

# 17. Sequence

```text
GUI
 │
 ▼
AnalyzeProjectCommand
 │
 ▼
CommandBus
 │
 ▼
AnalyzeProjectCommandHandler
 │
 ▼
AnalysisService
 │
 ├── Discover Documents
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
Background Workers
 │
 ▼
Analyze Project
 │
 ▼
ProjectAnalysisCompleted
```

---

# 18. Compliance Checklist

The implementation conforms to this specification only if it:

- analyzes the complete Project;
- creates exactly one Analysis Job;
- executes asynchronously;
- never modifies Project data;
- stores analysis results separately;
- publishes ProjectAnalysisStarted after successful completion.

---

End of Document
```