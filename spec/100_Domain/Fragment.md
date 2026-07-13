# Voxarium Software Architecture Specification

Document Path:
spec/100_Domain/Fragment.md

Document ID: DOM-105

Title: Fragment

Version: 1.0.0

Status: Accepted

Classification: Normative

Depends On

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

---

# 1. Purpose

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

---

# 26. Performance Requirements

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

---

End of Document