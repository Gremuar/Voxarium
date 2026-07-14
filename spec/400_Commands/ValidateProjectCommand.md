# Voxarium Software Architecture Specification

Document Path:
spec/400_Commands/ValidateProjectCommand.md

Document ID: CMD-061

Title: ValidateProjectCommand

Version: 1.0.0

Status: Accepted

Classification: Normative

Depends On

- Project
- Document
- Fragment
- Validation_Service
- ValidationJob
- Command_Model
- Command_Bus

Referenced By

- Validation_Service
- Workflow_Engine
- Maintenance_Service
- User_Interface_Architecture

---

# 1. Purpose

ValidateProjectCommand requests complete validation of a Project.

The command SHALL verify structural, semantic and configuration integrity.

The command SHALL NOT modify Project data.

---

# 2. Responsibility

Execution SHALL be performed by ValidateProjectCommandHandler.

The handler SHALL create a Validation Job and submit it to the Validation Service.

---

# 3. Command Definition

## Name

ValidateProjectCommand

## Category

Maintenance Commands

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

### ValidationLevel

Type

Enumeration

Allowed values:

- Quick
- Standard
- Full

Default:

Standard

---

### ValidateDocuments

Type

Boolean

Default:

true

---

### ValidateFragments

Type

Boolean

Default:

true

---

### ValidateConfiguration

Type

Boolean

Default:

true

---

### ValidateAssets

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

- Project does not exist;
- Validation Service is unavailable;
- another Validation Job for the Project is already active.

Validation SHALL complete before execution begins.

---

# 6. Execution Rules

Execution SHALL:

1. Load the Project Aggregate.
2. Build a Validation Plan.
3. Create a Validation Job.
4. Register the Job with the Validation Service.
5. Publish lifecycle events.

Execution SHALL complete immediately.

Validation SHALL execute asynchronously.

---

# 7. Validation Scope

The validation process SHALL verify:

- Project structure;
- Document hierarchy;
- Fragment ordering;
- missing references;
- invalid identifiers;
- orphan entities;
- Role assignments;
- Voice Profile assignments;
- Generation Presets;
- Pronunciation Dictionaries;
- Asset consistency;
- Timeline integrity.

Validation SHALL classify findings as:

- Error
- Warning
- Information

Validation SHALL NOT modify persisted Project data.

---

# 8. Result

Successful execution SHALL return:

ValidateProjectResult

The result SHALL contain:

- JobId
- ProjectId
- ValidationLevel
- Errors
- Warnings
- Information

---

# 9. Published Events

Successful execution SHALL publish:

- ProjectValidationStarted
- JobQueued

Background execution SHALL additionally publish:

- ProjectValidationCompleted

Upon failure:

- ProjectValidationFailed

---

# 10. Error Conditions

Execution MAY fail with:

- ProjectNotFound
- ValidationServiceUnavailable
- ValidationAlreadyRunning
- ValidationFailed
- InternalError

---

# 11. Idempotency

Submitting an identical validation request while an equivalent Validation Job is active SHALL return the existing Job.

Duplicate Validation Jobs SHALL NOT be created.

---

# 12. Transaction Requirements

The transaction SHALL include:

- Validation Job creation;
- queue registration.

Validation SHALL execute outside the transaction.

---

# 13. Authorization

The caller SHALL possess permission to validate the Project.

---

# 14. Performance Requirements

Command execution SHOULD complete within 30 milliseconds.

The command SHALL NOT wait for validation completion.

---

# 15. Thread Safety

Only one Validation Job MAY exist for the same Project.

Different Projects MAY be validated concurrently.

---

# 16. AI Implementation Rules

AI-generated implementations SHALL:

- validate persisted Project data only;
- never modify Project entities;
- classify findings as Errors, Warnings and Information;
- execute asynchronously;
- publish lifecycle events only after successful transaction completion.

---

# 17. Sequence

```text
GUI
 │
 ▼
ValidateProjectCommand
 │
 ▼
CommandBus
 │
 ▼
ValidateProjectCommandHandler
 │
 ▼
ValidationService
 │
 ├── Build Validation Plan
 │
 ├── Create Validation Job
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
Validate Project
 │
 ▼
ProjectValidationCompleted
```

---

# 18. Compliance Checklist

The implementation conforms to this specification only if it:

- validates all Project entities;
- validates references and configuration;
- never modifies Project data;
- creates exactly one Validation Job;
- executes asynchronously;
- publishes ProjectValidationStarted after successful completion.

---

End of Document