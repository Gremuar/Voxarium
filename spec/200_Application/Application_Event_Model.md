# Voxarium Software Architecture Specification

Document Path:
spec/200_Application/Application_Event_Model.md

Document ID: APP-015

Title: Application Event Model

Version: 1.0.0

Status: Accepted

Classification: Normative

Depends On

- APP-006 Event Bus
- APP-002 Command Model
- APP-003 Query Model
- APP-008 Job Orchestrator
- APP-014 Plugin Runtime

Referenced By

- UI Layer
- Workflow Engine
- Monitoring System
- Notification System
- Plugin API
- Logging System

---

# 1. Purpose

Настоящий документ определяет модель событий приложения Voxarium.

Application Event Model описывает:

- структуру событий;
- категории событий;
- жизненный цикл событий;
- правила публикации;
- правила подписки;
- использование событий различными подсистемами.

---

# 2. General Principle

События являются основным механизмом слабой связи между модулями.

Модуль, создавший событие, не должен знать:

- кто его получает;
- сколько подписчиков существует;
- какие действия будут выполнены.

Пример:

```
FragmentGenerated

        ↓

 ┌──────────────┬──────────────┬──────────────┐

 UI Update   Statistics    Workflow Update

```

---

# 3. Event Categories

В Voxarium используются следующие категории событий.

---

# 3.1 Domain Events

События предметной области.

Создаются Domain Layer.

Примеры:

```
ProjectCreated

DocumentImported

FragmentCreated

RoleAssigned

VoiceAssigned

ProductionCompleted

```

---

# 3.2 Application Events

События выполнения сценариев.

Создаются Application Layer.

Примеры:

```
ImportStarted

GenerationRequested

WorkflowStarted

ExportStarted

```

---

# 3.3 Infrastructure Events

События состояния системы.

Создаются Infrastructure Layer.

Примеры:

```
GPUAvailable

WorkerStarted

DiskSpaceLow

PluginLoaded

```

---

# 3.4 User Interface Events

События состояния представления.

Создаются UI Layer.

Примеры:

```
ViewOpened

SelectionChanged

PlaybackStarted

```

UI Events не должны влиять на Domain.

---

# 4. Event Structure

Каждое событие имеет обязательную структуру:

```
Event Envelope

{

EventId

EventType

SchemaVersion

CreatedAt

CorrelationId

Source

Payload

Metadata

}

```

---

# 5. Event ID

Каждое событие получает уникальный идентификатор.

Формат:

UUID v7

Используется для:

- диагностики;
- повторной доставки;
- журналирования.

---

# 6. Correlation ID

Correlation ID связывает события одной операции.

Пример:

```
Import Book

Correlation:

abc-123


Events:

DocumentImported

TextParsed

RolesDetected

VoicesAssigned

```

---

# 7. Event Ordering

Для одного объекта порядок событий гарантируется.

Пример:

```
FragmentCreated

↓

VoiceAssigned

↓

GenerationStarted

↓

GenerationCompleted

```

Для разных объектов порядок не гарантируется.

---

# 8. Event Publishing Rules

События публикуются:

- после успешного изменения состояния;
- после Commit;
- после подтверждения операции.

Запрещено публиковать событие о состоянии, которое не сохранено.

---

# 9. Event Naming Convention

Используется форма:

Past Tense Verb

Примеры:

Правильно:

```
ProjectCreated

VoiceAssigned

AudioGenerated

```

Неправильно:

```
CreateProject

AssignVoice

GenerateAudio

```

---

# 10. Event Payload Rules

Payload должен содержать:

- идентификаторы;
- изменившиеся значения;
- необходимые данные для реакции.

Payload не должен содержать:

- большие бинарные данные;
- аудиофайлы;
- модели;
- открытые соединения.

---

# 11. Large Data Handling

Большие данные передаются через ссылки.

Например:

Неправильно:

```
AudioGenerated

{

audioBytes: 200MB

}

```

Правильно:

```
AudioGenerated

{

AssetId:

audio-file-123

}

```

---

# 12. Subscription Model

Подписка выполняется по:

- типу события;
- категории;
- Aggregate;
- Project;
- Plugin Capability.

---

# 13. Event Handlers

Event Handler должен:

- выполнять одну задачу;
- быть идемпотентным;
- не изменять чужие Aggregate;
- использовать Command для изменений.

---

# 14. запрещённая схема

Недопустимо:

```
Event Handler

↓

прямое изменение Domain объекта

```

Правильно:

```
Event Handler

↓

Command Bus

↓

Command

↓

Handler

↓

Domain

```

---

# 15. UI Integration

UI подписывается на события.

Примеры:

```
GenerationProgressChanged

↓

Progress Bar


FragmentGenerated

↓

Update Timeline


VoiceAssigned

↓

Refresh Voice Panel

```

---

# 16. Workflow Integration

Workflow Engine использует события как триггеры.

Пример:

```
DocumentImported

↓

Start Role Detection

```

```
GenerationCompleted

↓

Start Audio Merge

```

---

# 17. Plugin Integration

Plugin могут:

- подписываться;
- публиковать собственные события;
- реагировать на системные события.

---

# 18. Event Persistence

Для критических событий допускается хранение.

Используется для:

- восстановления;
- аудита;
- диагностики;
- аналитики.

---

# 19. Event Replay

Система должна поддерживать повторное воспроизведение событий.

Использование:

- восстановление Read Model;
- отладка;
- миграция данных.

---

# 20. Error Handling

Ошибка Event Handler:

не должна отменять уже завершённую операцию.

Ошибка должна:

- фиксироваться;
- повторяться;
- попадать в Dead Letter Queue.

---

# 21. Security

События могут содержать пользовательские данные.

Необходимо:

- фильтровать доступ;
- скрывать запрещённые данные;
- контролировать Plugin подписки.

---

# 22. Performance Requirements

Event System должна поддерживать:

- большое количество событий;
- асинхронную доставку;
- пакетную обработку;
- низкие задержки.

---

# 23. Standard Core Events

Минимальный набор:

## Project

```
ProjectCreated

ProjectOpened

ProjectSaved

ProjectClosed

ProjectDeleted

```

---

## Document

```
DocumentImported

DocumentParsed

DocumentNormalized

```

---

## Timeline

```
FragmentCreated

FragmentUpdated

FragmentDeleted

FragmentMerged

FragmentSplit

```

---

## Voice

```
VoiceProfileCreated

VoiceAssigned

VoiceCloned

```

---

## Generation

```
GenerationStarted

GenerationProgressChanged

GenerationCompleted

GenerationFailed

```

---

## Job

```
JobCreated

JobQueued

JobStarted

JobCompleted

JobFailed

JobCancelled

```

---

## Plugin

```
PluginLoaded

PluginFailed

PluginUpdated

```

---

# 24. Test Requirements

Необходимо тестировать:

- публикацию событий;
- доставку;
- порядок;
- повторную обработку;
- ошибочные Handler;
- Plugin подписки;
- Replay.

---

# 25. Compliance

Любая реализация Event Model обязана соответствовать настоящему документу.

---

End of Document