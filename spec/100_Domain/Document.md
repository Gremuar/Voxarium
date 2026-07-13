# Voxarium Software Architecture Specification

Document Path:
spec/100_Domain/Document.md

<<<<<<< HEAD
Document ID: DOM-103

Title: Document

Version: 1.0.0
=======
Document ID: DOM-003

Title: Document

Version: 2.0.0
>>>>>>> c975edf (t)

Status: Accepted

Classification: Normative

Depends On

<<<<<<< HEAD
- SAS-001 Glossary
- SAS-002 Domain Ontology
- SAS-003 Architecture Principles
- Project.md
- Source.md

Referenced By

- Timeline.md
- Fragment.md
- Import_Module.md
- Document_Module.md
- IImporter.md
- ITimelineService.md
- Project_Format.md
=======
- SAS-000 Project Philosophy
- SAS-001 Glossary
- SAS-002 Domain Ontology
- SAS-003 Architecture Principles
- Project
- Source

Referenced By

- Fragment
- Timeline
- Search_Index_Service
- Generation_Service
- Workflow_Engine
- Project_Service
>>>>>>> c975edf (t)

---

# 1. Purpose

<<<<<<< HEAD
Document является каноническим внутренним представлением текстового содержимого проекта.

Document существует исключительно внутри платформы Voxarium и не зависит от формата импортированного материала.

Document представляет собой единое нормализованное текстовое пространство, на основе которого выполняются все последующие операции платформы:

- анализ структуры;
- поиск;
- разбиение на Fragment;
- назначение Role;
- генерация речи;
- экспорт.

Никакой модуль системы не должен работать непосредственно с Source после завершения импорта.

---

# 2. Responsibility

Document отвечает исключительно за:

- хранение нормализованного текста;
- хранение структуры документа;
- отображение текста на Source;
- хранение пользовательской разметки;
- обеспечение стабильных ссылок на текстовые диапазоны.

Document не отвечает за:

- генерацию речи;
- хранение Speech Segment;
- выполнение Workflow;
- выбор Voice Profile;
- работу AI.

---

# 3. Aggregate

Document является Aggregate Root.

Document принадлежит одному Project.

Document не принадлежит Production.

Все Production используют один и тот же Document.

---

# 4. Business Motivation

Document существует для отделения пользовательской работы от формата исходных данных.

После импорта пользователь больше не работает с PDF, DOCX, EPUB или SRT.

Пользователь работает только с Document.

Это позволяет:

- менять Import Plugin без изменения проекта;
- создавать несколько Production;
- повторно импортировать Source;
- использовать единый механизм анализа текста;
- обеспечить независимость Core от файловых форматов.

---

# 5. Identity

Каждый Document обладает постоянным UUID v7.

Идентификатор создаётся один раз.

Изменение идентификатора запрещено.

---

# 6. Required Attributes

| Name | Type | Required | Mutable |
|----------|----------|----------|----------|
| id | UUIDv7 | Yes | No |
| title | String | Yes | Yes |
| language | LanguageCode | Yes | Yes |
| createdAt | UTC DateTime | Yes | No |
| updatedAt | UTC DateTime | Yes | Yes |
| rootNodeId | UUID | Yes | No |

---

# 7. Optional Attributes

| Name | Type |
|----------|----------|
| author | String |
| description | String |
| metadata | Map<String, Value> |

---

# 8. Internal Representation

Document обязан хранить текст в каноническом виде.

Внутреннее представление не должно зависеть от:

- PDF;
- DOCX;
- EPUB;
- FB2;
- Markdown;
- HTML;
- Subtitle Format.

Все специальные особенности форматов должны быть устранены на этапе импорта.

---

# 9. Text Model

Document представляет текст как последовательность логических блоков.

Минимальные типы блоков.

- Chapter
- Section
- Paragraph
- Dialogue
- Narration
- Quote
- Note
- Subtitle
- Stage Direction
- Custom Block

Архитектура должна позволять добавление новых типов без изменения Core.

---

# 10. Stable Text Ranges

Каждый участок текста должен обладать постоянным идентификатором.

