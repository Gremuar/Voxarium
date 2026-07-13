# Voxarium Software Architecture Specification

Document Path:
spec/200_Application/Queue.md

Document ID: APP-010

Title: Queue

Version: 1.0.0

Status: Accepted

Classification: Normative

Depends On

- DOM-114 Job
- APP-008 Job Orchestrator
- APP-009 Scheduler
- APP-006 Event Bus

Referenced By

- Worker.md
- Scheduler.md
- Job Repository
- Persistence Layer

---

# 1. Purpose

Queue является компонентом системы выполнения задач Voxarium, предназначенным для хранения и управления ожидающими выполнения Job.

Queue является механизмом доставки задач между Job Orchestrator и Scheduler.

Queue не принимает решений о запуске задач.

---

# 2. Responsibilities

Queue отвечает за:

- хранение Job в состоянии Queued;
- быстрый поиск ожидающих задач;
- изменение состояния ожидания;
- временное резервирование Job;
- восстановление после сбоя;
- обеспечение порядка обработки.

Queue не отвечает за:

- выбор оптимальной задачи;
- выполнение Job;
- управление Worker;
- анализ ресурсов;
- бизнес-логику.

---

# 3. Architectural Position

```
Command Handler

↓

Job Orchestrator

↓

Queue

↓

Scheduler

↓

Worker

```

---

# 4. Queue Principles

Queue должна обеспечивать:

- надёжность;
- сохранность задач;
- возможность восстановления;
- высокую скорость операций;
- поддержку приоритетов;
- поддержку большого количества Job.

---

# 5. Queue Item

Queue хранит ссылку на Job.

Queue Item содержит:

- Job ID;
- Priority;
- Enqueue Time;
- State;
- Required Capabilities;
- Scheduling Metadata.

Queue Item не содержит бизнес-данные Job.

---

# 6. Queue States

Минимально:

Waiting

Reserved

Dispatched

Completed

Cancelled

Expired

Failed

---

# 7. Queue Lifecycle

Создание Job

↓

Queued

↓

Queue

↓

Scheduler

↓

Reserved

↓

Worker Assignment

↓

Running

↓

Completed / Failed

---

# 8. Priority Queue

Queue должна поддерживать сортировку по:

1. Priority.
2. Deadline.
3. Waiting Time.
4. Creation Time.

---

# 9. Fair Scheduling Support

Queue должна предоставлять Scheduler информацию для предотвращения голодания.

Например:

Job ожидает:

10 минут

↓

его эффективный приоритет увеличивается.

---

# 10. Reservation

Перед передачей Worker Scheduler резервирует Job.

Reservation предотвращает:

- двойной запуск;
- выполнение двумя Worker;
- потерю задачи.

---

# 11. Reservation Timeout

Если Worker не подтвердил получение Job,

Reservation автоматически снимается.

Job возвращается в очередь.

---

# 12. Persistence

Queue должна поддерживать сохранение состояния.

После перезапуска приложения:

- Queued Job должны быть восстановлены;
- Reserved Job должны пройти проверку;
- Running Job должны быть проверены.

---

# 13. Queue Storage

Архитектура должна поддерживать различные реализации:

Local Memory Queue

↓

Local Persistent Queue

↓

Database Queue

↓

Distributed Queue

Core не зависит от реализации.

---

# 14. Transaction Safety

Операции:

- добавление Job;
- резервирование;
- удаление;
- изменение состояния

должны быть атомарными.

---

# 15. Duplicate Prevention

Queue обязана предотвращать:

- повторное добавление одного Job;
- создание нескольких активных Queue Item для одного Job.

---

# 16. Batch Operations

Queue должна поддерживать:

- массовое добавление Job;
- массовое получение;
- массовое обновление состояния.

Это необходимо для больших проектов.

---

# 17. Filtering

Scheduler может запрашивать:

- только GPU Job;
- только CPU Job;
- Job конкретного Plugin;
- Job конкретного Project;
- Job определённого приоритета.

---

# 18. Dead Letter Queue

Job, которые невозможно выполнить после всех попыток,

перемещаются в отдельную Dead Letter Queue.

Информация сохраняется:

- причина ошибки;
- количество попыток;
- последний Worker;
- время ошибки.

---

# 19. Event Integration

Queue публикует события:

JobQueued

JobReserved

JobReleased

JobExpired

JobRemoved

---

# 20. Thread Safety

Queue должна поддерживать:

- одновременное добавление Job;
- получение Job Scheduler;
- обновление состояния Worker.

---

# 21. Performance Requirements

Минимальные требования:

- добавление Job: O(log n) или лучше;
- получение следующего Job: O(log n) или лучше;
- поддержка сотен тысяч Job;
- низкая задержка доступа.

---

# 22. Plugin Integration

Plugin не должны обращаться к Queue напрямую.

Все операции выполняются через:

Job Orchestrator

или

Application Ports.

---

# 23. Recovery

После аварии Queue должна:

- восстановить состояние;
- удалить устаревшие Reservation;
- вернуть потерянные Job;
- уведомить Scheduler.

---

# 24. Test Requirements

Должны существовать тесты:

- добавление Job;
- порядок приоритетов;
- резервирование;
- отмена;
- восстановление;
- конкурентный доступ;
- Dead Letter Queue.

---

# 25. Compliance

Любая реализация Queue обязана соответствовать настоящему документу.

---

# Appendix A. Example

Queue:

```
Priority  Waiting

Critical:
 Generate Fragment 12

High:
 Clone Voice

Normal:
 Generate Chapter 3
 Generate Chapter 4

Low:
 Export Preview
```

Scheduler:

↓

анализирует ресурсы

↓

назначает:

Generate Fragment 12

на GPU Worker

---

End of Document