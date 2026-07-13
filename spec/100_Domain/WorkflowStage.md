# Voxarium Software Architecture Specification

Document Path:
spec/100_Domain/WorkflowStage.md

Document ID: DOM-017

Title: WorkflowStage

Version: 1.0.0

Status: Accepted

Classification: Normative

Depends On

- SAS-000 Project Philosophy
- SAS-001 Glossary
- SAS-003 Architecture Principles
- Workflow

Referenced By

- Workflow_Engine
- Scheduler
- Queue
- Job
- Worker

---

# 1. Purpose

WorkflowStage представляет собой один логический этап Workflow.

WorkflowStage описывает:

- выполняемую операцию;
- входные данные;
- выходные данные;
- условия запуска;
- условия завершения.

WorkflowStage не выполняет работу самостоятельно.

WorkflowStage является Domain Entity.

---

# 2. Responsibilities

WorkflowStage SHALL отвечать за:

- описание логического действия;
- хранение зависимостей;
- хранение политики выполнения;
- описание входов;
- описание выходов;
- описание условий завершения.

---

# 3. Non-Responsibilities

WorkflowStage SHALL NOT:

- выполнять вычисления;
- запускать Worker;
- создавать Job;
- обращаться к Queue;
- обращаться к Runtime;
- обращаться к Infrastructure.

---

# 4. Ownership

WorkflowStage принадлежит Workflow.

```
Workflow
    │
    ├── WorkflowStage
    ├── WorkflowStage
    └── WorkflowStage
```

WorkflowStage SHALL NOT существовать отдельно.

---

# 5. Identity

Каждый WorkflowStage имеет неизменяемый Identifier.

Identifier SHALL:

- быть уникальным внутри Workflow;
- никогда не изменяться;
- сохраняться после сериализации.

---

# 6. Metadata

| Property | Required | Mutable |
|----------|----------|---------|
| Identifier | Yes | No |
| Name | Yes | Yes |
| StageType | Yes | No |
| Enabled | Yes | Yes |
| Revision | Yes | Yes |

---

# 7. Stage Type

WorkflowStage SHALL иметь один StageType.

Минимальный набор типов.

- Import
- Parse
- Analyze
- Transform
- Generate
- Validate
- Export
- ExecutePlugin
- Custom

Plugin MAY регистрировать дополнительные типы.

---

# 8. Inputs

WorkflowStage MAY принимать:

- Document;
- Fragment;
- SpeechSegment;
- Timeline;
- Production;
- AudioTrack;
- Asset;
- Project.

Domain определяет только логические типы входных данных.

---

# 9. Outputs

WorkflowStage MAY производить:

- Document;
- Timeline;
- AudioTrack;
- Asset;
- Report;
- Export Package.

Выход определяется исключительно логически.

---

# 10. Dependencies

WorkflowStage MAY зависеть от нескольких WorkflowStage.

Все зависимости образуют DAG.

Циклы запрещены.

---

# 11. Execution Policy

WorkflowStage определяет логическую политику исполнения.

Поддерживаются значения.

- Automatic
- Manual
- Conditional

Application Layer определяет механизм реализации.

---

# 12. Retry Policy

WorkflowStage MAY определять политику повторного выполнения.

Поддерживаются:

- Never
- Once
- Limited
- Unlimited

Число повторов определяется Application Layer.

---

# 13. Failure Policy

WorkflowStage MAY определять реакцию на ошибку.

Поддерживаются варианты.

- Stop Workflow
- Skip Stage
- Retry
- Continue
- Execute Recovery Stage

---

# 14. Completion Conditions

WorkflowStage считается завершённым только если выполнены все условия завершения.

Условия определяются декларативно.

---

# 15. Lifecycle

```
Created

↓

Configured

↓

Ready

↓

Archived
```

Во время выполнения Workflow изменение Stage запрещено.

---

# 16. Invariants

WorkflowStage SHALL удовлетворять следующим требованиям.

- Identifier существует.
- Name существует.
- StageType определён.
- Revision ≥ 1.
- отсутствуют циклические зависимости.

---

# 17. Creation Rules

При создании SHALL:

- создать Identifier;
- установить Revision = 1;
- опубликовать WorkflowStageCreated.

---

# 18. Modification Rules

Любое изменение SHALL:

- проверять DAG;
- увеличивать Revision;
- публиковать WorkflowStageModified.

---

# 19. Persistence

WorkflowStage сериализуется исключительно как часть Workflow.

WorkflowStage SHALL NOT знать:

- Queue;
- Job;
- Worker;
- Thread;
- Runtime.

---

# 20. Concurrency

Поддерживается конкурентное чтение.

Конкурентная запись запрещена.

---

# 21. Domain Events

WorkflowStage публикует:

- WorkflowStageCreated
- WorkflowStageModified
- WorkflowStageEnabled
- WorkflowStageDisabled
- WorkflowStageDeleted

---

# 22. Commands

Поддерживаются команды.

- CreateWorkflowStage
- UpdateWorkflowStage
- RemoveWorkflowStage
- EnableWorkflowStage
- DisableWorkflowStage

---

# 23. Extension Rules

Plugin MAY:

- регистрировать новые StageType;
- добавлять пользовательские свойства;
- добавлять политики выполнения.

Plugin SHALL NOT:

- нарушать DAG;
- изменять обязательные свойства;
- нарушать инварианты.

---

# 24. AI Implementation Requirements

WorkflowStage SHALL описывать исключительно бизнес-этап.

Запрещается хранить:

- Thread;
- Task;
- Future;
- asyncio;
- процессы;
- параметры Scheduler.

Все механизмы выполнения принадлежат Application Layer.

---

# 25. Test Requirements

Минимальный набор тестов.

- создание;
- изменение;
- проверка DAG;
- сериализация;
- десериализация;
- проверка событий;
- проверка инвариантов.

---

# 26. Compliance Checklist

Реализация соответствует настоящей спецификации только если:

- WorkflowStage принадлежит Workflow;
- является вершиной DAG;
- не зависит от Runtime;
- реализованы все события;
- реализованы все команды;
- соблюдены все инварианты;
- сериализация полностью воспроизводима.

---

End of Document