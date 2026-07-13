# Voxarium Software Architecture Specification

Document Path:
spec/100_Domain/Job.md

Document ID: DOM-114

Title: Job

Version: 1.0.0

Status: Accepted

Classification: Normative

Depends On

- SAS-001 Glossary
- SAS-002 Domain Ontology
- SAS-003 Architecture Principles
- Workflow.md

Referenced By

- Queue.md
- Scheduler.md
- Worker.md
- Generation_Module.md
- Import_Module.md
- Export_Module.md
- VoiceClone_Module.md
- AI_Module.md
- Project_Format.md

---

# 1. Purpose

Job представляет собой минимальную независимую единицу выполнения в системе Voxarium.

Любая длительная, ресурсоёмкая или потенциально отменяемая операция должна выполняться исключительно в виде Job.

Job является фундаментальной единицей исполнения прикладной логики.

Core не выполняет тяжёлые операции напрямую.

Все подобные действия выполняются через Job System.

---

# 2. Responsibility

Job отвечает исключительно за:

- описание выполняемой операции;
- хранение состояния выполнения;
- хранение параметров запуска;
- хранение результата выполнения;
- хранение информации об ошибках;
- поддержку отмены и восстановления.

Job не отвечает за:

- планирование;
- распределение задач;
- выполнение TTS;
- управление потоками.

Эти функции принадлежат Scheduler и Worker.

---

# 3. Business Motivation

Использование Job позволяет:

- выполнять операции асинхронно;
- использовать несколько CPU/GPU одновременно;
- безопасно прерывать операции;
- восстанавливать выполнение после сбоя;
- распределять задачи между несколькими компьютерами;
- реализовать серверный режим работы.

---

# 4. Aggregate

Job является Aggregate Root.

Job принадлежит одному Project.

Workflow может создавать множество Job.

---

# 5. Identity

Каждый Job имеет постоянный UUID v7.

UUID никогда не изменяется.

---

# 6. Required Attributes

| Name | Type | Required | Mutable |
|------|------|----------|----------|
| id | UUIDv7 | Yes | No |
| jobType | JobType | Yes | No |
| state | JobState | Yes | Yes |
| priority | JobPriority | Yes | Yes |
| createdAt | UTC DateTime | Yes | No |
| updatedAt | UTC DateTime | Yes | Yes |

---

# 7. Optional Attributes

| Name | Type |
|------|------|
| workflowId | UUID |
| ownerId | UUID |
| parentJobId | UUID |
| progress | Percentage |
| result | JobResult |
| error | JobError |
| metadata | Map<String, Value> |

---

# 8. Standard Job Types

Минимально поддерживаются:

- Import
- Parse
- Character Detection
- Translation
- Voice Cloning
- Speech Generation
- Audio Validation
- Loudness Normalization
- Export
- Cleanup
- AI Analysis
- Plugin Execution

Plugin могут регистрировать собственные Job Type.

---

# 9. Job State

Job может находиться только в одном состоянии.

Created

Queued

Waiting

Running

Paused

Completed

Cancelled

Failed

Archived

---

# 10. State Machine

Допустимые переходы.

Created

↓

Queued

↓

Running

↓

Completed

Также допускаются:

Running → Paused

Paused → Running

Running → Failed

Running → Cancelled

Failed → Queued

Completed → Archived

Cancelled → Archived

---

# 11. Progress

Каждый Job публикует прогресс выполнения.

Диапазон:

0%

↓

100%

Если вычисление процента невозможно, используется неопределённый режим (Indeterminate).

---

# 12. Parent–Child Jobs

Job может создавать дочерние Job.

Пример.

Generate Chapter

↓

Generate Fragment 1

Generate Fragment 2

Generate Fragment 3

...

Parent Job считается завершённым только после завершения всех дочерних Job.

---

# 13. Retry Policy

Job может иметь собственную политику повторного выполнения.

Поддерживаются:

- Never
- Immediate
- Delayed
- Manual
- Exponential Backoff

---

# 14. Cancellation

Любой Job должен поддерживать безопасную отмену.

При отмене:

- освобождаются ресурсы;
- сохраняется состояние;
- результаты остаются согласованными.

Частично созданные данные не должны повреждать Project.

---

# 15. Priority

Поддерживаются уровни приоритета.

Critical

High

Normal

Low

Background

Scheduler обязан учитывать приоритет при выборе следующего Job.

---

# 16. Dependencies

Job может зависеть от других Job.

Запуск допускается только после успешного завершения всех зависимостей.

Циклические зависимости запрещены.

---

# 17. Commands

CreateJob

QueueJob

PauseJob

ResumeJob

CancelJob

RetryJob

ArchiveJob

DeleteJob

---

# 18. Domain Events

JobCreated

JobQueued

JobStarted

JobPaused

JobResumed

JobCompleted

JobCancelled

JobFailed

JobArchived

---

# 19. Invariants

Job обязан удовлетворять следующим требованиям.

Имеет UUID.

Имеет Job Type.

Имеет одно состояние.

Имеет корректный жизненный цикл.

Не содержит циклических зависимостей.

---

# 20. Validation

Перед постановкой в очередь проверяются:

- корректность параметров;
- существование зависимостей;
- отсутствие циклов;
- допустимость Job Type;
- доступность необходимых Plugin.

---

# 21. Recovery

После восстановления приложения все Job должны перейти в согласованное состояние.

Job, находившиеся в состоянии Running, автоматически переводятся в Waiting Recovery.

Scheduler самостоятельно принимает решение:

- продолжить выполнение;
- повторить выполнение;
- пометить Job как Failed.

---

# 22. Performance Requirements

Job должен быть максимально лёгкой сущностью.

Создание десятков тысяч Job не должно приводить к существенному увеличению потребления памяти.

Очередь должна поддерживать миллионы Job.

---

# 23. Extensibility

Plugin могут добавлять:

- собственные Job Type;
- собственные параметры;
- пользовательские результаты;
- дополнительные диагностические данные.

Core рассматривает эти данные как непрозрачные расширения.

---

# 24. Test Requirements

Должны существовать автоматические тесты, проверяющие:

- создание Job;
- жизненный цикл;
- отмену;
- повторное выполнение;
- дочерние Job;
- зависимости;
- восстановление после сбоя;
- масштабирование до миллионов Job.

---

# 25. Future Compatibility

Архитектура должна поддерживать:

- распределённое выполнение;
- удалённые Worker;
- выполнение в контейнерах;
- облачные вычисления;
- GPU-кластеры;
- сетевое распределение нагрузки.

Настоящий документ определяет только предметную модель Job.

---

# 26. Compliance

Любая реализация Job обязана соответствовать требованиям настоящего документа.

Изменение модели Job допускается исключительно посредством изменения настоящей спецификации и оформления соответствующего Architecture Decision Record.

---

End of Document