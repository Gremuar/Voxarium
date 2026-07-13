# Voxarium Software Architecture Specification

Document Path:
spec/100_Domain/SpeechSegment.md

<<<<<<< HEAD
Document ID: DOM-108

Title: Speech Segment

Version: 1.0.0
=======
Document ID: DOM-008

Title: SpeechSegment

Version: 2.0.0
>>>>>>> c975edf (t)

Status: Accepted

Classification: Normative

Depends On

<<<<<<< HEAD
- SAS-001 Glossary
- SAS-002 Domain Ontology
- SAS-003 Architecture Principles
- Fragment.md
- VoiceProfile.md
- Production.md

Referenced By

- AudioTrack.md
- Playback_Module.md
- Export_Module.md
- Waveform_Module.md
- Cache_Module.md
- Project_Format.md
=======
- SAS-000 Project Philosophy
- SAS-001 Glossary
- SAS-002 Domain Ontology
- SAS-003 Architecture Principles
- Document
- Timeline
- Fragment
- Role
- VoiceProfile
- Emotion
- GenerationPreset

Referenced By

- Generation_Service
- Audio_Service
- Playback_Module
- Production
- Workflow
>>>>>>> c975edf (t)

---

# 1. Purpose

<<<<<<< HEAD
Speech Segment представляет собой результат одной успешной генерации речи для конкретного Fragment.

Speech Segment является неизменяемым объектом.

Каждая повторная генерация создаёт новый Speech Segment.

Изменение существующего Speech Segment запрещено.

---

# 2. Responsibility

Speech Segment отвечает исключительно за:

- представление результата генерации;
- хранение информации о происхождении результата;
- хранение ссылок на аудиоресурсы;
- хранение технических параметров генерации;
- обеспечение воспроизводимости результата.

Speech Segment не отвечает за:

- генерацию речи;
- хранение текста;
- выполнение Workflow;
- управление Timeline.

---

# 3. Aggregate

Speech Segment принадлежит одному Fragment.

Fragment может иметь множество Speech Segment.

Одновременно активным может быть только один Speech Segment.

---

# 4. Business Motivation

Speech Segment позволяет пользователю:

- хранить историю генераций;
- сравнивать различные варианты;
- быстро переключаться между версиями;
- не терять удачные результаты после повторной генерации;
- выполнять A/B-сравнение различных моделей.

---

# 5. Identity

Каждый Speech Segment обладает постоянным UUID v7.

UUID никогда не изменяется.

---

# 6. Required Attributes

| Name | Type | Required | Mutable |
|------|------|----------|----------|
| id | UUIDv7 | Yes | No |
| fragmentId | UUID | Yes | No |
| voiceProfileId | UUID | Yes | No |
| engineId | PluginId | Yes | No |
| createdAt | UTC DateTime | Yes | No |
| assetId | UUID | Yes | No |
| duration | Duration | Yes | No |
| sampleRate | Integer | Yes | No |
| channels | Integer | Yes | No |

---

# 7. Optional Attributes

| Name | Type |
|------|------|
| generationPresetId | UUID |
| generationParameters | EngineConfiguration |
| waveformPreviewId | UUID |
| loudnessLUFS | Float |
| peakLevel | Float |
| notes | String |
| metadata | Map<String, Value> |

---

# 8. Immutability

После завершения генерации изменение Speech Segment запрещено.

Запрещается изменять:

- аудиофайл;
- параметры генерации;
- Voice Profile;
- Engine;
- длительность;
- происхождение.

Любое изменение создаёт новый Speech Segment.

---

# 9. Audio Asset

Speech Segment не хранит аудио внутри себя.

Аудиоданные принадлежат сущности Asset.

Speech Segment содержит только ссылку на Asset.

Это позволяет:

- повторно использовать ресурсы;
- выполнять дедупликацию;
- отделить предметную модель от хранения файлов.

---

# 10. Generation Provenance

