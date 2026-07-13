# Voxarium Software Architecture Specification

Document Path:
spec/300_Contracts/ISpeechEngine.md

Document ID: CTR-008

Title: ISpeechEngine

Version: 1.0.0

Status: Accepted

Classification: Normative

Depends On

- CTR-000 IService
- SpeechSegment
- VoiceProfile
- GenerationPreset
- AudioTrack

Referenced By

- Generation_Service
- Plugin_Runtime
- Workflow_Engine

---

# 1. Purpose

ISpeechEngine defines the contract implemented by every speech synthesis engine integrated into Voxarium.

The contract abstracts all speech synthesis providers behind a unified interface.

The Application Layer SHALL interact only with ISpeechEngine.

---

# 2. Responsibilities

An implementation SHALL:

- synthesize speech;
- report synthesis capabilities;
- validate synthesis requests;
- expose engine metadata;
- report progress for long-running operations.

---

# 3. Non-Responsibilities

An implementation SHALL NOT:

- manage Projects;
- manage Jobs;
- access GUI;
- manage Timeline;
- perform Export;
- persist generated audio.

---

# 4. Capabilities

Every engine SHALL expose immutable capability information.

Capability information SHALL include:

- Engine Identifier;
- Engine Version;
- Supported Languages;
- Supported Sample Rates;
- Supported Audio Formats;
- Supported Voice Types;
- Streaming Support;
- Voice Cloning Support;
- Emotion Support;
- SSML Support.

Capabilities SHALL remain constant during runtime.

---

# 5. Operations

## 5.1 ValidateRequest

### Purpose

Validates whether a synthesis request can be executed.

### Parameters

- SpeechSegment
- VoiceProfile
- GenerationPreset

### Returns

ValidationResult

Validation SHALL NOT start synthesis.

---

## 5.2 Synthesize

### Purpose

Generates speech from a SpeechSegment.

### Parameters

- SpeechSegment
- VoiceProfile
- GenerationPreset

### Returns

Generated AudioTrack

---

## 5.3 Cancel

### Purpose

Requests cancellation of an active synthesis operation.

Cancellation SHOULD be cooperative.

---

## 5.4 GetCapabilities

### Purpose

Returns immutable engine capabilities.

### Returns

SpeechEngineCapabilities

---

## 5.5 HealthCheck

### Purpose

Verifies engine availability.

### Returns

EngineHealthStatus

---

# 6. Audio Requirements

Generated audio SHALL:

- contain exactly one spoken SpeechSegment;
- preserve text order;
- use the requested sampling configuration whenever supported;
- contain no additional silence unless requested by GenerationPreset.

---

# 7. Error Model

Implementations SHALL distinguish at least:

- InvalidRequest;
- UnsupportedLanguage;
- UnsupportedVoice;
- EngineUnavailable;
- ModelNotLoaded;
- ResourceExhausted;
- Cancelled;
- InternalFailure.

---

# 8. Performance Requirements

The contract SHALL support:

- asynchronous execution;
- progress reporting;
- cancellation;
- parallel independent synthesis requests.

---

# 9. Thread Safety

Independent synthesis operations MAY execute concurrently.

Implementations SHALL document any concurrency limitations.

---

# 10. Dependencies

ISpeechEngine SHALL depend only on Domain Model.

The contract SHALL NOT depend on:

- GUI;
- Application Services;
- Infrastructure.

---

# 11. AI Implementation Rules

Implementations SHALL:

- be deterministic for identical input when deterministic mode is enabled;
- avoid modifying Domain objects;
- return immutable synthesis results;
- report failures without corrupting engine state.

---

# 12. Compatibility

Different speech engines SHALL be interchangeable without changing Application Layer code.

Application Services SHALL NOT rely on engine-specific behavior unless explicitly declared through capabilities.

---

# 13. Test Requirements

Every implementation SHALL pass:

- capability tests;
- validation tests;
- synthesis tests;
- cancellation tests;
- concurrency tests;
- health check tests.

---

# 14. Compliance Checklist

An implementation conforms to ISpeechEngine only if it:

- supports capability discovery;
- validates requests;
- synthesizes exactly one SpeechSegment per request;
- supports cancellation;
- reports progress;
- exposes health status;
- remains independent from Application Layer.

---

End of Document