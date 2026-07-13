# Voxarium Software Architecture Specification

Document Path:
spec/400_Commands/SaveProjectAsCommand.md

Document ID: CMD-005

Title: SaveProjectAsCommand

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

SaveProjectAsCommand requests creation of a new persistent copy of an existing Project.

The original Project SHALL remain unchanged.

The command SHALL preserve Project identity within the current Runtime unless explicitly configured otherwise.

---

# 2. Responsibility

Execution SHALL be performed by SaveProjectAsCommandHandler.

The handler is responsible for creating a complete copy of the Project in a new location.

---

# 3. Command Definition

## Name

SaveProjectAsCommand

## Category

Project Commands

## Layer

Application

---

# 4. Parameters

## Required

### ProjectId

Type

Identifier

Identifier of the Project to copy.

---

### TargetLocation

Type

DirectoryPath

Constraints

- SHALL be absolute.
- SHALL be writable.
- SHALL NOT reference the current Project directory.

---

## Optional

### ProjectName

Type

String

If omitted, the current Project name SHALL be used.

---

### OverwriteExisting

Type

Boolean

Default:

false

If false, execution SHALL fail when the destination already exists.

---

# 5. Validation Rules

Execution SHALL fail if:

- Project is not opened;
- target directory is invalid;
- destination already exists and overwrite is disabled;
- target location is unavailable;
- Project contains invalid state.

---

# 6. Execution Rules

Execution SHALL:

1. Validate Project.
2. Flush pending modifications.
3. Serialize Project.
4. Create destination structure.
5. Write Project files.
6. Verify written data.
7. Register the new Project location.

Execution SHALL be atomic.

---

# 7. Result

Successful execution SHALL return:

SaveProjectAsResult

The result SHALL contain:

- ProjectId
- NewLocation
- WrittenFiles
- WrittenBytes
- Duration

---

# 8. Published Events

Successful execution SHALL publish:

- ProjectSaving
- ProjectSavedAs

Failed execution SHALL publish:

- ProjectSaveFailed

---

# 9. Error Conditions

Execution MAY fail with:

- InvalidDestination
- DestinationAlreadyExists
- StorageUnavailable
- SerializationFailed
- AccessDenied
- ValidationFailed
- InternalError

---

# 10. Idempotency

The command is NOT idempotent.

Repeated execution MAY overwrite previous output only when OverwriteExisting is enabled.

---

# 11. Transaction Requirements

The destination SHALL contain either:

- a complete valid Project, or
- no Project.

Partial copies SHALL NOT remain after failure.

---

# 12. Authorization

The caller SHALL possess permission to write to the destination.

---

# 13. Performance Requirements

Large Projects SHOULD provide progress reporting.

Cancellation SHALL leave the destination in a recoverable state.

---

# 14. Thread Safety

Only one SaveProjectAs operation SHALL execute for a Project simultaneously.

---

# 15. AI Implementation Rules

AI-generated implementations SHALL:

- preserve Project consistency;
- verify copied data before completion;
- avoid modifying the source Project;
- clean incomplete output after failure;
- publish events only after successful completion.

---

# 16. Sequence

```text
GUI
 │
 ▼
SaveProjectAsCommand
 │
 ▼
CommandBus
 │
 ▼
SaveProjectAsCommandHandler
 │
 ▼
ProjectService
 │
 ▼
Serializer
 │
 ▼
Destination Storage
 │
 ▼
Verification
 │
 ▼
ProjectSavedAs Event
```

---

# 17. Compliance Checklist

The implementation conforms to this specification only if it:

- creates a complete Project copy;
- preserves source Project integrity;
- validates the destination;
- verifies written data;
- removes incomplete output after failure;
- publishes ProjectSavedAs after successful completion.

---

End of Document