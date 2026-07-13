# Voxarium Software Architecture Specification

Document Path:
spec/000_Foundation/SAS-002_Domain_Ontology.md

Document ID: SAS-002

Title: Domain Ontology

<<<<<<< HEAD
Version: 1.0.0
=======
Version: 2.0.0
>>>>>>> c975edf (t)

Status: Accepted

Classification: Normative

Depends On

- SAS-000 Project Philosophy
- SAS-001 Glossary

Referenced By

<<<<<<< HEAD
- All Domain documents
- All Module documents
- All Contract documents
- All GUI documents
=======
- All Domain Documents
- All Application Documents
>>>>>>> c975edf (t)

---

# 1. Purpose

<<<<<<< HEAD
Настоящий документ определяет предметную модель (Domain Model) платформы Voxarium.

Документ описывает архитектурные сущности и отношения между ними.

Предметная модель является первичным источником истины (Single Source of Truth) для всей архитектуры.

Ни один модуль Core, Plugin, пользовательский интерфейс или API не могут вводить собственные сущности предметной области без внесения изменений в настоящий документ.

---

# 2. Domain Principles

Предметная модель должна описывать реальные объекты, существующие с точки зрения пользователя.

Предметная модель не должна содержать технических сущностей реализации.

Следующие понятия не являются частью Domain Model:

- SQL-таблицы;
- ORM-модели;
- REST API;
- JSON-структуры;
- классы Python;
- Qt Widgets;
- потоки выполнения;
- базы данных;
- файловые форматы;
- внутренние структуры кэша.

Эти элементы относятся к инфраструктурному уровню и описываются отдельными документами.

---

# 3. Domain Hierarchy

Верхний уровень предметной модели представлен единственной сущностью.

```
Project
```

Все остальные сущности принадлежат одному Project.

Существование пользовательских сущностей вне Project запрещено.

---

# 4. Aggregate Roots

Следующие сущности являются Aggregate Root.

- Project
- Production
- Document
- Voice Profile
- Export Profile
- Generation Preset

Aggregate Root являются единственными точками входа для изменения принадлежащих им объектов.

---

# 5. Domain Entities

Предметная область состоит из следующих сущностей.

## Project

Контейнер верхнего уровня.

Объединяет все данные проекта.

---

## Source

Импортированный оригинальный источник информации.

---

## Document

Внутреннее представление текста.

---

## Production

Отдельная производственная версия проекта.

---

## Timeline

Последовательность озвучивания.

---

## Fragment

Минимальная логическая единица генерации.

---

## Role

Персонаж или логическая роль.

---

## Voice Profile

Описание характеристик будущего голоса.

---

## Speech Segment

Сгенерированный аудиофрагмент.

---

## Audio Track

Последовательность Speech Segment.

---

## Workflow

Длительная операция.

---

## Job

Минимальная задача выполнения.

---

## Asset

Бинарный ресурс.

---

## Export Profile

Конфигурация экспорта.

---

## Generation Preset

Конфигурация генерации.

---

## Plugin Data

Область хранения данных Plugin.

---

# 6. Entity Relationships
=======
Настоящий документ определяет формальную онтологию предметной области Voxarium.

Он описывает:

- типы объектов;
- отношения между объектами;
- владельцев объектов;
- допустимые ссылки;
- агрегаты;
- жизненные циклы;
- правила целостности.

Любая реализация системы SHALL соответствовать настоящей модели.

---

# 2. Domain Classification

Все объекты предметной области относятся ровно к одной из следующих категорий.

- Aggregate Root
- Entity
- Value Object
- Enumeration
- Domain Service
- Domain Event

Объект SHALL принадлежать только одной категории.

---

# 3. Aggregate Roots

Aggregate Root являются единственными точками изменения соответствующих агрегатов.

Система определяет следующие Aggregate Root.

| Aggregate | Owner |
|------------|-------|
| Project | User |
| Workflow | Project |
| Production | Project |
| Job | Workflow |

Изменение дочерних сущностей SHALL выполняться только через Aggregate Root.

---

# 4. Entities

Entity обладают собственной идентичностью.

К ним относятся:

- Source
- Document
- Timeline
- Fragment
- Role
- VoiceProfile
- SpeechSegment
- Asset
- Emotion

Entity имеют стабильный идентификатор.

Изменение атрибутов Entity НЕ изменяет их идентичность.

---

# 5. Value Objects

Value Object не имеют собственной идентичности.

Примеры:

- TimeRange
- AudioFormat
- VoiceParameters
- GenerationParameters
- ExportSettings
- FileChecksum
- SampleRate
- LanguageCode

Value Object SHALL быть неизменяемыми.

---

# 6. Enumerations

Перечисления определяют ограниченный набор допустимых значений.

Примеры:

- GenerationStatus
- JobStatus
- FragmentType
- AssetType
- ExportFormat
- EmotionType
- VoiceGender

Добавление новых элементов перечислений SHALL сохранять обратную совместимость.

---

