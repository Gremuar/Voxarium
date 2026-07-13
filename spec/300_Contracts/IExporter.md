# Voxarium Software Architecture Specification

Document Path:
spec/300_Contracts/IExporter.md

Document ID: CTR-013

Title: IExporter

Version: 1.0.0

Status: Accepted

Classification: Normative

Category: Provider Contract (SPI)

Depends On

- Project
- Production
- AudioTrack
- ExportProfile

Referenced By

- IExportService
- Plugin_Runtime
- Export_Service

---

# 1. Purpose

IExporter defines the provider contract implemented by all export plugins.

An exporter converts Voxarium Domain objects into an external representation.

The exporter SHALL NOT coordinate application workflows or manage persistence.

---

# 2. Responsibilities

An implementation SHALL provide:

- export validation;
- capability reporting;
- metadata generation;
- export execution;
- progress reporting.

---

# 3. Non-Responsibilities

An implementation SHALL NOT:

- create Jobs;
- publish Application Events;
- modify Project;
- modify Production;
- modify AudioTrack;
- access GUI;
- manage transactions.

---

# 4. Supported Targets

An implementation SHALL declare supported:

- output formats;
- codecs;
- metadata standards;
- container formats.

Examples:

- WAV
- FLAC
- MP3
- OGG
- AAC
- OPUS
- EPUB
- DAISY

---

# 5. Operations

## 5.1 CanExport

### Signature

CanExport(ExportProfile)

### Purpose

Determines whether the exporter supports the requested export profile.

### Returns

Boolean

The operation SHALL NOT modify state.

---

## 5.2 Validate

### Signature

Validate(Project, ExportProfile)

### Purpose

Validates export prerequisites.

### Returns

ValidationResult

Validation SHALL NOT perform export.

---

## 5.3 Export

### Signature

Export(Project, ExportProfile)

### Purpose

Exports Project content.

### Returns

ExportResult

The operation SHALL NOT create Jobs.

---

## 5.4 ExportProduction

### Signature

ExportProduction(Production, ExportProfile)

### Purpose

Exports a Production object.

### Returns

ExportResult

---

## 5.5 GetCapabilities

### Signature

GetCapabilities()

### Returns

ExporterCapabilities

---

## 5.6 HealthCheck

### Signature

HealthCheck()

### Returns

ProviderHealthStatus

---

# 6. Export Result

ExportResult SHALL contain:

- exported artifacts;
- generated metadata;
- warnings;
- diagnostics;
- statistics.

ExportResult SHALL be immutable.

---

# 7. Capability Model

Capabilities SHALL include:

- provider identifier;
- provider version;
- supported formats;
- supported codecs;
- supported metadata standards;
- streaming support;
- batch support.

---

# 8. Validation Rules

Before export begins the exporter SHALL verify:

- output format support;
- codec compatibility;
- required metadata;
- profile validity.

Validation failures SHALL NOT produce partial output.

---

# 9. Error Model

Implementations SHALL distinguish:

- UnsupportedFormat;
- UnsupportedCodec;
- InvalidProfile;
- WriteFailure;
- ResourceUnavailable;
- Cancelled;
- InternalFailure.

---

# 10. Thread Safety

Independent export operations MAY execute concurrently.

Any implementation-specific limitations SHALL be documented.

---

# 11. Dependencies

The contract SHALL depend only on the Domain Model.

The contract SHALL NOT depend on:

- Application Layer;
- GUI;
- Workflow;
- persistence implementation.

---

# 12. AI Implementation Rules

Implementations SHALL:

- never modify Domain objects;
- never create Jobs;
- never publish Application Events;
- produce deterministic output for identical input and configuration;
- return immutable ExportResult objects.

---

# 13. Test Requirements

Every implementation SHALL pass:

- format validation tests;
- metadata export tests;
- successful export tests;
- unsupported format tests;
- write failure tests;
- concurrent export tests.

---

# 14. Compliance Checklist

An implementation conforms to IExporter only if it:

- validates export requests;
- supports capability discovery;
- exports without modifying the Domain Model;
- reports deterministic results;
- remains independent from the Application Layer.

---

End of Document