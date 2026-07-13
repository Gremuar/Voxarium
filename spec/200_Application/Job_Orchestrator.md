# Voxarium Software Architecture Specification

Document Path:
spec/200_Application/Job_Orchestrator.md

Document ID: APP-008

Title: Job Orchestrator

Version: 1.0.0

Status: Accepted

Classification: Normative

Depends On

- APP-001 Application Architecture
- APP-004 Command Bus
- APP-006 Event Bus
- DOM-113 Workflow
- DOM-114 Job

Referenced By

- Queue Manager
- Scheduler
- Worker
- Generation Module
- Import Module
- Export Module
- Voice Cloning Module
- AI Module

---

# 1. Purpose

Job Orchestrator является центральным координатором жизненного цикла Job.

Он отвечает за преобразование пользовательских операций и Workflow в последовательность независимых Job, управление их зависимостями, постановку в очередь и контроль выполнения.

Job Orchestrator не выполняет Job самостоятельно.

Исполнение Job осуществляется Worker.

---

# 2. Responsibilities

Job Orchestrator отвечает за:

- создание Job;
- построение графа зависимостей;
- регистрацию Job;
- передачу Job в Queue;
- запуск Scheduler;
- обработку результатов выполнения;
- публикацию событий жизненного цикла Job.

Job Orchestrator не отвечает за:

- выполнение бизнес-логики;
- выполнение TTS;
- работу с GPU;
- выбор Worker;
- управление потоками.

---

# 3. Architectural Position

Application Layer

↓

Job Orchestrator

↓

Queue

↓

Scheduler

↓

Worker

↓

Infrastructure

---

# 4. General Principles

Job Orchestrator должен:

- быть полностью независимым от типа Job;
- работать исключительно с абстракцией Job;
- не содержать логики конкретных модулей;
- не знать о реализации Plugin.

---

# 5. Job Creation

Job может быть создан:

- Command Handler;
- Workflow Engine;
- Plugin;
- System Service.

После создания Job регистрируется в Job Repository.

---

# 6. Dependency Graph

Job могут образовывать ориентированный ациклический граф (DAG).

Пример:

Import Book

↓

Parse Document

↓

Detect Roles

↓

Assign Voices

↓

Generate Fragments

↓

Merge Audio

↓

Export

Каждая вершина графа представляет собой независимый Job.

---

# 7. Parent–Child Relationship

Job может содержать дочерние Job.

Parent Job считается завершённым только после успешного завершения всех дочерних Job.

При отмене Parent Job отменяются все дочерние Job, если политика выполнения не определяет иное.

---

# 8. Queue Registration

После проверки зависимостей Job помещается в Queue.

Queue определяет только порядок хранения.

Queue не принимает решений о запуске.

---

# 9. Scheduler Interaction

Scheduler регулярно запрашивает Job, готовые к выполнению.

Job считается готовым, если:

- выполнены все зависимости;
- доступны необходимые ресурсы;
- соблюдены ограничения политики выполнения.

---

# 10. Resource Requirements

Каждый Job может описывать необходимые ресурсы.

Минимально поддерживаются:

- CPU;
- GPU;
- RAM;
- Disk Space;
- Network;
- Plugin Capability.

Scheduler использует эту информацию при выборе Worker.

---

# 11. Retry Policy

Job Orchestrator применяет политику повторного выполнения.

Поддерживаются:

- Immediate Retry;
- Delayed Retry;
- Exponential Backoff;
- Manual Retry.

Политика может быть переопределена конкретным Job Type.

---

# 12. Failure Handling

При ошибке Job Orchestrator обязан:

- зарегистрировать ошибку;
- сохранить диагностическую информацию;
- определить дальнейшую политику;
- опубликовать событие JobFailed.

Workflow может продолжить выполнение только при наличии соответствующей политики.

---

# 13. Cancellation

Job Orchestrator поддерживает отмену:

- отдельного Job;
- группы Job;
- Parent Job;
- Workflow;
- всего Project.

Отмена должна выполняться безопасно и детерминированно.

---

# 14. Pause and Resume

Job могут быть приостановлены.

После возобновления выполнение продолжается с последней согласованной точки.

Если конкретный Job Type не поддерживает продолжение, допускается повторный запуск.

---

# 15. Progress Aggregation

Job Orchestrator вычисляет общий прогресс.

Например:

Project

↓

Production

↓

Workflow

↓

Parent Job

↓

Child Job

↓

Progress

Пользователь всегда должен видеть прогресс на любом уровне.

---

# 16. Event Integration

Job Orchestrator публикует события:

JobCreated

JobQueued

JobStarted

JobProgressChanged

JobPaused

JobResumed

JobCompleted

JobCancelled

JobFailed

JobRetried

---

# 17. Plugin Integration

Plugin могут:

- создавать Job;
- определять собственные Job Type;
- предоставлять Worker Capability.

Plugin не могут вмешиваться в работу Orchestrator.

---

# 18. Recovery

После аварийного завершения приложения Job Orchestrator обязан:

- восстановить граф зависимостей;
- восстановить очередь;
- определить незавершённые Job;
- повторно зарегистрировать готовые к выполнению Job.

---

# 19. Performance Requirements

Job Orchestrator должен поддерживать:

- сотни тысяч Job в одном Project;
- десятки тысяч одновременно ожидающих Job;
- быстрое построение графа зависимостей;
- минимальное потребление памяти.

---

# 20. Thread Safety

Job Orchestrator полностью потокобезопасен.

Создание Job, отмена и изменение состояния могут выполняться одновременно из разных потоков.

---

# 21. Test Requirements

Должны существовать тесты, проверяющие:

- построение графа;
- зависимости;
- Parent–Child отношения;
- отмену;
- повторное выполнение;
- восстановление после сбоя;
- параллельное создание Job;
- агрегацию прогресса.

---

# 22. Compliance

Любая реализация Job Orchestrator обязана соответствовать настоящему документу.

---

# Appendix A. Reference Execution Flow

User Action

↓

Command

↓

Command Bus

↓

Handler

↓

Job Orchestrator

↓

Job Graph

↓

Queue

↓

Scheduler

↓

Worker

↓

Event Bus

↓

GUI Update

---

# Appendix B. Example Job Graph

Create Audiobook

├── Import Book
├── Parse Book
├── Detect Chapters
├── Detect Roles
├── Assign Voices
├── Generate Chapter 1
│   ├── Fragment 1
│   ├── Fragment 2
│   ├── Fragment 3
│   └── ...
├── Generate Chapter 2
├── Generate Chapter 3
├── Normalize Audio
├── Merge Audio
├── Generate Metadata
└── Export Audiobook

---

End of Document