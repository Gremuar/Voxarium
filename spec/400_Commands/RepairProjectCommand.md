# Voxarium Software Architecture Specification

Document Path:
spec/400_Commands/RepairProjectCommand.md

Document ID: CMD-063

Title: RepairProjectCommand

Version: 1.0.0

Status: Accepted

Classification: Normative

Depends On

- Project
- Document
- Fragment
- Maintenance_Service
- Repair_Service
- Validation_Service
- Command_Model
- Command_Bus

Referenced By

- Maintenance_Service
- Repair_Service
- Workflow_Engine
- User_Interface_Architecture

---

# 1. Purpose

RepairProjectCommand requests automatic repair of recoverable Project inconsistencies.

The command SHALL restore internal consistency without modifying user-authored content.

The command SHALL NOT perform destructive operations.

---

# 2. Responsibility

Execution SHALL be performed by RepairProjectCommandHandler.

The handler SHALL create a Repair Job and submit it to the Maintenance Service.

---

# 3. Command Definition

## Name

RepairProjectCommand

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

### RepairMode

Type

Enumeration

Allowed values:

- Safe
- Standard
- Aggressive

Default:

Safe

---

### RepairIndexes

Type

Boolean

Default:

true

---

### RepairReferences

Type

Boolean

Default:

true

---

### RepairMetadata

Type

Boolean

Default:

true

---

### RepairTimeline

Type

Boolean

Default:

true

---

### ValidateAfterRepair

Type

Boolean

Default:

true

Performs a full validation after the repair process completes.

---

### DryRun

Type

Boolean

Default:

false

When enabled, the command SHALL report planned repairs without applying them.

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
- Maintenance Service is unavailable;
- Repair Service is unavailable;
- an equivalent Repair Job is already active.

Validation SHALL complete before execution begins.

---

# 6. Execution Rules

Execution SHALL:

1. Load the Project Aggregate.
2. Analyze recoverable inconsistencies.
3. Build a Repair Plan.
4. Create a Repair Job.
5. Register the Job with the Maintenance Service.
6. Publish lifecycle events.

Execution SHALL complete immediately.

Repair SHALL execute asynchronously.

---

# 7. Repair Rules

The repair process MAY:

- rebuild missing indexes;
- restore derived metadata;
- repair broken internal references;
- recreate derived Timeline information;
- remove invalid cache entries;
- regenerate derived internal structures.

The repair process SHALL NOT:

- modify Document text;
- modify Fragment text;
- modify Roles;
- modify Voice Profiles;
- modify Pronunciation Dictionaries;
- delete user-created entities.

When `DryRun` is enabled, no modifications SHALL be applied.

If `ValidateAfterRepair` is enabled, a Project Validation Job SHALL be scheduled after successful completion.

---

# 8. Result

Successful execution SHALL return:

RepairProjectResult

The result SHALL contain:

- JobId
- ProjectId
- RepairMode
- RepairedItems
- RemainingIssues

When `DryRun` is enabled, the result SHALL contain the Repair Plan without applying changes.

---

# 9. Published Events

Successful execution SHALL publish:

- ProjectRepairStarted
- JobQueued

Background execution SHALL additionally publish:

- ProjectRepairCompleted

If post-repair validation is requested:

- ProjectValidationStarted

Upon failure:

- ProjectRepairFailed

---

# 10. Error Conditions

Execution MAY fail with:

- ProjectNotFound
- MaintenanceServiceUnavailable
- RepairServiceUnavailable
- RepairAlreadyRunning
- ValidationFailed
- InternalError

---

# 11. Idempotency

Submitting an identical repair request while an equivalent Repair Job is active SHALL return the existing Job.

Duplicate Repair Jobs SHALL NOT be created.

Repeated execution SHALL repair only inconsistencies still present.

---

# 12. Transaction Requirements

The transaction SHALL include:

- Repair Job creation;
- queue registration.

Repair operations SHALL execute outside the transaction.

---

# 13. Authorization

The caller SHALL possess permission to maintain the Project.

---

# 14. Performance Requirements

Command execution SHOULD complete within 30 milliseconds.

The command SHALL NOT wait for repair completion.

---

# 15. Thread Safety

Only one Repair Job MAY exist for the same Project.

Different Projects MAY be repaired concurrently.

---

# 16. AI Implementation Rules

AI-generated implementations SHALL:

- repair only recoverable inconsistencies;
- never modify user-authored content;
- honor DryRun mode;
- execute asynchronously;
- schedule validation when requested;
- publish lifecycle events only after successful transaction completion.

---

# 17. Sequence

```text
GUI
 │
 ▼
RepairProjectCommand
 │
 ▼
CommandBus
 │
 ▼
RepairProjectCommandHandler
 │
 ▼
MaintenanceService
 │
 ├── Analyze Inconsistencies
 │
 ├── Build Repair Plan
 │
 ├── Create Repair Job
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
Repair Project
 │
 │
 ├── Validate Project (optional)
 │
 ▼
ProjectRepairCompleted
```

---

# 18. Compliance Checklist

The implementation conforms to this specification only if it:

- repairs only recoverable inconsistencies;
- never modifies user-authored content;
- supports DryRun mode;
- optionally performs post-repair validation;
- creates exactly one Repair Job;
- executes asynchronously;
- publishes ProjectRepairStarted after successful completion.

---

End of Document