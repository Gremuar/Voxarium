# Voxarium Software Architecture Specification

Document Path:
spec/100_Domain/Timeline.md

<<<<<<< HEAD
Document ID: DOM-104

Title: Timeline

Version: 1.0.0
=======
Document ID: DOM-004

Title: Timeline

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
- Production.md
- Document.md

Referenced By

- Fragment.md
- Workflow.md
- Playback_Module.md
- Generation_Module.md
- Export_Module.md
- ITimelineService.md
- Project_Format.md
=======
- SAS-000 Project Philosophy
- SAS-001 Glossary
- SAS-002 Domain Ontology
- SAS-003 Architecture Principles
- Project
- Document
- SpeechSegment

Referenced By

- Generation_Service
- Audio_Service
- Playback_Module
- Export_Service
- Production
- Workflow
>>>>>>> c975edf (t)

---

# 1. Purpose

<<<<<<< HEAD
Timeline является центральной сущностью производственного процесса Voxarium.

Timeline определяет логический сценарий создания аудиопроизведения.

Все операции генерации речи, предварительного прослушивания, экспорта, регенерации, редактирования и сборки аудио выполняются исключительно относительно Timeline.

Timeline не является текстом.

Timeline не является аудио.

Timeline представляет собой сценарий производства аудиоконтента.

---

# 2. Responsibility

Timeline отвечает исключительно за:

- порядок следования Fragment;
- логическую структуру озвучивания;
- организацию групп Fragment;
- управление ветвями производства;
- хранение пользовательских пометок;
- хранение редакторских комментариев;
- организацию областей генерации.

Timeline не отвечает за:

- хранение текста;
- хранение аудио;
- генерацию речи;
- выбор Speech Engine;
- выполнение Workflow.

---

# 3. Aggregate

Timeline является Aggregate Root.

Все Fragment принадлежат одному Timeline.

Fragment не может принадлежать нескольким Timeline одновременно.

---

# 4. Business Motivation

Timeline существует независимо от структуры Document.

Это позволяет пользователю:

- изменять порядок озвучивания;
- объединять несколько частей книги;
- пропускать отдельные участки;
- создавать альтернативные варианты озвучивания;
- создавать сокращённые версии;
- формировать различные сценарии экспорта.

Изменение Timeline не изменяет Document.

---

# 5. Identity

Каждый Timeline имеет постоянный UUID v7.

Идентификатор создаётся при создании Timeline.

Изменение идентификатора запрещается.

---

# 6. Required Attributes

| Name | Type | Required | Mutable |
|---------|---------|---------|---------|
| id | UUIDv7 | Yes | No |
| name | String | Yes | Yes |
| productionId | UUID | Yes | No |
| createdAt | UTC DateTime | Yes | No |
| updatedAt | UTC DateTime | Yes | Yes |
| rootGroupId | UUID | Yes | No |

---

# 7. Timeline Structure

Timeline представляет собой упорядоченное дерево.

Корневой элемент всегда существует.

Каждый узел дерева является одним из следующих типов.

- Group

- Fragment

- Marker

- Gap

- Branch

Добавление новых типов допускается посредством Plugin.

---

# 8. Ordering

Порядок элементов является явным.

Каждый элемент имеет:

- предыдущий элемент;
- следующий элемент;
- родительскую группу.

Абсолютные индексы не используются.

Архитектура должна поддерживать эффективную перестановку элементов без полного пересчёта структуры.

---

# 9. Groups

Group используется для логического объединения Fragment.

Примеры.

Глава

Сцена

Эпизод

Часть книги

Диалог

Музыкальная вставка

Произвольная пользовательская группа

Group не содержит собственного текста.

---

# 10. Fragment Placement

Каждый Fragment обязан принадлежать одной Group.

Fragment всегда располагается в одном месте Timeline.

Копирование Fragment создаёт новый Fragment.

Совместное использование одного Fragment несколькими ветвями запрещено.

---

# 11. Branches

Timeline обязан поддерживать ветвление.

Branch представляет альтернативный сценарий производства.

Примеры.

Основная версия

↓

Версия YouTube

↓

Версия без комментариев

↓

Версия с другой озвучкой

Все Branch используют один Document.

Каждый Branch содержит собственный набор Fragment.

---

# 12. Markers