Fragment никогда не должен ссылаться на абсолютную позицию символов.

Fragment всегда ссылается на стабильный Text Range.

Это позволяет безопасно редактировать Document без разрушения существующих ссылок.

---

# 11. Text Editing

Document поддерживает редактирование.

Допустимые операции.

- вставка текста;
- удаление текста;
- замена текста;
- объединение блоков;
- разделение блоков;
- изменение структуры.

Любое изменение публикует Domain Event.

---

# 12. Structural Editing

Document должен поддерживать изменение структуры независимо от содержимого.

Пользователь может:

- объединять главы;
- разделять главы;
- переносить разделы;
- изменять порядок блоков;
- создавать новые блоки.

---

# 13. Mapping to Source

Каждый логический блок может хранить ссылку на исходный Source.

Связь должна быть обратимой.

Пользователь должен иметь возможность определить происхождение любого участка текста.

Если Document построен из нескольких Source, отображение сохраняется отдельно для каждого Source.

---

# 14. Multiple Sources

Document может быть создан:

- из одного Source;
- из нескольких Source.

Порядок объединения определяется Import Plugin.

После создания Document происхождение каждого блока должно сохраняться.

---

# 15. Relationship with Timeline

Timeline строится на основании Document.

Timeline не хранит текст.

Timeline хранит ссылки на диапазоны Document.

Изменение Timeline не изменяет Document.

---

# 16. Relationship with Fragment

Fragment всегда связан с диапазоном текста внутри Document.

Несколько Fragment могут ссылаться на различные диапазоны одного Document.

Fragment не владеет текстом.

Document остаётся единственным владельцем текста.

---

# 17. Search

Document обязан поддерживать поиск.

Минимально поддерживаются.

- поиск по тексту;
- поиск по регулярному выражению;
- поиск без учёта регистра;
- поиск с учётом языка;
- поиск по пользовательским меткам.

Архитектура должна допускать полнотекстовую индексацию.

---

# 18. Annotation

Document поддерживает пользовательские аннотации.

Аннотации могут использоваться для:

- комментариев;
- редакторских пометок;
- указаний диктору;
- указаний AI;
- заметок.

Аннотации не являются частью текста.

---

# 19. Tags

Любой диапазон текста может иметь произвольное количество тегов.

Примеры.

Emotion

Important

Retry

Translated

Reviewed

Ignore

Custom

Типы тегов не ограничиваются Core.

---

# 20. Validation

Document должен удовлетворять следующим требованиям.

- отсутствуют циклические ссылки;
- отсутствуют повреждённые диапазоны;
- отсутствуют пересекающиеся структурные блоки;
- все ссылки на Source корректны;
- структура дерева валидна.

---

# 21. Immutability Rules

Document является изменяемой сущностью.

Однако каждое изменение должно выполняться через Command.

Прямое изменение внутренней структуры запрещено.

---

# 22. Versioning

Document обязан поддерживать внутреннее версионирование.

Каждое изменение создаёт новую ревизию.

Архитектура должна поддерживать возможность хранения полной истории изменений.

Конкретная стратегия хранения определяется документами раздела `600_Project_Format`.

---

# 23. Recovery

После аварийного завершения приложения Document должен быть восстановлен до последнего согласованного состояния.

Незавершённые изменения не должны приводить к повреждению структуры документа.

---

# 24. Performance Requirements

Document должен поддерживать работу с документами объёмом более 10 миллионов символов.

Редактирование не должно требовать полного копирования текста.

Архитектура должна поддерживать ленивую загрузку, частичную индексацию и инкрементальное обновление структуры.

---

# 25. Security

Document не должен содержать исполняемый код.

HTML, JavaScript, VBA, макросы, встроенные сценарии и аналогичные механизмы должны удаляться или переводиться в безопасное представление на этапе импорта.

---

# 26. Extensibility

Document должен поддерживать расширение структуры без изменения Core.

Plugin может добавлять:

- новые типы блоков;
- новые виды аннотаций;
- новые виды тегов;
- дополнительные метаданные.

