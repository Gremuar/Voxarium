# Voxarium Software Architecture Specification

Document Path:
spec/100_Domain/VoiceProfile.md

<<<<<<< HEAD
Document ID: DOM-107

Title: Voice Profile

Version: 1.0.0
=======
Document ID: DOM-007

Title: VoiceProfile

Version: 2.0.0
>>>>>>> c975edf (t)

Status: Accepted

Classification: Normative

Depends On

<<<<<<< HEAD
- SAS-001 Glossary
- SAS-002 Domain Ontology
- SAS-003 Architecture Principles
- Role.md
- Fragment.md

Referenced By

- SpeechSegment.md
- VoiceClone.md
- TTS_Plugin_API.md
- VoiceLibrary.md
- Generation_Module.md
- Playback_Module.md
- Export_Module.md
- Project_Format.md
=======
- SAS-000 Project Philosophy
- SAS-001 Glossary
- SAS-002 Domain Ontology
- SAS-003 Architecture Principles
- Project
- Role

Referenced By

- SpeechSegment
- GenerationPreset
- Voice_Service
- Generation_Service
- Workflow
>>>>>>> c975edf (t)

---

# 1. Purpose

<<<<<<< HEAD
Voice Profile представляет собой каноническое описание голоса, используемого платформой Voxarium.

Voice Profile является абстракцией над конкретной технологией синтеза речи.

Core никогда не работает с голосами конкретного TTS Engine напрямую.

Core взаимодействует исключительно с Voice Profile.

Любой Speech Engine обязан преобразовывать Voice Profile в собственное внутреннее представление.

---

# 2. Responsibility

Voice Profile отвечает исключительно за:

- описание голоса;
- хранение параметров синтеза;
- хранение информации о происхождении голоса;
- хранение ссылок на необходимые ресурсы;
- совместимость с несколькими Speech Engine;
- идентификацию голоса внутри Project.

Voice Profile не отвечает за:

- генерацию речи;
- выполнение AI-модели;
- хранение аудио;
- выполнение Workflow.

---

# 3. Business Motivation

Единая модель Voice Profile позволяет:

- менять TTS Engine без изменения проекта;
- использовать один голос в нескольких движках (если поддерживается);
- хранить библиотеку голосов;
- переносить проекты между компьютерами;
- повторно использовать клонированные голоса;
- отделить предметную модель от реализации синтеза речи.

---

# 4. Aggregate

Voice Profile является Aggregate Root.

Voice Profile принадлежит одному Project.

В перспективе архитектура должна поддерживать использование глобальной библиотеки Voice Profile без изменения модели Project.
=======
VoiceProfile представляет собой описание голоса, доступного системе для генерации речи.

VoiceProfile является абстракцией над конкретной технологией синтеза речи.

VoiceProfile описывает возможности голоса, но не способ его реализации.

VoiceProfile не является AI-моделью.

VoiceProfile не является Voice Engine.

VoiceProfile является Domain Entity.

---

# 2. Responsibilities

VoiceProfile SHALL отвечать за:

- идентификацию голоса;
- описание характеристик голоса;
- хранение пользовательского имени;
- хранение языка;
- хранение пола голоса;
- хранение поддерживаемых возможностей;
- хранение происхождения голоса;
- хранение статуса доступности.

---

# 3. Non-Responsibilities

VoiceProfile SHALL NOT:

- выполнять генерацию речи;
- хранить параметры AI Engine;
- содержать путь к модели;
- содержать путь к файлам;
- обращаться к GPU;
- обращаться к Runtime;
- выполнять клонирование голоса.

---

# 4. Ownership

VoiceProfile принадлежит Project.

```
Project
    │
    └── VoiceProfiles
            │
            └── VoiceProfile
```
>>>>>>> c975edf (t)

---

# 5. Identity

<<<<<<< HEAD
Каждый Voice Profile обладает постоянным UUID v7.

UUID не изменяется в течение всего жизненного цикла.

---

# 6. Required Attributes

