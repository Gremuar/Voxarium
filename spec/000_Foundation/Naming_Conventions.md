# Naming Conventions

**Document Path:**
`spec/000_Foundation/Naming_Conventions.md`

**Document ID:** FOUND-010

**Version:** 1.0.0

**Status:** Draft

**Classification:** Normative

---

# 1. Purpose

This document defines the naming conventions used throughout the Voxarium architecture specification and implementation.

Its purpose is to establish a single, unambiguous terminology that remains consistent across documentation, source code, APIs, project formats, plugins, and user interface components.

---

# 2. Scope

These conventions apply to:

* specification documents;
* architectural components;
* source code;
* public APIs;
* commands;
* events;
* contracts;
* domain model;
* project files;
* plugins;
* test artifacts.

---

# 3. General Principles

Names SHALL be:

* descriptive;
* unambiguous;
* consistent;
* stable over time;
* written in English.

Names SHALL describe the represented concept rather than the implementation.

---

# 4. Language

English SHALL be the canonical language of the architecture.

Localized user interface strings SHALL NOT influence architectural terminology.

Translations SHALL preserve the canonical meaning of terms.

---

# 5. Case Conventions

The following naming styles SHALL be used.

| Element               | Convention                        |
| --------------------- | --------------------------------- |
| Classes               | PascalCase                        |
| Interfaces            | PascalCase                        |
| Enums                 | PascalCase                        |
| Methods               | PascalCase or language convention |
| Properties            | PascalCase or language convention |
| Constants             | UPPER_SNAKE_CASE                  |
| Variables             | camelCase or language convention  |
| Packages / Namespaces | language convention               |
| Files                 | PascalCase                        |
| Folders               | PascalCase                        |

---

# 6. Document Names

Specification documents SHALL use PascalCase.

Examples:

* Architecture_Principles.md
* Component_Model.md
* VoiceProfile.md
* ProjectSettings.md

Document names SHALL describe a single architectural concept.

---

# 7. Domain Entities

Domain entities SHALL be singular nouns.

Examples:

* Project
* Document
* Fragment
* Speaker
* Timeline
* VoiceProfile

Plural entity names are prohibited.

---

# 8. Value Objects

Value Objects SHALL be named using descriptive nouns.

Examples:

* TimeRange
* FilePath
* LanguageCode
* VoiceIdentifier

Generic names such as:

* Data
* Value
* Object
* Item

SHALL NOT be used.

---

# 9. Services

Service names SHALL end with the suffix:

```text
Service
```

Examples:

* ProjectService
* AudioGenerationService
* ValidationService

Service names SHALL describe business capabilities rather than implementation details.

---

# 10. Repositories

Repository names SHALL end with:

```text
Repository
```

Examples:

* ProjectRepository
* DictionaryRepository
* VoiceRepository

Repository names SHALL correspond to aggregate roots.

---

# 11. Factories

Factory names SHALL end with:

```text
Factory
```

Examples:

* ProjectFactory
* VoiceProfileFactory

Factories SHALL describe the object they create.

---

# 12. Commands

Command names SHALL:

* begin with a verb;
* describe an intention;
* end with the suffix:

```text
Command
```

Examples:

* CreateProjectCommand
* GenerateAudioCommand
* ValidateDocumentCommand

---

# 13. Events

Event names SHALL:

* describe completed actions;
* use past tense;
* end with:

```text
Event
```

Examples:

* ProjectCreatedEvent
* TimelineUpdatedEvent
* VoiceAssignedEvent

Event names SHALL NEVER describe intentions.

---

# 14. Queries

Query names SHALL begin with verbs such as:

* Get
* Find
* Search
* List
* Load

Examples:

* GetProjectQuery
* FindVoiceQuery
* SearchFragmentsQuery

Queries SHALL NOT modify application state.

---

# 15. Data Transfer Objects

DTO names SHALL end with:

```text
Dto
```

Examples:

* ProjectDto
* VoiceProfileDto
* TimelineDto

DTOs SHALL contain no business logic.

---

# 16. Interfaces

Interface names SHALL describe capabilities.

The project SHALL consistently use either:

* `IProjectRepository`

or

* `ProjectRepository`

depending on the implementation language and project-wide convention.

Mixed styles are prohibited.

---

# 17. Enumerations

Enumeration names SHALL be singular.

Enumeration values SHALL be descriptive and stable.

Abbreviations SHOULD be avoided.

---

# 18. Plugin Names

Plugin names SHALL:

* be globally unique;
* describe functionality;
* avoid vendor-specific prefixes unless required.

Examples:

* AzureSpeechPlugin
* PiperPlugin
* XTTSPlugin

---

# 19. File and Folder Names

File names SHALL correspond to the primary architectural concept contained within the file.

Folders SHALL group related concepts.

Folder names SHALL remain stable.

---

# 20. Abbreviations

Only widely recognized abbreviations MAY be used.

Examples:

* API
* URI
* UUID
* JSON
* XML
* UTF

Project-specific abbreviations SHALL be documented before use.

---

# 21. Reserved Terms

The following architectural terms have fixed meanings and SHALL be used consistently:

* Aggregate
* Entity
* Value Object
* Command
* Query
* Event
* Service
* Repository
* Factory
* Contract
* Component
* Context
* Plugin

Alternative terminology SHALL NOT be introduced without architectural review.

---

# 22. Deprecated Names

Renaming public architectural concepts SHALL require:

* an Architecture Decision Record;
* documentation updates;
* migration guidance where applicable.

Deprecated names SHALL NOT be reused for different concepts.

---

# 23. Compliance

All new documents, source code, APIs, and architectural artifacts SHALL comply with this naming convention.

Architecture reviews SHALL verify terminology consistency across the entire specification.

---

# 24. References

* Documentation_Index.md
* Architecture_Principles.md
* Component_Model.md
* Event_Model.md
* Layered_Architecture.md
* Coding_Standards.md

---

**End of Document**
