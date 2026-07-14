# Voxarium Software Architecture Specification

Document Path:

spec/400_Commands/MigrateProjectCommand.md

Document ID: CMD-068

Title: MigrateProjectCommand

Version: 1.0.0

Status: Accepted

Classification: Normative

Depends On

- Project
- Migration_Service
- Validation_Service
- Storage_Service
- Command_Model
- Command_Bus

Referenced By

- Migration_Service
- Upgrade_Service
- Workflow_Engine
- User_Interface_Architecture

---

# 1. Purpose

MigrateProjectCommand requests migration of a Project from one schema version to another.

The command SHALL upgrade persisted Project data while preserving semantic equivalence.

Migration SHALL preserve repository consistency throughout the process.

---

# 2. Responsibility

Execution SHALL be performed by MigrateProjectCommandHandler.

The handler SHALL create a Migration Job and submit it to the Migration Service.

---

# 3. Command Definition

## Name

MigrateProjectCommand

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

### ValidateBeforeMigration

Type

Boolean

Default:

true

---

### ValidateAfterMigration

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

When enabled, the migration SHALL be analyzed without modifying persisted data.

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
- target schema version is unsupported;
- Migration Service is unavailable;
- another Migration Job for the same Project is already active.

Validation SHALL complete before execution begins.

---

# 6. Execution Rules

Execution SHALL:

1. Load the Project Aggregate.
2. Verify schema compatibility.
3. Build a Migration Plan.
4. Create a Migration Job.
5. Register the Job with the Migration Service.
6. Publish lifecycle events.

Execution SHALL complete immediately.

Migration SHALL execute asynchronously.

---

# 7. Migration Rules

Migration SHALL:

- preserve Project identifiers;
- preserve Document identifiers;
- preserve Fragment identifiers;
- preserve semantic meaning of all entities;
- migrate metadata;
- migrate configuration;
- migrate Timeline information;
- migrate Generation Presets;
- migrate Pronunciation Dictionaries.

Migration SHALL NOT:

- modify user-authored text;
- remove supported entities;
- lose references;
- introduce duplicate identifiers.

When `DryRun` is enabled, the Migration Plan SHALL be generated without applying changes.

When `CreateBackup` is enabled, a complete backup SHALL be created before migration begins.

If `ValidateAfterMigration` is enabled, a Validation Job SHALL be scheduled after successful migration.

---

# 8. Result

Successful execution SHALL return:

MigrateProjectResult

The result SHALL contain:

- JobId
- ProjectId
- SourceSchemaVersion
- TargetSchemaVersion
- MigratedObjects

---

# 9. Published Events

Successful execution SHALL publish:

- ProjectMigrationStarted
- JobQueued

Background execution SHALL additionally publish:

- ProjectMigrationCompleted

If validation is enabled:

- ProjectValidationStarted

Upon failure:

- ProjectMigrationFailed

---

# 10. Error Conditions

Execution MAY fail with:

- ProjectNotFound
- UnsupportedSchemaVersion
- MigrationServiceUnavailable
- MigrationAlreadyRunning
- ValidationFailed
- InternalError

---

# 11. Idempotency

Submitting an identical migration request while an equivalent Migration Job is active SHALL return the existing Job.

Duplicate Migration Jobs SHALL NOT be created.

---

# 12. Transaction Requirements

The transaction SHALL include:

- Migration Job creation;
- queue registration.

Migration SHALL execute outside the transaction.

Migrated Project state SHALL become visible atomically.

---

# 13. Authorization

The caller SHALL possess permission to migrate Projects.

---

# 14. Performance Requirements

Command execution SHOULD complete within 30 milliseconds.

The command SHALL NOT wait for migration completion.

---

# 15. Thread Safety

Only one Migration Job MAY exist for the same Project.

Different Projects MAY be migrated concurrently.

---

# 16. AI Implementation Rules

AI-generated implementations SHALL:

- preserve semantic equivalence of Project data;
- never modify user-authored content;
- support DryRun mode;
- create backups before migration when requested;
- execute asynchronously;
- publish lifecycle events only after successful transaction completion.

---

# 17. Sequence

```text
GUI
 │
 ▼
MigrateProjectCommand
 │
 ▼
CommandBus
 │
 ▼
MigrateProjectCommandHandler
 │
 ▼
MigrationService
 │
 ├── Verify Schema
 │
 ├── Build Migration Plan
 │
 ├── Create Backup (optional)
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
Migrate Project
 │
 │
 ├── Validate Project (optional)
 │
 ▼
ProjectMigrationCompleted
```

---

# 18. Compliance Checklist

The implementation conforms to this specification only if it:

- preserves semantic equivalence;
- never modifies user-authored content;
- preserves entity identifiers whenever possible;
- supports DryRun mode;
- optionally creates a backup before migration;
- creates exactly one Migration Job;
- executes asynchronously;
- publishes ProjectMigrationStarted after successful completion.

---

End of Document