# 7. Ownership Model

Каждый объект имеет единственного владельца.

Владение означает:

- ответственность за жизненный цикл;
- ответственность за сохранение;
- ответственность за удаление.

Ссылка не является владением.

---

# 8. Ownership Tree
>>>>>>> c975edf (t)

```
Project
│
├── Sources
│
├── Documents
<<<<<<< HEAD
│
├── Productions
│      │
│      ├── Timeline
│      │       │
│      │       └── Fragments
│      │
│      ├── Speech Segments
│      │
│      ├── Audio Tracks
│      │
│      └── Workflow
│
├── Roles
│
├── Voice Profiles
│
├── Export Profiles
│
├── Generation Presets
│
├── Assets
│
└── Plugin Data
```

---

# 7. Ownership Rules

Каждая сущность имеет единственного владельца.

Владение не может быть разделено.

Владение не может быть циклическим.

Передача владения между агрегатами запрещена.

---

# 8. References

Связи между агрегатами осуществляются исключительно посредством идентификаторов.

Прямая вложенность объектов между агрегатами запрещена.

Например:

Fragment хранит идентификатор Role.

Fragment не хранит объект Role.

---

# 9. Identity

Каждая сущность обладает постоянным идентификатором.

Идентификатор создаётся один раз.

Изменение идентификатора запрещено.

Идентификатор не зависит:

- от имени;
- от положения в проекте;
- от используемого движка;
- от файловой структуры.

---

# 10. Lifetime

Каждая сущность имеет жизненный цикл.

Создание.

↓

Использование.

↓

Изменение.

↓

Архивация (опционально).

↓

Удаление.

Все переходы жизненного цикла должны выполняться посредством Command.

---

# 11. Immutability

Следующие сущности являются неизменяемыми после создания.

Source

Speech Segment

Log Entry

Diagnostic Report

Любое изменение этих сущностей приводит к созданию новой версии.

---

# 12. Mutable Entities

Следующие сущности допускают изменение.

Project

Document

Timeline

Fragment

Role

Voice Profile

Production

Workflow

Generation Preset

Export Profile

Settings

---

# 13. Versioning

Версионирование является свойством Domain Model.

Любая изменяемая сущность должна поддерживать историю изменений.

Первая версия платформы может хранить только последнюю редакцию.

Архитектура обязана предусматривать поддержку полноценной истории.

---

# 14. Domain Events

Любое изменение состояния сущности должно сопровождаться публикацией Domain Event.
=======
│   │
│   ├── Fragments
│   │
│   └── Timeline
│
├── Roles
│
├── VoiceProfiles
│
├── Productions
│
├── Assets
│
└── Workflows
    │
    └── Jobs
```

Данная структура SHALL быть единственным деревом владения объектов.

---

# 9. Reference Rules

Допускаются только ссылки.

```
Fragment
────────────► Role

Fragment
────────────► Emotion

SpeechSegment
────────────► Fragment

SpeechSegment
────────────► VoiceProfile

Timeline
────────────► SpeechSegment

Production
────────────► Timeline

Workflow
────────────► Production
```

Ссылки НЕ изменяют жизненный цикл объекта.

---

# 10. Forbidden References

Запрещены следующие зависимости.

```
VoiceProfile
────────► Project

Role
────────► Workflow

Fragment
────────► Project

Job
────────► GUI

Asset
────────► Plugin

Timeline
────────► File System
```

Подобные зависимости нарушают модель агрегатов.

---

# 11. Object Identity

Каждый Entity обязан иметь постоянный идентификатор.

Идентификатор:

- уникален внутри Project;
- никогда не изменяется;
- используется всеми ссылками.

Запрещается использовать позицию объекта как идентификатор.

---

# 12. Lifecycle Ownership

Создание и удаление объектов определяется владельцем.

| Object | Created By | Deleted By |
|----------|------------|------------|
| Source | Project | Project |
| Document | Project | Project |
| Fragment | Document | Document |
| Timeline | Document | Document |
| SpeechSegment | Timeline | Timeline |
| Role | Project | Project |
| VoiceProfile | Project | Project |
| Asset | Project | Project |
| Workflow | Project | Project |
| Job | Workflow | Workflow |

Никакой другой компонент SHALL NOT выполнять данные операции напрямую.

---

# 13. Aggregate Boundaries

Каждый Aggregate обеспечивает:

- согласованность данных;
- выполнение инвариантов;
- публикацию Domain Events.

Изменения за пределами Aggregate запрещены.

---

# 14. Invariants

Следующие правила являются обязательными.

Project SHALL иметь уникальный Identifier.

Document SHALL принадлежать ровно одному Project.

Fragment SHALL принадлежать ровно одному Document.

Timeline SHALL принадлежать ровно одному Document.

SpeechSegment SHALL ссылаться на существующий Fragment.

Role SHALL принадлежать одному Project.

VoiceProfile SHALL принадлежать одному Project.

Workflow SHALL принадлежать одному Project.

Job SHALL принадлежать одному Workflow.

---

# 15. Multiplicity

Кардинальность отношений.

```
Project
1
↓

