# Voxarium Software Architecture Specification

Document Path:
spec/100_Domain/Production.md

Document ID: DOM-101

Title: Production

Version: 1.0.0

Status: Accepted

Classification: Normative

Depends On

- SAS-001 Glossary
- SAS-002 Domain Ontology
- SAS-003 Architecture Principles
- Project.md

Referenced By

- Timeline.md
- Fragment.md
- SpeechSegment.md
- AudioTrack.md
- Workflow.md
- GenerationPreset.md
- ExportProfile.md

---

# 1. Purpose

Production представляет собой независимую производственную редакцию проекта.

Production предназначен для хранения полного набора данных, необходимых для создания одного законченного варианта озвучки.

Несколько Production могут использовать один и тот же исходный Document, одни и те же Role и одни и те же Voice Profile, но содержать различные результаты генерации, различные настройки, различные Timeline и различные аудиофайлы.

Production является основной рабочей областью пользователя после завершения импорта проекта.

---

# 2. Responsibility

Production отвечает исключительно за:

- организацию процесса генерации речи;
- хранение Timeline;
- хранение результатов генерации;
- хранение производственных настроек;
- хранение Workflow;
- хранение результатов экспорта;
- хранение состояния процесса производства.

Production не отвечает за:

- импорт документов;
- хранение исходного текста;
- управление Project;
- работу Plugin;
- выполнение Speech Engine.

---

# 3. Aggregate Root

Production является Aggregate Root.

Все сущности, относящиеся к процессу генерации речи, принадлежат одной Production.

Запрещается совместное использование производственных сущностей несколькими Production.

---

# 4. Business Motivation

Production позволяет создавать различные варианты одного произведения без копирования всего проекта.

Типичные сценарии.

• Мужская версия озвучки

• Женская версия озвучки

• Детская версия

• Английская локализация

• Черновая генерация

• Финальная редакция

• Версия для YouTube

• Версия для аудиокниги

Каждый такой вариант является отдельной Production.

---

# 5. Identity

Каждая Production обладает постоянным UUID v7.

Изменение идентификатора запрещено.

---

# 6. Required Attributes

| Name | Type | Required | Mutable |
|---------|---------|---------|---------|
| id | UUIDv7 | Yes | No |
| name | String | Yes | Yes |
| createdAt | UTC DateTime | Yes | No |
| updatedAt | UTC DateTime | Yes | Yes |
| timelineId | UUID | Yes | No |
| generationPresetId | UUID | Yes | Yes |
| status | ProductionStatus | Yes | Yes |

---

# 7. Optional Attributes

| Name | Type |
|---------|---------|
| description | String |
| notes | String |
| exportProfileId | UUID |
| language | LanguageCode |
| metadata | Map<String, Value> |

---

# 8. Owned Collections

Production владеет следующими сущностями.

Timeline

Speech Segments

Audio Tracks

Workflow

Generation Queue

Generation History

Diagnostics

Reports

Temporary Cache

---

# 9. External References

Production может ссылаться на следующие сущности Project.

Document

Role

Voice Profile

Generation Preset

Export Profile

Asset

Все ссылки осуществляются исключительно посредством UUID.

---

# 10. Production Status

Production может находиться только в одном из следующих состояний.

Created

Ready

Generating

Paused

Completed

Exporting

Failed

Archived

ReadOnly

Удаление состояния запрещается.

Добавление нового состояния требует изменения настоящего документа.

---

# 11. State Machine

Допустимые переходы.

Created

↓

Ready

↓

Generating

↓

Paused

↓

Generating

↓

Completed

↓

Exporting

↓

Completed

Допускаются переходы.

Generating → Failed

Exporting → Failed

Ready → Archived

Completed → Archived

Archived → Ready

Переходы, отсутствующие в настоящем документе, запрещены.

---

# 12. Invariants

Production обязана удовлетворять следующим условиям.

Production всегда содержит один Timeline.

Timeline всегда принадлежит одной Production.

Все Speech Segment принадлежат одной Production.

Все Workflow принадлежат одной Production.

Все Audio Track принадлежат одной Production.

Удаление Timeline невозможно.

Удаление Production удаляет все принадлежащие ей сущности.

---

# 13. Commands

Следующие команды изменяют состояние Production.

CreateProduction

RenameProduction

DuplicateProduction

ArchiveProduction

RestoreProduction

DeleteProduction

ChangeGenerationPreset

AssignExportProfile

StartGeneration

PauseGeneration

ResumeGeneration

StopGeneration

StartExport

CancelExport

---

# 14. Domain Events

ProductionCreated

ProductionRenamed

ProductionArchived

ProductionRestored

ProductionDeleted

GenerationStarted

GenerationPaused

GenerationResumed

GenerationCompleted

GenerationFailed

ExportStarted

ExportCompleted

ExportFailed

---

# 15. Duplication

Production поддерживает клонирование.

При клонировании должны быть скопированы.

Timeline

Generation Settings

Workflow Configuration

Production Metadata

При клонировании не должны копироваться.

Speech Segment

Temporary Cache

Running Workflow

Temporary Reports

Diagnostics Cache

История генерации может копироваться в зависимости от пользовательских настроек.

---

# 16. Relationship with Timeline

Production всегда содержит один активный Timeline.

Timeline определяет логический порядок генерации.

Замена Timeline допускается только через специализированную Command.

---

# 17. Relationship with Speech Segments

Каждый Speech Segment принадлежит одной Production.

Speech Segment не может использоваться другой Production.

Повторная генерация Fragment создает новую ревизию Speech Segment.

Предыдущие ревизии сохраняются до явного удаления пользователем или выполнения политики очистки.

---

# 18. Relationship with Workflow

Каждая длительная операция Production оформляется как Workflow.

Workflow может существовать после завершения операции для целей аудита и диагностики.

Удаление Workflow регулируется политикой хранения истории.

---

# 19. Validation

Перед сохранением должны быть проверены.

- наличие Timeline;
- корректность ссылок;
- отсутствие циклических зависимостей;
- отсутствие дублирующихся UUID;
- согласованность состояния Workflow;
- согласованность очереди генерации.

---

# 20. Recovery

После аварийного завершения приложения Production должна быть восстановлена.

Если генерация была прервана, Workflow должен быть переведен в состояние Recovery Pending.

После восстановления пользователь должен иметь возможность:

- продолжить генерацию;
- отменить генерацию;
- выполнить генерацию заново.

---

# 21. Performance Requirements

Production должна поддерживать работу с очень большими проектами.

Архитектура не должна предполагать загрузку всех Speech Segment в оперативную память одновременно.

Speech Segment, журналы и диагностические данные должны поддерживать ленивую загрузку.

---

# 22. Security

Production не должна содержать исполняемый код.

Все пользовательские данные рассматриваются как данные.

Любая интерпретация данных выполняется исключительно соответствующим модулем или Plugin.

---

# 23. Extensibility

Production должна поддерживать хранение дополнительных данных Plugin.

Core не должен анализировать структуру этих данных.

Удаление Plugin не должно нарушать возможность открытия Production.

---

# 24. Test Requirements

Должны существовать автоматические тесты для проверки:

- создания Production;
- дублирования;
- смены состояния;
- восстановления после сбоя;
- запуска генерации;
- остановки генерации;
- экспорта;
- проверки инвариантов;
- проверки ссылочной целостности;
- удаления.

---

# 25. Compliance

Любая реализация сущности Production обязана соответствовать настоящему документу.

Изменение модели Production допускается только посредством изменения настоящей спецификации с оформлением соответствующего Architecture Decision Record.

---

End of Document