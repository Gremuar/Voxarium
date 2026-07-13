# Voxarium Software Architecture Specification

Document Path:
spec/100_Domain/Emotion.md

Document ID: DOM-112

Title: Emotion

Version: 1.0.0

Status: Accepted

Classification: Normative

Depends On

- SAS-001 Glossary
- SAS-002 Domain Ontology
- SAS-003 Architecture Principles
- Role.md
- Fragment.md
- VoiceProfile.md

Referenced By

- GenerationPreset.md
- Generation_Module.md
- TTS_Plugin_API.md
- Project_Format.md

---

# 1. Purpose

Emotion представляет собой независимую предметную сущность, описывающую эмоциональное состояние, с которым должен быть озвучен Fragment.

Emotion не является параметром конкретного Speech Engine.

Emotion является абстрактным семантическим описанием эмоционального окраса речи.

Каждый TTS Plugin самостоятельно преобразует Emotion во внутренние параметры используемого Speech Engine.

---

# 2. Responsibility

Emotion отвечает исключительно за:

- описание эмоционального состояния;
- хранение параметров интерпретации;
- обеспечение независимости проекта от конкретного Speech Engine;
- хранение пользовательских эмоций.

Emotion не отвечает за:

- генерацию речи;
- изменение текста;
- выполнение Workflow;
- выбор Voice Profile.

---

# 3. Business Motivation

Использование отдельной сущности Emotion позволяет:

- одинаково описывать эмоции для различных TTS Engine;
- централизованно изменять эмоциональную окраску;
- повторно использовать эмоции;
- автоматически преобразовывать эмоции в параметры конкретной модели.

---

# 4. Aggregate

Emotion является Aggregate Root.

Emotion принадлежит одному Project.

В дальнейшем архитектура должна поддерживать глобальную библиотеку Emotion.

---

# 5. Identity

Каждая Emotion обладает постоянным UUID v7.

UUID никогда не изменяется.

---

# 6. Required Attributes

| Name | Type | Required | Mutable |
|------|------|----------|----------|
| id | UUIDv7 | Yes | No |
| name | String | Yes | Yes |
| createdAt | UTC DateTime | Yes | No |
| updatedAt | UTC DateTime | Yes | Yes |

---

# 7. Optional Attributes

| Name | Type |
|------|------|
| description | String |
| intensity | Float |
| valence | Float |
| arousal | Float |
| tags | Set<String> |
| metadata | Map<String, Value> |

---

# 8. Standard Emotion Set

Core определяет минимальный рекомендуемый набор.

- Neutral
- Calm
- Happy
- Joy
- Excited
- Sad
- Angry
- Fear
- Surprise
- Whisper
- Serious
- Dramatic
- Friendly
- Confident
- Curious

Данный перечень не является закрытым.

---

# 9. Intensity

Каждая Emotion может иметь интенсивность.

Рекомендуемый диапазон:

0.0 — 1.0

Интенсивность является рекомендацией.

Конкретный Plugin самостоятельно определяет способ её интерпретации.

---

# 10. Emotional Dimensions

Для обеспечения совместимости между различными моделями Emotion может описываться через универсальные параметры.

Минимально поддерживаются:

- Valence
- Arousal
- Dominance

Plugin может использовать эти параметры вместо фиксированных категорий.

---

# 11. Engine Mapping

Каждый Speech Plugin самостоятельно отображает Emotion во внутренние параметры модели.

Например:

Neutral

↓

Style = Default

↓

Emotion Token = Neutral

↓

Temperature = 0.4

↓

Internal Engine Parameters

Core не участвует в этом преобразовании.

---

# 12. Relationship with Role

Role может иметь Emotion по умолчанию.

Все Fragment данной Role наследуют Emotion.

При наличии локального значения Fragment оно имеет больший приоритет.

---

# 13. Relationship with Fragment

Fragment может явно назначить Emotion.

Если Emotion отсутствует:

используется Emotion Role.

Если Role также не содержит Emotion:

используется значение Production.

Если оно отсутствует:

используется Engine Default.

---

# 14. Relationship with Generation Preset

Preset может определять параметры интерпретации Emotion.

Emotion остаётся предметной сущностью.

Preset определяет только особенности генерации.

---

# 15. Commands

CreateEmotion

RenameEmotion

DuplicateEmotion

DeleteEmotion

AssignEmotion

ImportEmotion

ExportEmotion

---

# 16. Domain Events

EmotionCreated

EmotionUpdated

EmotionAssigned

EmotionDeleted

EmotionImported

EmotionExported

---

# 17. Validation

При сохранении проверяются:

- уникальность UUID;
- корректность диапазонов;
- корректность интенсивности;
- корректность размерностей;
- отсутствие повреждённых ссылок.

---

# 18. Invariants

Emotion обязана удовлетворять следующим требованиям.

Имеет UUID.

Имеет имя.

Не зависит от конкретного Engine.

Может использоваться любым количеством Fragment.

---

# 19. Recovery

После восстановления проекта Emotion должна полностью восстановить все связи.

Отсутствие установленного Plugin не должно влиять на существование Emotion.

---

# 20. Performance Requirements

Emotion должна быть максимально лёгкой сущностью.

Получение Emotion должно иметь сложность O(1).

Загрузка дополнительных параметров выполняется лениво.

---

# 21. Extensibility

Plugin могут добавлять:

- собственные модели эмоций;
- дополнительные эмоциональные параметры;
- многомерные эмоциональные пространства;
- экспериментальные модели поведения.

Core рассматривает эти данные как непрозрачные расширения.

---

# 22. Test Requirements

Должны существовать автоматические тесты, проверяющие:

- создание Emotion;
- назначение Fragment;
- наследование от Role;
- интенсивность;
- экспорт;
- импорт;
- восстановление после сбоя;
- проверку инвариантов.

---

# 23. Future Compatibility

Архитектура должна поддерживать:

- динамические эмоции;
- эмоциональные кривые;
- изменение эмоций внутри Fragment;
- AI-генерацию эмоциональных профилей;
- библиотеки эмоций.

Настоящий документ описывает только предметную модель.

---

# 24. Compliance

Любая реализация Emotion обязана соответствовать требованиям настоящего документа.

Изменение модели Emotion допускается исключительно посредством изменения настоящей спецификации и оформления соответствующего Architecture Decision Record.

---

End of Document