Каждый Speech Segment обязан хранить происхождение результата.

Минимально фиксируются:

- используемый TTS Plugin;
- версия Plugin;
- Voice Profile;
- Generation Preset;
- дата генерации;
- параметры генерации;
- версия модели;
- используемое устройство (CPU/GPU).

---

# 11. Quality Information

Speech Segment может содержать сведения о качестве.

Примеры:

- пользовательская оценка;
- автоматическая оценка;
- MOS (если поддерживается);
- наличие артефактов;
- необходимость регенерации.

Core не интерпретирует специализированные оценки Plugin.

---

# 12. Playback Metadata

Speech Segment может содержать дополнительные сведения.

- рекомендуемая громкость;
- точки начала и конца;
- обнаруженные паузы;
- длительность речи;
- длительность тишины;
- речевой темп.

Эти данные используются Playback и Export Module.

---

# 13. Relationship with Fragment

Fragment является владельцем Speech Segment.

Удаление Fragment не должно автоматически уничтожать Speech Segment.

Политика удаления определяется пользователем или настройками проекта.

---

# 14. Relationship with Voice Profile

Speech Segment всегда хранит ссылку на Voice Profile, использованный во время генерации.

Последующее изменение Voice Profile не изменяет существующие Speech Segment.

Это обеспечивает воспроизводимость результатов.

---

# 15. Relationship with Engine

Speech Segment обязан хранить идентификатор Plugin, выполнившего генерацию.

Даже если Plugin впоследствии удалён, информация о происхождении должна сохраняться.

---

# 16. Active Version

Fragment может иметь множество Speech Segment.

Один из них назначается активным.

Переключение активной версии не изменяет сами Speech Segment.

Изменяется только ссылка внутри Fragment.

---

# 17. Commands

RegisterSpeechSegment

ActivateSpeechSegment

ArchiveSpeechSegment

DeleteSpeechSegment

RateSpeechSegment

AddReview

---

# 18. Domain Events

SpeechSegmentCreated

SpeechSegmentActivated

SpeechSegmentArchived

SpeechSegmentDeleted

SpeechSegmentRated

---

# 19. Invariants

Speech Segment обязан удовлетворять следующим требованиям.

Имеет Fragment.

Имеет Voice Profile.

Имеет Asset.

Имеет Engine.

Имеет длительность.

Не содержит собственного аудио.

После создания является неизменяемым.

---

# 20. Validation

Перед регистрацией проверяются:

- существование Fragment;
- существование Voice Profile;
- существование Asset;
- доступность файла;
- корректность длительности;
- корректность аудиоформата.

---

# 21. Recovery

После восстановления проекта Speech Segment должен корректно восстанавливать связи:

- с Fragment;
- с Asset;
- с Voice Profile.

Отсутствие Plugin не должно делать Speech Segment недействительным.

Прослушивание должно оставаться возможным при наличии Asset.

---

# 22. Performance Requirements

Speech Segment должен быть лёгким объектом.

При открытии проекта запрещается автоматически загружать аудиофайл.

Загрузка аудио выполняется только при:

- воспроизведении;
- экспорте;
- анализе;
- построении Waveform.

---

# 23. Extensibility

Plugin могут добавлять:

- собственные метрики качества;
- дополнительные параметры синтеза;
- диагностические данные;
- служебные сведения.

Core рассматривает эти данные как непрозрачные расширения.

---

# 24. Test Requirements

Должны существовать автоматические тесты, проверяющие:

- регистрацию Speech Segment;
- неизменяемость;
- хранение происхождения;
- переключение активной версии;
- восстановление после сбоя;
- проверку ссылочной целостности;
- работу без установленного Plugin;
- проверку инвариантов.

---

# 25. Future Compatibility

Архитектура должна поддерживать:

- потоковую генерацию;
- многоканальный звук;
- пространственное аудио;
- дополнительные дорожки;
- альтернативные форматы хранения аудио.

Настоящий документ описывает только базовую модель.

