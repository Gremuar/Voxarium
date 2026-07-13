# Voxarium Software Architecture Specification

Document Path:
spec/300_Contracts/IVoiceCloner.md

Document ID: CTR-009

Title: IVoiceCloner

Version: 1.0.0

Status: Accepted

Classification: Normative

Depends On

- CTR-000 IService
- VoiceProfile
- Asset
- Job

Referenced By

- Voice_Service
- Generation_Service
- Plugin_Runtime

---

# 1. Purpose

IVoiceCloner defines the public contract implemented by voice cloning providers.

The contract abstracts voice cloning technologies behind a unified interface.

Voice cloning SHALL be independent from speech synthesis.

---

# 2. Responsibilities

An implementation SHALL provide operations for:

- validating source recordings;
- creating voice models;
- updating voice models;
- deleting voice models;
- exporting voice models when supported;
- reporting provider capabilities.

---

# 3. Non-Responsibilities

An implementation SHALL NOT:

- synthesize speech;
- generate AudioTrack;
- manage Projects;
- manage Timeline;
- access GUI;
- store Project data.

---

# 4. Supported Input

A provider SHALL declare supported input characteristics.

These MAY include:

- minimum recording duration;
- maximum recording duration;
- supported sample rates;
- supported audio formats;
- mono/stereo requirements;
- language restrictions;
- noise tolerance.

---

# 5. Operations

## 5.1 ValidateRecording

### Signature

ValidateRecording(AudioAsset)

### Purpose

Validates whether the supplied recording can be used for cloning.

### Returns

ValidationResult

---

## 5.2 CloneVoice

### Signature

CloneVoice(AudioAsset, VoiceProfileName)

### Purpose

Creates a new voice model.

### Returns

Job

### Published Events

- VoiceCloneRequested

---

## 5.3 UpdateVoiceModel

### Signature

UpdateVoiceModel(VoiceProfileId, AdditionalRecording)

### Purpose

Improves an existing voice model.

### Returns

Job

### Published Events

- VoiceModelUpdateRequested

---

## 5.4 DeleteVoiceModel

### Signature

DeleteVoiceModel(VoiceProfileId)

### Purpose

Deletes a cloned voice model.

### Returns

None

---

## 5.5 GetCapabilities

### Signature

GetCapabilities()

### Returns

VoiceClonerCapabilities

---

## 5.6 HealthCheck

### Signature

HealthCheck()

### Returns

ProviderHealthStatus

---

# 6. Capability Model

Capabilities SHALL include:

- provider identifier;
- provider version;
- supported languages;
- supported cloning modes;
- minimum recording duration;
- maximum recording duration;
- online/offline support;
- GPU requirements;
- batch support.

---

# 7. Error Model

The implementation SHALL distinguish:

- InvalidRecording;
- RecordingTooShort;
- UnsupportedFormat;
- UnsupportedLanguage;
- ProviderUnavailable;
- ModelCreationFailed;
- Cancelled;
- InternalFailure.

---

# 8. Performance Requirements

The contract SHALL support:

- asynchronous execution;
- progress reporting;
- cancellation.

Voice cloning SHOULD NOT block the calling thread.

---

# 9. Thread Safety

Multiple independent cloning operations MAY execute concurrently.

Provider-specific limitations SHALL be documented.

---

# 10. Dependencies

IVoiceCloner SHALL depend only on Domain Model.

The contract SHALL NOT depend on:

- GUI;
- Application Layer;
- Infrastructure.

---

# 11. AI Implementation Rules

Implementations SHALL:

- never modify Project state;
- never synthesize speech;
- validate recordings before cloning;
- return immutable capability information.

---

# 12. Compatibility

Voice models produced by different providers MAY be incompatible.

Providers SHALL expose compatibility information through their capabilities.

---

# 13. Test Requirements

Every implementation SHALL pass:

- recording validation tests;
- voice cloning tests;
- cancellation tests;
- capability tests;
- health check tests.

---

# 14. Compliance Checklist

An implementation conforms to IVoiceCloner only if it:

- validates recordings;
- supports asynchronous cloning;
- exposes immutable capabilities;
- supports health checks;
- remains independent from Application Layer.

---

End of Document