| Name | Type | Required | Mutable |
|------|------|----------|----------|
| id | UUIDv7 | Yes | No |
| name | String | Yes | Yes |
| providerType | VoiceProviderType | Yes | No |
| createdAt | UTC DateTime | Yes | No |
| updatedAt | UTC DateTime | Yes | Yes |
| defaultLanguage | LanguageCode | Yes | Yes |

---

# 7. Optional Attributes

| Name | Type |
|------|------|
| description | String |
| gender | Gender |
| ageCategory | AgeCategory |
| tags | Set<String> |
| author | String |
| license | String |
| previewAssetId | UUID |
| metadata | Map<String, Value> |

---

# 8. Voice Provider Types

Минимально поддерживаются следующие категории.

- Native TTS Voice
- Cloned Voice
- Imported Voice
- Cloud Voice
- User Voice
- System Voice
- Plugin Voice

Core не должен ограничивать перечень типов.

---

# 9. Engine Independence

Voice Profile не содержит информации о внутреннем устройстве конкретного TTS Engine.

Запрещается хранить:

- внутренние классы Engine;
- ссылки на объекты памяти;
- сериализованные модели;
- структуры данных конкретного фреймворка.

Все специфические параметры должны храниться в Engine Configuration.

---

# 10. Voice Resources

Voice Profile может ссылаться на следующие ресурсы:

- модель голоса;
- файл эмбеддингов;
- словарь произношения;
- пользовательский лексикон;
- образец аудио;
- дополнительные модели;
- служебные данные Plugin.

Все ссылки выполняются через Asset.

---

# 11. Voice Parameters

Voice Profile может определять параметры по умолчанию.

Минимальный перечень.

- Speech Rate
- Pitch
- Volume
- Speaking Style
- Stability
- Similarity
- Emotion Intensity
- Seed
- Temperature

Каждый параметр может быть переопределён Fragment.

---

# 12. Voice Capabilities

Каждый Voice Profile должен публиковать свои возможности.

Минимальный перечень.

- Multilingual
- Voice Cloning
- Emotion Support
- Singing Support
- Streaming
- Real Time
- GPU Required
- Offline
- Online

Capabilities используются Core только для принятия решений.

---

# 13. Language Support

Voice Profile может поддерживать несколько языков.

Для каждого языка допускаются отдельные настройки.

Если язык Fragment не поддерживается Voice Profile, используется механизм разрешения несовместимости, определённый модулем Generation.

---

# 14. Relationship with Role

Role использует Voice Profile по умолчанию.

Несколько Role могут использовать один Voice Profile.

Удаление Voice Profile не должно автоматически удалять Role.

Пользователь обязан выбрать замену.

---

# 15. Relationship with Fragment

Fragment может локально переопределить Voice Profile.

При отсутствии локального переопределения используется Voice Profile, назначенный Role.

---

# 16. Relationship with Speech Engine

Каждый TTS Plugin обязан предоставить механизм преобразования Voice Profile в внутреннее представление своего Engine.

Core никогда не вызывает Engine напрямую.

Взаимодействие осуществляется исключительно через контракт `ISpeechEngine`.

---

# 17. Voice Origin

Voice Profile обязан хранить происхождение.

Минимально.

- создан пользователем;
- импортирован;
- клонирован;
- получен из Plugin;
- системный голос;
- получен из библиотеки.

---

# 18. Voice Cloning

Если Voice Profile создан клонированием, должны сохраняться:

- идентификатор процедуры клонирования;
- используемый Plugin;
- параметры клонирования;
- дата создания;
- используемые образцы.

Исходные аудиофайлы не являются частью Voice Profile.

Они принадлежат Asset.

---

# 19. Commands

CreateVoiceProfile

ImportVoiceProfile

CloneVoice

RenameVoice

AssignVoiceResource

DeleteVoiceProfile

DuplicateVoiceProfile

UpdateVoiceParameters
=======
Каждый VoiceProfile обязан иметь неизменяемый Identifier.

