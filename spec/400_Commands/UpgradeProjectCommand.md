# Voxarium Software Architecture Specification

Document Path:

spec/400_Commands/UpgradeProjectCommand.md

Document ID: CMD-069

Title: UpgradeProjectCommand

Version: 1.0.0

Status: Accepted

Classification: Normative

Depends On

- Project
- Upgrade_Service
- Migration_Service
- Validation_Service
- Backup_Service
- Command_Model
- Command_Bus

Referenced By

- Upgrade_Service
- Workflow_Engine
- User_Interface_Architecture

---

# 1. Purpose

UpgradeProjectCommand requests upgrading a Project to the current application version.

The command SHALL coordinate all required upgrade operations.

The command SHALL preserve Project integrity.

---

# 2. Responsibility

Execution SHALL be performed by UpgradeProjectCommandHandler.

The handler SHALL create an Upgrade Job and submit it to the Upgrade Service.

---

# 3. Command Definition

## Name

UpgradeProjectCommand

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

## Optional

### TargetApplicationVersion

Type

Version

Default:

Latest

---

### CreateBackup

Type

Boolean

Default:

true

---

### ValidateBeforeUpgrade

Type

Boolean

Default:

true

---

### ValidateAfterUpgrade

Type

Boolean

Default:

true

---

### UpgradeSchema

Type

Boolean

Default:

true

---

### UpgradeIndexes

Type

Boolean

Default:

true

---

### UpgradeMetadata

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
- Upgrade Service is unavailable;
- current Project version is unsupported;
- another Upgrade Job is already active.

Validation SHALL complete before execution begins.

---

# 6. Execution Rules

Execution SHALL:

1. Load the Project Aggregate.
2. Determine upgrade path.
3. Create an Upgrade Plan.
4. Create an Upgrade Job.
5. Register the Job.
6. Publish lifecycle events.

Execution SHALL complete immediately.

Upgrade SHALL execute asynchronously.

---

# 7. Upgrade Rules

The upgrade process SHALL:

- migrate repository schema;
- update derived metadata;
- rebuild indexes when required;
- upgrade internal configuration;
- preserve all user-authored content;
- preserve Project identifiers.

The upgrade process SHALL NOT:

- delete user entities;
- modify Document text;
- modify Fragment text;
- remove supported configuration.

When CreateBackup is enabled a verified backup SHALL be created before any modification.

When DryRun is enabled no modifications SHALL be performed.

---

# 8. Result

Successful execution SHALL return:

UpgradeProjectResult

The result SHALL contain:

- JobId
- ProjectId
- PreviousVersion
- CurrentVersion
- UpgradeSummary

---

# 9. Published Events

Successful execution SHALL publish:

- ProjectUpgradeStarted
- JobQueued

Background execution SHALL additionally publish:

- ProjectUpgradeCompleted

If validation is enabled:

- ProjectValidationStarted

Upon failure:

- ProjectUpgradeFailed

---

# 10. Error Conditions

Execution MAY fail with:

- ProjectNotFound
- UnsupportedProjectVersion
- UpgradeServiceUnavailable
- UpgradeAlreadyRunning
- ValidationFailed
- InternalError

---

# 11. Idempotency

Submitting an identical upgrade request while an equivalent Upgrade Job is active SHALL return the existing Job.

Duplicate Upgrade Jobs SHALL NOT be created.

---

# 12. Transaction Requirements

The transaction SHALL include:

- Upgrade Job creation;
- queue registration.

Upgrade execution SHALL occur outside the transaction.

The upgraded Project SHALL become visible atomically.

---

# 13. Authorization

The caller SHALL possess permission to upgrade Projects.

---

# 14. Performance Requirements

Command execution SHOULD complete within 30 milliseconds.

The command SHALL NOT wait for upgrade completion.

---

# 15. Thread Safety

Only one Upgrade Job MAY exist for the same Project.

Different Projects MAY be upgraded concurrently.

---

# 16. AI Implementation Rules

AI-generated implementations SHALL:

- preserve user-authored content;
- preserve Project identifiers;
- support DryRun mode;
- create backups before modification when requested;
- execute asynchronously;
- publish lifecycle events only after successful transaction completion.

---

# 17. Sequence

```text
GUI
 │
 ▼
UpgradeProjectCommand
 │
 ▼
CommandBus
 │
 ▼
UpgradeProjectCommandHandler
 │
 ▼
UpgradeService
 │
 ├── Determine Upgrade Path
 │
 ├── Create Backup (optional)
 │
 ├── Build Upgrade Plan
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
Upgrade Project
 │
 │
 ├── Validate Project
 │
 ▼
ProjectUpgradeCompleted
```

---

# 18. Compliance Checklist

The implementation conforms to this specification only if it:

- upgrades Projects to the current application version;
- preserves user-authored content;
- preserves identifiers;
- supports DryRun mode;
- optionally creates a backup;
- creates exactly one Upgrade Job;
- executes asynchronously;
- publishes ProjectUpgradeStarted after successful completion.

---

End of Document