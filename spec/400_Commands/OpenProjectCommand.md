# Voxarium Software Architecture Specification

Document Path:
spec/400_Commands/OpenProjectCommand.md

Document ID: CMD-002

Title: OpenProjectCommand

Version: 1.0.0

Status: Accepted

Classification: Normative

Depends On

- Project
- Project_Service
- Command_Model
- Command_Bus

Referenced By

- Workflow_Engine
- Use_Case_Handler
- User_Interface_Architecture

---

# 1. Purpose

OpenProjectCommand requests opening an existing Project.

The command SHALL describe the user's intent to open a Project.

The command SHALL NOT contain business logic.

---

# 2. Responsibility

The command requests loading of a Project into the active application session.

Execution SHALL be performed by OpenProjectCommandHandler.

---

# 3. Command Definition

## Name

OpenProjectCommand

## Category

Project Commands

## Layer

Application

---

# 4. Parameters

## Required

### ProjectLocation

Type

DirectoryPath

Constraints

- SHALL be an absolute path.
- SHALL exist.
- SHALL reference a valid Voxarium Project.

---

## Optional

### OpenMode

Type

Enumeration

Allowed values:

- Normal
- ReadOnly
- Recovery

Default:

Normal

---

### ValidateProject

Type

Boolean

Default:

true

When enabled, the project SHALL be validated before opening.

---

# 5. Validation Rules

The command SHALL fail if:

- the directory does not exist;
- the directory is inaccessible;
- the project manifest is missing;
- the project version is unsupported;
- validation detects unrecoverable corruption.

---

# 6. Execution Rules

Execution SHALL:

1. Verify project existence.
2. Validate project format.
3. Load project metadata.
4. Restore project structure.
5. Restore runtime indexes.
6. Restore generation state.
7. Restore workflow state.
8. Register the Project as active.

Execution SHALL be atomic.

---

# 7. Result

Successful execution SHALL return:

ProjectId

The returned identifier SHALL reference the active Project.

---

# 8. Published Events

Successful execution SHALL publish:

- ProjectOpening
- ProjectOpened

If project migration is required:

- ProjectMigrationStarted
- ProjectMigrationCompleted

Failed execution SHALL NOT publish ProjectOpened.

---

# 9. Error Conditions

Execution MAY fail with:

- ProjectNotFound
- InvalidProjectFormat
- UnsupportedProjectVersion
- ProjectCorrupted
- AccessDenied
- StorageUnavailable
- MigrationFailed
- InternalError

---

# 10. Idempotency

Opening an already opened Project SHALL return the existing active Project unless explicit reload is requested.

Repeated execution SHALL NOT duplicate application state.

---

# 11. Transaction Requirements

Project activation SHALL occur only after successful loading.

Incomplete loading SHALL leave no partially initialized runtime state.

---

# 12. Authorization

The caller SHALL possess permission to open the requested Project.

---

# 13. Performance Requirements

Metadata loading SHOULD complete within one second.

Large Projects MAY continue background indexing after opening.

The user interface SHALL become responsive before background indexing is completed.

---

# 14. Thread Safety

Only one instance of the same Project MAY be opened within a single Application Runtime.

Different Projects MAY be opened concurrently by independent Runtime instances.

---

# 15. AI Implementation Rules

AI-generated implementations SHALL:

- separate loading from validation;
- restore runtime state after loading the Domain Model;
- initialize indexes asynchronously where possible;
- avoid loading unnecessary assets during startup;
- publish lifecycle events only after successful initialization.

---

# 16. Sequence

```text
GUI
 │
 ▼
OpenProjectCommand
 │
 ▼
CommandBus
 │
 ▼
OpenProjectCommandHandler
 │
 ▼
ProjectService
 │
 ▼
Project Repository
 │
 ▼
Runtime Initialization
 │
 ▼
ProjectOpened Event
```

---

# 17. Compliance Checklist

The command conforms to this specification only if it:

- validates the Project before activation;
- restores runtime state;
- initializes background services;
- returns the active Project identifier;
- publishes ProjectOpened after successful initialization;
- leaves no partial runtime state after failure.

---

End of Document