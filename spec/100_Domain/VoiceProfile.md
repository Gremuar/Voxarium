# Voxarium Software Architecture Specification

Document Path:
spec/100_Domain/VoiceProfile.md

Document ID: DOM-107

Title: Voice Profile

Version: 1.0.0

Status: Accepted

Classification: Normative

Depends On

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

---

# 1. Purpose

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

---

# 5. Identity

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

---

# 20. Domain Events

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

---

End of Document