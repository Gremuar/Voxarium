# Voxarium Software Architecture Specification

Document Path:
spec/300_Contracts/ITimelineService.md

Document ID: CTR-003

Title: ITimelineService

Version: 1.0.0

Status: Accepted

Classification: Normative

Depends On

- CTR-000 IService
- Project
- Timeline
- Fragment
- SpeechSegment
- AudioTrack

Referenced By

- Timeline_Service
- Generation_Service
- Workflow_Engine
- Audio_Service
- Export_Service
- User_Interface_Architecture

---

# 1. Purpose

ITimelineService определяет публичный контракт управления Timeline проекта.

Контракт отвечает за построение, изменение, синхронизацию и анализ временной структуры проекта.

Timeline является производным представлением Domain Model и не является источником истины.

---

# 2. Responsibilities

Контракт SHALL обеспечивать:

- создание Timeline;
- перестроение Timeline;
- синхронизацию Timeline с Document;
- управление элементами Timeline;
- вычисление временных характеристик;
- получение информации о Timeline.

---

# 3. Non-Responsibilities

Контракт SHALL NOT:

- изменять Document;
- изменять SpeechSegment;
- выполнять генерацию;
- выполнять экспорт;
- выполнять воспроизведение.

---

# 4. Lifecycle Operations

## 4.1 CreateTimeline

### Purpose

Создает новую Timeline.

### Parameters

- ProjectId

### Returns

- Timeline

### Preconditions

- Project существует.

### Postconditions

- Создана новая Timeline.

### Published Events

- TimelineCreated

### Errors

- ProjectNotFound

---

## 4.2 RebuildTimeline

### Purpose

Полностью перестраивает Timeline на основании текущего состояния Domain Model.

### Parameters

- TimelineId

### Returns

- Timeline

### Preconditions

- Timeline существует.

### Postconditions

- Timeline полностью пересчитана.

### Published Events

- TimelineRebuilt

### Errors

- TimelineNotFound
- ValidationFailed

---

## 4.3 SynchronizeTimeline

### Purpose

Синхронизирует Timeline после изменения Domain Model.

### Parameters

- TimelineId

### Returns

- Timeline

### Preconditions

- Timeline существует.

### Postconditions

- Timeline соответствует текущему состоянию Project.

### Published Events

- TimelineSynchronized

### Errors

- TimelineNotFound

---

# 5. Structural Operations

## 5.1 InsertTimelineItem

### Purpose

Добавляет новый элемент Timeline.

### Parameters

- TimelineId
- Position

### Returns

- TimelineItem

### Published Events

- TimelineItemInserted

---

## 5.2 RemoveTimelineItem

### Purpose

Удаляет элемент Timeline.

### Parameters

- TimelineItemId

### Returns

Нет.

### Published Events

- TimelineItemRemoved

---

## 5.3 MoveTimelineItem

### Purpose

Изменяет порядок элемента Timeline.

### Parameters

- TimelineItemId
- NewPosition

### Returns

- TimelineItem

### Published Events

- TimelineItemMoved

---

# 6. Timing Operations

## 6.1 RecalculateDurations

### Purpose

Пересчитывает длительности всех элементов Timeline.

### Parameters

- TimelineId

### Returns

- Timeline

### Published Events

- TimelineDurationRecalculated

---

## 6.2 RecalculateOffsets

### Purpose

Пересчитывает временные смещения.

### Parameters

- TimelineId

### Returns

- Timeline

### Published Events

- TimelineOffsetsRecalculated

---

# 7. Query Operations

Контракт SHALL предоставлять запросы:

- GetTimeline
- GetTimelineItem
- GetTimelineStatistics
- GetTotalDuration
- GetCurrentRevision
- FindTimelineItemsByFragment
- FindTimelineItemsBySpeechSegment

Query SHALL NOT изменять состояние системы.

---

# 8. Synchronization Rules

Timeline SHALL автоматически отражать изменения:

- Document;
- Fragment;
- SpeechSegment;
- AudioTrack.

Механизм синхронизации определяется реализацией.

---

# 9. Transaction Rules

Каждая операция изменения SHALL выполняться в пределах одной прикладной транзакции.

---

# 10. Thread Safety

Контракт SHALL поддерживать параллельные операции чтения.

Изменение одной Timeline SHALL сериализоваться.

---

# 11. Dependencies

Контракт SHALL зависеть только от:

- Domain Model;
- IService.

Контракт SHALL NOT зависеть от:

- GUI;
- Infrastructure;
- AI Runtime.

---

# 12. AI Implementation Rules

Реализация SHALL:

- считать Timeline производной моделью;
- не использовать Timeline как источник истины;
- выполнять пересчет только через публичные операции;
- публиковать события после успешного завершения транзакции.

---

# 13. Test Requirements

Для каждой операции SHALL существовать тесты:

- успешное выполнение;
- нарушение Preconditions;
- проверка Postconditions;
- публикация событий;
- откат транзакции.

---

# 14. Compliance Checklist

Контракт соответствует настоящей спецификации только если:

- предоставляет полный набор операций управления Timeline;
- разделяет Commands и Queries;
- определяет Preconditions и Postconditions;
- документирует события;
- не изменяет Domain Model напрямую;
- соответствует IService.

---

End of Document