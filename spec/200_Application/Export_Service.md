# Voxarium Software Architecture Specification

Document Path:
spec/200_Application/Export_Service.md

Document ID: APP-023

Title: Export Service

Version: 1.0.0

Status: Accepted

Classification: Normative

Depends On

- DOM-101 Project
- DOM-108 Timeline
- DOM-102 Asset
- APP-017 Project Service
- APP-021 Timeline Service
- APP-020 Audio Service
- APP-015 Application Event Model
- Export Plugin Contract

Referenced By

- UI Export Wizard
- Publishing Module
- External Integrations
- Workflow Engine

---

# 1. Purpose

Export Service является подсистемой финальной подготовки результатов проекта Voxarium.

Основная задача:

преобразовать внутреннюю модель проекта в готовые пользовательские продукты.

Примеры:

- аудиокнига;
- озвученное видео;
- набор аудиофайлов;
- субтитры;
- архив проекта.

---

# 2. Main Concept

Внутреннее представление Voxarium:

```
Project

↓

Timeline

↓

Assets

↓

Export

↓

External Format

```

---

# 3. Responsibilities

Export Service отвечает за:

- подготовку экспортных задач;
- сборку результата;
- создание файлов;
- добавление метаданных;
- выбор формата;
- проверку результата.

Export Service не отвечает за:

- генерацию речи;
- обработку исходного текста;
- редактирование Timeline;
- работу конкретного кодировщика.

---

# 4. Architectural Position

```
Project

↓

Timeline

↓

Export Service

↓

Export Plugin

↓

Final Product

```

---

# 5. Export Types

Минимальная поддержка:

---

## Audio Export

Форматы:

```
WAV

MP3

FLAC

OGG

AAC

```

---

## Audiobook Export

Форматы:

```
M4B

MKA

ZIP Package

```

---

## Subtitle Export

Форматы:

```
SRT

ASS

VTT

```

---

## Project Export

Форматы:

```
VXP Archive

Backup Package

```

---

# 6. Export Workflow

Общий процесс:

```
Select Export

↓

Validate Project

↓

Prepare Timeline

↓

Render

↓

Encode

↓

Add Metadata

↓

Validate Output

↓

Complete

```

---

# 7. Export Profile

Экспорт должен использовать профиль.

Пример:

```
Audiobook High Quality


Format:

M4B


Audio:

AAC

192 kbps


Metadata:

Enabled

```

---

# 8. Render Process

Timeline преобразуется:

```
Timeline

↓

Audio Composition

↓

Master Track

↓

Encoder

↓

File

```

---

# 9. Chapter Support

Аудиокнига должна поддерживать главы.

Источник:

```
Timeline Markers

↓

Chapters

↓

M4B Chapters

```

---

# 10. Metadata

Поддерживаются:

- название;
- автор;
- исполнитель;
- обложка;
- описание;
- язык;
- жанр;
- дата.

---

# 11. Cover Support

Проект может содержать:

```
Cover Image

↓

Embedded Metadata

```

---

# 12. Multiple Output

Один Workflow может создавать:

```
Audiobook.m4b

+

MP3 Chapters

+

SRT

+

Project Backup

```

---

# 13. Export Plugin System

Форматы подключаются через Plugin.

Примеры:

```
Export.M4B

Export.YouTube

Export.Podcast

Export.Custom

```

---

# 14. Export Contract

Export Plugin предоставляет:

```
validate()

prepare()

render()

encode()

finalize()

```

---

# 15. Incremental Export

Поддерживается:

- экспорт одной главы;
- экспорт выбранного диапазона;
- обновление части результата.

---

# 16. Resume Export

При сбое:

- сохранить прогресс;
- продолжить;
- не пересобирать готовые части.

---

# 17. Validation

После экспорта проверяется:

- файл существует;
- формат корректен;
- длительность;
- метаданные;
- читаемость.

---

# 18. Compression

Поддерживается:

- качество;
- размер;
- битрейт;
- кодек.

---

# 19. Streaming Export

Архитектура должна позволять:

- потоковый экспорт;
- большие книги;
- отсутствие полной загрузки в RAM.

---

# 20. Publishing Integration

Возможное расширение:

```
Export

↓

Publishing Plugin

↓

External Platform

```

---

# 21. Workflow Integration

Пример:

```
Audiobook Production Workflow


Generate

↓

Process

↓

Timeline

↓

Export M4B

```

---

# 22. Event Integration

Export Service публикует:

```
ExportStarted

ExportProgressChanged

ExportCompleted

ExportFailed

```

---

# 23. Security

Перед экспортом проверяются:

- доступ к файлам;
- права;
- наличие необходимых данных.

---

# 24. Performance Requirements

Export Service должен поддерживать:

- большие проекты;
- длинные аудиокниги;
- параллельные экспорты;
- фоновые операции.

---

# 25. Test Requirements

Проверяются:

- все форматы;
- метаданные;
- главы;
- ошибки;
- восстановление;
- большие проекты.

---

# 26. Compliance

Любая реализация Export Service обязана соответствовать настоящему документу.

---

# Appendix A. Audiobook Export Example

Project:

```
Book Project

Timeline:

Chapter 1

Chapter 2

Chapter 3

```

Export:

```
Render Timeline

↓

Encode AAC

↓

Create M4B

↓

Insert:

- chapters
- cover
- metadata

↓

Final:

book.m4b

```

---

End of Document