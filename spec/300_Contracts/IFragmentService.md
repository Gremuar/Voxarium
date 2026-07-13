# Voxarium Software Architecture Specification

Document Path:
spec/300_Contracts/IFragmentService.md

Document ID: CTR-015

Title: IFragmentService

Version: 1.0.0

Status: Accepted

Classification: Normative

Category: Application Service Contract

Depends On

- CTR-000 IService
- Fragment
- Timeline
- Document
- SpeechSegment
- Role
- VoiceProfile

Referenced By

- Timeline_Service
- Workflow_Engine
- Generation_Service
- User_Interface_Architecture

---

# 1. Purpose

IFragmentService defines the public Application Service contract responsible for managing Fragment entities.

A Fragment is the smallest editable semantic unit within a Document that participates in generation workflows.

The service coordinates creation, editing, validation and organization of Fragments while preserving document consistency.

---

# 2. Responsibilities

The service SHALL provide operations for:

- creating Fragments;
- modifying Fragment content;
- splitting Fragments;
- merging Fragments;
- moving Fragments;
- assigning Roles;
- assigning Voice Profiles;
- assigning Speech Segments;
- validating Fragment integrity.

---

# 3. Non-Responsibilities

The service SHALL NOT:

- synthesize speech;
- clone voices;
- generate audio;
- import documents;
- export projects;
- execute Workflow.

---

# 4. Lifecycle Operations

## 4.1 CreateFragment

### Signature

CreateFragment(DocumentId, Position)

### Returns

Fragment

### Published Events

- FragmentCreated

---

## 4.2 UpdateFragment

### Signature

UpdateFragment(FragmentId, FragmentDefinition)

### Returns

Fragment

### Published Events

- FragmentUpdated

---

## 4.3 DeleteFragment

### Signature

DeleteFragment(FragmentId)

### Published Events

- FragmentDeleted

---

# 5. Structure Operations

## 5.1 SplitFragment

### Signature

SplitFragment(FragmentId, Offset)

### Returns

Fragment[]

### Published Events

- FragmentSplit

---

## 5.2 MergeFragments

### Signature

MergeFragments(FragmentIds)

### Returns

Fragment

### Published Events

- FragmentsMerged

---

## 5.3 MoveFragment

### Signature

MoveFragment(FragmentId, Position)

### Published Events

- FragmentMoved

---

# 6. Assignment Operations

The service SHALL provide:

- AssignRole
- RemoveRole
- AssignVoiceProfile
- RemoveVoiceProfile
- AssignSpeechSegment
- RemoveSpeechSegment

Each assignment SHALL preserve referential integrity.

---

# 7. Text Operations

The service SHALL provide:

- GetText
- ReplaceText
- AppendText
- PrependText
- ClearText

All modifications SHALL preserve Unicode correctness.

---

# 8. Validation Operations

The service SHALL provide:

- ValidateFragment
- ValidateAssignments
- ValidateTimelineReferences

Validation SHALL NOT modify system state.

---

# 9. Query Operations

The service SHALL provide:

- GetFragment
- GetFragments
- FindFragments
- GetFragmentStatistics
- GetAssignedRole
- GetAssignedVoiceProfile

Queries SHALL NOT modify system state.

---

# 10. Consistency Rules

Every Fragment SHALL belong to exactly one Document.

A Fragment MAY reference:

- zero or one Role;
- zero or one VoiceProfile;
- zero or more SpeechSegments.

No dangling references SHALL exist.

---

# 11. Transaction Rules

Every modifying operation SHALL execute atomically.

Structural modifications SHALL leave the Document in a valid state.

---

# 12. Thread Safety

Concurrent read operations MAY execute simultaneously.

Concurrent modification of the same Fragment SHALL be serialized.

---

# 13. Dependencies

The contract SHALL depend only on:

- Domain Model;
- IService.

The contract SHALL NOT depend on:

- GUI;
- Speech Engines;
- Storage implementation.

---

# 14. AI Implementation Rules

Implementations SHALL:

- preserve Fragment identity;
- preserve ordering inside a Document;
- maintain referential integrity;
- publish lifecycle events after successful completion.

---

# 15. Test Requirements

Tests SHALL verify:

- creation;
- update;
- deletion;
- split;
- merge;
- move;
- assignment operations;
- validation;
- concurrent modification.

---

# 16. Compliance Checklist

The implementation conforms to this specification only if it:

- manages the complete Fragment lifecycle;
- preserves document consistency;
- preserves referential integrity;
- supports structural editing operations;
- conforms to IService.

---

End of Document