Core не должен интерпретировать специализированные данные Plugin.
=======
Document представляет логически завершённый текстовый документ внутри проекта.

Document является основной структурной единицей предметной области, объединяющей текст, его логическую структуру, временную шкалу и результаты подготовки к генерации речи.

Document не является файлом.

Document является внутренним представлением текста после его импорта.

---

# 2. Responsibilities

Document SHALL отвечать за:

- хранение текстовой структуры;
- владение Fragment;
- владение Timeline;
- хранение метаданных документа;
- хранение информации о языке;
- хранение информации о состоянии подготовки;
- обеспечение ссылочной целостности внутри документа.

---

# 3. Non-Responsibilities

Document SHALL NOT:

- хранить исходный файл;
- выполнять импорт;
- выполнять экспорт;
- выполнять генерацию речи;
- хранить Audio;
- выполнять синтез речи;
- выполнять поиск;
- выполнять индексацию.

---

# 4. Aggregate

Document является Aggregate Root второго уровня.

Структура агрегата:

```
Project
    │
    └── Document
            │
            ├── Fragments
            │
            └── Timeline
                    │
                    └── SpeechSegments
```

Все изменения Fragment и Timeline SHALL выполняться через Document.

---

# 5. Ownership

Document принадлежит одному Project.

Document владеет:

- Fragment;
- Timeline.

Document НЕ владеет:

- Source;
- Role;
- VoiceProfile;
- Workflow;
- Production.

---

# 6. Identity

Document обязан иметь неизменяемый Identifier.

Identifier SHALL:

- быть уникальным внутри Project;
- использоваться всеми внутренними ссылками;
- сохраняться после сериализации;
- никогда не изменяться.

---

# 7. Metadata

Document содержит следующие свойства.

| Property | Required | Mutable |
|-----------|----------|---------|
| Identifier | Yes | No |
| Name | Yes | Yes |
| SourceId | Yes | No |
| Language | Yes | Yes |
| Description | No | Yes |
| CreatedUtc | Yes | No |
| ModifiedUtc | Yes | Yes |
| Revision | Yes | Yes |
| Status | Yes | Yes |

---

# 8. Status

Допустимые состояния.

- Imported
- Parsed
- Edited
- Validated
- ReadyForGeneration
- Archived

Document SHALL находиться ровно в одном состоянии.

---

# 9. Lifecycle

```
Imported

↓

Parsed

↓

Edited

↓

Validated

↓

ReadyForGeneration

↓

Archived
```

Переход в Archived является необратимым.

---

# 10. State Transition Rules

Допустимы только следующие переходы.

```
Imported
↓

Parsed

Parsed
↓

Edited

Edited
↓

Validated

Validated
↓

ReadyForGeneration

ReadyForGeneration
↓

Edited

Validated
↓

Archived

ReadyForGeneration
↓

Archived
```

Иные переходы SHALL завершаться ошибкой.

---

# 11. Source Relationship

Каждый Document SHALL ссылаться ровно на один Source.

Source SHALL существовать.

Удаление Source при существующем Document запрещено.

Document не копирует информацию Source.

---

# 12. Fragment Collection

Document содержит упорядоченную коллекцию Fragment.

Коллекция SHALL:

- иметь детерминированный порядок;
- не содержать дубликатов;
- обеспечивать поиск по Identifier;
- обеспечивать стабильность ссылок.

Изменение порядка SHALL выполняться через команды Document.

---

# 13. Timeline

Каждый Document содержит ровно один Timeline.

Timeline SHALL существовать всегда.

Пустой Timeline допустим.

Создание нескольких Timeline запрещено.

---

# 14. Language

Document имеет основной язык.

Все Fragment по умолчанию наследуют язык Document.

Fragment MAY переопределять язык.

---

# 15. Revision

Document содержит номер ревизии.

Ревизия SHALL увеличиваться при любом изменении структуры документа.

Изменение только служебных данных MAY не увеличивать ревизию.

---

# 16. Invariants

Document SHALL удовлетворять следующим требованиям.

