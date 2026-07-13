# Voxarium Software Architecture Specification

Document Path:
spec/200_Application/Document_Service.md

Document ID: APP-030

Title: Document Service

Version: 1.0.0

Status: Accepted

Classification: Normative

Depends On

- SAS-003 Architecture Principles
- SAS-006 Common Domain Patterns
- Project
- Document
- Fragment
- SpeechSegment
- Role

Referenced By

- Project_Service
- Timeline_Service
- Generation_Service
- Search_Index_Service
- User_Interface_Architecture

---

# 1. Purpose

Document Service является единственной точкой входа Application Layer для управления текстовыми документами проекта.

Сервис инкапсулирует все операции изменения структуры документа независимо от пользовательского интерфейса и способа хранения данных.

---

# 2. Responsibilities

Document Service SHALL:

- создавать документы;
- удалять документы;
- изменять свойства документа;
- управлять структурой Fragment;
- управлять SpeechSegment;
- выполнять операции разделения и объединения;
- выполнять перемещение элементов;
- публиковать события приложения.

---

# 3. Non-Responsibilities

Document Service SHALL NOT:

- выполнять импорт файлов;
- выполнять экспорт;
- генерировать речь;
- воспроизводить аудио;
- управлять Timeline;
- выполнять поиск;
- сохранять проект на диск.

---

# 4. Public Operations

Document Service предоставляет следующие операции.

### Document

- CreateDocument
- DeleteDocument
- RenameDocument
- DuplicateDocument

### Fragment

- CreateFragment
- DeleteFragment
- MoveFragment
- SplitFragment
- MergeFragment

### SpeechSegment

- CreateSpeechSegment
- DeleteSpeechSegment
- SplitSpeechSegment
- MergeSpeechSegment
- MoveSpeechSegment

---

# 5. Structural Rules

Все изменения SHALL сохранять корректность структуры.

Допустимая иерархия.

```
Project

└── Document

    └── Fragment

        └── SpeechSegment
```

Нарушение структуры запрещено.

---

# 6. Editing Operations

Document Service SHALL поддерживать:

- вставку;
- удаление;
- копирование;
- вырезание;
- перемещение;
- дублирование;
- изменение порядка элементов.

Все операции должны быть атомарными.

---

# 7. Text Integrity

После любой операции SHALL выполняться проверка:

- отсутствия потерянных сегментов;
- отсутствия циклических ссылок;
- корректности Identifier;
- корректности Revision.

---

# 8. Transaction Rules

Каждая публичная операция SHALL выполняться как единая транзакция.

При ошибке состояние документа должно быть полностью восстановлено.

---

# 9. Interaction With Timeline

Document Service SHALL NOT изменять Timeline напрямую.

Если изменение документа влияет на Timeline —

публикуется Application Event.

Timeline Service самостоятельно принимает решение о пересборке Timeline.

---

# 10. Interaction With Generation

Document Service SHALL NOT инициировать генерацию.

После изменения SpeechSegment публикуется событие:

```
SpeechSegmentChanged
```

Generation Service самостоятельно принимает решение о необходимости новой генерации.

---

# 11. Validation

Перед изменением SHALL проверяться:

- существование Document;
- существование Fragment;
- существование SpeechSegment;
- допустимость операции;
- соблюдение инвариантов Domain.

---

# 12. Event Publication

После успешного изменения публикуются Application Events.

Минимальный набор.

- DocumentCreated
- DocumentDeleted
- DocumentRenamed
- FragmentCreated
- FragmentDeleted
- FragmentMoved
- SpeechSegmentCreated
- SpeechSegmentDeleted
- SpeechSegmentMoved
- SpeechSegmentChanged

---

# 13. Error Categories

Ошибки классифицируются следующим образом.

- Validation Error
- Domain Rule Violation
- Concurrent Modification
- Missing Entity
- Internal Error

Ошибки SHALL возвращаться вызывающему компоненту.

---

# 14. Concurrency

Document Service SHALL использовать оптимистичную блокировку.

Конфликтующие изменения должны обнаруживаться по Revision Aggregate Root.

---

# 15. Dependencies

Document Service MAY использовать:

- Project Service;
- Event Bus;
- Command Bus;
- Query Bus.

Document Service SHALL NOT зависеть от:

- GUI;
- Storage;
- Audio Service;
- Playback Service;
- Generation Runtime.

---

# 16. AI Implementation Rules

Реализация SHALL:

- изменять Domain только через Aggregate Root;
- использовать Commands;
- публиковать Application Events;
- не обращаться напрямую к Repository других Aggregate;
- не изменять Timeline напрямую.

---

# 17. Test Requirements

Минимальный набор тестов.

- создание документа;
- удаление документа;
- создание Fragment;
- перемещение Fragment;
- разделение Fragment;
- объединение Fragment;
- создание SpeechSegment;
- перемещение SpeechSegment;
- публикация событий;
- откат транзакции при ошибке.

---

# 18. Compliance Checklist

Document Service соответствует настоящей спецификации только если:

- является единственной точкой изменения Document;
- не изменяет Timeline напрямую;
- не инициирует генерацию;
- публикует события;
- поддерживает атомарные операции;
- использует оптимистичную блокировку;
- не зависит от GUI;
- не зависит от Infrastructure.

---

End of Document