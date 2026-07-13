# Voxarium Software Architecture Specification

Document Path:
spec/100_Domain/GenerationPreset.md

<<<<<<< HEAD
Document ID: DOM-110

Title: Generation Preset

Version: 1.0.0
=======
Document ID: DOM-011

Title: GenerationPreset

Version: 2.0.0
>>>>>>> c975edf (t)

Status: Accepted

Classification: Normative

Depends On

<<<<<<< HEAD
- SAS-001 Glossary
- SAS-002 Domain Ontology
- SAS-003 Architecture Principles
- VoiceProfile.md

Referenced By

- Fragment.md
- Production.md
- Workflow.md
- Generation_Module.md
- TTS_Plugin_API.md
- Project_Format.md
=======
- SAS-000 Project Philosophy
- SAS-001 Glossary
- SAS-002 Domain Ontology
- SAS-003 Architecture Principles
- Project
- VoiceProfile

Referenced By

- Fragment
- SpeechSegment
- Generation_Service
- Workflow
- Production
>>>>>>> c975edf (t)

---

# 1. Purpose

<<<<<<< HEAD
Generation Preset представляет собой именованный набор параметров генерации речи.

Preset позволяет повторно использовать одинаковые настройки генерации для различных Production, Role, Fragment и Workflow.

Generation Preset является независимой доменной сущностью.

Preset не принадлежит конкретному TTS Engine.

Preset является абстракцией над параметрами синтеза речи.

---

# 2. Responsibility

Generation Preset отвечает исключительно за:

- хранение параметров генерации;
- хранение политики наследования параметров;
- публикацию совместимых настроек для Speech Engine;
- обеспечение повторяемости генерации.

Preset не отвечает за:

- выполнение генерации;
- выбор голоса;
- хранение аудио;
- хранение текста.

---

# 3. Business Motivation

Использование Preset позволяет:

- применять одинаковые настройки ко всему проекту;
- быстро переключать режимы генерации;
- хранить корпоративные стандарты озвучивания;
- создавать специализированные шаблоны;
- повторно использовать параметры между проектами.

---

# 4. Aggregate

Generation Preset является Aggregate Root.

Preset принадлежит одному Project.

В дальнейшем допускается существование глобальной библиотеки Preset.
=======
GenerationPreset представляет собой именованный набор параметров генерации речи.

Preset позволяет повторно использовать одинаковые настройки генерации во множестве Fragment и SpeechSegment без дублирования параметров.

GenerationPreset является исключительно описанием пользовательских намерений.

Preset не содержит параметров конкретного AI Engine.

---

# 2. Responsibilities

GenerationPreset SHALL отвечать за:

- хранение параметров генерации;
- повторное использование настроек;
- централизованное управление параметрами;
- обеспечение наследования настроек;
- хранение пользовательских метаданных;
- обеспечение воспроизводимости генерации.

---

# 3. Non-Responsibilities

GenerationPreset SHALL NOT:

- выполнять генерацию речи;
- хранить путь к модели;
- хранить параметры GPU;
- хранить внутренние параметры конкретного движка;
- выполнять преобразование параметров;
- выбирать AI Engine.

---

# 4. Ownership

GenerationPreset принадлежит Project.

```
Project
    │
    └── GenerationPresets
            │
            └── GenerationPreset
```

Preset SHALL NOT существовать вне Project.
>>>>>>> c975edf (t)

---

# 5. Identity

<<<<<<< HEAD
Каждый Preset имеет постоянный UUID v7.

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
| tags | Set<String> |
| metadata | Map<String, Value> |

---

# 8. Canonical Parameters

Preset может содержать любые параметры генерации.

Core определяет только канонические параметры.

Минимальный перечень:

- Speech Rate
- Pitch
- Volume
- Temperature
- Seed
- Style
- Stability
- Similarity
- Emotion Strength
- Silence Threshold
- Pause Scale
- Pronunciation Dictionary
- Lexicon
- Language
- Output Sample Rate

Plugin могут добавлять собственные параметры.

---

# 9. Parameter Resolution

При генерации применяется следующий порядок разрешения параметров.
=======
Каждый GenerationPreset обязан иметь неизменяемый Identifier.

Identifier SHALL:

- быть уникальным внутри Project;
- использоваться всеми ссылками;
- никогда не изменяться;
- сохраняться после сериализации.

---

# 6. Metadata

GenerationPreset содержит следующие свойства.

