# Voxarium Software Architecture Specification

Document Path:
spec/400_Commands/AnalyzePronunciationCommand.md

Document ID: CMD-052

Title: AnalyzePronunciationCommand

Version: 1.0.0

Status: Accepted

Classification: Normative

Depends On

- Project
- Document
- Fragment
- PronunciationDictionary
- Analysis_Service
- AnalysisJob
- Command_Model
- Command_Bus

Referenced By

- Dictionary_Service
- Analysis_Service
- Workflow_Engine
- User_Interface_Architecture

---

# 1. Purpose

AnalyzePronunciationCommand requests analysis of pronunciation quality within the selected scope.

The command SHALL identify words requiring pronunciation entries.

The command SHALL NOT modify any Pronunciation Dictionary.

---

# 2. Responsibility

Execution SHALL be performed by AnalyzePronunciationCommandHandler.

The handler SHALL create an Analysis Job and submit it to the Analysis Service.

---

# 3. Command Definition

## Name

AnalyzePronunciationCommand

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

### Language

Type

LanguageCode

Default:

AutoDetect

---

### IncludeExistingDictionaryEntries

Type

Boolean

Default:

true

---

### DetectUnknownWords

Type

Boolean

Default:

true

---

### DetectAbbreviations

Type

Boolean

Default:

true

---

### DetectNumbers

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
- no textual content exists;
- Analysis Service is unavailable;
- an equivalent Analysis Job is already running.

Validation SHALL complete before execution begins.

---

# 6. Execution Rules

Execution SHALL:

1. Load the target Aggregate.
2. Collect textual content.
3. Build an Analysis Plan.
4. Create an Analysis Job.
5. Register the Job with the Analysis Service.
6. Publish lifecycle events.

Execution SHALL complete immediately.

Analysis SHALL execute asynchronously.

---

# 7. Analysis Rules

The analysis MAY identify:

- unknown words;
- missing pronunciation entries;
- duplicate dictionary entries;
- inconsistent pronunciations;
- abbreviations;
- numeric expressions;
- foreign-language words;
- ambiguous pronunciation candidates.

The analysis SHALL NOT modify:

- Documents;
- Fragments;
- Dictionaries;
- Voice Profiles;
- Generation Presets.

Analysis SHALL produce recommendations only.

---

# 8. Result

Successful execution SHALL return:

AnalyzePronunciationResult

The result SHALL contain:

- JobId
- Scope
- TargetId
- UnknownWords
- SuggestedDictionaryEntries
- Warnings

---

# 9. Published Events

Successful execution SHALL publish:

- PronunciationAnalysisStarted
- JobQueued

Background execution SHALL additionally publish:

- PronunciationAnalysisCompleted

Upon failure:

- PronunciationAnalysisFailed

---

# 10. Error Conditions

Execution MAY fail with:

- TargetNotFound
- EmptyContent
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

The caller SHALL possess permission to analyze the selected object.

---

# 14. Performance Requirements

Command execution SHOULD complete within 30 milliseconds.

The command SHALL NOT wait for analysis completion.

---

# 15. Thread Safety

Only one active pronunciation analysis MAY exist for the same target.

Independent targets MAY be analyzed concurrently.

---

# 16. AI Implementation Rules

AI-generated implementations SHALL:

- produce recommendations only;
- never modify pronunciation dictionaries;
- never modify Project data;
- execute asynchronously;
- publish lifecycle events only after successful transaction completion.

---

# 17. Sequence

```text
GUI
 │
 ▼
AnalyzePronunciationCommand
 │
 ▼
CommandBus
 │
 ▼
AnalyzePronunciationCommandHandler
 │
 ▼
AnalysisService
 │
 ├── Collect Text
 │
 ├── Analyze Pronunciation
 │
 ├── Create Recommendations
 │
 ▼
JobQueued Event
 │
 ▼
Background Worker
 │
 ▼
PronunciationAnalysisCompleted
```

---

# 18. Compliance Checklist

The implementation conforms to this specification only if it:

- analyzes existing textual content only;
- never modifies pronunciation dictionaries;
- creates exactly one Analysis Job;
- executes asynchronously;
- produces recommendations only;
- publishes PronunciationAnalysisStarted after successful completion.

---

End of Document