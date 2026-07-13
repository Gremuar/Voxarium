# Voxarium Software Architecture Specification

Document Path:
spec/100_Domain/Project.md

<<<<<<< HEAD
Document ID: DOM-100

Title: Project

Version: 1.0.0
=======
Document ID: DOM-001

Title: Project

Version: 2.0.0
>>>>>>> c975edf (t)

Status: Accepted

Classification: Normative

Depends On

<<<<<<< HEAD
=======
- SAS-000 Project Philosophy
>>>>>>> c975edf (t)
- SAS-001 Glossary
- SAS-002 Domain Ontology
- SAS-003 Architecture Principles

Referenced By

<<<<<<< HEAD
- Production.md
- Source.md
- Document.md
- Timeline.md
- Role.md
- VoiceProfile.md
- Workflow.md
- Asset.md
- Storage specifications
- GUI specifications
=======
- Source
- Document
- Timeline
- Fragment
- Role
- VoiceProfile
- Asset
- Workflow
- Production
- GenerationPreset
- Project_Service
- Import_Service
- Export_Service
>>>>>>> c975edf (t)

---

# 1. Purpose

<<<<<<< HEAD
Project является главной пользовательской сущностью платформы Voxarium.

Все действия пользователя выполняются внутри Project.

Project представляет собой полностью самодостаточную рабочую область, содержащую все данные, необходимые для воспроизведения полного процесса создания речевого контента.

Project является единственной точкой входа в предметную модель.

---

# 2. Responsibility

Project отвечает исключительно за:

- объединение доменных сущностей;
- хранение общей информации;
- управление жизненным циклом проекта;
- обеспечение ссылочной целостности;
- предоставление общей области хранения данных.

Project не отвечает:

- за генерацию речи;
- за импорт документов;
- за работу Speech Engine;
- за воспроизведение аудио;
- за экспорт;
- за выполнение Workflow.

---

# 3. Aggregate Root

Project является Aggregate Root верхнего уровня.

Все остальные доменные объекты принадлежат одному Project.

Не допускается существование сущности без Project.

---

# 4. Lifecycle

Жизненный цикл Project.
=======
Project представляет собой корневой Aggregate Root всей предметной модели Voxarium.

Все пользовательские данные, независимо от их назначения, SHALL принадлежать ровно одному Project.

Никакие Domain Entity SHALL NOT существовать вне Project.

---

# 2. Responsibilities

Project SHALL отвечать за:

- владение всеми Domain Entity;
- управление жизненным циклом проекта;
- хранение глобальных метаданных;
- обеспечение ссылочной целостности;
- публикацию событий верхнего уровня;
- управление версиями проекта;
- регистрацию используемых компонентов;
- контроль совместимости формата проекта.

---

# 3. Non-Responsibilities

Project SHALL NOT:

- выполнять импорт;
- выполнять экспорт;
- выполнять генерацию речи;
- выполнять обработку аудио;
- обращаться к AI-моделям;
- обращаться к файловой системе;
- содержать алгоритмы Workflow;
- выполнять поиск.

Эти обязанности принадлежат Application Layer.

---

# 4. Aggregate Root

Project является Aggregate Root.

Следующие объекты могут изменяться только через Project:

- Source
- Document
- Role
- VoiceProfile
- Asset
- Workflow
- Production
- GenerationPreset

Изменение данных агрегата в обход Project запрещено.

---

# 5. Ownership

Project является владельцем следующих коллекций.

```
Project
│
├── Sources
├── Documents
├── Roles
├── VoiceProfiles
├── Assets
├── Workflows
├── Productions
└── GenerationPresets
```

Удаление Project SHALL удалять весь агрегат.

---

# 6. Identity

Каждый Project обязан иметь неизменяемый идентификатор.

Identifier SHALL:

- быть глобально уникальным;
- сохраняться в течение всей жизни проекта;
- использоваться при сериализации;
- использоваться всеми внутренними ссылками.

