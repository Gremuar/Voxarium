# Voxarium Software Architecture Specification

Document Path:
spec/100_Domain/Role.md

<<<<<<< HEAD
Document ID: DOM-106

Title: Role

Version: 1.0.0
=======
Document ID: DOM-006

Title: Role

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
- Fragment.md

Referenced By

- VoiceProfile.md
- Emotion.md
- SpeechSegment.md
- Generation_Module.md
- CharacterDetection_Module.md
- Project_Format.md
=======
- SAS-000 Project Philosophy
- SAS-001 Glossary
- SAS-002 Domain Ontology
- SAS-003 Architecture Principles
- Project

Referenced By

- Fragment
- VoiceProfile
- SpeechSegment
- Voice_Service
- Generation_Service
>>>>>>> c975edf (t)

---

# 1. Purpose

<<<<<<< HEAD
Role представляет собой логическую роль (персонажа, диктора, рассказчика, системного голоса или иной сущности), которой принадлежат один или несколько Fragment.

Role является абстрактным описанием говорящего.

Role не является голосом.

Role не является аудиозаписью.

Role определяет **КТО говорит**, а Voice Profile определяет **КАК звучит этот говорящий**.

Это разделение является фундаментальным принципом архитектуры Voxarium.

---

# 2. Responsibility

Role отвечает исключительно за:

- идентификацию говорящего;
- объединение Fragment одного персонажа;
- хранение параметров поведения персонажа;
- хранение связей с Voice Profile;
- хранение пользовательских характеристик.

Role не отвечает за:

- генерацию речи;
- хранение аудио;
- выполнение Workflow;
- работу AI Engine;
- хранение текста.

---

# 3. Aggregate

Role является Aggregate Root.

Role принадлежит одному Project.

Role используется всеми Production данного Project.

Изменение Role автоматически влияет на все Production, если локальные переопределения отсутствуют.

---

# 4. Business Motivation

Разделение понятий Role и Voice Profile позволяет:

- менять голос персонажа без изменения структуры проекта;
- использовать одного персонажа в нескольких Production;
- создавать разные локализации;
- быстро переключать актеров озвучивания;
- повторно использовать персонажей в нескольких книгах одной серии (через будущий механизм Library).
=======
Role представляет собой абстрактную сущность, описывающую персонажа, диктора, рассказчика или любую другую логическую роль, от имени которой произносится текст.

Role НЕ является голосом.

Role НЕ является AI-моделью.

Role является семантической сущностью предметной области.

---

# 2. Responsibilities

Role SHALL отвечать за:

- идентификацию персонажа;
- хранение пользовательских метаданных;
- хранение описания персонажа;
- хранение предпочтительных VoiceProfile;
- хранение правил генерации речи;
- обеспечение согласованности озвучивания всех связанных Fragment.

---

# 3. Non-Responsibilities

Role SHALL NOT:

- хранить аудио;
- выполнять синтез речи;
- содержать параметры AI-модели;
- содержать модель клонирования голоса;
- выполнять генерацию;
- определять Timeline.

---

# 4. Ownership

Role принадлежит Project.

```
Project
    │
    └── Roles
            │
            └── Role
```

Role SHALL NOT принадлежать Document.
>>>>>>> c975edf (t)

---

# 5. Identity

<<<<<<< HEAD
Каждая Role обладает постоянным UUID v7.

UUID никогда не изменяется.

---

# 6. Required Attributes

| Name | Type | Required | Mutable |
|------|------|----------|----------|
| id | UUIDv7 | Yes | No |
| name | String | Yes | Yes |
| roleType | RoleType | Yes | Yes |
| defaultVoiceProfileId | UUID | Yes | Yes |
| createdAt | UTC DateTime | Yes | No |
| updatedAt | UTC DateTime | Yes | Yes |

---

# 7. Optional Attributes

| Name | Type |
|------|------|
| description | String |
| gender | Gender |
| ageCategory | AgeCategory |
| language | LanguageCode |
| defaultEmotionId | UUID |
| avatarAssetId | UUID |
| notes | String |
| metadata | Map<String, Value> |

---

# 8. Role Types

Минимальный перечень системных типов.

- Narrator
- Character
- Announcer
- System
- Translator
- Singer
- Background Voice
- Unknown

Plugin могут добавлять собственные типы.

---

# 9. Narrator

Каждый Project обязан содержать минимум одну системную Role типа Narrator.

