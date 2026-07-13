# Voxarium Software Architecture Specification

Document Path:
spec/300_Contracts/IService.md

Document ID: CTR-000

Title: IService

Version: 1.0.0

Status: Accepted

Classification: Normative

Depends On

- SAS-003 Architecture Principles
- SAS-006 Common Domain Patterns
- SAS-007 Module Architecture

Referenced By

- IProjectService
- IDocumentService
- ITimelineService
- IVoiceService
- IGenerationService
- IImporter
- IExporter
- IAudioProcessor
- IPlaybackService

---

# 1. Purpose

Настоящий документ определяет обязательные требования ко всем публичным сервисным контрактам Application Layer.

IService не является программным интерфейсом, который необходимо реализовывать буквально. Он представляет собой архитектурный шаблон (Architectural Contract), которому SHALL соответствовать все сервисные интерфейсы системы.

---

# 2. Goals

Контракт IService обеспечивает:

- единообразие публичного API;
- независимость от реализации;
- предсказуемость поведения сервисов;
- возможность автоматической генерации кода;
- совместимость между модулями.

---

# 3. General Principles

Каждый сервис SHALL:

- иметь единственную ответственность;
- быть слабо связанным с другими сервисами;
- взаимодействовать через контракты;
- быть независимым от GUI;
- быть независимым от Infrastructure.

---

# 4. Public API

Публичный API SHALL состоять только из операций предметной области.

Запрещается публиковать:

- внутренние методы;
- служебные методы;
- методы инициализации реализации;
- методы освобождения ресурсов реализации.

---

# 5. Operation Categories

Все публичные операции относятся к одной из следующих категорий.

### Commands

Изменяют состояние системы.

### Queries

Не изменяют состояние системы.

### Notifications

Публикуют информацию без изменения состояния.

Смешивание нескольких категорий в одной операции запрещено.

---

# 6. Naming Rules

Для команд SHALL использоваться следующие префиксы:

- Create
- Update
- Delete
- Rename
- Move
- Merge
- Split
- Generate
- Import
- Export
- Validate
- Execute

Для запросов SHALL использоваться:

- Get
- Find
- Search
- List
- Resolve
- Calculate

---

# 7. Side Effects

Query SHALL NOT:

- изменять Domain Model;
- публиковать Domain Events;
- изменять состояние проекта.

Command MAY:

- изменять Aggregate;
- публиковать Domain Events;
- инициировать Workflow.

---

# 8. Transactions

Каждая операция записи SHALL выполняться в пределах одной прикладной транзакции.

Границы транзакции определяются Application Layer.

---

# 9. Cancellation

Длительные операции SHOULD поддерживать отмену выполнения.

Если операция не поддерживает отмену, это должно быть явно указано в спецификации соответствующего контракта.

---

# 10. Error Model

Контракты SHALL использовать единый механизм представления ошибок.

Ошибки подразделяются на:

- Validation;
- Conflict;
- NotFound;
- PermissionDenied;
- Cancelled;
- InternalFailure.

Конкретный формат результата определяется отдельной спецификацией.

---

# 11. Thread Safety

Контракт SHALL документировать требования к потокобезопасности.

Если специальных требований нет, сервис считается безопасным для параллельного использования несколькими клиентами.

---

# 12. Dependencies

Контракт SHALL ссылаться только на:

- Domain Model;
- Foundation;
- другие публичные контракты.

Контракт SHALL NOT зависеть от реализации сервисов.

---

# 13. Versioning

Каждый контракт обязан иметь собственную версию.

Несовместимые изменения SHALL сопровождаться увеличением Major Version.

Совместимые изменения SHALL увеличивать Minor Version.

---

# 14. Extensibility

Контракт MAY расширяться добавлением новых операций.

Удаление или изменение существующих операций без изменения Major Version запрещено.

---

# 15. AI Implementation Rules

ИИ-агент SHALL:

- реализовывать контракт полностью;
- не изменять семантику операций;
- не добавлять скрытых зависимостей;
- соблюдать разделение Command и Query;
- использовать только публичные типы Domain Model.

---

# 16. Test Requirements

Для каждого сервисного контракта SHALL существовать:

- Contract Tests;
- Compatibility Tests;
- Versioning Tests.

---

# 17. Compliance Checklist

Контракт соответствует настоящей спецификации только если:

- определяет единственную область ответственности;
- разделяет Commands и Queries;
- не зависит от реализации;
- документирует требования к транзакциям;
- документирует модель ошибок;
- допускает независимую реализацию.

---

End of Document