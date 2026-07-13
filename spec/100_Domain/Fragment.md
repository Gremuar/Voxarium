# Voxarium Software Architecture Specification

Document Path:
spec/100_Domain/Fragment.md

<<<<<<< HEAD
Document ID: DOM-105

Title: Fragment

Version: 1.0.0
=======
Document ID: DOM-005

Title: Fragment

Version: 2.0.0
>>>>>>> c975edf (t)

Status: Accepted

Classification: Normative

Depends On

<<<<<<< HEAD
- SAS-001 Glossary
- SAS-002 Domain Ontology
- SAS-003 Architecture Principles
- Document.md
- Timeline.md
- Production.md

Referenced By

- Role.md
- VoiceProfile.md
- SpeechSegment.md
- Emotion.md
- Generation_Module.md
- Playback_Module.md
- Export_Module.md
- Project_Format.md
=======
- SAS-000 Project Philosophy
- SAS-001 Glossary
- SAS-002 Domain Ontology
- SAS-003 Architecture Principles
- Document
- Role
- Emotion

Referenced By

- Timeline
- SpeechSegment
- Generation_Service
- Voice_Service
- Search_Index_Service
>>>>>>> c975edf (t)

---

# 1. Purpose

<<<<<<< HEAD
Fragment является основной производственной единицей платформы Voxarium.

Именно Fragment представляет одну законченную реплику, повествовательный фрагмент, описание, субтитр или иной логически неделимый участок текста, который может быть независимо обработан системой.

Все операции генерации речи выполняются исключительно над Fragment.

Fragment является минимальной единицей:

- назначения роли;
- назначения голоса;
- генерации;
- регенерации;
- предварительного прослушивания;
- экспорта;
- оценки качества.

---

# 2. Responsibility

Fragment отвечает исключительно за:

- ссылку на текст Document;
- производственные параметры;
- назначенную Role;
- настройки генерации;
- ссылки на результаты генерации;
- пользовательские комментарии.

Fragment не отвечает за:

- хранение текста;
- хранение аудио;
- выполнение генерации;
- выполнение Workflow;
- выбор AI Engine.

---

# 3. Aggregate

Fragment принадлежит одному Timeline.

Fragment не может существовать вне Timeline.

Fragment не может принадлежать нескольким Timeline одновременно.

---

# 4. Business Motivation

Fragment является основной рабочей единицей пользователя.

Практически все действия пользователя выполняются именно над Fragment.

Пользователь может:

- прослушать Fragment;
- изменить голос;
- изменить эмоцию;
- изменить скорость речи;
- изменить произношение;
- изменить текст;
- выполнить регенерацию;
- сравнить версии генерации;
- принять или отклонить результат.

---

# 5. Identity

Каждый Fragment обладает постоянным UUID v7.

UUID никогда не изменяется.

Все версии генерации принадлежат одному Fragment.

---

# 6. Required Attributes

| Name | Type | Required | Mutable |
|------|------|----------|----------|
| id | UUIDv7 | Yes | No |
| documentRangeId | UUID | Yes | Yes |
| roleId | UUID | Yes | Yes |
| orderKey | String | Yes | Yes |
| state | FragmentState | Yes | Yes |
| enabled | Boolean | Yes | Yes |
| locked | Boolean | Yes | Yes |

---

# 7. Optional Attributes

| Name | Type |
|------|------|
| title | String |
| notes | String |
| emotionId | UUID |
| voiceProfileOverrideId | UUID |
| generationPresetOverrideId | UUID |
| exportFlags | Set |
| customProperties | Map<String, Value> |

---

# 8. Text Reference

Fragment никогда не хранит текст.

Fragment хранит исключительно ссылку на диапазон Document.

Document остаётся единственным владельцем текста.

Изменение текста автоматически отражается во всех связанных Fragment.

---

# 9. Role Assignment

Каждый Fragment обязан иметь одну назначенную Role.

Даже авторский текст принадлежит специальной системной роли Narrator.

Отсутствие Role запрещается.

---

# 10. Voice Resolution

Сам Fragment не хранит голос.