Narrator используется для:

- авторского текста;
- описаний;
- ремарок;
- любых Fragment без явно определённого говорящего.

Удаление Narrator запрещается.

---

# 10. Character Detection

Role может быть создана:

- пользователем;
- автоматически AI;
- Import Plugin;
- Character Detection Plugin.

После автоматического определения пользователь остаётся окончательным владельцем решения.

AI никогда не изменяет существующие Role без явного подтверждения пользователя.

---

# 11. Relationship with Fragment

Каждый Fragment обязан ссылаться ровно на одну Role.

Role может использоваться любым количеством Fragment.

Изменение Role автоматически влияет на все связанные Fragment.

---

# 12. Relationship with Voice Profile

Role может иметь один голос по умолчанию.

Production может локально переопределить этот голос.

Fragment также может иметь собственное переопределение.

Приоритет разрешения определяется документом `Fragment.md`.

---

# 13. Relationship with Emotion

Role может содержать эмоцию по умолчанию.

Если Fragment не определяет эмоцию самостоятельно, используется значение Role.

---

# 14. Commands

CreateRole

RenameRole

MergeRoles

SplitRole

DeleteRole

AssignDefaultVoice

AssignDefaultEmotion

ChangeRoleType

---

# 15. Merge

Merge Roles объединяет две или более Role.

После объединения:

- все Fragment начинают ссылаться на новую Role;
- история изменений сохраняется;
- объединённые Role переводятся в состояние Archived.

Физическое удаление не выполняется.

---

# 16. Split

Split Role создаёт новую Role.

Пользователь выбирает Fragment, которые должны перейти к новой Role.

История происхождения должна сохраняться.

---

# 17. Domain Events

RoleCreated

RoleRenamed

RoleMerged

RoleSplit

RoleArchived

VoiceAssigned

EmotionAssigned

---

# 18. Invariants

Role обязана удовлетворять следующим требованиям.

Каждая Role имеет имя.

Каждая Role принадлежит одному Project.

Каждая Role имеет один Voice Profile по умолчанию.

Narrator существует всегда.

Две системные Role Narrator запрещены.

UUID уникален.

---

# 19. Validation

Перед сохранением проверяются:

- уникальность UUID;
- существование Voice Profile;
- существование Emotion;
- отсутствие циклических ссылок;
- корректность типа Role.

---

# 20. Recovery

После восстановления проекта все ссылки между Role и Fragment должны быть полностью восстановлены.

Отсутствующий Voice Profile не делает Role недействительной.

В этом случае используется механизм разрешения голоса по умолчанию.

---

# 21. Performance Requirements

Role должна оставаться лёгкой сущностью.

Количество связанных Fragment может достигать миллионов.

Получение списка Fragment не должно требовать хранения их идентификаторов внутри Role.

Связь должна быть реализована через индекс предметной модели.

---

# 22. Extensibility

Plugin могут расширять Role посредством:

- дополнительных характеристик персонажа;
- пользовательских классификаций;
- AI-атрибутов;
- биографии;
- параметров синтеза;
- внешних идентификаторов.

Core не должен анализировать данные расширений.

---

# 23. Test Requirements

Должны существовать автоматические тесты, проверяющие:

- создание Role;
- создание Narrator;
- объединение Role;
- разделение Role;
- назначение Voice Profile;
- автоматическое определение персонажей;
- восстановление ссылок;
- проверку инвариантов.

---

# 24. Future Compatibility

Архитектура должна поддерживать появление библиотеки Role.

В будущих версиях одна Role может экспортироваться в отдельный пакет и использоваться несколькими Project без изменения текущей модели.

Настоящий документ не определяет механизм такой библиотеки.

---

# 25. Compliance

Любая реализация сущности Role обязана соответствовать настоящему документу.

Изменение модели Role допускается исключительно посредством изменения настоящей спецификации и оформления соответствующего Architecture Decision Record.
=======
Каждый Role обязан иметь неизменяемый Identifier.

Identifier SHALL:

- быть уникальным внутри Project;
- использоваться всеми ссылками;
- никогда не изменяться;
- сохраняться при сериализации.

---

# 6. Metadata

Role содержит следующие свойства.

| Property | Required | Mutable |
|----------|----------|---------|
| Identifier | Yes | No |
| Name | Yes | Yes |
| Description | No | Yes |
| Color | No | Yes |
| Notes | No | Yes |
| Revision | Yes | Yes |