Identifier SHALL NOT изменяться.

---

# 7. Metadata

Project обязан содержать минимум следующие метаданные.

| Property | Required | Mutable |
|----------|----------|---------|
| Identifier | Yes | No |
| Name | Yes | Yes |
| Description | No | Yes |
| Version | Yes | Yes |
| FormatVersion | Yes | Yes |
| Language | Yes | Yes |
| Author | No | Yes |
| CreatedUtc | Yes | No |
| ModifiedUtc | Yes | Yes |
| ApplicationVersion | Yes | Yes |

Дополнительные свойства MAY быть добавлены в будущем без нарушения обратной совместимости.

---

# 8. Child Collections

Каждая дочерняя коллекция обладает следующими свойствами.

- уникальные идентификаторы элементов;
- детерминированный порядок хранения;
- возможность поиска по Identifier;
- отсутствие дубликатов.

---

# 9. Invariants

Project SHALL удовлетворять следующим инвариантам.

- Identifier уникален.
- Name не пустой.
- Version определена.
- FormatVersion определена.
- Все дочерние объекты имеют уникальные Identifier.
- Все ссылки указывают на существующие объекты.
- Не существует объектов без владельца.
- Не существует циклического владения.

Нарушение любого инварианта делает Project некорректным.

---

# 10. Lifecycle

Project проходит следующие состояния.
>>>>>>> c975edf (t)

```
Created

↓

Opened

↓

Modified

↓

Saved

↓

<<<<<<< HEAD
Archived (optional)

↓

=======
>>>>>>> c975edf (t)
Closed

↓

<<<<<<< HEAD
Deleted
```

Удаление является необратимой операцией.

---

# 5. Identity

Каждый Project имеет постоянный идентификатор.

Тип идентификатора:

```
UUID v7
```

Идентификатор создаётся один раз.

Изменение идентификатора запрещено.

---

# 6. Required Attributes

Каждый Project обязан содержать следующие обязательные атрибуты.

| Name | Type | Required | Mutable |
|----------|----------|----------|----------|
| id | UUIDv7 | Yes | No |
| name | String | Yes | Yes |
| formatVersion | Version | Yes | No |
| createdAt | DateTime UTC | Yes | No |
| updatedAt | DateTime UTC | Yes | Yes |
| defaultLanguage | LanguageCode | Yes | Yes |
| activeProductionId | UUID | Yes | Yes |

---

# 7. Optional Attributes

| Name | Type |
|----------|----------|
| description | String |
| author | String |
| organization | String |
| copyright | String |
| tags | List<String> |
| customProperties | Map<String, Value> |

Project обязан поддерживать произвольные пользовательские свойства.

---

# 8. Contained Collections

Project агрегирует следующие коллекции.

Sources

Documents

Productions

Roles

Voice Profiles

Generation Presets

Export Profiles

Assets

Plugin Data

Settings

Logs

Cache

Наличие дополнительных коллекций допускается только после изменения предметной модели.

---

# 9. Ownership Rules

Project является владельцем всех агрегатов.

Удаление Project приводит к удалению всех принадлежащих данных.

Совместное владение агрегатами несколькими Project запрещается.

---

# 10. Project State

Project может находиться в одном из состояний.

Created

Open

Modified

Saving

ReadOnly

Migrating

Corrupted

Closed

Переходы между состояниями определяются Command.

---

# 11. Invariants

Project обязан удовлетворять следующим инвариантам.

Project всегда содержит минимум одну Production.

Project всегда содержит один активный Production.

Project всегда содержит один активный язык.

Все идентификаторы внутри Project уникальны.

Каждая сущность принадлежит только одному Project.

Project никогда не содержит циклических зависимостей между агрегатами.

---

# 12. Relationships

Project

owns

Sources

Documents

Productions

Roles

Voice Profiles

Assets

Generation Presets

Export Profiles