---

# 26. Compliance

Любая реализация Speech Segment обязана соответствовать настоящему документу.

Изменение модели Speech Segment допускается исключительно посредством изменения настоящей спецификации и оформления соответствующего Architecture Decision Record.
=======
SpeechSegment представляет собой минимальную исполняемую единицу генерации речи.

SpeechSegment связывает семантическую модель документа (Fragment) с процессом синтеза речи.

Именно SpeechSegment передается в Generation Service.

SpeechSegment не содержит аудио.

SpeechSegment не является результатом генерации.

---

# 2. Responsibilities

SpeechSegment SHALL отвечать за:

- ссылку на Fragment;
- хранение параметров исполнения;
- выбор VoiceProfile;
- выбор Role;
- выбор Emotion;
- хранение GenerationPreset;
- хранение состояния генерации;
- хранение информации о результате генерации.

---

# 3. Non-Responsibilities

SpeechSegment SHALL NOT:

- хранить текст документа;
- хранить аудиоданные;
- выполнять синтез речи;
- выполнять обработку аудио;
- определять порядок воспроизведения;
- обращаться к AI Engine.

---

# 4. Ownership

SpeechSegment принадлежит Timeline.

```
Project
    │
    └── Document
            │
            └── Timeline
                    │
                    └── SpeechSegment
```

SpeechSegment SHALL NOT существовать вне Timeline.

---

# 5. Aggregate Membership

SpeechSegment является Entity агрегата Document.

Все изменения SHALL выполняться через Document.

Прямое изменение SpeechSegment запрещено.

---

# 6. Identity

Каждый SpeechSegment обязан иметь неизменяемый Identifier.

Identifier SHALL:

- быть уникальным внутри Project;
- использоваться всеми ссылками;
- сохраняться после сериализации;
- никогда не изменяться.

---

# 7. Relationships

SpeechSegment обязан ссылаться на:

- Fragment.

SpeechSegment MAY ссылаться на:

- Role;
- VoiceProfile;
- Emotion;
- GenerationPreset.

Все ссылки являются логическими.

SpeechSegment не владеет ни одним из перечисленных объектов.

---

# 8. Effective Configuration

Во время генерации используется эффективная конфигурация.

Она вычисляется следующим образом.

```
SpeechSegment

↓

GenerationPreset

↓

Role

↓

VoiceProfile

↓

Project Defaults
```

SpeechSegment хранит только пользовательские переопределения.

Производная конфигурация не сериализуется.

---

# 9. Metadata

SpeechSegment содержит следующие свойства.

| Property | Required | Mutable |
|----------|----------|---------|
| Identifier | Yes | No |
| FragmentId | Yes | No |
| RoleId | No | Yes |
| VoiceProfileId | No | Yes |
| EmotionId | No | Yes |
| GenerationPresetId | No | Yes |
| GenerationState | Yes | Yes |
| Revision | Yes | Yes |

---

# 10. Generation State

Допустимые состояния.

- Pending
- Queued
- Generating
- Generated
- Failed
- Invalidated
- Skipped

В каждый момент времени Segment SHALL находиться ровно в одном состоянии.

---

# 11. State Transition Rules

Допустимы следующие переходы.

```
Pending

↓

Queued

↓

Generating

↓

Generated


Generating

↓

Failed


Generated

↓

Invalidated


Invalidated

↓

Queued


Pending

↓

Skipped
```

Другие переходы запрещены.

---

# 12. Invalidated State

SpeechSegment SHALL переходить в состояние Invalidated если изменяется:

- текст Fragment;
- VoiceProfile;
- Role;
- Emotion;
- GenerationPreset.

Invalidated означает, что ранее сгенерированное аудио больше не является актуальным.

---

# 13. Generation Result

SpeechSegment SHALL хранить только логическое состояние результата.

Например:

- отсутствует результат;
- результат актуален;
- результат устарел;
- произошла ошибка.

