# Voxarium Software Architecture Specification

Document Path:
spec/100_Domain/Workflow.md

<<<<<<< HEAD
Document ID: DOM-113

Title: Workflow

Version: 1.0.0
=======
Document ID: DOM-012

Title: Workflow

Version: 2.0.0
>>>>>>> c975edf (t)

Status: Accepted

Classification: Normative

Depends On

<<<<<<< HEAD
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
=======
- SAS-000 Project Philosophy
- SAS-001 Glossary
- SAS-002 Domain Ontology
- Project
- Document
- Production

Referenced By

- Workflow_Engine
- Job_Orchestrator
- Scheduler
- Queue
- Worker
>>>>>>> c975edf (t)

---

# 1. Purpose

<<<<<<< HEAD
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
=======
Workflow представляет собой декларативное описание процесса обработки данных.

Workflow определяет:

- какие действия необходимо выполнить;
- в каком порядке они должны быть выполнены;
- при каких условиях допускается переход между этапами;
- какие объекты проекта участвуют в процессе.

Workflow не выполняет операции самостоятельно.

Workflow является исключительно моделью предметной области.

---

# 2. Responsibilities

Workflow SHALL отвечать за:

- описание последовательности этапов;
- описание зависимостей между этапами;
- хранение параметров запуска;
- хранение пользовательских настроек;
- хранение текущего состояния выполнения;
- обеспечение воспроизводимости процесса.

---

# 3. Non-Responsibilities

Workflow SHALL NOT:

- выполнять генерацию;
- выполнять экспорт;
- выполнять импорт;
- выполнять обработку аудио;
- запускать Worker;
- управлять потоками;
- содержать очередь задач.

---

# 4. Ownership

Workflow принадлежит Project.

```
Project
    │
    └── Workflows
            │
            └── Workflow
```

Workflow SHALL NOT существовать вне Project.
>>>>>>> c975edf (t)

---

# 5. Identity

<<<<<<< HEAD
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
=======
Каждый Workflow имеет неизменяемый Identifier.

Identifier SHALL:

- быть уникальным внутри Project;
- сохраняться при сериализации;
- никогда не изменяться.

---

# 6. Metadata

| Property | Required | Mutable |
|-----------|----------|---------|
| Identifier | Yes | No |
| Name | Yes | Yes |
| Description | No | Yes |
| Status | Yes | Yes |
| Revision | Yes | Yes |
| CreatedUtc | Yes | No |
| ModifiedUtc | Yes | Yes |

---

# 7. Workflow Scope

Workflow MAY работать с:

- одним Document;
- несколькими Document;
- одним Production;
- всем Project.

Workflow SHALL явно определять область применения.

---

# 8. Workflow Stages

Workflow состоит из последовательности Stage.

Каждый Stage представляет логический этап обработки.

Примеры:

- Import
- Parse
- Analyze
- Assign Voices
- Generate Speech
- Validate
- Export
- Publish

Domain не ограничивает набор Stage.

---

# 9. Dependencies

Workflow SHALL представлять зависимости в виде ориентированного ациклического графа (Directed Acyclic Graph, DAG).

Каждый Stage может иметь:

- ни одной зависимости;
- одну зависимость;
- несколько зависимостей.

Циклические зависимости запрещены.

---

# 10. Status

Допустимые состояния Workflow.

- Draft
- Ready
- Running
- Paused
- Completed
- Failed
- Cancelled
- Archived

Workflow SHALL находиться только в одном состоянии.

---

# 11. Lifecycle

```
Draft

↓

Ready

↓

Running

↓

Completed
```

Допускаются переходы.

```
Running → Paused

Paused → Running

Running → Failed

Running → Cancelled

Completed → Archived
```

Другие переходы запрещены.

---

# 12. Determinism

Workflow SHALL быть полностью детерминированным.

При одинаковых:

- входных данных;
- конфигурации;
- версии приложения;

Workflow обязан строить одинаковый план выполнения.

---

# 13. Versioning

Каждый Workflow имеет Revision.

Любое изменение структуры SHALL увеличивать Revision.

Во время выполнения изменение структуры запрещено.

---

# 14. Invariants

Workflow SHALL удовлетворять следующим требованиям.

- Identifier существует.
- Name существует.
- Stage уникальны.
- отсутствуют циклы.
- существует единственная начальная вершина.
- все ссылки корректны.
- Revision ≥ 1.

---

# 15. Creation Rules

Workflow создаётся через Workflow Service.

Во время создания SHALL:

- создать Identifier;
- установить Revision = 1;
- установить состояние Draft;
- опубликовать WorkflowCreated.

---

# 16. Modification Rules

Любое изменение SHALL:

- проверять DAG;
- увеличивать Revision;
- публиковать WorkflowModified.

---

# 17. Execution Model

Workflow описывает только план выполнения.

Фактическое выполнение принадлежит:

- Workflow Engine;
- Job Orchestrator;
- Scheduler;
- Queue;
- Worker.

---

# 18. Persistence

Workflow сериализуется как часть Project.

Workflow SHALL NOT знать:

- Runtime;
- Worker;
- Queue;
- Thread Pool;
- процессы ОС.

---

# 19. Concurrency

Workflow допускает:

- конкурентное чтение.

Не допускает:

- конкурентную модификацию.

---

# 20. Domain Events

Workflow публикует:

- WorkflowCreated
- WorkflowModified
- WorkflowStarted
- WorkflowPaused
- WorkflowCompleted
- WorkflowFailed
- WorkflowCancelled
- WorkflowArchived

---

# 21. Commands

Поддерживаются команды.

- CreateWorkflow
- UpdateWorkflow
- ValidateWorkflow
- StartWorkflow
- PauseWorkflow
- ResumeWorkflow
- CancelWorkflow
- ArchiveWorkflow

---

# 22. Extension Rules

Plugin MAY:

- добавлять новые типы Stage;
- добавлять пользовательские параметры;
- добавлять собственные проверки.

Plugin SHALL NOT:

- нарушать структуру DAG;
- изменять обязательные свойства;
- нарушать инварианты.

---

# 23. AI Implementation Requirements

Workflow SHALL описывать исключительно бизнес-процесс.

Реализация SHALL NOT содержать:

- Thread;
- Task;
- Future;
- asyncio;
- процессы;
- сетевые соединения.

Все механизмы исполнения принадлежат Application Layer.

---

# 24. Test Requirements

Минимальный набор тестов.

- создание Workflow;
- проверка DAG;
- обнаружение циклов;
- изменение Revision;
- сериализация;
- десериализация;
- проверка состояний;
- проверка публикации событий;
- проверка инвариантов.

---

# 25. Compliance Checklist

Реализация соответствует настоящей спецификации только если:

- Workflow принадлежит Project;
- является DAG;
- полностью детерминирован;
- не зависит от Runtime;
- реализованы все события;
- реализованы все команды;
- соблюдены все инварианты;
- сериализация полностью воспроизводима.
>>>>>>> c975edf (t)

---

End of Document