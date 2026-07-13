# Voxarium Software Architecture Specification

Document Path:
spec/100_Domain/Project.md

Document ID: DOM-100

Title: Project

Version: 1.0.0

Status: Accepted

Classification: Normative

Depends On

- SAS-001 Glossary
- SAS-002 Domain Ontology
- SAS-003 Architecture Principles

Referenced By

- Production.md
- Source.md
- Document.md
- Timeline.md
- Role.md
- VoiceProfile.md
- Workflow.md
- Asset.md
- Storage specifications
- GUI specifications

---

# 1. Purpose

Project является главной пользовательской сущностью платформы Voxarium.

Все действия пользователя выполняются внутри Project.

Project представляет собой полностью самодостаточную рабочую область, содержащую все данные, необходимые для воспроизведения полного процесса создания речевого контента.

Project является единственной точкой входа в предметную модель.

---

# 2. Responsibility

Project отвечает исключительно за:

- объединение доменных сущностей;
- хранение общей информации;
- управление жизненным циклом проекта;
- обеспечение ссылочной целостности;
- предоставление общей области хранения данных.

Project не отвечает:

- за генерацию речи;
- за импорт документов;
- за работу Speech Engine;
- за воспроизведение аудио;
- за экспорт;
- за выполнение Workflow.

---

# 3. Aggregate Root

Project является Aggregate Root верхнего уровня.

Все остальные доменные объекты принадлежат одному Project.

Не допускается существование сущности без Project.

---

# 4. Lifecycle

Жизненный цикл Project.

```
Created

↓

Opened

↓

Modified

↓

Saved

↓

Archived (optional)

↓

Closed

↓

Deleted
```

Удаление является необратимой операцией.

---

# 5. Identity

Каждый Project имеет постоянный идентификатор.

Тип идентификатора:

```
UUID v7
```

Идентификатор создаётся один раз.

Изменение идентификатора запрещено.

---

# 6. Required Attributes

Каждый Project обязан содержать следующие обязательные атрибуты.

| Name | Type | Required | Mutable |
|----------|----------|----------|----------|
| id | UUIDv7 | Yes | No |
| name | String | Yes | Yes |
| formatVersion | Version | Yes | No |
| createdAt | DateTime UTC | Yes | No |
| updatedAt | DateTime UTC | Yes | Yes |
| defaultLanguage | LanguageCode | Yes | Yes |
| activeProductionId | UUID | Yes | Yes |

---

# 7. Optional Attributes

| Name | Type |
|----------|----------|
| description | String |
| author | String |
| organization | String |
| copyright | String |
| tags | List<String> |
| customProperties | Map<String, Value> |

Project обязан поддерживать произвольные пользовательские свойства.

---

# 8. Contained Collections

Project агрегирует следующие коллекции.

Sources

Documents

Productions

Roles

Voice Profiles

Generation Presets

Export Profiles

Assets

Plugin Data

Settings

Logs

Cache

Наличие дополнительных коллекций допускается только после изменения предметной модели.

---

# 9. Ownership Rules

Project является владельцем всех агрегатов.

Удаление Project приводит к удалению всех принадлежащих данных.

Совместное владение агрегатами несколькими Project запрещается.

---

# 10. Project State

Project может находиться в одном из состояний.

Created

Open

Modified

Saving

ReadOnly

Migrating

Corrupted

Closed

Переходы между состояниями определяются Command.

---

# 11. Invariants

Project обязан удовлетворять следующим инвариантам.

Project всегда содержит минимум одну Production.

Project всегда содержит один активный Production.

Project всегда содержит один активный язык.

Все идентификаторы внутри Project уникальны.

Каждая сущность принадлежит только одному Project.

Project никогда не содержит циклических зависимостей между агрегатами.

---

# 12. Relationships

Project

owns

Sources

Documents

Productions

Roles

Voice Profiles

Assets

Generation Presets

Export Profiles

Plugin Data

Settings

Project не владеет Plugin.

Project не владеет Core.

Project не владеет Runtime.

---

# 13. Commands

Следующие команды изменяют состояние Project.

CreateProject

OpenProject

RenameProject

ChangeProjectDescription

ChangeProjectLanguage

SaveProject

CloseProject

ArchiveProject

DeleteProject

RestoreProject

Каждая команда публикует соответствующий Domain Event.

---

# 14. Domain Events

ProjectCreated

ProjectOpened

ProjectModified

ProjectSaved

ProjectClosed

ProjectArchived

ProjectDeleted

ProjectRecovered

ProjectMigrated

ProjectCorrupted

---

# 15. Business Rules

Project обязан оставаться согласованным после любой операции.

Все изменения должны быть атомарными.

Любая ошибка изменения должна приводить к откату операции.

Частично изменённый Project считается повреждённым.

---

# 16. Serialization

Project является сериализуемой сущностью.

Сериализация не должна зависеть:

- от языка программирования;
- от ORM;
- от базы данных;
- от внутреннего представления памяти.

Конкретный формат определяется документами раздела `600_Project_Format`.

---

# 17. Persistence

Project должен поддерживать:

- создание;
- загрузку;
- сохранение;
- резервное копирование;
- миграцию;
- восстановление.

Механизм хранения определяется Storage Layer.

---

# 18. Versioning

Project содержит номер версии формата.

Изменение версии формата допускается исключительно механизмом миграции.

Ручное изменение версии запрещается.

---

# 19. Recovery

После аварийного завершения приложения Project должен быть восстановлен до последнего согласованного состояния.

Восстановление должно быть идемпотентным.

Повторное выполнение процедуры восстановления не должно изменять корректный Project.

---

# 20. Validation

Перед открытием Project должны быть проверены:

- формат проекта;
- структура каталогов;
- обязательные файлы;
- ссылки между сущностями;
- целостность идентификаторов;
- совместимость версии.

При обнаружении ошибок Project переводится в состояние Corrupted или ReadOnly в зависимости от характера проблемы.

---

# 21. Security

Project не должен содержать исполняемый код.

Project не должен автоматически выполнять сценарии, макросы или внешние программы.

Plugin Data рассматриваются как данные и не должны интерпретироваться Core как исполняемый код.

---

# 22. Extensibility

Project обязан предоставлять изолированные области хранения данных для Plugin.

Core не должен зависеть от внутреннего содержимого Plugin Data.

Добавление новых типов пользовательских данных не должно требовать изменения существующих агрегатов.

---

# 23. Performance Requirements

Открытие Project не должно требовать полной загрузки всех данных в оперативную память.

Архитектура должна поддерживать ленивую загрузку (Lazy Loading) крупных коллекций.

Доступ к отдельным агрегатам не должен требовать полного построения всей предметной модели.

---

# 24. Test Requirements

Должны существовать автоматические тесты, проверяющие:

- создание Project;
- сохранение;
- повторное открытие;
- миграцию;
- восстановление;
- проверку инвариантов;
- обнаружение повреждений;
- работу в режиме ReadOnly.

---

# 25. Compliance

Любая реализация сущности Project обязана соответствовать требованиям настоящего документа.

Изменение модели Project допускается только посредством изменения настоящей спецификации и оформления соответствующего ADR.

---

End of Document