*
Document

Document
1
↓

*
Fragment

Document
1
↓

1
Timeline

Timeline
1
↓

*
SpeechSegment

Role
1
↓

*
Fragment

VoiceProfile
1
↓

*
SpeechSegment

Workflow
1
↓

*
Job
```

Любое нарушение кардинальности является ошибкой модели.

---

# 16. Referential Integrity

Удаление объекта SHALL проверять существующие ссылки.

Если существуют обязательные ссылки, удаление запрещается.

Если существуют необязательные ссылки, они должны быть корректно обновлены.

Запрещается существование "висячих" ссылок.

---

# 17. Domain Events

Каждый Aggregate публикует события изменения состояния.
>>>>>>> c975edf (t)

Примеры:

ProjectCreated

<<<<<<< HEAD
RoleCreated

VoiceAssigned

FragmentUpdated

SpeechGenerated

WorkflowCompleted

Удаление события запрещается.

Событие является неизменяемым.

---

# 15. Commands

Изменение состояния допускается исключительно посредством Command.

Прямое изменение состояния запрещено.

Каждая команда имеет:

- инициатора;
- время создания;
- уникальный идентификатор;
- параметры;
- результат выполнения.

---

# 16. Queries

Получение информации осуществляется посредством Query.

Query не изменяет состояние системы.

Повторный вызов Query не должен изменять Domain Model.

---

# 17. Business Rules

Бизнес-правила относятся исключительно к предметной модели.

Бизнес-правила не должны зависеть:

- от GUI;
- от Storage;
- от Plugin;
- от сетевых сервисов;
- от Speech Engine.

---

# 18. Invariants

Следующие инварианты являются обязательными.

Project всегда содержит хотя бы одну Production.

Production всегда содержит один активный Timeline.

Fragment всегда принадлежит одному Timeline.

Timeline всегда принадлежит одной Production.

Role может использоваться несколькими Fragment.

Voice Profile может использоваться несколькими Role.

Speech Segment всегда создаётся для одного Fragment.

Fragment может иметь несколько Speech Segment различных ревизий.

Source никогда не изменяется после импорта.

Document всегда связан хотя бы с одним Source.

Удаление Document запрещено, если существуют зависимые Production.

Нарушение любого инварианта считается повреждением модели.

---

# 19. Domain Boundaries

Предметная модель не содержит информации о:

- расположении файлов;
- базе данных;
- формате сериализации;
- реализации Plugin;
- GUI;
- потоках выполнения;
- очередях сообщений;
- используемой библиотеке TTS.

Эти аспекты определяются отдельными документами спецификации.

---

# 20. Extensibility

Добавление новой сущности допускается только при соблюдении следующих условий.

Новая сущность должна:

- иметь самостоятельное бизнес-значение;
- обладать собственным жизненным циклом;
- иметь уникальную ответственность;
- не дублировать существующую сущность.

Изменение существующей предметной модели оформляется посредством ADR.

---

# 21. Compliance

Все документы спецификации обязаны использовать исключительно сущности, определённые настоящим документом.

Создание новых доменных сущностей вне настоящего документа запрещено.
=======
ProjectOpened

DocumentImported

FragmentCreated

FragmentDeleted

RoleAssigned

VoiceAssigned

WorkflowStarted

JobCompleted

Детальный каталог событий определяется разделом `500_Events`.

---

# 18. Commands

Изменение агрегатов SHALL выполняться только через команды.

Примеры:

CreateProject

ImportDocument

SplitFragment

AssignRole

AssignVoice

CreateWorkflow

StartJob

Полный каталог команд определяется разделом `400_Commands`.

---

# 19. Persistence Independence

Онтология не зависит от способа хранения.

Одинаковая модель SHALL использоваться:

- в памяти;
- на диске;
- при сериализации;
- при импорте;
- при экспорте.

---

# 20. Extension Rules

Plugin MAY создавать новые объекты только через опубликованные контракты.

Plugin SHALL NOT изменять существующую онтологию.

Plugin SHALL NOT изменять отношения владения.

Plugin SHALL NOT изменять кардинальности.

Расширения допускаются только через предусмотренные точки расширения.

---

# 21. AI Implementation Requirements

ИИ-агент, реализующий систему, SHALL использовать настоящую онтологию как единственный источник истины о предметной модели.

Любая попытка добавить новые отношения владения, изменить агрегаты или нарушить кардинальности считается отклонением от архитектуры.

---

# 22. Compliance Checklist

Документ предметной области соответствует настоящей онтологии только если:

- объект имеет определённую категорию;
- определён владелец объекта;
- определён жизненный цикл;
- определены допустимые ссылки;
- определены запрещённые ссылки;
- определены инварианты;
- определены кардинальности;
- определены Domain Events;
- определены Commands;
- отсутствуют неоднозначности владения.
>>>>>>> c975edf (t)

---

End of Document