Алгоритм определения голоса:

Voice Override Fragment

↓

Role Voice Profile

↓

Production Default Voice

↓

Project Default Voice

↓

System Default Voice

Таким образом, Fragment всегда может быть озвучен.

---

# 11. Emotion Resolution

Fragment может переопределять эмоцию.

При отсутствии локального значения используется:

Role Emotion

↓

Production Default

↓

Engine Default

---

# 12. Generation Parameters

Fragment может переопределять:

- скорость речи;
- высоту голоса;
- громкость;
- температуру модели;
- seed;
- стиль речи;
- язык;
- произношение;
- словарь;
- паузы.

Все параметры являются необязательными.

---

# 13. Fragment State

Fragment может находиться только в одном состоянии.

New

Ready

Queued

Generating

Generated

Reviewed

Approved

Rejected

Failed

Disabled

Archived

---

# 14. State Machine

Допустимые переходы.

New

↓

Ready

↓

Queued

↓

Generating

↓

Generated

↓

Reviewed

↓

Approved

Допускаются переходы:

Generated → Rejected

Rejected → Queued

Generating → Failed

Failed → Queued

Approved → Archived

Disabled может быть установлен из любого состояния.

---

# 15. Speech Versions

Каждая генерация создаёт новую Speech Version.

Fragment хранит историю генераций.

Пользователь может:

- переключаться между версиями;
- удалять версии;
- закреплять лучшую;
- сравнивать версии.

Удаление текущей версии автоматически делает активной предыдущую.

---

# 16. Review

Fragment поддерживает процесс проверки качества.

Минимальные результаты проверки.

Approved

Rejected

Needs Regeneration

Needs Editing

Pending Review

Review не изменяет текст.

---

# 17. Comments

Fragment поддерживает произвольное количество комментариев.

Комментарии используются:

- редактором;
- диктором;
- AI;
- системой диагностики.

Комментарии не участвуют в генерации.

---

# 18. Tags

Fragment может иметь любое количество тегов.

Примеры.

Character

Music

Retry

Important

Translated

Needs Human Review

Favorite

Custom

---

# 19. Relationship with Speech Segment

Один Fragment может иметь множество Speech Segment.

Только один Speech Segment является активным.

Остальные считаются историческими версиями.

---

# 20. Relationship with Workflow

Workflow никогда не изменяет Fragment напрямую.

Изменение Fragment выполняется исключительно через Command.

---

# 21. Commands

CreateFragment

SplitFragment

MergeFragment

AssignRole

AssignVoiceOverride

AssignEmotion

QueueGeneration

StartGeneration

FinishGeneration

ApproveFragment

RejectFragment

ArchiveFragment

DeleteFragment

---

# 22. Domain Events

FragmentCreated

FragmentUpdated

FragmentSplit

FragmentMerged

FragmentQueued

GenerationStarted

GenerationCompleted

GenerationFailed

FragmentApproved

FragmentRejected

FragmentArchived

---

# 23. Invariants

Fragment обязан удовлетворять следующим требованиям.

Имеет одну Role.

Имеет ссылку на Document.

Принадлежит одному Timeline.

Имеет одно текущее состояние.

Имеет один активный Speech Segment либо не имеет ни одного.

Не содержит собственного текста.

---

# 24. Validation

Перед генерацией должны быть проверены:

- существование Document Range;
- существование Role;
- корректность Voice Profile;
- корректность Preset;
- доступность Engine;
- корректность состояния Fragment.

---

# 25. Recovery

При аварийном завершении генерации Fragment переводится в состояние Failed.

Частично созданные Speech Segment сохраняются только при наличии признака успешного восстановления.

В противном случае результаты считаются недействительными.
=======
Fragment представляет собой минимальную логическую единицу текста, с которой работает система.

Именно Fragment является объектом назначения роли, эмоции, параметров генерации и большинства пользовательских операций редактирования.

Fragment является основной единицей генерации речи.

---

# 2. Responsibilities

Fragment SHALL отвечать за:

- хранение текста;
- хранение логической позиции;
- хранение ссылок на Role;
- хранение ссылок на Emotion;
- хранение пользовательских параметров генерации;
- хранение состояния подготовки к генерации;
- обеспечение неизменности собственной идентичности.

---

# 3. Non-Responsibilities

Fragment SHALL NOT:

- хранить аудио;
- хранить SpeechSegment;
- определять порядок воспроизведения;
- выполнять синтез речи;
- обращаться к AI Engine;
- выполнять импорт;
- выполнять экспорт.

---

# 4. Ownership

Fragment принадлежит Document.

```
Project
    │
    └── Document
            │
            └── Fragment
```

Fragment SHALL NOT существовать вне Document.

---

# 5. Aggregate Membership

Fragment является Entity агрегата Document.

Изменение Fragment SHALL происходить исключительно через Document.

Прямое изменение Fragment другими объектами запрещено.

---

# 6. Identity

Каждый Fragment обязан иметь неизменяемый Identifier.

Identifier SHALL:

- быть уникальным внутри Project;
- использоваться всеми ссылками;
- сохраняться после сериализации;
- никогда не изменяться.

---

# 7. Fragment Types

Поддерживаются следующие типы Fragment.

- Narration
- Dialogue
- Thought
- Quote
- Heading
- Note
- Metadata
- Silence

Plugin MAY регистрировать дополнительные типы.

---

# 8. Text

Fragment содержит текст.

Текст SHALL:

- храниться в Unicode;
- сохранять все символы пользователя;
- поддерживать многострочное содержимое;
- не содержать служебной разметки приложения.

Fragment SHALL хранить исходный текст пользователя.

Нормализация текста выполняется Generation Service.

---

# 9. Metadata

Fragment содержит следующие свойства.

| Property | Required | Mutable |
|----------|----------|---------|
| Identifier | Yes | No |
| Type | Yes | Yes |
| Text | Yes | Yes |
| Language | No | Yes |
| RoleId | No | Yes |
| EmotionId | No | Yes |
| GenerationPresetId | No | Yes |
| Notes | No | Yes |
| Revision | Yes | Yes |

---

# 10. Relationships

Fragment может ссылаться на:

- Role
- Emotion
- GenerationPreset

Fragment SHALL NOT владеть этими объектами.

Все ссылки являются необязательными.

---

# 11. Position

Fragment имеет логический порядок внутри Document.

Порядок определяется исключительно Document.

Fragment SHALL NOT хранить собственный индекс.

Положение Fragment вычисляется из структуры Document.

---

# 12. Language

Fragment MAY переопределять язык Document.

Если язык не определён, используется язык Document.

---

# 13. Revision

Любое изменение текста SHALL увеличивать Revision.

Изменение только ссылок MAY также увеличивать Revision.

Revision SHALL быть монотонно возрастающим.

---

# 14. Lifecycle

```
Created

↓

Edited

↓

Validated

↓

ReadyForGeneration

↓

Archived
```

---

# 15. Generation State

Для генерации используются следующие состояния.

- NotGenerated
- Queued
- Generating
- Generated
- Invalidated

Изменение текста SHALL автоматически переводить состояние в Invalidated.

---

# 16. Invariants

Fragment SHALL удовлетворять следующим требованиям.

- Identifier существует.
- Text существует.
- Text не пустой.
- Revision ≥ 1.
- Все ссылки корректны.
- Type определён.
- Fragment принадлежит одному Document.

---

# 17. Creation Rules

Fragment создаётся только через Document.

Во время создания SHALL:

- создать Identifier;
- установить Revision = 1;
- установить состояние Created;
- опубликовать FragmentCreated.

---

# 18. Modification Rules

При изменении текста SHALL:

- обновить Revision;
- обновить Modified Timestamp Document;
- инвалидировать связанные SpeechSegment;
- опубликовать FragmentModified.

Изменение текста SHALL NOT изменять Identifier.

---

# 19. Split Rules

Fragment MAY быть разделён.

После разделения:

исходный Fragment удаляется;

создаются новые Fragment;

создаются новые Identifier;

публикуется FragmentSplit.

История операции сохраняется.

---