Marker представляет логическую отметку.

Marker может использоваться для:

- начала главы;
- конца главы;
- контрольной точки;
- экспортной области;
- пользовательской навигации;
- автоматической генерации.

Marker не влияет на текст.

---

# 13. Gaps

Gap представляет искусственную паузу.

Gap не содержит текста.

Gap используется для:

- музыкальных вставок;
- пауз;
- рекламных блоков;
- звуковых эффектов;
- пользовательских задержек.

Gap имеет собственную длительность.

---

# 14. Enable / Disable

Любой Fragment может быть отключён.

Отключённый Fragment:

- не участвует в генерации;
- не участвует в экспорте;
- сохраняется в Timeline.

Удаление не требуется.

---

# 15. Locking

Любой элемент Timeline может быть заблокирован.

Заблокированный элемент запрещается:

- перемещать;
- изменять;
- удалять.

Генерация при этом допускается.

---

# 16. Selection

Timeline обязан поддерживать множественный выбор элементов.

Выбранные элементы используются для:

- пакетной генерации;
- массового назначения Role;
- пакетного изменения параметров;
- экспорта;
- удаления.

Selection не является частью предметной модели и относится к состоянию пользовательского интерфейса.

---

# 17. Commands

Следующие команды изменяют Timeline.

CreateTimeline

RenameTimeline

CreateGroup

DeleteGroup

MoveGroup

CreateFragment

MoveFragment

DuplicateFragment

DeleteFragment

CreateMarker

DeleteMarker

CreateGap

DeleteGap

CreateBranch

DeleteBranch

EnableFragment

DisableFragment

LockItem

UnlockItem

---

# 18. Domain Events

TimelineCreated

TimelineRenamed

FragmentMoved

FragmentCreated

FragmentDeleted

GroupCreated

GroupDeleted

BranchCreated

BranchDeleted

MarkerCreated

GapCreated

TimelineUpdated

---

# 19. Invariants

Timeline обязан удовлетворять следующим требованиям.

Существует ровно один Root Group.

Каждый Fragment принадлежит одному Timeline.

Каждый Fragment принадлежит одной Group.

Циклические ссылки запрещены.

Все элементы достижимы от Root Group.

Пустые ссылки запрещены.

Повреждённые ссылки запрещены.

---

# 20. Relationship with Document

Timeline не содержит текст.

Все текстовые данные находятся исключительно в Document.

Timeline хранит ссылки на Fragment.

Fragment хранит ссылки на диапазоны Document.

---

# 21. Relationship with Speech Segments

Timeline не хранит аудио.

Speech Segment связывается с Fragment.

Удаление Fragment не должно автоматически удалять Speech Segment.

Политика удаления определяется пользователем.

---

# 22. Relationship with Workflow

Workflow использует Timeline как источник задач.

Timeline не содержит информации о выполнении Workflow.

Состояние выполнения хранится отдельно.

---

# 23. Validation

При проверке Timeline должны контролироваться.

- отсутствие циклов;
- наличие Root Group;
- достижимость всех элементов;
- отсутствие дублирующихся UUID;
- корректность ссылок;
- корректность Branch;
- отсутствие недостижимых элементов.

---

# 24. Recovery

После аварийного завершения приложения Timeline должен быть восстановлен полностью.

Повреждение одного Fragment не должно делать недоступным весь Timeline.

Архитектура должна поддерживать частичное восстановление.
=======
Timeline представляет собой временную модель документа.

Timeline определяет последовательность воспроизведения SpeechSegment, их временные отношения, порядок генерации и итоговую структуру будущего аудиопроизведения.

Timeline является единственным источником истины о порядке воспроизведения речи внутри Document.

---

# 2. Responsibilities

Timeline SHALL отвечать за:

- хранение последовательности SpeechSegment;
- определение порядка воспроизведения;
- хранение временных параметров;
- хранение пауз;
- хранение переходов;
- контроль непротиворечивости последовательности;
- обеспечение синхронизации с Fragment.

---

# 3. Non-Responsibilities

Timeline SHALL NOT:

- хранить текст;
- хранить роли;
- хранить VoiceProfile;
- выполнять генерацию речи;
- хранить Audio;
- выполнять экспорт;
- выполнять микширование;
- выполнять воспроизведение.

---

# 4. Ownership

