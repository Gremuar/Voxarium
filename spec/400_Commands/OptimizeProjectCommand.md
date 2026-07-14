# Voxarium Software Architecture Specification

Document Path:
spec/400_Commands/OptimizeProjectCommand.md

Document ID: CMD-060

Title: OptimizeProjectCommand

Version: 1.0.0

Status: Accepted

Classification: Normative

Depends On

- Project
- Document
- Fragment
- AudioAsset
- Maintenance_Service
- Optimization_Service
- Command_Model
- Command_Bus

Referenced By

- Maintenance_Service
- Optimization_Service
- Workflow_Engine
- User_Interface_Architecture

---

# 1. Purpose

OptimizeProjectCommand requests optimization of Project resources to improve storage efficiency and runtime performance.

The command SHALL optimize derived artifacts and internal storage structures.

The command SHALL NOT modify business data.

---

# 2. Responsibility

Execution SHALL be performed by OptimizeProjectCommandHandler.

The handler SHALL create an Optimization Job and submit it to the Maintenance Service.

---

# 3. Command Definition

## Name

OptimizeProjectCommand

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

### OptimizationMode

Type

Enumeration

Allowed values:

- Quick
- Standard
- Full

Default:

Standard

---

### OptimizeIndexes

Type

Boolean

Default:

true

---

### OptimizeStorage

Type

Boolean

Default:

true

---

### RemoveUnusedArtifacts

Type

Boolean

Default:

false

---

### CompactMetadata

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
- Maintenance Service is unavailable;
- an equivalent Optimization Job is already active.

Validation SHALL complete before execution begins.

---

# 6. Execution Rules

Execution SHALL:

1. Load the Project Aggregate.
2. Build an Optimization Plan.
3. Create an Optimization Job.
4. Register the job with the Maintenance Service.
5. Publish lifecycle events.

Execution SHALL complete immediately.

Optimization SHALL execute asynchronously.

---

# 7. Optimization Rules

The optimization process MAY include:

- rebuilding internal caches;
- compacting metadata;
- optimizing indexes;
- reclaiming unused storage;
- removing orphaned temporary artifacts;
- reorganizing internal storage structures.

Optimization SHALL NOT modify:

- Project;
- Document;
- Fragment;
- Role;
- VoiceProfile;
- GenerationPreset;
- PronunciationDictionary.

Generated audio SHALL NOT be regenerated.

User content SHALL NOT be altered.

---

# 8. Result

Successful execution SHALL return:

OptimizeProjectResult

The result SHALL contain:

- JobId
- ProjectId
- OptimizationMode

---

# 9. Published Events

Successful execution SHALL publish:

- ProjectOptimizationStarted
- JobQueued

Background execution SHALL additionally publish:

- ProjectOptimizationCompleted

Upon failure:

- ProjectOptimizationFailed

---

# 10. Error Conditions

Execution MAY fail with:

- ProjectNotFound
- MaintenanceServiceUnavailable
- OptimizationAlreadyRunning
- ValidationFailed
- InternalError

---

# 11. Idempotency

Submitting an identical optimization request while an equivalent Optimization Job is active SHALL return the existing Job.

Duplicate Optimization Jobs SHALL NOT be created.

---

# 12. Transaction Requirements

The transaction SHALL include:

- Optimization Job creation;
- queue registration.

Optimization SHALL execute outside the transaction.

---

# 13. Authorization

The caller SHALL possess permission to maintain the Project.

---

# 14. Performance Requirements

Command execution SHOULD complete within 30 milliseconds.

The command SHALL NOT wait for optimization completion.

---

# 15. Thread Safety

Only one Optimization Job MAY exist for the same Project.

Different Projects MAY be optimized concurrently.

---

# 16. AI Implementation Rules

AI-generated implementations SHALL:

- optimize only derived artifacts and internal structures;
- never modify business entities;
- preserve all user content;
- execute asynchronously;
- publish lifecycle events only after successful transaction completion.

---

# 17. Sequence

```text
GUI
 │
 ▼
OptimizeProjectCommand
 │
 ▼
CommandBus
 │
 ▼
OptimizeProjectCommandHandler
 │
 ▼
MaintenanceService
 │
 ├── Build Optimization Plan
 │
 ├── Create Optimization Job
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
Optimize Storage
 │
 ▼
Compact Metadata
 │
 ▼
ProjectOptimizationCompleted
```

---

# 18. Compliance Checklist

The implementation conforms to this specification only if it:

- optimizes only derived artifacts and internal structures;
- never modifies business entities;
- preserves all user content;
- creates exactly one Optimization Job;
- executes asynchronously;
- publishes ProjectOptimizationStarted after successful completion.

---

End of Document