Информация о самих аудиофайлах хранится вне SpeechSegment.

---

# 14. Invariants

SpeechSegment SHALL удовлетворять следующим требованиям.

- Identifier существует.
- Fragment существует.
- Revision ≥ 1.
- GenerationState определён.
- Все ссылки корректны.
- Segment принадлежит одному Timeline.

---

# 15. Creation Rules

SpeechSegment создаётся автоматически при построении Timeline.

Во время создания SHALL:

- создать Identifier;
- установить GenerationState = Pending;
- установить Revision = 1;
- опубликовать SpeechSegmentCreated.

---

# 16. Modification Rules

Любое изменение SHALL:

- увеличить Revision;
- проверить ссылки;
- инвалидировать результат генерации;
- опубликовать SpeechSegmentModified.

---

# 17. Split Rules

При разделении Fragment соответствующий SpeechSegment SHALL быть заменён новыми SpeechSegment.

Новые Segment получают новые Identifier.

---

# 18. Merge Rules

При объединении Fragment соответствующие SpeechSegment SHALL быть заменены новым SpeechSegment.

История предыдущих Segment сохраняется через Domain Events.

---

# 19. Persistence

SpeechSegment сериализуется как часть Timeline.

SpeechSegment SHALL NOT знать:

- файловую систему;
- формат аудио;
- путь к файлам;
- Runtime;
- AI Engine.

---

# 20. Concurrency

Допускается:

- конкурентное чтение.

Не допускается:

- конкурентное изменение.

---

# 21. Domain Events

SpeechSegment публикует:

- SpeechSegmentCreated
- SpeechSegmentModified
- SpeechSegmentQueued
- SpeechSegmentGenerationStarted
- SpeechSegmentGenerated
- SpeechSegmentFailed
- SpeechSegmentInvalidated
- SpeechSegmentDeleted

---

# 22. Commands

Поддерживаются команды.

- QueueSpeechSegment
- UpdateSpeechSegment
- AssignVoiceProfile
- AssignRole
- AssignEmotion
- AssignGenerationPreset
- InvalidateSpeechSegment
- RetrySpeechSegment

---

# 23. Performance Requirements

Timeline SHALL поддерживать:

- не менее 1 000 000 SpeechSegment;
- пакетное обновление состояния;
- пакетную постановку в очередь;
- эффективную фильтрацию по состояниям.

---

# 24. Extension Rules

Plugin MAY:

- добавлять собственные параметры исполнения;
- добавлять пользовательские метаданные;
- реализовывать дополнительные состояния через Extension Metadata.

Plugin SHALL NOT:

- изменять обязательные свойства;
- изменять Identifier;
- нарушать модель владения.

---

# 25. AI Implementation Requirements

SpeechSegment SHALL быть полностью независим от конкретного AI Engine.

Реализация SHALL NOT содержать:

- путь к модели;
- параметры GPU;
- параметры CUDA;
- внутренние параметры XTTS;
- внутренние параметры Piper;
- внутренние параметры Kokoro;
- внутренние параметры StyleTTS.

Все параметры конкретной технологии принадлежат Infrastructure Layer.

---

# 26. Test Requirements

Минимальный набор тестов.

- создание Segment;
- изменение VoiceProfile;
- изменение Role;
- изменение Emotion;
- постановка в очередь;
- успешная генерация;
- ошибка генерации;
- инвалидирование;
- сериализация;
- десериализация;
- проверка инвариантов;
- проверка событий.

---

# 27. Compliance Checklist

Реализация соответствует настоящей спецификации только если:

- Segment принадлежит Timeline;
- существует ссылка на Fragment;
- отсутствуют вычисляемые данные;
- отсутствует аудио;
- отсутствует зависимость от AI Runtime;
- реализованы все события;
- реализованы все команды;
- соблюдены все инварианты;
- сериализация полностью воспроизводима;
- отсутствует скрытое состояние.
>>>>>>> c975edf (t)

---

End of Document