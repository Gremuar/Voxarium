# Voxarium Software Architecture Specification

Document Path:
spec/100_Domain/SpeechSegment.md

Document ID: DOM-108

Title: Speech Segment

Version: 1.0.0

Status: Accepted

Classification: Normative

Depends On

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

---

# 1. Purpose

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

---

End of Document