Plugin Data

Settings

Project не владеет Plugin.

Project не владеет Core.

Project не владеет Runtime.

---

# 13. Commands

Следующие команды изменяют состояние Project.

CreateProject

OpenProject

RenameProject

ChangeProjectDescription

ChangeProjectLanguage

SaveProject

CloseProject

ArchiveProject

DeleteProject

RestoreProject

Каждая команда публикует соответствующий Domain Event.

---

# 14. Domain Events

ProjectCreated

ProjectOpened

ProjectModified

ProjectSaved

ProjectClosed

ProjectArchived

ProjectDeleted

ProjectRecovered

ProjectMigrated

ProjectCorrupted

---

# 15. Business Rules

Project обязан оставаться согласованным после любой операции.

Все изменения должны быть атомарными.

Любая ошибка изменения должна приводить к откату операции.

Частично изменённый Project считается повреждённым.

---

# 16. Serialization

Project является сериализуемой сущностью.

Сериализация не должна зависеть:

- от языка программирования;
- от ORM;
- от базы данных;
- от внутреннего представления памяти.

Конкретный формат определяется документами раздела `600_Project_Format`.

---

# 17. Persistence

Project должен поддерживать:

- создание;
- загрузку;
- сохранение;
- резервное копирование;
- миграцию;
- восстановление.

Механизм хранения определяется Storage Layer.

---

# 18. Versioning

Project содержит номер версии формата.

Изменение версии формата допускается исключительно механизмом миграции.

Ручное изменение версии запрещается.

---

# 19. Recovery

После аварийного завершения приложения Project должен быть восстановлен до последнего согласованного состояния.

Восстановление должно быть идемпотентным.

Повторное выполнение процедуры восстановления не должно изменять корректный Project.

---

# 20. Validation

Перед открытием Project должны быть проверены:

- формат проекта;
- структура каталогов;
- обязательные файлы;
- ссылки между сущностями;
- целостность идентификаторов;
- совместимость версии.

При обнаружении ошибок Project переводится в состояние Corrupted или ReadOnly в зависимости от характера проблемы.

---

# 21. Security

Project не должен содержать исполняемый код.

Project не должен автоматически выполнять сценарии, макросы или внешние программы.

Plugin Data рассматриваются как данные и не должны интерпретироваться Core как исполняемый код.

---

# 22. Extensibility

Project обязан предоставлять изолированные области хранения данных для Plugin.

Core не должен зависеть от внутреннего содержимого Plugin Data.

Добавление новых типов пользовательских данных не должно требовать изменения существующих агрегатов.

---

# 23. Performance Requirements

Открытие Project не должно требовать полной загрузки всех данных в оперативную память.

Архитектура должна поддерживать ленивую загрузку (Lazy Loading) крупных коллекций.

Доступ к отдельным агрегатам не должен требовать полного построения всей предметной модели.

---

# 24. Test Requirements

Должны существовать автоматические тесты, проверяющие:

- создание Project;
- сохранение;
- повторное открытие;
- миграцию;
- восстановление;
- проверку инвариантов;
- обнаружение повреждений;
- работу в режиме ReadOnly.

---

# 25. Compliance

Любая реализация сущности Project обязана соответствовать требованиям настоящего документа.

Изменение модели Project допускается только посредством изменения настоящей спецификации и оформления соответствующего ADR.
=======
Archived
```

Возврат из состояния Archived запрещён.

---

# 11. State Transitions

Допустимые переходы.

```
Created
    ↓
Opened

Opened
    ↓
Modified

Modified
    ↓
Saved

Saved
    ↓
Modified

Saved
    ↓
Closed

Closed
    ↓
Opened

Closed
    ↓
