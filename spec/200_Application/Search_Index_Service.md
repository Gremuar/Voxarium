# Voxarium Software Architecture Specification

Document Path:
spec/200_Application/Search_Index_Service.md

Document ID: APP-024

Title: Search Index Service

Version: 1.0.0

Status: Accepted

Classification: Normative

Depends On

- DOM-101 Project
- DOM-103 Document
- DOM-104 Text Fragment
- DOM-105 Character
- DOM-106 Voice Profile
- DOM-102 Asset
- APP-017 Project Service
- APP-015 Application Event Model

Referenced By

- UI Search Interface
- Project Navigator
- Timeline Editor
- Character Management
- Voice Management
- Workflow Engine

---

# 1. Purpose

Search Index Service является подсистемой поиска и индексации данных внутри Voxarium.

Основная задача:

обеспечить быстрый поиск по содержимому проекта независимо от физического расположения данных.

---

# 2. Main Concept

Voxarium работает с большими проектами:

- книги на тысячи страниц;
- десятки тысяч текстовых фрагментов;
- сотни персонажей;
- тысячи аудиофрагментов;
- множество версий генерации.

Прямой поиск по исходным данным становится неэффективным.

Поэтому используется индекс.

```
Project Data

↓

Index Builder

↓

Search Index

↓

Query

↓

Results

```

---

# 3. Responsibilities

Search Index Service отвечает за:

- построение индекса;
- обновление индекса;
- выполнение запросов;
- поиск текста;
- поиск объектов проекта;
- поиск связанных данных.

Search Index Service не отвечает за:

- изменение данных;
- хранение оригиналов;
- генерацию аудио;
- управление проектом.

---

# 4. Architectural Position

```
Domain Objects

↓

Events

↓

Search Index Service

↓

Search Database

↓

UI Query

```

---

# 5. Indexed Entities

Минимально индексируются:

---

## Documents

Индекс:

- название;
- автор;
- текст;
- главы;
- разделы.

---

## Text Fragments

Индекс:

- текст;
- позиция;
- персонаж;
- глава.

---

## Characters

Индекс:

- имя;
- описание;
- связанные фрагменты.

---

## Voice Profiles

Индекс:

- имя;
- описание;
- язык;
- характеристики.

---

## Audio Assets

Индекс:

- название;
- источник;
- дата;
- параметры генерации.

---

## Jobs

Индекс:

- тип;
- статус;
- ошибки.

---

# 6. Index Model

Индекс содержит:

```
Object ID

Object Type

Project ID

Search Text

Metadata

Relations

Location

```

---

# 7. Search Types

Поддерживаются:

---

## Full Text Search

Пример:

```
"лесная дорога"

```

Поиск:

- книги;
- главы;
- реплики.

---

## Metadata Search

Пример:

```
voice: narrator

```

---

## Structural Search

Пример:

```
Chapter 5

Character: John

```

---

## Semantic Search

Расширение:

по смыслу текста.

Пример:

```
сцены с конфликтом

```

---

# 8. Search Query Model

Запрос:

```
Search Request

{

Text

Filters

Project Scope

Object Types

Options

}

```

---

# 9. Search Result Model

Результат:

```
Search Result

{

Object ID

Type

Preview

Location

Score

}

```

---

# 10. Relevance Ranking

Результаты сортируются по:

- совпадению текста;
- позиции;
- частоте;
- типу объекта;
- пользовательскому контексту.

---

# 11. Incremental Index Update

Индекс обновляется через события.

Пример:

```
TextFragmentUpdated

↓

Update Index

```

Не требуется полная перестройка.

---

# 12. Event Integration

Используются:

```
DocumentImported

FragmentCreated

FragmentUpdated

CharacterCreated

VoiceCreated

AudioGenerated

```

---

# 13. Index Building

При открытии старого проекта:

```
Check Index

↓

Valid

↓

Use


Invalid

↓

Rebuild

```

---

# 14. Project Isolation

Индекс должен учитывать границы проекта.

Запрещено:

```
Project A

↓

Search

↓

Project B Data

```

---

# 15. Offline Operation

Поиск должен работать полностью локально.

Внешние сервисы не обязательны.

---

# 16. Storage

Возможные реализации:

- SQLite FTS;
- embedded search engine;
- локальная индексная база.

Выбор реализации скрыт за интерфейсом.

---

# 17. Semantic Search Extension

Архитектура должна позволять добавить:

- embeddings;
- vector search;
- AI-поиск.

Пример:

```
Text

↓

Embedding Plugin

↓

Vector Index

↓

Semantic Query

```

---

# 18. AI Integration

В будущем:

пользователь:

> "Найди все сцены, где герой спорит с наставником"

Система:

```
Semantic Search

↓

Relevant Fragments

```

---

# 19. UI Integration

Поиск используется для:

- навигации;
- перехода к фрагменту;
- поиска ошибок;
- анализа проекта.

---

# 20. Workflow Integration

Workflow может использовать поиск.

Пример:

```
Find all fragments:

Character = Hero


↓

Regenerate Voice

```

---

# 21. Performance Requirements

Search Index Service должен обеспечивать:

- быстрый поиск;
- работу с большими книгами;
- обновление без блокировки;
- низкое потребление ресурсов.

---

# 22. Recovery

При повреждении индекса:

```
Delete Index

↓

Rebuild

↓

Continue

```

Оригинальные данные не должны быть затронуты.

---

# 23. Security

Индекс может содержать:

- текст;
- метаданные;
- ссылки.

Необходимо:

- соблюдать права доступа;
- не хранить лишние копии данных.

---

# 24. Test Requirements

Проверяются:

- построение индекса;
- обновление;
- поиск;
- фильтры;
- восстановление;
- большие проекты.

---

# 25. Compliance

Любая реализация Search Index Service обязана соответствовать настоящему документу.

---

# Appendix A. Example

Проект:

```
War and Peace

```

Запрос:

```
"битва"

```

Результат:

```
Chapter 12

Fragment 845


Character:

Narrator


Audio:

generated_845.wav

```

---

End of Document