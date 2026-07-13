# Voxarium Software Architecture Specification

Document Path:
spec/100_Domain/Workflow.md

Document ID: DOM-113

Title: Workflow

Version: 1.0.0

Status: Accepted

Classification: Normative

Depends On

- SAS-001 Glossary
- SAS-002 Domain Ontology
- SAS-003 Architecture Principles
- Project.md
- Production.md
- Timeline.md
- Fragment.md

Referenced By

- Queue_Module.md
- Generation_Module.md
- Export_Module.md
- Scheduler.md
- Automation_Module.md
- Project_Format.md

---

# 1. Purpose

Workflow представляет собой описание последовательности автоматических операций, выполняемых над Project или его частью.

Workflow является независимой предметной сущностью.

Workflow не содержит бизнес-логики генерации.

Workflow определяет:

- что необходимо выполнить;
- в какой последовательности;
- при каких условиях;
- с какими параметрами.

Исполнение Workflow выполняется инфраструктурным модулем Workflow Engine.

---

# 2. Responsibility

Workflow отвечает исключительно за:

- описание последовательности операций;
- описание зависимостей между операциями;
- хранение условий выполнения;
- хранение параметров запуска;
- поддержку автоматизации производственного процесса.

Workflow не отвечает за:

- генерацию речи;
- импорт документов;
- экспорт аудио;
- работу TTS Engine;
- хранение результатов.

---

# 3. Business Motivation

Workflow позволяет автоматизировать производственные процессы.

Примеры.

Импорт книги

↓

Автоматическое определение персонажей

↓

Назначение голосов

↓

Генерация

↓

Проверка ошибок

↓

Экспорт

↓

Создание аудиокниги

Без участия пользователя.

---

# 4. Aggregate

Workflow является Aggregate Root.

Workflow принадлежит одному Project.

Project может содержать любое количество Workflow.

---

# 5. Identity

Каждый Workflow имеет постоянный UUID v7.

UUID никогда не изменяется.

---

# 6. Required Attributes

| Name | Type | Required | Mutable |
|------|------|----------|----------|
| id | UUIDv7 | Yes | No |
| name | String | Yes | Yes |
| enabled | Boolean | Yes | Yes |
| createdAt | UTC DateTime | Yes | No |
| updatedAt | UTC DateTime | Yes | Yes |

---

# 7. Workflow Structure

Workflow состоит из последовательности Step.

Каждый Step является независимой задачей.

Workflow может иметь:

- линейную структуру;
- условные переходы;
- параллельные ветви;
- циклы с ограничением;
- точки завершения.

---

# 8. Workflow Step

Каждый Step имеет:

- идентификатор;
- тип;
- входные параметры;
- выходные параметры;
- условия выполнения;
- зависимости.

Core определяет только базовую модель Step.

Конкретная логика определяется соответствующим модулем.

---

# 9. Standard Step Types

Минимально поддерживаются:

- Import Source
- Parse Document
- Detect Roles
- Assign Voices
- Assign Emotions
- Apply Dictionary
- Queue Generation
- Generate Speech
- Validate Audio
- Normalize Loudness
- Export Audio
- Execute Plugin
- Wait
- User Confirmation

Plugin могут регистрировать собственные типы Step.

---

# 10. Conditions

Каждый Step может иметь условия запуска.

Примеры:

- завершён предыдущий Step;
- отсутствуют ошибки;
- доступен GPU;
- установлен Plugin;
- пользователь подтвердил действие;
- существует подключение к сети.

---

# 11. Parameters

Каждый Step может иметь параметры.

Например:

- список Fragment;
- Voice Profile;
- Preset;
- язык;
- каталог экспорта;
- используемый Plugin.

Параметры сериализуются независимо от реализации Step.

---

# 12. Execution Model

Workflow является декларативным.

Workflow описывает процесс.

Workflow Engine принимает решение о фактическом выполнении.

Core не содержит планировщика.

---

# 13. Retry Policy

Каждый Step может определять политику повторного выполнения.

Минимально поддерживаются:

- Never Retry
- Retry Immediately
- Retry N Times
- Retry With Delay
- Manual Retry

---

# 14. Failure Policy

Workflow определяет поведение при ошибках.

Минимально:

- Stop Workflow
- Skip Step
- Retry
- Continue
- Ask User
- Execute Recovery Step

---

# 15. Parallel Execution

Workflow допускает параллельное выполнение независимых Step.

Workflow Engine самостоятельно определяет допустимый уровень параллелизма.

Порядок выполнения должен быть детерминирован при наличии зависимостей.

---

# 16. Relationship with Timeline

Workflow может работать:

- со всем Timeline;
- с выбранными Group;
- с выбранными Fragment;
- с отдельной Branch.

Timeline не содержит Workflow.

---

# 17. Relationship with Fragment

Workflow никогда не изменяет Fragment напрямую.

Все изменения выполняются через соответствующие Command предметной модели.

---

# 18. Commands

CreateWorkflow

RenameWorkflow

DeleteWorkflow

EnableWorkflow

DisableWorkflow

DuplicateWorkflow

ExecuteWorkflow

CancelWorkflow

---

# 19. Domain Events

WorkflowCreated

WorkflowUpdated

WorkflowStarted

WorkflowCompleted

WorkflowCancelled

WorkflowFailed

WorkflowPaused

WorkflowResumed

---

# 20. Invariants

Workflow обязан удовлетворять следующим требованиям.

Имеет один Root Step.

Не содержит циклических зависимостей без явного ограничения.

Все Step достижимы.

Все ссылки валидны.

Каждый Step имеет уникальный идентификатор.

---

# 21. Validation

Перед выполнением проверяются:

- корректность структуры;
- существование всех Plugin;
- существование всех зависимостей;
- корректность параметров;
- отсутствие циклов;
- совместимость Step.

---

# 22. Recovery

Workflow должен поддерживать продолжение выполнения после аварийного завершения приложения.

Состояние каждого Step должно сохраняться.

После восстановления Workflow Engine обязан продолжить выполнение с последнего согласованного состояния.

---

# 23. Performance Requirements

Workflow должен поддерживать выполнение тысяч Step.

Проверка зависимостей должна иметь сложность, близкую к O(n).

Параллельные Step должны распределяться между доступными вычислительными ресурсами.

---

# 24. Extensibility

Plugin могут добавлять:

- собственные типы Step;
- собственные условия;
- пользовательские действия;
- специализированные параметры;
- интеграцию с внешними системами.

Core не должен содержать информации о внутреннем устройстве пользовательских Step.

---

# 25. Test Requirements

Должны существовать автоматические тесты, проверяющие:

- создание Workflow;
- выполнение линейного процесса;
- выполнение параллельных ветвей;
- обработку ошибок;
- повторные попытки;
- отмену выполнения;
- восстановление после сбоя;
- проверку структуры;
- работу пользовательских Step.

---

# 26. Future Compatibility

Архитектура должна поддерживать:

- визуальный редактор Workflow;
- шаблоны Workflow;
- импорт и экспорт Workflow;
- удалённое выполнение;
- распределённые Workflow;
- совместную работу нескольких пользователей.

Настоящий документ определяет только предметную модель Workflow.

---

# 27. Compliance

Любая реализация Workflow обязана соответствовать требованиям настоящего документа.

Изменение модели Workflow допускается исключительно посредством изменения настоящей спецификации и оформления соответствующего Architecture Decision Record.

---

End of Document