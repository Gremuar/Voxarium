# Voxarium Software Architecture Specification

Document Path:

spec/400_Commands/DowngradeProjectCommand.md

Document ID: CMD-070

Title: DowngradeProjectCommand

Version: 1.0.0

Status: Accepted

Classification: Normative

Depends On

- Project
- Downgrade_Service
- Migration_Service
- Backup_Service
- Validation_Service
- Command_Model
- Command_Bus

Referenced By

- Downgrade_Service
- Workflow_Engine
- User_Interface_Architecture

---

# 1. Purpose

DowngradeProjectCommand requests conversion of a Project to an earlier supported repository schema.

The command SHALL preserve Project integrity while producing a repository compatible with the requested version.

Downgrade SHALL be permitted only when explicitly supported.

---

# 2. Responsibility

Execution SHALL be performed by DowngradeProjectCommandHandler.

The handler SHALL create a Downgrade Job and submit it to the Downgrade Service.

---

# 3. Command Definition

## Name

DowngradeProjectCommand

## Category

Administration Commands

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

### TargetSchemaVersion

Type

Version

Target repository schema version.

---

## Optional

### CreateBackup

Type

Boolean

Default:

true

---

### ValidateBeforeDowngrade

Type

Boolean

Default:

true

---

### ValidateAfterDowngrade

Type

Boolean

Default:

true

---

### DryRun

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
- target version is unsupported;
- downgrade path does not exist;
- Downgrade Service is unavailable;
- another Downgrade Job is already active.

Validation SHALL complete before execution begins.

---

# 6. Execution Rules

Execution SHALL:

1. Load the Project Aggregate.
2. Verify downgrade compatibility.
3. Build a Downgrade Plan.
4. Create a Downgrade Job.
5. Register the Job.
6. Publish lifecycle events.

Execution SHALL complete immediately.

Downgrade SHALL execute asynchronously.

---

# 7. Downgrade Rules

The downgrade process SHALL:

- preserve user-authored content;
- preserve entity identifiers whenever possible;
- convert metadata to the target schema;
- downgrade internal configuration;
- rebuild derived structures if required.

The downgrade process SHALL NOT:

- silently discard supported data;
- modify Document text;
- modify Fragment text;
- remove Project entities.

When the target schema cannot represent specific data, execution SHALL fail unless an explicit migration rule exists.

When CreateBackup is enabled, a verified backup SHALL be created before downgrade.

When DryRun is enabled, no modifications SHALL be applied.

---

# 8. Result

Successful execution SHALL return:

DowngradeProjectResult

The result SHALL contain:

- JobId
- ProjectId
- SourceSchemaVersion
- TargetSchemaVersion
- DowngradeSummary

---

# 9. Published Events

Successful execution SHALL publish:

- ProjectDowngradeStarted
- JobQueued

Background execution SHALL additionally publish:

- ProjectDowngradeCompleted

If validation is enabled:

- ProjectValidationStarted

Upon failure:

- ProjectDowngradeFailed

---

# 10. Error Conditions

Execution MAY fail with:

- ProjectNotFound
- UnsupportedSchemaVersion
- DowngradeNotSupported
- DowngradeServiceUnavailable
- DowngradeAlreadyRunning
- ValidationFailed
- InternalError

---

# 11. Idempotency

Submitting an identical downgrade request while an equivalent Downgrade Job is active SHALL return the existing Job.

Duplicate Downgrade Jobs SHALL NOT be created.

---

# 12. Transaction Requirements

The transaction SHALL include:

- Downgrade Job creation;
- queue registration.

Downgrade SHALL execute outside the transaction.

Updated repository state SHALL become visible atomically.

---

# 13. Authorization

The caller SHALL possess permission to downgrade Projects.

---

# 14. Performance Requirements

Command execution SHOULD complete within 30 milliseconds.

The command SHALL NOT wait for downgrade completion.

---

# 15. Thread Safety

Only one Downgrade Job MAY exist for the same Project.

Different Projects MAY be downgraded concurrently.

---

# 16. AI Implementation Rules

AI-generated implementations SHALL:

- preserve user-authored content;
- preserve repository consistency;
- support DryRun mode;
- create backups before downgrade when requested;
- execute asynchronously;
- publish lifecycle events only after successful transaction completion.

---

# 17. Sequence

```text
GUI
 │
 ▼
DowngradeProjectCommand
 │
 ▼
CommandBus
 │
 ▼
DowngradeProjectCommandHandler
 │
 ▼
DowngradeService
 │
 ├── Verify Compatibility
 │
 ├── Create Backup (optional)
 │
 ├── Build Downgrade Plan
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
Downgrade Project
 │
 │
 ├── Validate Project
 │
 ▼
ProjectDowngradeCompleted
```

---

# 18. Compliance Checklist

The implementation conforms to this specification only if it:

- downgrades only to supported schema versions;
- preserves repository consistency;
- preserves user-authored content;
- supports DryRun mode;
- optionally creates a backup before downgrade;
- creates exactly one Downgrade Job;
- executes asynchronously;
- publishes ProjectDowngradeStarted after successful completion.

---

End of Document