Color используется исключительно GUI.

Domain не определяет формат хранения цвета.

---

# 7. Preferred Voice

Role MAY иметь предпочтительный VoiceProfile.

```
Role

────────────► VoiceProfile
```

Предпочтительный VoiceProfile может отсутствовать.

Фактический VoiceProfile определяется Generation Service.

---

# 8. Relationships

Role может использоваться:

- Fragment;
- SpeechSegment;
- Workflow;
- Plugin.

Role никем не владеет.

---

# 9. Assignment Rules

Один Role может использоваться неограниченным количеством Fragment.

Каждый Fragment MAY иметь:

- одного Role;
- либо не иметь Role.

Назначение нескольких Role одному Fragment запрещено.

---

# 10. Lifecycle

```
Created

↓

Configured

↓

Active

↓

Archived
```

---

# 11. Active State

Role считается Active если:

- существует;
- не архивирован;
- может использоваться Fragment.

---

# 12. Archive Rules

Архивирование Role запрещает новые назначения.

Существующие Fragment сохраняют ссылку.

Автоматическое удаление ссылок не выполняется.

---

# 13. Invariants

Role SHALL удовлетворять следующим требованиям.

- Identifier существует.
- Name существует.
- Name не пустой.
- Revision ≥ 1.
- Identifier уникален.

---

# 14. Creation Rules

Role создаётся через Project Service.

Во время создания SHALL:

- создать Identifier;
- установить Revision = 1;
- опубликовать RoleCreated.

---

# 15. Modification Rules

Изменение допускается для:

- Name;
- Description;
- Notes;
- Preferred Voice.

Любое изменение SHALL:

- увеличивать Revision;
- публиковать RoleModified.

---

# 16. Merge Rules

Несколько Role MAY объединяться.

Во время объединения SHALL:

- выбрать целевой Role;
- переназначить все Fragment;
- переназначить SpeechSegment;
- архивировать остальные Role;
- опубликовать RoleMerged.

Identifier целевого Role сохраняется.

---

# 17. Deletion Rules

Удаление допускается только если отсутствуют ссылки.

Если Role используется хотя бы одним Fragment —

удаление SHALL завершаться ошибкой.

Рекомендуется архивирование.

---

# 18. Persistence

Role сериализуется как часть Project.

Role SHALL NOT знать:

- JSON;
- XML;
- файловую систему;
- AI Runtime.

---

# 19. Concurrency

Поддерживается:

- конкурентное чтение.

Не поддерживается:

- конкурентная запись.

---

# 20. Domain Events

Role публикует:

- RoleCreated
- RoleModified
- RoleArchived
- RoleMerged
- RoleDeleted
- PreferredVoiceChanged

---

# 21. Commands

Поддерживаются команды.

- CreateRole
- RenameRole
- ArchiveRole
- DeleteRole
- MergeRoles
- AssignPreferredVoice

---

# 22. Performance Requirements

Project SHALL поддерживать минимум:

- 10 000 Role;
- поиск по Identifier менее 5 мс;
- поиск по имени менее 20 мс.

---

# 23. Extension Rules

Plugin MAY:

- добавлять пользовательские свойства;
- добавлять собственные категории Role;
- хранить дополнительные метаданные.

Plugin SHALL NOT:

- изменять обязательные свойства;
- изменять Identifier;
- изменять правила владения.

---

# 24. AI Implementation Requirements

Role SHALL оставаться полностью независимой от конкретной технологии синтеза речи.

Запрещается хранить внутри Role:

- параметры XTTS;
- параметры Piper;
- параметры GPT-SoVITS;
- параметры StyleTTS;
- параметры любой конкретной AI-модели.

Role описывает исключительно персонажа предметной области.

---

# 25. Test Requirements

Минимальный набор тестов.

- создание Role;
- изменение имени;
- назначение Preferred Voice;
- объединение Role;
- архивирование;
- сериализация;
- десериализация;
- проверка инвариантов;
- проверка публикации событий.

---

# 26. Compliance Checklist

Реализация соответствует настоящей спецификации только если:

- Role принадлежит Project;
- Identifier неизменяем;
- отсутствует зависимость от AI-моделей;
- реализованы все события;
- реализованы все команды;
- соблюдены все инварианты;
- отсутствует скрытое состояние;
- сериализация воспроизводима;
- отсутствует доступ к Infrastructure.
>>>>>>> c975edf (t)

---

End of Document