# 20. Merge Rules

Несколько Fragment MAY объединяться.

После объединения:

создаётся новый Fragment;

старые Fragment архивируются;

создаётся новый Identifier;

публикуется FragmentMerged.

---

# 21. Relationship With SpeechSegment

Fragment не хранит SpeechSegment.

SpeechSegment всегда ссылается на Fragment.

Один Fragment MAY использоваться несколькими SpeechSegment.

---

# 22. Persistence

Fragment сериализуется только как часть Document.

Fragment SHALL NOT знать:

- JSON;
- XML;
- файловую систему;
- SQLite;
- сетевые протоколы.

---

# 23. Concurrency

Допускается:

- конкурентное чтение.

Не допускается:

- конкурентное изменение.

Запись SHALL сериализоваться Application Layer.

---

# 24. Domain Events

Fragment публикует следующие события.

- FragmentCreated
- FragmentModified
- FragmentDeleted
- FragmentSplit
- FragmentMerged
- FragmentValidated
- FragmentArchived

---

# 25. Commands

Поддерживаются следующие команды.

- CreateFragment
- UpdateFragmentText
- AssignRole
- AssignEmotion
- AssignGenerationPreset
- SplitFragment
- MergeFragments
- DeleteFragment
>>>>>>> c975edf (t)

---

# 26. Performance Requirements

<<<<<<< HEAD
Fragment должен занимать минимальный объём памяти.

Загрузка истории Speech Version должна выполняться лениво.

Работа с миллионами Fragment должна быть возможна без полного размещения объектов в оперативной памяти.

---

# 27. Extensibility

Plugin могут добавлять:

- собственные параметры генерации;
- собственные состояния проверки;
- пользовательские метки;
- диагностические атрибуты;
- дополнительные правила генерации.

Core не должен зависеть от структуры расширений.

---

# 28. Test Requirements

Должны существовать автоматические тесты, проверяющие:

- создание Fragment;
- назначение Role;
- переопределение Voice;
- изменение состояния;
- очередь генерации;
- создание нескольких Speech Version;
- переключение между версиями;
- утверждение результата;
- отказ генерации;
- восстановление после сбоя;
- проверку инвариантов.

---

# 29. Compliance

Любая реализация сущности Fragment обязана соответствовать требованиям настоящего документа.

Изменение модели Fragment допускается только посредством изменения настоящей спецификации и оформления соответствующего Architecture Decision Record.
=======
Document SHALL поддерживать работу минимум с:

- 1 000 000 Fragment;
- временем поиска Fragment менее 10 мс по Identifier;
- линейной сериализацией структуры.

---

# 27. Extension Rules

Plugin MAY:

- добавлять собственные пользовательские свойства;
- регистрировать новые Fragment Type;
- хранить дополнительные метаданные.

Plugin SHALL NOT:

- изменять обязательные свойства;
- изменять Identifier;
- изменять правила владения.

---

# 28. AI Implementation Requirements

ИИ SHALL реализовывать Fragment как полностью независимую Entity.

Запрещается:

- использовать позицию как Identifier;
- хранить SpeechSegment внутри Fragment;
- хранить Audio внутри Fragment;
- хранить вычисляемые данные.

Все производные данные должны вычисляться другими сервисами.

---

# 29. Test Requirements

Минимальный набор тестов.

- создание Fragment;
- изменение текста;
- назначение Role;
- назначение Emotion;
- назначение GenerationPreset;
- разделение Fragment;
- объединение Fragment;
- проверка Revision;
- сериализация;
- десериализация;
- публикация событий;
- проверка инвариантов.

---

# 30. Compliance Checklist

Реализация соответствует настоящему документу только если:

- Fragment принадлежит Document;
- Identifier неизменяем;
- Text является единственным источником текстового содержимого;
- отсутствуют вычисляемые данные;
- реализованы все события;
- реализованы все команды;
- соблюдены все инварианты;
- отсутствуют скрытые зависимости;
- отсутствует доступ к Infrastructure;
- сериализация полностью воспроизводима.
>>>>>>> c975edf (t)

---

End of Document