# Voxarium Software Architecture Specification

Document Path:
spec/100_Domain/GenerationPreset.md

Document ID: DOM-110

Title: Generation Preset

Version: 1.0.0

Status: Accepted

Classification: Normative

Depends On

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

---

# 1. Purpose

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

---

# 5. Identity

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

Fragment Override

↓

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

---

End of Document