- Identifier существует.
- Source существует.
- Timeline существует.
- Name не пустой.
- Все Fragment имеют уникальные Identifier.
- Все ссылки корректны.
- Нет дублирующихся Fragment.
- Нет циклических ссылок.
- Revision ≥ 1.

---

# 17. Creation Rules

Document создаётся исключительно через Import Service или Document Service.

При создании SHALL:

- создать Identifier;
- создать Timeline;
- создать пустую коллекцию Fragment;
- установить состояние Imported;
- опубликовать событие DocumentCreated.

---

# 18. Modification Rules

Любое изменение SHALL:

- проверять инварианты;
- увеличивать Revision (при структурных изменениях);
- обновлять ModifiedUtc;
- публиковать соответствующее Domain Event.

---

# 19. Deletion Rules

Удаление допускается только через Project.

Удаление SHALL удалить:

- Timeline;
- Fragment;
- Search Index;
- связанные SpeechSegment.

Document SHALL NOT удаляться напрямую другими объектами.

---

# 20. Relationships

```
Project
    │
    ├──── owns ───► Document
    │
    └──── owns ───► Source

Document
    │
    ├──── references ─► Source
    │
    ├──── owns ───────► Fragment
    │
    └──── owns ───────► Timeline
```

---

# 21. Concurrency

Document поддерживает:

- конкурентное чтение;
- единственную операцию записи.

Одновременное изменение несколькими потоками запрещено.

Изменения SHALL сериализоваться Application Layer.

---

# 22. Persistence

Document сериализуется исключительно как часть Project.

Document SHALL NOT знать:

- JSON;
- XML;
- SQLite;
- ZIP;
- файловую систему.

---

# 23. Domain Events

Document публикует:

- DocumentCreated
- DocumentOpened
- DocumentRenamed
- DocumentModified
- DocumentValidated
- DocumentArchived
- DocumentDeleted

---

# 24. Commands

Document поддерживает:

- CreateDocument
- RenameDocument
- ValidateDocument
- ArchiveDocument
- DeleteDocument
- RebuildTimeline
- ReorderFragments

---

# 25. Extension Rules

Plugin MAY:

- добавлять пользовательские свойства;
- хранить собственые метаданные;
- регистрировать пользовательские анализаторы.

Plugin SHALL NOT:

- изменять структуру агрегата;
- изменять обязательные свойства;
- создавать дополнительные Timeline;
- обходить Aggregate Root.

---

# 26. AI Implementation Requirements

ИИ SHALL реализовывать Document исключительно как Aggregate Root.

Недопустимо:

- изменять Fragment напрямую;
- изменять Timeline в обход Document;
- хранить скрытое состояние;
- нарушать инварианты.

Все операции изменения SHALL проходить через команды Application Layer.
>>>>>>> c975edf (t)

---

# 27. Test Requirements

<<<<<<< HEAD
Должны существовать автоматические тесты для проверки:

- создания Document;
- построения из одного Source;
- построения из нескольких Source;
- редактирования;
- поиска;
- отображения на Source;
- проверки ссылочной целостности;
- восстановления после сбоя;
- проверки стабильности Text Range;
- проверки версионирования.

---

# 28. Compliance

Любая реализация сущности Document обязана соответствовать требованиям настоящего документа.

Изменение модели Document допускается только посредством изменения настоящей спецификации и оформления соответствующего Architecture Decision Record.
=======
Обязательные тесты.

- создание Document;
- изменение имени;
- создание Timeline;
- создание Fragment;
- удаление Fragment;
- проверка ревизий;
- сериализация;
- десериализация;
- проверка всех инвариантов;
- проверка публикации событий;
- проверка допустимых переходов состояний.

---

# 28. Compliance Checklist

Реализация соответствует настоящей спецификации только если:

- Document является Aggregate Root;
- существует ровно один Timeline;
- существует ровно один Source;
- соблюдены все инварианты;
- реализованы все события;
- реализованы все команды;
- отсутствует доступ к Infrastructure;
- отсутствует скрытое состояние;
- обеспечена потокобезопасность;
- сериализация полностью воспроизводима.
>>>>>>> c975edf (t)

---

End of Document