# Voxarium Software Architecture Specification

Document Path:
spec/300_Contracts/IImporter.md

Document ID: CTR-012

Title: IImporter

Version: 1.0.0

Status: Accepted

Classification: Normative

Category: Provider Contract (SPI)

Depends On

- Source
- Project
- Document
- Asset

Referenced By

- IImportService
- Plugin_Runtime
- Import_Service

---

# 1. Purpose

IImporter defines the provider contract implemented by all import plugins.

An importer is responsible only for converting external data into the Voxarium Domain Model.

Importers SHALL NOT manage application workflows, jobs, user interaction or persistence.

---

# 2. Responsibilities

An implementation SHALL provide:

- format identification;
- source validation;
- metadata extraction;
- preview generation;
- conversion into Domain Model;
- capability reporting.

---

# 3. Non-Responsibilities

An implementation SHALL NOT:

- create Jobs;
- publish Application Events;
- save Project files;
- update GUI;
- manage transactions;
- execute Workflow.

---

# 4. Supported Sources

An implementation SHALL declare supported:

- file extensions;
- MIME types;
- URI schemes.

Example:

- .txt
- .docx
- .fb2
- .epub
- .pdf

---

# 5. Operations

## 5.1 CanImport

### Signature

CanImport(Source)

### Purpose

Determines whether the importer supports the supplied source.

### Returns

Boolean

This operation SHALL NOT modify any state.

---

## 5.2 ReadMetadata

### Signature

ReadMetadata(Source)

### Purpose

Reads source metadata without importing content.

### Returns

ImportMetadata

---

## 5.3 Preview

### Signature

Preview(Source)

### Purpose

Creates an immutable preview of the import result.

### Returns

ImportPreview

Preview SHALL NOT modify Domain objects.

---

## 5.4 Import

### Signature

Import(Source)

### Purpose

Imports external data into an in-memory Domain Model.

### Returns

ImportResult

Import SHALL NOT persist data.

---

## 5.5 GetCapabilities

### Signature

GetCapabilities()

### Returns

ImporterCapabilities

---

## 5.6 HealthCheck

### Signature

HealthCheck()

### Returns

ProviderHealthStatus

---

# 6. Import Result

ImportResult SHALL contain:

- imported Documents;
- imported Assets;
- imported metadata;
- diagnostics;
- warnings;
- statistics.

ImportResult SHALL be immutable.

---

# 7. Capability Model

Capabilities SHALL include:

- provider identifier;
- provider version;
- supported formats;
- supported encodings;
- preview support;
- metadata extraction support;
- streaming support.

---

# 8. Validation Rules

The importer SHALL validate:

- source availability;
- file integrity;
- supported version;
- encoding;
- structural consistency.

Validation errors SHALL NOT partially modify the Domain Model.

---

# 9. Error Model

Implementations SHALL distinguish:

- UnsupportedFormat;
- InvalidEncoding;
- CorruptedInput;
- UnsupportedVersion;
- ParsingFailed;
- ResourceUnavailable;
- InternalFailure.

---

# 10. Thread Safety

Independent import operations MAY execute concurrently.

Thread safety guarantees SHALL be documented by the implementation.

---

# 11. Dependencies

The contract SHALL depend only on the Domain Model.

The contract SHALL NOT depend on:

- GUI;
- Application Layer;
- persistence;
- Workflow.

---

# 12. AI Implementation Rules

Implementations SHALL:

- produce deterministic import results for identical input;
- never persist imported data;
- never create Jobs;
- never publish Application Events;
- return immutable ImportResult objects.

---

# 13. Test Requirements

Every implementation SHALL pass:

- format detection tests;
- metadata extraction tests;
- preview tests;
- successful import tests;
- corrupted input tests;
- unsupported format tests.

---

# 14. Compliance Checklist

An implementation conforms to IImporter only if it:

- detects supported formats;
- validates input;
- imports into an in-memory Domain Model;
- supports capability discovery;
- does not depend on the Application Layer.

---

End of Document