# Voxarium Software Architecture Specification

Document Path:
spec/200_Application/Event_Bus.md

Document ID: APP-006

Title: Event Bus

Version: 1.0.0

Status: Accepted

Classification: Normative

Depends On

- APP-001 Application Architecture
- APP-002 Command Model
- APP-004 Command Bus
- Все документы раздела 100_Domain

Referenced By

- Event Handlers
- Job System
- Workflow Engine
- Plugin System
- GUI
- Notification System
- Metrics Module

---

# 1. Purpose

Event Bus является централизованной системой доставки событий внутри приложения.

Event Bus обеспечивает слабую связанность между компонентами системы.

Ни один компонент не должен напрямую уведомлять другие компоненты о произошедших изменениях.

Все уведомления распространяются исключительно через Event Bus.

---

# 2. Responsibilities

Event Bus отвечает за:

- публикацию событий;
- маршрутизацию событий;
- доставку подписчикам;
- регистрацию обработчиков;
- управление порядком доставки;
- журналирование;
- диагностику.

Event Bus не отвечает за:

- изменение Domain Model;
- выполнение Command;
- выполнение Query;
- хранение состояния событий.

---

# 3. Event Types

Поддерживаются три категории событий.

## Domain Event

Возникает внутри Domain Model.

Примеры:

ProjectCreated

FragmentSplit

VoiceAssigned

JobCompleted

---

## Application Event

Возникает внутри Application Layer.

Примеры:

WorkflowStarted

ImportFinished

GenerationQueueCreated

PluginLoaded

---

## Integration Event

Предназначен для взаимодействия с внешними системами.

Примеры:

WebhookSent

RESTNotification

CloudSyncStarted

PluginMessageReceived

---

# 4. Event Structure

Каждое событие содержит:

Event Id

Event Type

Schema Version

Timestamp

Correlation Id

Source

Payload

Metadata

---

# 5. Event Lifecycle

Domain Model

↓

Domain Event

↓

Command Bus Commit

↓

Event Bus

↓

Event Handlers

↓

Infrastructure

---

# 6. Publishing Rules

Событие публикуется только после успешного завершения транзакции.

При Rollback публикация запрещается.

---

# 7. Delivery Model

По умолчанию используется модель:

At Least Once

Каждый обработчик обязан быть идемпотентным.

---

# 8. Event Ordering

Для одного Aggregate события должны доставляться в порядке их возникновения.

Для независимых Aggregate порядок доставки не гарантируется.

---

# 9. Event Handlers

Одно событие может иметь любое количество обработчиков.

Каждый обработчик является независимым.

Ошибка одного обработчика не должна останавливать выполнение остальных.

---

# 10. Synchronous Events

По умолчанию публикация выполняется синхронно до завершения Use Case.

Используется для:

- обновления Read Model;
- публикации внутренних уведомлений;
- запуска зависимых операций.

---

# 11. Asynchronous Events

Для длительных операций Event Bus может использовать асинхронную доставку.

Примеры:

- AI-анализ;
- индексация;
- обновление поискового индекса;
- синхронизация;
- телеметрия.

---

# 12. Event Handler Isolation

Каждый Event Handler должен быть независим.

Обработчики не должны взаимодействовать друг с другом.

Любой обработчик может быть отключён без влияния на остальные.

---

# 13. Retry Policy

При ошибке обработки допускаются:

- Immediate Retry
- Delayed Retry
- Exponential Backoff
- Dead Letter Queue

Политика определяется конфигурацией.

---

# 14. Dead Letter Queue

События, которые не удалось обработать после всех попыток,

должны быть помещены в Dead Letter Queue.

Администратор должен иметь возможность повторно отправить их.

---

# 15. Event Filtering

Подписчики могут получать:

- все события;
- события конкретного типа;
- события определённого Aggregate;
- события конкретного Plugin;
- события определённого Project.

---

# 16. Logging

Фиксируются:

- публикация события;
- обработчики;
- время доставки;
- ошибки;
- повторные попытки.

---

# 17. Metrics

Минимальный набор метрик.

Events/sec

Average Delivery Time

Failed Events

Retry Count

Handler Execution Time

Dead Letter Queue Size

---

# 18. Thread Safety

Event Bus полностью потокобезопасен.

Несколько событий могут публиковаться одновременно.

Независимые обработчики могут выполняться параллельно.

---

# 19. Plugin Integration

Plugin могут:

- публиковать собственные события;
- подписываться на события;
- создавать собственные типы событий.

Plugin не могут вмешиваться в Core Event Pipeline.

---

# 20. Security

Все события проходят проверку допустимости публикации.

Plugin не должны иметь возможности публиковать системные события Core.

---

# 21. Recovery

После аварийного завершения приложения должна существовать возможность определить:

- опубликовано ли событие;
- доставлено ли событие;
- какие обработчики завершились успешно;
- какие требуют повторного выполнения.

---

# 22. Performance Requirements

Event Bus должен поддерживать:

- десятки тысяч событий в минуту;
- параллельную обработку;
- минимальные задержки доставки;
- низкое потребление памяти.

---

# 23. Test Requirements

Должны существовать тесты, проверяющие:

- публикацию;
- доставку;
- порядок событий;
- многопоточность;
- идемпотентность;
- Retry;
- Dead Letter Queue;
- регистрацию обработчиков.

---

# 24. Compliance

Любая реализация Event Bus обязана соответствовать настоящему документу.

---

# Appendix A. Reference Event Flow

Command

↓

Command Handler

↓

Domain Model

↓

Commit

↓

Domain Events

↓

Event Bus

↓

Event Handlers

↓

Read Model

↓

Notifications

↓

Plugins

---

End of Document