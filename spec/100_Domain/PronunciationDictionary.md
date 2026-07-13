# Voxarium Software Architecture Specification

Document Path:
spec/100_Domain/PronunciationDictionary.md

Document ID: DOM-111

Title: Pronunciation Dictionary

Version: 1.0.0

Status: Accepted

Classification: Normative

Depends On

- SAS-001 Glossary
- SAS-002 Domain Ontology
- SAS-003 Architecture Principles
- Project.md
- Document.md

Referenced By

- Fragment.md
- GenerationPreset.md
- TTS_Plugin_API.md
- TextProcessing_Module.md
- Generation_Module.md
- Project_Format.md

---

# 1. Purpose

Pronunciation Dictionary представляет собой централизованный словарь правил произношения текста.

Словарь применяется перед передачей текста в Speech Engine.

Все преобразования выполняются логически, не изменяя исходный текст Document.

Document всегда остаётся неизменным.

Изменяется только текст, поступающий на генерацию речи.

---

# 2. Responsibility

Pronunciation Dictionary отвечает исключительно за:

- правила произношения;
- пользовательские словари;
- специальные правила языка;
- правила ударений;
- правила чтения сокращений;
- нормализацию текста перед синтезом.

Dictionary не отвечает за:

- генерацию речи;
- исправление текста;
- перевод;
- OCR;
- распознавание языка.

---

# 3. Business Motivation

Использование словаря позволяет:

- исправлять ошибки TTS;
- произносить редкие фамилии;
- правильно читать аббревиатуры;
- задавать ударения;
- создавать корпоративные словари;
- использовать один словарь во всех Production проекта.

---

# 4. Aggregate

Pronunciation Dictionary является Aggregate Root.

Project может содержать несколько словарей.

Одновременно активными могут быть несколько словарей.

---

# 5. Identity

Каждый Dictionary имеет постоянный UUID v7.

UUID никогда не изменяется.

---

# 6. Required Attributes

| Name | Type | Required | Mutable |
|------|------|----------|----------|
| id | UUIDv7 | Yes | No |
| name | String | Yes | Yes |
| language | LanguageCode | Yes | Yes |
| createdAt | UTC DateTime | Yes | No |
| updatedAt | UTC DateTime | Yes | Yes |

---

# 7. Dictionary Entry

Каждая запись словаря состоит из:

- Entry ID
- Pattern
- Replacement
- Rule Type
- Priority
- Enabled

Pattern представляет исходный текст.

Replacement представляет текст, который должен быть передан Speech Engine.

---

# 8. Rule Types

Минимально поддерживаются:

- Exact Match
- Case Insensitive
- Whole Word
- Regular Expression
- Prefix
- Suffix
- Contains
- Phonetic
- SSML
- Engine Specific

Plugin могут добавлять собственные типы.

---

# 9. Priority

Каждая запись имеет числовой приоритет.

Правила применяются в порядке убывания приоритета.

При совпадении используется первое успешно применённое правило.

---

# 10. Scope

Правило может иметь область действия.

Минимально:

- Entire Project
- Production
- Timeline
- Role
- Fragment
- Language

Одно правило может использоваться одновременно в нескольких областях.

---

# 11. Conditions

Правило может содержать дополнительные условия применения.

Примеры:

- только для Narrator;
- только для определённого Voice Profile;
- только для определённого языка;
- только для выбранного TTS Engine;
- только внутри диалогов;
- только в начале предложения.

Core предоставляет механизм проверки условий.

---

# 12. Resolution Pipeline

Перед генерацией текста применяется следующая последовательность.

Original Document Text

↓

Normalization

↓

Dictionary Rules

↓

Language Rules

↓

Engine Adapter

↓

Speech Engine

Изменения существуют только внутри Pipeline.

---

# 13. Engine Independence

Dictionary является полностью независимым от конкретного Speech Engine.

Если Engine поддерживает собственный словарь произношения, соответствующий Plugin самостоятельно выполняет преобразование правил.

Core не должен содержать Engine-специфичной логики.

---

# 14. Commands

CreateDictionary

DeleteDictionary

RenameDictionary

AddRule

UpdateRule

RemoveRule

EnableRule

DisableRule

ImportDictionary

ExportDictionary

---

# 15. Domain Events

DictionaryCreated

DictionaryDeleted

RuleAdded

RuleUpdated

RuleRemoved

RuleEnabled

RuleDisabled

DictionaryImported

DictionaryExported

---

# 16. Validation

При сохранении проверяются:

- корректность Pattern;
- корректность Replacement;
- отсутствие циклических замен;
- корректность регулярных выражений;
- корректность языка;
- допустимость Rule Type.

---

# 17. Conflict Resolution

Если несколько правил соответствуют одному участку текста:

1. применяется правило с наибольшим Priority;
2. при равенстве используется наиболее специфичное правило;
3. при полном совпадении выигрывает правило, созданное раньше.

Поведение должно быть детерминированным.

---

# 18. Relationship with Fragment

Fragment не содержит собственных правил произношения.

Fragment может только ссылаться на словарь либо использовать область действия Fragment в существующем словаре.

---

# 19. Relationship with Generation Preset

Preset может выбирать активный словарь по умолчанию.

При отсутствии выбора используется словарь проекта.

---

# 20. Recovery

После восстановления проекта словарь должен быть полностью восстановлен.

Ошибочная запись не должна делать недоступным весь словарь.

Недействительные правила автоматически пропускаются и отмечаются как Invalid.

---

# 21. Performance Requirements

Применение словаря должно выполняться потоковым способом.

Поиск правил должен иметь сложность, близкую к O(log n).

Архитектура должна поддерживать словари объёмом более 1 000 000 записей.

---

# 22. Extensibility

Plugin могут добавлять:

- собственные типы правил;
- специализированные фонетические модели;
- морфологические преобразования;
- языковые анализаторы;
- интеграцию с внешними словарями.

Core не должен зависеть от структуры расширений.

---

# 23. Test Requirements

Должны существовать автоматические тесты, проверяющие:

- создание словаря;
- применение правил;
- приоритеты;
- конфликтующие правила;
- регулярные выражения;
- импорт и экспорт;
- восстановление после сбоя;
- проверку производительности;
- проверку инвариантов.

---

# 24. Future Compatibility

Архитектура должна поддерживать:

- облачные словари;
- совместные словари команды;
- импорт словарей IPA;
- импорт словарей CMU;
- словари отдельных авторов;
- автоматическое пополнение словаря AI.

Настоящий документ определяет только предметную модель.

---

# 25. Compliance

Любая реализация Pronunciation Dictionary обязана соответствовать требованиям настоящего документа.

Изменение модели допускается исключительно посредством изменения настоящей спецификации и оформления соответствующего Architecture Decision Record.

---

End of Document