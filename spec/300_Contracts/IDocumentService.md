# Voxarium Software Architecture Specification

Document Path:
spec/300_Contracts/IDocumentService.md

Document ID: CTR-002

Title: IDocumentService

Version: 1.0.0

Status: Accepted

Classification: Normative

Depends On

- CTR-000 IService
- Project
- Document
- Fragment
- SpeechSegment
- Role

Referenced By

- Document_Service
- Timeline_Service
- Generation_Service
- User_Interface_Architecture

---

# 1. Purpose

IDocumentService определяет публичный контракт управления текстовыми документами проекта.

Контракт является единственной точкой входа для изменения структуры Document.

---

# 2. Responsibilities

Контракт SHALL обеспечивать:

- управление жизненным циклом Document;
- управление Fragment;
- управление SpeechSegment;
- структурные преобразования документа;
- проверку допустимости операций.

---

# 3. Non-Responsibilities

Контракт SHALL NOT:

- выполнять импорт;
- выполнять экспорт;
- изменять Timeline;
- выполнять генерацию речи;
- выполнять воспроизведение;
- сохранять проект.

---

# 4. Operations

## 4.1 CreateDocument

### Purpose

Создает новый Document внутри Project.

### Parameters

- ProjectId
- DocumentName

### Returns

- Document

### Preconditions

- Project существует.
- Имя документа допустимо.

### Postconditions

- Создан новый Document.
- Document добавлен в Project.

### Published Events

- DocumentCreated

### Errors

- ProjectNotFound
- DuplicateDocumentName
- ValidationFailed

---

## 4.2 DeleteDocument

### Purpose

Удаляет существующий Document.

### Parameters

- DocumentId

### Returns

Нет.

### Preconditions

- Document существует.

### Postconditions

- Document удален из Project.

### Published Events

- DocumentDeleted

### Errors

- DocumentNotFound
- ValidationFailed

---

## 4.3 RenameDocument

### Purpose

Изменяет имя документа.

### Parameters

- DocumentId
- NewName

### Returns

- Document

### Preconditions

- Document существует.
- Новое имя допустимо.

### Postconditions

- Имя документа обновлено.
- Revision увеличен.

### Published Events

- DocumentRenamed

### Errors

- DocumentNotFound
- DuplicateDocumentName
- ValidationFailed

---

## 4.4 CreateFragment

### Purpose

Создает новый Fragment.

### Parameters

- DocumentId
- InsertPosition

### Returns

- Fragment

### Preconditions

- Document существует.

### Postconditions

- Fragment добавлен в Document.

### Published Events

- FragmentCreated

### Errors

- DocumentNotFound
- InvalidInsertPosition

---

## 4.5 DeleteFragment

### Purpose

Удаляет Fragment.

### Parameters

- FragmentId

### Returns

Нет.

### Preconditions

- Fragment существует.

### Postconditions

- Fragment удален.

### Published Events

- FragmentDeleted

### Errors

- FragmentNotFound

---

## 4.6 SplitFragment

### Purpose

Разделяет Fragment на два независимых Fragment.

### Parameters

- FragmentId
- SplitOffset

### Returns

- Fragment
- Fragment

### Preconditions

- Fragment существует.
- Позиция разделения допустима.

### Postconditions

- Созданы два новых Fragment.
- Исходный Fragment удален.

### Published Events

- FragmentSplit

### Errors

- FragmentNotFound
- InvalidSplitOffset

---

## 4.7 MergeFragments

### Purpose

Объединяет два соседних Fragment.

### Parameters

- FirstFragmentId
- SecondFragmentId

### Returns

- Fragment

### Preconditions

- Оба Fragment существуют.
- Fragment являются соседними.

### Postconditions

- Создан объединенный Fragment.
- Исходные Fragment удалены.

### Published Events

- FragmentsMerged

### Errors

- FragmentNotFound
- InvalidMergeOperation

---

## 4.8 CreateSpeechSegment

### Purpose

Создает новый SpeechSegment.

### Parameters

- FragmentId
- InsertPosition

### Returns

- SpeechSegment

### Preconditions

- Fragment существует.

### Postconditions

- SpeechSegment добавлен.

### Published Events

- SpeechSegmentCreated

### Errors

- FragmentNotFound

---

## 4.9 DeleteSpeechSegment

### Purpose

Удаляет SpeechSegment.

### Parameters

- SpeechSegmentId

### Returns

Нет.

### Preconditions

- SpeechSegment существует.

### Postconditions

- SpeechSegment удален.

### Published Events

- SpeechSegmentDeleted

### Errors

- SpeechSegmentNotFound

---

## 4.10 MoveSpeechSegment

### Purpose

Перемещает SpeechSegment.

### Parameters

- SpeechSegmentId
- TargetFragmentId
- TargetPosition

### Returns

- SpeechSegment

### Preconditions

- SpeechSegment существует.
- TargetFragment существует.

### Postconditions

- SpeechSegment перемещен.

### Published Events

- SpeechSegmentMoved

### Errors

- SpeechSegmentNotFound
- FragmentNotFound

---

# 5. Transaction Rules

Все операции изменения SHALL выполняться в одной прикладной транзакции.

---

# 6. Thread Safety

Контракт допускает параллельные операции чтения.

Изменение одного Document SHALL сериализоваться.

---

# 7. Dependencies

Контракт SHALL зависеть только от Domain Model и IService.

---

# 8. AI Implementation Rules

Реализация SHALL:

- изменять Domain только через Aggregate Root;
- соблюдать порядок публикации событий;
- не изменять Timeline напрямую;
- не обращаться к Infrastructure.

---

# 9. Test Requirements

Для каждой операции SHALL существовать:

- успешный сценарий;
- сценарий нарушения Preconditions;
- проверка Postconditions;
- проверка опубликованных событий;
- проверка отката транзакции.

---

# 10. Compliance Checklist

Контракт соответствует настоящей спецификации только если:

- все операции имеют полную спецификацию;
- каждая операция определяет Preconditions;
- каждая операция определяет Postconditions;
- каждая операция определяет Published Events;
- каждая операция определяет Errors;
- контракт соответствует IService.

---

End of Document