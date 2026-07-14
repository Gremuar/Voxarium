# Voxarium Software Architecture Specification

Document Path:
spec/400_Commands/AnalyzeTimelineCommand.md

Document ID: CMD-055

Title: AnalyzeTimelineCommand

Version: 1.0.0

Status: Accepted

Classification: Normative

Depends On

- Project
- Document
- Fragment
- Timeline
- SpeechSegment
- Analysis_Service
- AnalysisJob
- Command_Model
- Command_Bus

Referenced By

- Timeline_Service
- Analysis_Service
- Generation_Service
- Workflow_Engine

---

# 1. Purpose

AnalyzeTimelineCommand evaluates the temporal consistency of Timeline data.

The command SHALL identify timing anomalies that may affect playback or subtitle generation.

The command SHALL NOT modify Timeline data.

---

# 2. Responsibility

Execution SHALL be performed by AnalyzeTimelineCommandHandler.

The handler SHALL create an Analysis Job and submit it to the Analysis Service.

---

# 3. Command Definition

## Name

AnalyzeTimelineCommand

## Category

Analysis Commands

## Layer

Application

---

# 4. Parameters

## Required

### Scope

Type

Enumeration

Allowed values:

- Document
- Project

---

### TargetId

Type

Identifier

Identifier corresponding to the selected Scope.

---

## Optional

### ValidateSpeechSegments

Type

Boolean

Default:

true

---

### ValidateFragmentOrder

Type

Boolean

Default:

true

---

### DetectOverlaps

Type

Boolean

Default:

true

---

### DetectGaps

Type

Boolean

Default:

true

---

### ValidateDurations

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

- the target object does not exist;
- no Timeline data is available;
- Analysis Service is unavailable;
- an equivalent Analysis Job is already active.

Validation SHALL complete before execution begins.

---

# 6. Execution Rules

Execution SHALL:

1. Load the target Aggregate.
2. Collect Timeline information.
3. Build an Analysis Plan.
4. Create an Analysis Job.
5. Register the Job with the Analysis Service.
6. Publish lifecycle events.

Execution SHALL complete immediately.

Timeline analysis SHALL execute asynchronously.

---

# 7. Analysis Rules

The analysis SHALL verify:

- chronological ordering;
- Fragment ordering;
- SpeechSegment continuity;
- overlapping segments;
- missing timing intervals;
- invalid durations;
- zero-length segments;
- orphan Timeline entries.

The analysis SHALL classify findings as:

- Error
- Warning
- Information

The command SHALL NOT modify Timeline data.

---

# 8. Result

Successful execution SHALL return:

AnalyzeTimelineResult

The result SHALL contain:

- JobId
- Scope
- TargetId
- Errors
- Warnings
- Information

---

# 9. Published Events

Successful execution SHALL publish:

- TimelineAnalysisStarted
- JobQueued

Background execution SHALL additionally publish:

- TimelineAnalysisCompleted

Upon failure:

- TimelineAnalysisFailed

---

# 10. Error Conditions

Execution MAY fail with:

- TargetNotFound
- TimelineNotAvailable
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

Timeline analysis SHALL execute outside the transaction.

---

# 13. Authorization

The caller SHALL possess permission to analyze the selected object.

---

# 14. Performance Requirements

Command execution SHOULD complete within 30 milliseconds.

The command SHALL NOT wait for analysis completion.

---

# 15. Thread Safety

Only one Timeline Analysis Job MAY exist for the same target.

Independent targets MAY be analyzed concurrently.

---

# 16. AI Implementation Rules

AI-generated implementations SHALL:

- analyze persisted Timeline data only;
- never modify Timeline objects;
- classify findings as Errors, Warnings and Information;
- execute asynchronously;
- publish lifecycle events only after successful transaction completion.

---

# 17. Sequence

```text
GUI
 │
 ▼
AnalyzeTimelineCommand
 │
 ▼
CommandBus
 │
 ▼
AnalyzeTimelineCommandHandler
 │
 ▼
AnalysisService
 │
 ├── Load Timeline
 │
 ├── Validate Ordering
 │
 ├── Detect Overlaps
 │
 ├── Detect Gaps
 │
 ├── Validate Durations
 │
 ▼
JobQueued Event
 │
 ▼
Background Worker
 │
 ▼
Generate Timeline Report
 │
 ▼
TimelineAnalysisCompleted
```

---

# 18. Compliance Checklist

The implementation conforms to this specification only if it:

- validates chronological ordering;
- detects overlaps and gaps;
- validates durations;
- never modifies Timeline data;
- creates exactly one Analysis Job;
- executes asynchronously;
- publishes TimelineAnalysisStarted after successful completion.

---

End of Document