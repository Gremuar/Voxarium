# Voxarium Software Architecture Specification

Document Path:
spec/Architecture_Map.md

Document ID: SAS-MAP-001

Title: Architecture Map

Version: 1.0.0

Status: Accepted

Classification: Normative

---

# 1. Purpose

Настоящий документ является точкой входа в архитектурную спецификацию Voxarium.

Документ определяет:

- структуру спецификации;
- зависимости между разделами;
- правила чтения документации;
- карту архитектурных компонентов.

Все остальные документы SHALL соответствовать настоящей карте.

---

# 2. Documentation Layers

Спецификация состоит из следующих уровней.

```
000_Foundation

↓

100_Domain

↓

200_Modules

↓

300_Contracts

↓

400_Commands

↓

500_Events

↓

600_Project_Format

↓

700_Plugins

↓

800_GUI

↓

900_Testing

↓

999_ADR
```

Каждый уровень зависит только от предыдущих.

---

# 3. Foundation

Foundation определяет фундаментальные правила архитектуры.

```
SAS-000 Project Philosophy

SAS-001 Glossary

SAS-002 Domain Ontology

SAS-003 Architecture Principles

SAS-004 Quality Attributes

SAS-005 Architecture Decision Process

SAS-006 Common Domain Patterns
```

Foundation SHALL NOT зависеть ни от одного другого раздела.

---

# 4. Domain

Domain описывает предметную область.

```
Project
Production
ProductionItem

Document
Timeline
Fragment
SpeechSegment

Role
VoiceProfile
Emotion
PronunciationDictionary

Workflow
WorkflowStage
Job

GenerationPreset
GenerationSession
GenerationResult

ExportProfile

Asset
AudioTrack
```

Domain SHALL NOT зависеть от Application.

---

# 5. Module Layer

Module Layer определяет крупные функциональные подсистемы.

```
Runtime Module

Project Module

Document Module

Timeline Module

Voice Module

Generation Module

Workflow Module

Audio Module

Playback Module

Export Module

Plugin Host Module

Storage Module

Logging Module

Diagnostics Module
```

Каждый Module использует Domain.

---

# 6. Contract Layer

Contracts определяют публичные интерфейсы.

Каждый Contract принадлежит одному Module.

Контракты SHALL NOT содержать бизнес-логику.

---

# 7. Command Layer

Commands описывают намерения изменения состояния системы.

Каждая команда:

- имеет единственного Handler;
- публикует Domain Events;
- изменяет Aggregate Root.

---

# 8. Event Layer

Events описывают завершившиеся бизнес-факты.

Event является immutable.

Events используются исключительно для обмена между компонентами.

---

# 9. Project Format

Project Format определяет сериализацию.

Раздел включает:

- структуру проекта;
- форматы файлов;
- правила миграции;
- правила совместимости.

---

# 10. Plugin Layer

Plugin Layer определяет:

- Plugin API;
- Extension Point;
- жизненный цикл расширений;
- правила совместимости.

---

# 11. GUI Layer

GUI Layer определяет:

- ViewModel;
- команды пользователя;
- навигацию;
- правила отображения.

GUI не содержит бизнес-логики.

---

# 12. Testing Layer

Testing определяет:

- Unit Tests;
- Integration Tests;
- Contract Tests;
- Performance Tests;
- Architecture Tests.

---

# 13. Aggregate Map

```
Project
│
├── Documents
│     ├── Timeline
│     ├── Fragment
│     └── SpeechSegment
│
├── Productions
│     └── ProductionItem
│
├── Workflows
│     └── WorkflowStage
│
├── Assets
│
├── VoiceProfiles
│
├── Roles
│
├── GenerationPresets
│
├── ExportProfiles
│
├── AudioTracks
│
└── GenerationSessions
        └── GenerationResult
```

Project является корневым Aggregate всей предметной области.

---

# 14. Dependency Rules

Разрешены только следующие направления зависимостей.

```
Foundation
      ▲

Domain
      ▲

Modules
      ▲

Contracts
      ▲

Commands / Events
      ▲

GUI
```

Обратные зависимости запрещены.

---

# 15. Implementation Order

Рекомендуемый порядок реализации.

```
Foundation

↓

Domain

↓

Contracts

↓

Commands

↓

Events

↓

Modules

↓

Infrastructure

↓

GUI

↓

Tests
```

Изменение порядка допускается только при наличии ADR.

---

# 16. AI Agent Rules

ИИ-агент SHALL:

- считать настоящую карту главным документом архитектуры;
- использовать ссылки между документами;
- не создавать зависимости, отсутствующие в настоящем документе;
- соблюдать направление зависимостей;
- соблюдать границы Aggregate.

---

# 17. Compliance Checklist

Архитектура соответствует настоящей карте только если:

- отсутствуют циклические зависимости;
- каждый документ принадлежит одному разделу;
- каждый раздел использует только разрешённые зависимости;
- каждый Aggregate имеет единственный Aggregate Root;
- Domain полностью независим от остальных слоёв.

---

End of Document