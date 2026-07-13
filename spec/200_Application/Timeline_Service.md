# Voxarium Software Architecture Specification

Document Path:
spec/200_Application/Timeline_Service.md

Document ID: APP-021

Title: Timeline Service

Version: 1.0.0

Status: Accepted

Classification: Normative

Depends On

- DOM-107 Audio Segment
- DOM-108 Timeline
- DOM-104 Text Fragment
- APP-017 Project Service
- APP-020 Audio Service
- APP-018 Generation Service
- Export Service

Referenced By

- UI Timeline Editor
- Audio Mixing Module
- Subtitle Export Module
- Audiobook Export Module
- Video Voiceover Module

---

# 1. Purpose

Timeline Service является подсистемой управления временной структурой аудиопроекта Voxarium.

Основная задача:

создать абстрактную модель последовательности звуковых и текстовых элементов, которая связывает:

- исходный текст;
- персонажей;
- голоса;
- аудиофрагменты;
- паузы;
- музыку;
- эффекты;
- главы;
- сцены.

---

# 2. Main Concept

В Voxarium итоговое произведение строится не из файлов, а из Timeline.

Файл является результатом сборки.

Главная модель:

```
Project

↓

Timeline

↓

Segments

↓

Audio Assets

```

---

# 3. Responsibilities

Timeline Service отвечает за:

- создание Timeline;
- управление сегментами;
- позиционирование аудио;
- изменение порядка;
- расчёт длительности;
- синхронизацию текста и звука;
- подготовку данных для экспорта.

Timeline Service не отвечает за:

- генерацию речи;
- обработку аудио;
- хранение физических файлов;
- кодирование итогового формата.

---

# 4. Architectural Position

```
Generation Service

↓

Audio Assets

↓

Timeline Service

↓

Composition

↓

Export Service

```

---

# 5. Timeline Model

Timeline является контейнером временных объектов.

Структура:

```
Timeline

{

Timeline ID

Project ID

Tracks

Markers

Duration

Version

}

```

---

# 6. Timeline Components

Timeline состоит из:

```
Tracks

Segments

Markers

Chapters

Scenes

```

---

# 7. Track Model

Track представляет отдельный поток.

Типы:

```
Voice Track

Music Track

Effect Track

Ambient Track

Subtitle Track

```

---

# 8. Audio Segment

Segment является минимальным элементом монтажа.

Содержит:

```
Segment ID

Asset ID

Start Time

Duration

Source Fragment

Character

Voice Profile

Volume

Effects

```

---

# 9. Text Synchronization

Каждый Audio Segment может быть связан с текстом.

Связь:

```
Text Fragment

↓

Audio Segment

↓

Time Range

```

Позволяет:

- подсветку текста;
- создание субтитров;
- навигацию по книге.

---

# 10. Timeline Generation

После генерации:

```
Audio Asset Created

↓

Create Segment

↓

Calculate Duration

↓

Insert Position

↓

Update Timeline

```

---

# 11. Automatic Placement

Timeline Service должен уметь автоматически размещать сегменты.

Пример:

```
Segment 1

00:00 - 00:10


Segment 2

00:10 - 00:25


Segment 3

00:25 - 00:40

```

---

# 12. Manual Editing

Пользователь может:

- перемещать сегменты;
- менять порядок;
- добавлять паузы;
- изменять громкость;
- редактировать дорожки.

---

# 13. Chapter Model

Произведение может иметь структуру:

```
Book

├── Chapter 1

│   ├── Scene 1

│   └── Scene 2


├── Chapter 2

└── Chapter 3

```

---

# 14. Scene Model

Scene объединяет связанные сегменты.

Пример:

```
Scene:

Conversation in room


Segments:

Narrator

Hero

Villain

```

---

# 15. Markers

Timeline поддерживает метки.

Используются для:

- глав;
- сцен;
- заметок;
- переходов.

---

# 16. Silence Segments

Пауза является объектом Timeline.

Пример:

```
Speech

↓

Silence 2 sec

↓

Speech

```

---

# 17. Dynamic Rebuild

При изменении:

- текста;
- голоса;
- аудио;

Timeline может быть пересобран частично.

---

# 18. Incremental Update

Изменение одного Fragment:

```
Fragment Changed

↓

Regenerate Audio

↓

Replace Segment

↓

Recalculate Timeline

```

Без полной пересборки.

---

# 19. Multi-language Support

Timeline должен поддерживать:

```
Original Language Track

↓

Translation Track

↓

Dub Track

```

---

# 20. Subtitle Integration

Timeline может использоваться для:

- SRT;
- ASS;
- VTT;
- встроенных субтитров.

---

# 21. Playback Integration

Timeline предоставляет данные для:

- предпрослушивания;
- навигации;
- синхронного чтения текста.

---

# 22. Export Integration

Export Service получает:

```
Timeline

↓

Render

↓

Final Output

```

---

# 23. Versioning

Timeline имеет версии.

Пример:

```
Timeline v1

Original


Timeline v2

Edited pauses


Timeline v3

New voices

```

---

# 24. Events

Timeline Service публикует:

```
TimelineCreated

SegmentAdded

SegmentUpdated

SegmentMoved

TimelineRebuilt

TimelineCompleted

```

---

# 25. Plugin Integration

Plugin могут расширять:

- анализ структуры;
- автоматический монтаж;
- интеллектуальные переходы.

---

# 26. Performance Requirements

Timeline Service должен поддерживать:

- длинные аудиокниги;
- тысячи сегментов;
- быстрый поиск;
- мгновенную навигацию.

---

# 27. Recovery

После сбоя:

- восстановить последнюю версию;
- проверить ссылки Asset;
- восстановить позиции.

---

# 28. Security

Timeline содержит ссылки на пользовательские материалы.

Необходимо:

- проверка доступа;
- защита от повреждения ссылок.

---

# 29. Test Requirements

Проверяются:

- создание Timeline;
- добавление Segment;
- пересчёт времени;
- синхронизация;
- экспорт;
- восстановление.

---

# 30. Compliance

Любая реализация Timeline Service обязана соответствовать настоящему документу.

---

# Appendix A. Example

Аудиокнига:

```
Timeline

Chapter 1

00:00

Narrator Segment


00:15

Hero Segment


00:30

Narrator Segment


00:45

Scene End Marker


01:00

Chapter 2

```

---

End of Document