Timeline принадлежит Document.

```
Project
    │
    └── Document
            │
            └── Timeline
                    │
                    └── SpeechSegments
```

Timeline SHALL NOT существовать вне Document.

---

# 5. Aggregate Boundary

Timeline является частью Aggregate Document.

Timeline SHALL NOT изменяться напрямую.

Все изменения выполняются исключительно через Document.

---

# 6. Identity

Timeline имеет собственный Identifier.

Identifier SHALL:

- быть уникальным внутри Project;
- никогда не изменяться;
- использоваться всеми ссылками;
- сохраняться при сериализации.

---

# 7. Metadata

Timeline содержит следующие свойства.

| Property | Required | Mutable |
|----------|----------|---------|
| Identifier | Yes | No |
| DocumentId | Yes | No |
| Revision | Yes | Yes |
| Duration | Yes | Yes |
| CreatedUtc | Yes | No |
| ModifiedUtc | Yes | Yes |

Duration представляет расчётную продолжительность Timeline.

Фактическая продолжительность аудио может отличаться до выполнения генерации.

---

# 8. SpeechSegment Collection

Timeline содержит упорядоченную коллекцию SpeechSegment.

Коллекция SHALL:

- быть полностью упорядоченной;
- иметь стабильные Identifier;
- не содержать дубликатов;
- обеспечивать быстрый поиск по Identifier;
- поддерживать детерминированную сериализацию.

---

# 9. Ordering

Порядок SpeechSegment определяется исключительно Timeline.

Никакие другие объекты системы SHALL NOT определять порядок воспроизведения.

Изменение порядка допускается только через Document.

---

# 10. Temporal Model

Каждый SpeechSegment имеет временное положение относительно предыдущего сегмента.

Timeline хранит:

- последовательность;
- длительность пауз;
- пользовательские задержки;
- пользовательские смещения.

Абсолютное время начала сегментов вычисляется динамически.

Timeline SHALL NOT хранить абсолютные временные координаты.

---

# 11. Relationship With Fragment

Каждый SpeechSegment обязан ссылаться ровно на один Fragment.

Fragment MAY иметь:

- один SpeechSegment;
- несколько SpeechSegment (например, при разделении длинного текста).

SpeechSegment без Fragment существовать не может.

---

# 12. Timeline Integrity

Timeline SHALL удовлетворять следующим требованиям.

- отсутствуют циклы;
- отсутствуют недостижимые сегменты;
- отсутствуют дубли Identifier;
- отсутствуют ссылки на удалённые Fragment;
- последовательность полностью определена.

---

# 13. Lifecycle

Timeline проходит следующие состояния.

```
Created

↓

Built

↓

Validated

↓

Modified

↓

Locked

↓

Archived
```

---

# 14. State Description

Created

Создан пустой Timeline.

Built

Построена последовательность SpeechSegment.

Validated

Проверена целостность.

Modified

Изменён пользователем.

Locked

Используется активной генерацией.

Archived

Timeline принадлежит архивному Document.

---

# 15. Lock Rules

Во время выполнения генерации Timeline SHALL переходить в состояние Locked.

В состоянии Locked запрещается:

- изменение порядка сегментов;
- удаление сегментов;
- изменение пауз;
- изменение структуры Timeline.

Допускается только чтение.

---

# 16. Revision

Любое структурное изменение SHALL увеличивать Revision.

Изменение Revision происходит автоматически.

---

# 17. Invariants

Timeline SHALL удовлетворять следующим требованиям.

- существует ровно один Document;
- Identifier уникален;
- отсутствуют дубли Segment;
- все ссылки корректны;
- Revision ≥ 1;
- порядок полностью определён;
- Duration ≥ 0.

---

# 18. Creation Rules

Timeline создаётся автоматически при создании Document.

Во время создания SHALL:

- создать Identifier;
- создать пустую коллекцию SpeechSegment;
- установить Revision = 1;
- опубликовать событие TimelineCreated.

---

# 19. Modification Rules

Любое изменение SHALL:

- проверять инварианты;
- увеличивать Revision;
- обновлять ModifiedUtc;
- публиковать соответствующее событие.

Частично повреждённый Timeline сохраняться не может.

---

# 20. Deletion Rules

Timeline удаляется исключительно вместе с Document.