Identifier SHALL:

- быть уникальным внутри Project;
- использоваться всеми ссылками;
- сохраняться после сериализации;
- никогда не изменяться.

---

# 6. Metadata

VoiceProfile содержит следующие свойства.

| Property | Required | Mutable |
|----------|----------|---------|
| Identifier | Yes | No |
| Name | Yes | Yes |
| Description | No | Yes |
| Language | Yes | Yes |
| Gender | No | Yes |
| Provider | Yes | No |
| Origin | Yes | No |
| Status | Yes | Yes |
| Revision | Yes | Yes |

---

# 7. Provider

Provider определяет логического поставщика голоса.

Примеры:

- XTTS
- Piper
- Kokoro
- GPT-SoVITS
- StyleTTS
- Plugin

Provider используется только для выбора соответствующего Speech Engine.

Domain не определяет внутреннее устройство Provider.

---

# 8. Origin

Origin определяет происхождение VoiceProfile.

Допустимые значения.

- BuiltIn
- Imported
- Cloned
- Downloaded
- Plugin

Origin является неизменяемым после создания VoiceProfile.

---

# 9. Status

Поддерживаются следующие состояния.

- Available
- Missing
- Disabled
- Updating
- Invalid

Недоступный VoiceProfile может использоваться в Project, но не может участвовать в генерации речи.

---

# 10. Capabilities

VoiceProfile описывает поддерживаемые возможности.

Примеры.

- Emotion Support
- Multi Speaker
- Streaming
- Voice Cloning
- Speed Control
- Pitch Control
- Style Control

Capabilities являются описанием возможностей.

Они не содержат параметры реализации.

---

# 11. Preferred Usage

VoiceProfile MAY использоваться:

- Role;
- GenerationPreset;
- SpeechSegment.

VoiceProfile никем не владеет.

---

# 12. Relationships

```
Role

────────────► VoiceProfile


SpeechSegment

────────────► VoiceProfile


GenerationPreset

────────────► VoiceProfile
```

Все ссылки являются необязательными.

---

# 13. Lifecycle

```
Registered

↓

Available

↓

Disabled

↓

Archived
```

---

# 14. Registration Rules

VoiceProfile создаётся:

- после обнаружения Engine;
- после импорта;
- после клонирования;
- Plugin.

После регистрации публикуется VoiceProfileRegistered.

---

# 15. Invariants

VoiceProfile SHALL удовлетворять следующим требованиям.

- Identifier существует.
- Name существует.
- Provider определён.
- Origin определён.
- Language определён.
- Revision ≥ 1.

---

# 16. Modification Rules

Допускается изменение.

- Name;
- Description;
- Language;
- Status.

Provider изменяться не может.

Origin изменяться не может.

Identifier изменяться не может.

---

# 17. Deletion Rules

Удаление допускается только если отсутствуют ссылки.

Если VoiceProfile используется:

- Role;
- SpeechSegment;
- GenerationPreset;

удаление SHALL завершаться ошибкой.

Рекомендуется перевод в состояние Disabled.

---

# 18. Persistence

VoiceProfile сериализуется как часть Project.

VoiceProfile SHALL NOT знать:

- файловую систему;
- расположение модели;
- формат модели;
- GPU;
- Runtime;
- Plugin API.

---

# 19. Concurrency

Поддерживается:

- конкурентное чтение.

Не допускается:

- конкурентная запись.
>>>>>>> c975edf (t)

---

# 20. Domain Events

<<<<<<< HEAD
VoiceProfileCreated

VoiceImported

VoiceCloned

VoiceUpdated

VoiceDeleted

VoiceParametersChanged

VoiceResourceChanged

---

# 21. Invariants

Voice Profile обязан удовлетворять следующим требованиям.

UUID уникален.

Имеет имя.

Имеет Provider Type.

Имеет язык по умолчанию.

Все Asset существуют.

Отсутствуют циклические ссылки.

---

# 22. Validation

Перед использованием Voice Profile должны быть проверены:

- существование всех Asset;
- совместимость Plugin;
- доступность модели;
- поддержка языка;
- корректность параметров;
- целостность данных.

---

# 23. Recovery

После восстановления проекта Voice Profile должен полностью восстанавливать все связи с Asset.

Недоступность TTS Plugin не должна повреждать Project.

Voice Profile остаётся валидным даже при отсутствии установленного Plugin.

В этом случае генерация становится временно недоступной.

---

# 24. Performance Requirements

Voice Profile должен быть максимально компактной сущностью.

Загрузка моделей запрещена во время открытия Project.

Модели должны загружаться исключительно по требованию соответствующего Plugin.

Core никогда не хранит модель голоса в памяти.

---

# 25. Extensibility

Plugin могут расширять Voice Profile посредством собственных конфигураций.

Для этого используется Engine Configuration.

Core рассматривает Engine Configuration как непрозрачный объект.

Добавление нового Speech Engine не должно требовать изменения структуры Voice Profile.

---

# 26. Test Requirements

Должны существовать автоматические тесты, проверяющие:

- создание Voice Profile;
- импорт;
- клонирование;
- назначение Role;
- восстановление после сбоя;
- работу с несколькими языками;
- проверку ссылок на Asset;
- проверку совместимости Plugin;
- проверку инвариантов.

---

# 27. Future Compatibility

Архитектура должна поддерживать:

- глобальную библиотеку голосов;
- обмен Voice Profile между Project;
- маркетплейс Voice Profile;
- удалённые каталоги Voice Profile;
- синхронизацию библиотек;
- независимое обновление Voice Profile.

Настоящий документ определяет только внутреннюю модель.

---

# 28. Compliance

Любая реализация Voice Profile обязана соответствовать настоящему документу.

Изменение модели Voice Profile допускается исключительно посредством изменения настоящей спецификации и оформления соответствующего Architecture Decision Record.
=======
VoiceProfile публикует:

- VoiceProfileRegistered
- VoiceProfileUpdated
- VoiceProfileDisabled
- VoiceProfileEnabled
- VoiceProfileArchived
- VoiceProfileDeleted

---

# 21. Commands

Поддерживаются следующие команды.

- RegisterVoiceProfile
- UpdateVoiceProfile
- EnableVoiceProfile
- DisableVoiceProfile
- ArchiveVoiceProfile
- DeleteVoiceProfile

---

# 22. Performance Requirements

Project SHALL поддерживать:

- не менее 50 000 VoiceProfile;
- поиск по Identifier менее 5 мс;
- поиск по имени менее 20 мс;
- фильтрацию по Language, Provider и Origin.

---

# 23. Extension Rules

Plugin MAY:

- регистрировать новые Provider;
- добавлять новые Capability;
- добавлять собственные метаданные.

Plugin SHALL NOT:

- изменять обязательные свойства;
- изменять Identifier;
- нарушать модель владения.

---

# 24. AI Implementation Requirements

VoiceProfile является исключительно описанием голоса.

Реализация SHALL NOT хранить:

- путь к модели;
- параметры GPU;
- параметры Runtime;
- параметры конкретной библиотеки;
- внутренние идентификаторы AI Engine.

Эти данные принадлежат Infrastructure Layer.

---

# 25. Test Requirements

Минимальный набор тестов.

- регистрация VoiceProfile;
- изменение имени;
- изменение статуса;
- сериализация;
- десериализация;
- проверка всех инвариантов;
- проверка событий;
- проверка невозможности удаления используемого VoiceProfile.

---

# 26. Compliance Checklist

Реализация соответствует настоящей спецификации только если:

- VoiceProfile принадлежит Project;
- Identifier неизменяем;
- отсутствует зависимость от AI Runtime;
- отсутствует путь к модели;
- отсутствует скрытое состояние;
- реализованы все события;
- реализованы все команды;
- соблюдены все инварианты;
- сериализация полностью воспроизводима.
>>>>>>> c975edf (t)

---

End of Document