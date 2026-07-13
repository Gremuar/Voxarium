# Voxarium Software Architecture Specification

Document Path:
spec/400_Commands/CreateProjectCommand.md

Document ID: CMD-001

Title: CreateProjectCommand

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
- Project_Service
- User_Interface_Architecture

---

# 1. Purpose

CreateProjectCommand requests creation of a new Project.

The command SHALL describe the user's intent only.

The command SHALL NOT contain business logic.

---

# 2. Responsibility

The command is responsible for requesting creation of a Project and providing all information required for its initialization.

Execution SHALL be performed by CreateProjectCommandHandler.

---

# 3. Command Definition

## Name

CreateProjectCommand

## Category

Project Commands

## Layer

Application

---

# 4. Parameters

## Required

### Name

Type

String

Constraints

- SHALL NOT be empty.
- SHALL be trimmed.
- Maximum length SHALL be 256 Unicode characters.

---

### Location

Type

DirectoryPath

Constraints

- SHALL be writable.
- SHALL be absolute.
- SHALL exist or be creatable.

---

## Optional

### Description

Type

String

Maximum length: 4096 characters.

---

### TemplateId

Type

Identifier

Specifies the project template to use during initialization.

---

### InitialSettings

Type

ProjectSettings

Initial project configuration.

---

# 5. Validation Rules

The command SHALL be rejected if:

- Name is empty.
- Name contains invalid filesystem characters.
- Location is unavailable.
- Project already exists at the specified location.
- TemplateId is unknown.

Validation SHALL occur before execution.

---

# 6. Execution Rules

Execution SHALL:

1. Validate parameters.
2. Create a Project aggregate.
3. Initialize default Project structure.
4. Persist the Project.
5. Publish lifecycle events.
6. Return the Project identifier.

Execution SHALL be atomic.

---

# 7. Result

Successful execution SHALL return:

ProjectId

The returned identifier SHALL uniquely identify the created Project.

---

# 8. Published Events

Successful execution SHALL publish:

- ProjectCreated

Subsequent initialization MAY publish:

- ProjectOpened
- ProjectInitialized

Failed execution SHALL NOT publish events.

---

# 9. Error Conditions

Execution MAY fail with:

- ValidationFailed
- ProjectAlreadyExists
- InvalidTemplate
- AccessDenied
- StorageUnavailable
- InternalError

---

# 10. Idempotency

The command is NOT idempotent.

Submitting the command multiple times SHALL create multiple Projects unless prevented by validation.

---

# 11. Transaction Requirements

The entire operation SHALL execute within a single Application transaction.

No partial Project SHALL remain after failure.

---

# 12. Authorization

The caller SHALL possess permission to create Projects.

Permission validation SHALL occur before execution.

---

# 13. Performance Requirements

Project creation SHOULD complete within one second under normal operating conditions.

Long-running initialization SHALL execute asynchronously.

---

# 14. Thread Safety

Concurrent creation of different Projects MAY execute simultaneously.

Concurrent creation targeting the same location SHALL be serialized.

---

# 15. AI Implementation Rules

AI-generated implementations SHALL:

- implement the command as an immutable object;
- perform no business logic inside the command;
- delegate execution to CreateProjectCommandHandler;
- preserve transactional consistency;
- publish events only after successful commit.

---

# 16. Sequence

```text
GUI
 │
 ▼
CreateProjectCommand
 │
 ▼
CommandBus
 │
 ▼
CreateProjectCommandHandler
 │
 ▼
ProjectService
 │
 ▼
Domain
 │
 ▼
Repository
 │
 ▼
ProjectCreated Event
```

---

# 17. Compliance Checklist

The command conforms to this specification only if it:

- is immutable;
- contains no business logic;
- is validated before execution;
- executes atomically;
- returns ProjectId;
- publishes ProjectCreated upon success.

---

End of Document