| Property | Required | Mutable |
|----------|----------|---------|
| Identifier | Yes | No |
| Name | Yes | Yes |
| Description | No | Yes |
| Category | No | Yes |
| Revision | Yes | Yes |
| CreatedUtc | Yes | No |
| ModifiedUtc | Yes | Yes |

---

# 7. Preset Parameters

Preset MAY содержать следующие логические параметры.

- Preferred VoiceProfile;
- Speaking Rate;
- Speaking Style;
- Emotion Intensity;
- Volume;
- Pitch;
- Pause Policy;
- Pronunciation Dictionary;
- Text Normalization Policy;
- Language Override.

Все параметры являются логическими.

Конкретная интерпретация выполняется соответствующим Speech Engine.

---

# 8. Parameter Semantics

Параметры GenerationPreset описывают желаемый результат.

Preset SHALL NOT определять:

- численные коэффициенты конкретного движка;
- названия внутренних параметров AI Engine;
- параметры CUDA;
- параметры ONNX Runtime;
- параметры PyTorch.

Generation Service выполняет преобразование логических параметров в параметры конкретного Speech Engine.

---

# 9. Inheritance Model

Настройки вычисляются по следующему порядку приоритета.

```
SpeechSegment Override

↓
>>>>>>> c975edf (t)

Fragment Override

↓

<<<<<<< HEAD
Role Override

↓

Production Preset

↓

Project Default Preset

↓

Voice Profile Default

↓

Engine Default

Каждый следующий уровень используется только при отсутствии значения на предыдущем.

---

# 10. Engine Independence

Preset не содержит внутренние структуры конкретного Engine.

Любые Engine-специфичные параметры помещаются в раздел Engine Configuration.

Core рассматривает их как непрозрачные данные.

---

# 11. Compatibility

Каждый Preset публикует информацию о совместимости.

Минимально:

- поддерживаемые движки;
- минимальная версия Plugin;
- обязательные возможности Engine;
- несовместимые параметры.

При отсутствии совместимости решение принимает Generation Module.

---

# 12. Validation Rules

Preset должен проходить проверку перед использованием.

Проверяются:

- допустимые диапазоны параметров;
- совместимость языка;
- корректность типов;
- отсутствие конфликтующих параметров;
- поддержка выбранным Engine.

---

# 13. Relationship with Voice Profile

Voice Profile может содержать собственные значения параметров.

Preset имеет более высокий приоритет.

Voice Profile используется только для отсутствующих параметров.

---

# 14. Relationship with Production

Production может иметь один Preset по умолчанию.

Все Fragment используют этот Preset, если локальное переопределение отсутствует.

---

# 15. Relationship with Fragment

Fragment может использовать любой Preset.

Fragment также может переопределять отдельные параметры Preset.

---

# 16. Commands

CreatePreset

RenamePreset

DuplicatePreset

DeletePreset

ValidatePreset

AssignPreset

ExportPreset

ImportPreset

---

# 17. Domain Events

PresetCreated

PresetUpdated

PresetDeleted

PresetValidated

PresetAssigned

PresetImported

PresetExported

---

# 18. Invariants

Preset обязан удовлетворять следующим требованиям.

UUID уникален.

Имеет имя.

Все параметры имеют корректные типы.

Отсутствуют конфликтующие значения.

---

# 19. Recovery

После восстановления проекта все Preset должны быть полностью восстановлены.

Отсутствие установленного Plugin не должно повреждать Preset.

Engine-специфичные параметры сохраняются даже при отсутствии соответствующего Plugin.

---

# 20. Performance Requirements

Preset должен быть лёгким объектом.

Получение параметров должно выполняться без обращения к TTS Engine.

Разрешение параметров должно иметь сложность O(1).

---

# 21. Extensibility

Plugin могут добавлять:

- собственные параметры;
- собственные группы параметров;
- диагностические настройки;
- экспериментальные функции.

Core не должен анализировать внутреннюю структуру расширений.

---

# 22. Test Requirements

Должны существовать автоматические тесты, проверяющие:

- создание Preset;
- наследование параметров;
- разрешение конфликтов;
- проверку диапазонов;
- совместимость с Engine;
- импорт и экспорт;
- восстановление после сбоя;
- проверку инвариантов.

---

# 23. Future Compatibility

Архитектура должна поддерживать:

- глобальную библиотеку Preset;
- обмен Preset между проектами;
- облачную синхронизацию;
- версионирование Preset;
- корпоративные каталоги Preset.

Настоящий документ описывает только внутреннюю модель.

---

# 24. Compliance

Любая реализация Generation Preset обязана соответствовать требованиям настоящего документа.

Изменение модели Preset допускается исключительно посредством изменения настоящей спецификации и оформления соответствующего Architecture Decision Record.
=======
GenerationPreset

↓

Project Defaults

↓

Engine Defaults
```

