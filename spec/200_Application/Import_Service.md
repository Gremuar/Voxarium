# Voxarium Software Architecture Specification

Document Path:
spec/200_Application/Import_Service.md

Document ID: APP-022

Title: Import Service

Version: 1.0.0

Status: Accepted

Classification: Normative

Depends On

- DOM-103 Document
- DOM-104 Text Fragment
- DOM-101 Project
- APP-017 Project Service
- APP-015 Application Event Model
- Plugin Architecture Specification

Referenced By

- Document Parser Plugins
- Subtitle Processing Module
- Audio Analysis Module
- Workflow Engine
- UI Import Wizard

---

# 1. Purpose

Import Service является подсистемой загрузки внешних данных в Voxarium.

Основная задача:

преобразовать внешние пользовательские материалы во внутреннюю модель проекта.

Поддерживаемые источники:

- книги;
- документы;
- сценарии;
- субтитры;
- текстовые файлы;
- аудиозаписи;
- метаданные.

---

# 2. Main Concept

Voxarium не работает напрямую с исходными файлами.

Процесс:

```
External File

↓

Import Service

↓

Internal Model

↓

Project

```

---

# 3. Responsibilities

Import Service отвечает за:

- приём файлов;
- определение формата;
- запуск Parser Plugin;
- извлечение содержимого;
- создание Document Entity;
- создание Text Fragment;
- импорт аудиоисточников;
- сохранение исходных данных.

Import Service не отвечает за:

- редактирование текста;
- генерацию речи;
- обработку аудио;
- экспорт.

---

# 4. Architectural Position

```
User

↓

Import Service

↓

Parser Plugin

↓

Document Model

↓

Project

```

---

# 5. Supported Import Types

Минимальная поддержка:

---

## Text Formats

```
TXT

MD

RTF

```

---

## Book Formats

```
EPUB

PDF

DOCX

ODT

```

---

## Subtitle Formats

```
SRT

ASS

VTT

SBV

```

---

## Audio Formats

```
WAV

MP3

FLAC

M4A

OGG

```

---

# 6. Import Workflow

Общий процесс:

```
Select File

↓

Detect Format

↓

Select Parser

↓

Extract Data

↓

Normalize

↓

Create Entities

↓

Save Project

```

---

# 7. Format Detection

Import Service определяет:

- расширение;
- MIME type;
- структуру файла;
- возможные ошибки.

---

# 8. Parser Plugin System

Каждый формат реализуется через Plugin.

Пример:

```
Document.Parser.EPUB

Document.Parser.PDF

Subtitle.Parser.SRT

Audio.Parser.WAV

```

---

# 9. Parser Contract

Parser Plugin обязан предоставлять:

```
detect()

validate()

parse()

extractMetadata()

```

---

# 10. Internal Document Model

После импорта создаётся:

```
Document

{

Document ID

Title

Author

Language

Sections

Fragments

Metadata

}

```

---

# 11. Text Normalization

После извлечения:

- удаляются лишние переносы;
- нормализуются пробелы;
- исправляется кодировка;
- сохраняется структура.

---

# 12. Structural Analysis

Система пытается определить:

- главы;
- разделы;
- абзацы;
- диалоги;
- списки.

---

# 13. Book Import

Для книг:

```
Book

↓

Chapters

↓

Sections

↓

Paragraphs

↓

Fragments

```

---

# 14. Subtitle Import

Субтитры преобразуются:

```
Subtitle Entry

{

Text

Start Time

End Time

Speaker

}

```

---

После импорта:

```
Subtitle

↓

Text Fragment

+

Timing Metadata

```

---

# 15. Audio Import

Аудио может использоваться для:

- клонирования голоса;
- анализа;
- сравнения;
- создания Voice Profile.

---

# 16. Voice Sample Import

Процесс:

```
Audio File

↓

Audio Analysis

↓

Voice Sample

↓

Voice Service

```

---

# 17. Character Detection

Import Service может обнаруживать:

- имена персонажей;
- диалоги;
- роли.

Пример:

```
"— Пойдём."

```

↓

```
Speaker Candidate

```

---

# 18. Language Detection

Определяется:

- язык текста;
- смешанные языки;
- необходимость обработки.

---

# 19. Import Preview

Перед окончательным импортом UI должен показывать:

- структуру;
- найденные главы;
- персонажей;
- количество фрагментов.

---

# 20. Import Configuration

Параметры:

```
Language

Encoding

Chapter Detection

Dialogue Detection

Keep Formatting

Create Characters

```

---

# 21. Incremental Import

Для больших файлов:

поддерживается:

- потоковый импорт;
- частичная обработка;
- отмена.

---

# 22. Duplicate Detection

Система должна определять:

- повторный импорт;
- одинаковые файлы;
- существующие документы.

---

# 23. Import History

Хранится:

```
Source File

Date

Parser

Version

Result

```

---

# 24. Error Handling

Ошибки:

```
Unsupported Format

Invalid File

Parser Failed

Encoding Error

Corrupted Data

```

---

# 25. Event Integration

Import Service публикует:

```
ImportStarted

ImportProgressChanged

DocumentImported

ImportCompleted

ImportFailed

```

---

# 26. Workflow Integration

Import может быть шагом:

```
Workflow:

Import Book

↓

Analyze

↓

Generate

```

---

# 27. Plugin Integration

Plugin могут добавлять:

- новые форматы;
- новые анализаторы;
- новые способы извлечения структуры.

---

# 28. Performance Requirements

Import Service должен поддерживать:

- большие книги;
- большие PDF;
- тысячи субтитров;
- потоковую обработку.

---

# 29. Security

Импортируемые файлы могут быть внешними.

Необходимо:

- проверка файлов;
- защита от вредоносных данных;
- безопасная обработка Parser Plugin.

---

# 30. Test Requirements

Проверяются:

- каждый формат;
- ошибки кодировки;
- большие документы;
- структура книги;
- субтитры;
- восстановление.

---

# 31. Compliance

Любая реализация Import Service обязана соответствовать настоящему документу.

---

# Appendix A. Example

Импорт EPUB:

```
book.epub

↓

EPUB Parser Plugin

↓

Document

↓

Chapter 1

↓

Fragment List

↓

Characters

↓

Workflow Ready

```

---

End of Document