Самостоятельное удаление Timeline запрещено.

---

# 21. Persistence

Timeline сериализуется исключительно как часть Document.

Timeline SHALL NOT знать:

- файловую систему;
- JSON;
- XML;
- SQLite;
- ZIP;
- сетевые протоколы.

---

# 22. Concurrency

Timeline поддерживает:

- конкурентное чтение;
- единственную операцию записи.

Во время состояния Locked изменение запрещено.

---

# 23. Domain Events

Timeline публикует следующие события.

- TimelineCreated
- TimelineBuilt
- TimelineValidated
- TimelineModified
- TimelineLocked
- TimelineUnlocked
- TimelineArchived

---

# 24. Commands

Timeline поддерживает следующие команды через Document.

- BuildTimeline
- ValidateTimeline
- RebuildTimeline
- LockTimeline
- UnlockTimeline
- ReorderSpeechSegments
- UpdateSegmentTiming

Прямое выполнение команд Timeline запрещено.
>>>>>>> c975edf (t)

---

# 25. Performance Requirements

<<<<<<< HEAD
Timeline должен поддерживать проекты с количеством Fragment не менее 1 000 000.

Перемещение Fragment должно иметь сложность, близкую к O(1), независимо от размера Timeline.

Сворачивание и разворачивание Group не должно изменять внутреннюю структуру данных.

Загрузка дочерних элементов должна поддерживать ленивую и инкрементальную обработку.

---

# 26. Extensibility

Plugin могут добавлять:

- собственные типы Marker;
- собственные типы Group;
- дополнительные атрибуты элементов;
- пользовательские области Timeline;
- специальные производственные узлы.

Core не должен анализировать внутреннюю структуру расширений Plugin.

---

# 27. Test Requirements

Должны существовать автоматические тесты, проверяющие:

- создание Timeline;
- создание Group;
- создание Fragment;
- перестановку элементов;
- создание Branch;
- создание Marker;
- создание Gap;
- блокировку элементов;
- отключение Fragment;
- восстановление после сбоя;
- проверку инвариантов;
- работу с Timeline, содержащим более одного миллиона Fragment.

---

# 28. Compliance

Любая реализация сущности Timeline обязана соответствовать требованиям настоящего документа.

Изменение модели Timeline допускается только посредством изменения настоящей спецификации и оформления соответствующего Architecture Decision Record.
=======
Timeline SHALL поддерживать работу с документами, содержащими не менее:

- 100 000 SpeechSegment;
- 10 000 Fragment;
- 100 часов итогового аудио.

Типичные операции:

- поиск Segment;
- вставка Segment;
- удаление Segment;
- изменение порядка.

не должны требовать полного перестроения Timeline.

---

# 26. Extension Rules

Plugin MAY:

- добавлять пользовательские свойства Segment;
- реализовывать собственные алгоритмы построения Timeline;
- добавлять дополнительную служебную информацию.

Plugin SHALL NOT:

- изменять модель владения;
- изменять обязательные свойства;
- изменять порядок в обход Document.

---

# 27. AI Implementation Requirements

ИИ SHALL реализовывать Timeline как полностью детерминированную структуру данных.

Недопустимо:

- хранение скрытого порядка;
- вычисление порядка случайным образом;
- зависимость порядка от внутреннего расположения объектов в памяти;
- хранение абсолютных временных координат.

Все вычисления Timeline должны быть воспроизводимыми.

---

# 28. Test Requirements

Минимальный набор тестов SHALL включать.

- создание Timeline;
- построение Timeline;
- изменение порядка Segment;
- сериализацию;
- десериализацию;
- проверку Revision;
- проверку всех инвариантов;
- проверку состояния Locked;
- проверку публикации Domain Events;
- проверку работы с большим количеством Segment.

---

# 29. Compliance Checklist

Реализация Timeline соответствует настоящей спецификации только если:

- существует ровно один владелец (Document);
- соблюдены все инварианты;
- реализованы все состояния жизненного цикла;
- реализованы все события;
- реализованы все команды;
- отсутствует скрытое состояние;
- порядок воспроизведения полностью детерминирован;
- поддерживается потокобезопасное чтение;
- сериализация полностью воспроизводима;
- производительность соответствует установленным требованиям.
>>>>>>> c975edf (t)

---

End of Document