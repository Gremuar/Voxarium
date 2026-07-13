# Voxarium Software Architecture Specification

Document Path:
spec/300_Contracts/ISourceService.md

Document ID: CTR-014

Title: ISourceService

Version: 1.0.0

Status: Accepted

Classification: Normative

Category: Application Service Contract

Depends On

- CTR-000 IService
- Source
- Project
- Asset

Referenced By

- Project_Service
- Import_Service
- Workflow_Engine
- User_Interface_Architecture

---

# 1. Purpose

ISourceService defines the public Application Service contract for managing Source objects.

A Source represents an external or internal source of project content.

The service is responsible for the lifecycle of Source entities only.

---

# 2. Responsibilities

The service SHALL provide:

- creation of sources;
- registration of external sources;
- modification of source metadata;
- source validation;
- source attachment to projects;
- source detachment;
- source removal.

---

# 3. Non-Responsibilities

The service SHALL NOT:

- import documents;
- parse source content;
- generate speech;
- modify Documents;
- modify Timeline.

---

# 4. Lifecycle Operations

## 4.1 CreateSource

### Signature

CreateSource(ProjectId, SourceDefinition)

### Purpose

Creates a new Source.

### Returns

Source

### Published Events

- SourceCreated

---

## 4.2 UpdateSource

### Signature

UpdateSource(SourceId, SourceDefinition)

### Purpose

Updates Source metadata.

### Returns

Source

### Published Events

- SourceUpdated

---

## 4.3 DeleteSource

### Signature

DeleteSource(SourceId)

### Purpose

Removes a Source.

### Published Events

- SourceDeleted

---

# 5. Attachment Operations

## 5.1 AttachSource

### Signature

AttachSource(ProjectId, SourceId)

### Published Events

- SourceAttached

---

## 5.2 DetachSource

### Signature

DetachSource(ProjectId, SourceId)

### Published Events

- SourceDetached

---

# 6. Validation Operations

The service SHALL provide:

- ValidateSource
- ValidateAvailability
- ValidateIntegrity

Validation SHALL NOT modify the Domain Model.

---

# 7. Query Operations

The service SHALL provide:

- GetSource
- GetSources
- FindSources
- GetSourceStatistics
- GetSourceMetadata

Queries SHALL NOT modify system state.

---

# 8. Source State

A Source SHALL exist in one of the following states:

- Registered
- Available
- Unavailable
- Invalid
- Archived

State transitions SHALL be deterministic.

---

# 9. Transaction Rules

Every modifying operation SHALL execute atomically.

---

# 10. Thread Safety

Read operations MAY execute concurrently.

Modification of the same Source SHALL be serialized.

---

# 11. Dependencies

The contract SHALL depend only on:

- Domain Model;
- IService.

The contract SHALL NOT depend on:

- GUI;
- parser implementations;
- AI Runtime.

---

# 12. AI Implementation Rules

Implementations SHALL:

- preserve Source identity;
- never parse content directly;
- never perform import;
- publish lifecycle events after successful completion.

---

# 13. Test Requirements

Tests SHALL verify:

- creation;
- update;
- deletion;
- attachment;
- validation;
- concurrent access.

---

# 14. Compliance Checklist

The implementation conforms to this specification only if it:

- manages Source lifecycle;
- validates sources;
- does not perform parsing;
- does not perform import;
- conforms to IService.

---

End of Document