# Voxarium Software Architecture Specification

Document Path:
spec/100_Domain/ProductionItem.md

Document ID: DOM-014

Title: ProductionItem

Version: 1.0.0

Status: Accepted

Classification: Normative

Depends On

- SAS-000 Project Philosophy
- SAS-001 Glossary
- SAS-003 Architecture Principles
- Production
- Document
- Timeline

Referenced By

- Audio_Service
- Export_Service
- Playback_Module

---

# 1. Purpose

ProductionItem представляет собой элемент композиции Production.

ProductionItem связывает конкретный Document с конкретной редакцией Timeline и определяет правила его включения в итоговое произведение.

ProductionItem является самостоятельной Domain Entity.

---

# 2. Responsibilities

ProductionItem SHALL отвечать за:

- ссылку на Document;
- ссылку на используемый Timeline;
- порядок расположения внутри Production;
- пользовательские параметры воспроизведения;
- состояние готовности элемента.

---

# 3. Non-Responsibilities

ProductionItem SHALL NOT:

- хранить текст;
- хранить SpeechSegment;
- хранить AudioTrack;
- выполнять генерацию;
- выполнять экспорт;
- выполнять обработку аудио.

---

# 4. Ownership

ProductionItem принадлежит Production.

```
Project
    │
    └── Production
            │
            └── ProductionItem
```

ProductionItem SHALL NOT существовать вне Production.

---

# 5. Identity

Каждый ProductionItem имеет неизменяемый Identifier.

Identifier SHALL:

- быть уникальным внутри Project;
- сохраняться при сериализации;
- никогда не изменяться.

---

# 6. Metadata

| Property | Required | Mutable |
|----------|----------|---------|
| Identifier | Yes | No |
| DocumentId | Yes | No |
| TimelineId | Yes | Yes |
| Order | Yes | Yes |
| Enabled | Yes | Yes |
| Revision | Yes | Yes |

---

# 7. Timeline Reference

ProductionItem всегда использует ровно один Timeline.

Допускается замена Timeline на другую редакцию.

После замены SHALL увеличиваться Revision.

---

# 8. Playback Properties

ProductionItem MAY содержать следующие логические параметры.

- Enabled
- Volume Adjustment
- Fade In
- Fade Out
- Start Offset
- End Offset

Все параметры являются декларативными.

Конкретная обработка принадлежит Audio Service.

---

# 9. Ordering

Порядок определяется исключительно коллекцией Production.

Поле Order является служебным и должно соответствовать положению элемента в коллекции.

---

# 10. Lifecycle

```
Created

↓

Configured

↓

Ready

↓

Archived
```

---

# 11. Invariants

ProductionItem SHALL удовлетворять следующим требованиям.

- Identifier существует.
- Document существует.
- Timeline существует.
- Revision ≥ 1.
- Document принадлежит тому же Project.

---

# 12. Creation Rules

При создании SHALL:

- создать Identifier;
- установить Revision = 1;
- установить Enabled = true;
- опубликовать ProductionItemCreated.

---

# 13. Modification Rules

Любое изменение SHALL:

- проверять ссылки;
- увеличивать Revision;
- публиковать ProductionItemModified.

---

# 14. Deletion Rules

Удаление ProductionItem SHALL NOT удалять:

- Document;
- Timeline;
- AudioTrack.

Удаляется только ссылка внутри Production.

---

# 15. Persistence

ProductionItem сериализуется исключительно как часть Production.

---

# 16. Concurrency

Допускается конкурентное чтение.

Конкурентная запись запрещена.

---

# 17. Domain Events

ProductionItem публикует:

- ProductionItemCreated
- ProductionItemModified
- ProductionItemRemoved
- ProductionItemEnabled
- ProductionItemDisabled

---

# 18. Commands

Поддерживаются команды.

- AddProductionItem
- RemoveProductionItem
- ReorderProductionItem
- ReplaceTimeline
- EnableProductionItem
- DisableProductionItem

---

# 19. AI Implementation Requirements

ProductionItem SHALL описывать только логическую композицию произведения.

Запрещается хранить:

- аудиофайлы;
- пути к файлам;
- параметры кодеков;
- параметры микширования.

---

# 20. Test Requirements

Минимальный набор тестов.

- создание;
- изменение Timeline;
- изменение порядка;
- сериализация;
- десериализация;
- проверка инвариантов;
- публикация событий.

---

# 21. Compliance Checklist

Реализация соответствует настоящей спецификации только если:

- ProductionItem принадлежит Production;
- хранит только логические ссылки;
- не содержит аудио;
- реализованы все события;
- реализованы все команды;
- соблюдены все инварианты;
- сериализация полностью воспроизводима.

---

End of Document