Каждый следующий уровень используется только при отсутствии значения на предыдущем уровне.

---

# 10. Relationships

GenerationPreset MAY использоваться:

- Fragment;
- SpeechSegment;
- Workflow.

Preset никем не владеет.

---

# 11. Lifecycle

```
Created

↓

Active

↓

Archived
```

Архивированный Preset не может назначаться новым объектам.

Существующие ссылки сохраняются.

---

# 12. Invariants

GenerationPreset SHALL удовлетворять следующим требованиям.

- Identifier существует.
- Name существует.
- Name не пустой.
- Revision ≥ 1.

---

# 13. Creation Rules

GenerationPreset создаётся через Generation Service.

Во время создания SHALL:

- создать Identifier;
- установить Revision = 1;
- опубликовать GenerationPresetCreated.

---

# 14. Modification Rules

Допускается изменение:

- Name;
- Description;
- Category;
- логических параметров.

Любое изменение SHALL:

- увеличивать Revision;
- публиковать GenerationPresetModified;
- инвалидировать связанные SpeechSegment.

---

# 15. Deletion Rules

Удаление допускается только при отсутствии ссылок.

Если Preset используется хотя бы одним Fragment или SpeechSegment —

удаление SHALL завершаться ошибкой.

Рекомендуется архивирование.

---

# 16. Effective Configuration

Во время генерации вычисляется Effective Generation Configuration.

Алгоритм вычисления SHALL быть полностью детерминированным.

Результат вычисления SHALL NOT сериализоваться.

Результат SHALL существовать только во время выполнения Generation Service.

---

# 17. Persistence

GenerationPreset сериализуется как часть Project.

Preset SHALL NOT знать:

- формат хранения;
- файловую систему;
- Runtime;
- AI Engine;
- Plugin API.

---

# 18. Concurrency

Поддерживается:

- конкурентное чтение.

Не допускается:

- конкурентная запись.

---

# 19. Domain Events

GenerationPreset публикует:

- GenerationPresetCreated
- GenerationPresetModified
- GenerationPresetArchived
- GenerationPresetDeleted

---

# 20. Commands

Поддерживаются команды.

- CreateGenerationPreset
- UpdateGenerationPreset
- ArchiveGenerationPreset
- DeleteGenerationPreset

---

# 21. Performance Requirements

Project SHALL поддерживать:

- не менее 10 000 Preset;
- массовое применение Preset;
- быстрое вычисление Effective Configuration.

Изменение одного Preset SHALL NOT требовать немедленного пересчёта всех SpeechSegment.

Инвалидация SHALL выполняться лениво (Lazy Invalidation).

---

# 22. Extension Rules

Plugin MAY:

- добавлять собственные логические параметры;
- добавлять пользовательские категории;
- расширять метаданные.

Plugin SHALL NOT:

- изменять обязательные свойства;
- изменять Identifier;
- нарушать модель наследования.

---

# 23. AI Implementation Requirements

GenerationPreset SHALL быть полностью независимым от конкретной технологии синтеза речи.

Запрещается хранить:

- параметры XTTS;
- параметры Piper;
- параметры Kokoro;
- параметры GPT-SoVITS;
- параметры StyleTTS;
- параметры Coqui;
- параметры CUDA;
- параметры ONNX Runtime.

Все подобные сведения принадлежат Infrastructure Layer.

---

# 24. Test Requirements

Минимальный набор тестов.

- создание Preset;
- изменение параметров;
- наследование параметров;
- вычисление Effective Configuration;
- сериализация;
- десериализация;
- проверка инвариантов;
- проверка публикации событий;
- проверка Lazy Invalidation.

---

# 25. Compliance Checklist

Реализация соответствует настоящей спецификации только если:

- GenerationPreset принадлежит Project;
- Identifier неизменяем;
- реализована модель наследования;
- отсутствует зависимость от AI Engine;
- отсутствуют вычисляемые данные в сериализованном виде;
- реализованы все события;
- реализованы все команды;
- соблюдены все инварианты;
- сериализация полностью воспроизводима.
>>>>>>> c975edf (t)

---

End of Document