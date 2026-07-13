# Voxarium Software Architecture Specification

Document Path:
spec/300_Contracts/IProjectService.md

Document ID: CTR-001

Title: IProjectService

Version: 1.0.0

Status: Accepted

Classification: Normative

Depends On

- CTR-000 IService
- Project
- Document
- Production
- Asset
- Workflow

Referenced By

- Project_Service
- User_Interface_Architecture
- Import_Service
- Export_Service

---

# 1. Purpose

IProjectService определяет публичный контракт управления жизненным циклом Project.

Контракт предоставляет единственную точку доступа к операциям уровня проекта.

---

# 2. Responsibilities

Контракт SHALL предоставлять операции:

- создания проекта;
- открытия проекта;
- закрытия проекта;
- сохранения проекта;
- сохранения проекта под новым именем;
- клонирования проекта;
- удаления проекта;
- получения информации о проекте.

---

# 3. Non-Responsibilities

Контракт SHALL NOT:

- изменять Document;
- выполнять импорт;
- выполнять экспорт;
- выполнять генерацию речи;
- выполнять воспроизведение;
- работать напрямую с файловой системой.

---

# 4. Commands

Контракт SHALL определять следующие команды.

```
CreateProject

OpenProject

CloseProject

SaveProject

SaveProjectAs

DuplicateProject

DeleteProject
```

Каждая команда изменяет состояние Application.

---

# 5. Queries

Контракт SHALL предоставлять следующие запросы.

```
GetCurrentProject

GetProjectMetadata

GetProjectStatistics

IsProjectModified

CanCloseProject
```

Запросы SHALL NOT изменять состояние системы.

---

# 6. Preconditions

Перед выполнением операций SHALL проверяться:

- корректность параметров;
- допустимость текущего состояния приложения;
- существование проекта (если применимо);
- отсутствие конфликтующих операций.

---

# 7. Postconditions

После успешного выполнения операции SHALL быть гарантировано:

- согласованное состояние Project;
- обновление Revision при изменении;
- публикация необходимых Domain и Application Events.

---

# 8. Error Model

Контракт SHALL поддерживать следующие категории ошибок.

- ProjectNotFound
- ProjectAlreadyOpened
- InvalidProject
- AccessDenied
- ValidationFailed
- OperationCancelled
- InternalFailure

---

# 9. Transactions

Все операции записи SHALL выполняться в рамках одной прикладной транзакции.

---

# 10. Events

Успешное выполнение операций MAY приводить к публикации:

- ProjectCreated
- ProjectOpened
- ProjectClosed
- ProjectSaved
- ProjectDeleted

Конкретный набор событий определяется реализацией Application Layer.

---

# 11. Thread Safety

Контракт SHALL допускать параллельное выполнение операций чтения.

Операции изменения Project SHALL быть сериализованы.

---

# 12. Dependencies

Контракт SHALL зависеть только от:

- Domain Model;
- базовых архитектурных контрактов.

Контракт SHALL NOT зависеть от:

- GUI;
- Infrastructure;
- AI Runtime.

---

# 13. AI Implementation Rules

Реализация SHALL:

- работать только через Aggregate Root Project;
- не обращаться напрямую к инфраструктуре хранения;
- публиковать события после успешного завершения транзакции;
- соблюдать правила IService.

---

# 14. Test Requirements

Контракт SHALL иметь тесты:

- создание проекта;
- открытие проекта;
- сохранение проекта;
- закрытие проекта;
- клонирование проекта;
- удаление проекта;
- обработка ошибок.

---

# 15. Compliance Checklist

Контракт соответствует настоящей спецификации только если:

- предоставляет все обязательные команды;
- предоставляет все обязательные запросы;
- не зависит от реализации;
- поддерживает транзакционность;
- документирует ошибки;
- соответствует IService.

---

End of Document