Archived
```

Недопустимые переходы SHALL завершаться ошибкой.

---

# 12. Creation Rules

Project SHALL создаваться исключительно Project Service.

Во время создания SHALL быть выполнены:

- генерация Identifier;
- создание обязательных коллекций;
- инициализация метаданных;
- установка версии формата;
- публикация события ProjectCreated.

---

# 13. Modification Rules

Любое изменение агрегата SHALL:

- выполняться через Application Layer;
- проверять инварианты;
- обновлять ModifiedUtc;
- публиковать соответствующее событие.

Прямое изменение дочерних коллекций запрещено.

---

# 14. Deletion Rules

Удаление Project допускается только после подтверждения пользователя.

Удаление SHALL:

- завершить все активные Workflow;
- отменить все Job;
- освободить ресурсы;
- удалить временные данные;
- удалить дочерние объекты.

Частичное удаление агрегата запрещено.

---

# 15. Persistence

Project не знает способа хранения.

Project SHALL сериализоваться исключительно через соответствующие Contracts.

Никакой код Domain SHALL NOT обращаться к файловой системе.

---

# 16. Concurrency

Project является объектом с эксклюзивной записью.

Допускается:

- конкурентное чтение;
- единственная операция записи.

Одновременное изменение агрегата несколькими потоками запрещено.

---

# 17. Domain Events

Project публикует следующие события.

- ProjectCreated
- ProjectOpened
- ProjectClosed
- ProjectSaved
- ProjectModified
- ProjectRenamed
- ProjectArchived
- ProjectFormatUpgraded

Полный состав событий определяется разделом `500_Events`.

---

# 18. Commands

Допустимые команды.

- CreateProject
- OpenProject
- SaveProject
- RenameProject
- CloseProject
- ArchiveProject
- UpgradeProjectFormat

Команды SHALL выполняться через Application Layer.

---

# 19. Relationships

Project владеет:

- Source
- Document
- Role
- VoiceProfile
- Workflow
- Production
- Asset
- GenerationPreset

Project НЕ владеет:

- Plugin
- AI Engine
- Runtime
- GUI Components

---

# 20. Error Conditions

Следующие ситуации SHALL считаться ошибками.

- дублирование Identifier;
- пустое имя проекта;
- повреждение ссылок;
- отсутствие обязательных коллекций;
- неизвестная версия формата;
- нарушение инвариантов.

Project SHALL NOT переходить в неконсистентное состояние.

---

# 21. Extension Rules

Plugin MAY:

- добавлять собственные метаданные;
- регистрировать собственные ресурсы;
- хранить собственные данные в предусмотренных разделах проекта.

Plugin SHALL NOT:

- изменять структуру агрегата;
- изменять обязательные свойства;
- изменять жизненный цикл Project.

---

# 22. AI Implementation Requirements

Реализация Project SHALL обеспечивать:

- полное соблюдение модели агрегата;
- невозможность обхода Aggregate Root;
- строгую проверку инвариантов;
- детерминированное поведение;
- отсутствие скрытого состояния.

Если реализация требует дополнительных архитектурных решений, спецификация должна быть дополнена до начала реализации.

---

# 23. Test Requirements

Минимальный набор тестов SHALL включать:

- создание проекта;
- открытие проекта;
- сохранение проекта;
- повторное открытие проекта;
- проверку уникальности Identifier;
- проверку всех инвариантов;
- проверку ссылочной целостности;
- проверку публикации Domain Events;
- проверку допустимых переходов состояний;
- проверку восстановления после сериализации.

---

# 24. Compliance Checklist

Реализация Project соответствует настоящей спецификации только если:

- Project является единственным Aggregate Root верхнего уровня;
- все дочерние объекты принадлежат Project;
- соблюдены все инварианты;
- реализованы все допустимые переходы состояний;
- реализованы все обязательные события;
- реализованы все обязательные команды;
- отсутствует прямой доступ к инфраструктуре;
- отсутствует скрытое состояние;
- соблюдена модель конкурентного доступа;
- обеспечена полная детерминированность поведения.
>>>>>>> c975edf (t)

---

End of Document