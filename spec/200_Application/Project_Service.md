# Voxarium Software Architecture Specification

Document Path:
spec/200_Application/Project_Service.md

Document ID: APP-017

Title: Project Service

Version: 1.0.0

Status: Accepted

Classification: Normative

Depends On

- DOM-101 Project
- DOM-102 Asset
- DOM-103 Document
- APP-016 Workflow Engine
- APP-008 Job Orchestrator
- APP-015 Application Event Model
- Persistence Layer

Referenced By

- UI Layer
- Import Module
- Generation Module
- Export Module
- Voice Module
- Timeline Module

---

# 1. Purpose

Project Service является Application Layer компонентом, управляющим главным пользовательским объектом Voxarium — Project.

Project является центральной единицей работы пользователя.

Любая операция в Voxarium выполняется внутри контекста Project.

---

# 2. Main Concept

В Voxarium пользователь работает не с отдельными файлами, а с проектами.

Проект объединяет:

- исходные документы;
- импортированные данные;
- персонажей;
- голосовые профили;
- настройки генерации;
- промежуточные результаты;
- аудиофрагменты;
- временную шкалу;
- историю операций;
- экспортированные результаты.

---

# 3. Project Responsibilities

Project Service отвечает за:

- создание проекта;
- открытие проекта;
- сохранение проекта;
- закрытие проекта;
- управление состоянием;
- доступ модулей к данным проекта;
- запуск Workflow внутри проекта.

---

# 4. Project Boundary

Все действия должны иметь Project Context.

Пример:

```
Generate Speech

нельзя:

Global Text

↓

TTS


можно:

Project

↓

Document

↓

Fragment

↓

Voice Assignment

↓

Generation Job

```

---

# 5. Project Lifecycle

Состояния проекта:

```
Created

↓

Initialized

↓

Active

↓

Processing

↓

Completed

↓

Archived

↓

Deleted

```

---

# 6. Project Creation

При создании проекта создаются:

```
Project ID

Metadata

Storage Structure

Configuration

Event Stream

Initial Settings

```

---

# 7. Project Identifier

Каждый проект имеет уникальный ID.

Требования:

- глобальная уникальность;
- неизменность;
- использование во всех подсистемах.

Формат:

UUID v7.

---

# 8. Project Structure

Логическая структура:

```
Project

├── Metadata

├── Settings

├── Sources

│   ├── Documents

│   ├── Subtitles

│   └── Audio Samples


├── Content Model

│   ├── Chapters

│   ├── Sections

│   └── Fragments


├── Characters

├── Voice Profiles

├── Timeline

├── Generated Assets

├── Workflows

├── Jobs

├── Events

└── Exports

```

---

# 9. Project Storage

Project должен иметь переносимое хранилище.

Минимальная структура:

```
MyBook.vxp

├── project.json

├── assets/

├── audio/

├── models/

├── cache/

├── exports/

└── logs/

```

---

# 10. Project File Format

Основной формат:

```
.vxp

```

Файл является контейнером проекта.

Внутри:

- метаданные;
- ссылки;
- настройки;
- структура проекта.

Большие файлы хранятся отдельно.

---

# 11. Project Configuration

Настройки проекта:

```
Language

Default Voice

Audio Format

Sample Rate

Generation Settings

Processing Pipeline

Export Settings

```

---

# 12. Project Context

Каждый модуль получает Project Context.

Context предоставляет:

- доступ к данным;
- настройки;
- Storage;
- Event Publishing;
- Logging.

---

# 13. Project Isolation

Проекты полностью независимы.

Один проект не может:

- видеть файлы другого;
- использовать его настройки;
- изменять его состояние.

---

# 14. Multiple Projects

Приложение должно поддерживать:

- несколько открытых проектов;
- переключение между проектами;
- фоновые процессы;
- очередь разных проектов.

---

# 15. Project Processing

Процесс:

```
Open Project

↓

Select Workflow

↓

Create Jobs

↓

Execute

↓

Store Results

↓

Update Project

```

---

# 16. Project Events

Project Service публикует:

```
ProjectCreated

ProjectOpened

ProjectSaved

ProjectChanged

ProjectProcessingStarted

ProjectProcessingCompleted

ProjectClosed

```

---

# 17. Project Versioning

Проект должен поддерживать версионирование.

Хранятся:

- изменения структуры;
- настройки;
- результаты операций.

---

# 18. Undo / Redo

Изменения проекта должны поддерживать:

- историю действий;
- отмену;
- повтор.

---

# 19. Autosave

Project Service должен поддерживать:

- автоматическое сохранение;
- восстановление после сбоя;
- защиту от потери данных.

---

# 20. Locking

Для предотвращения конфликтов:

```
Project Lock

↓

Operation

↓

Save

↓

Release

```

---

# 21. Import Integration

Импорт всегда выполняется внутри Project.

Пример:

```
Create Project

↓

Import EPUB

↓

Store Source

↓

Create Document Entity

```

---

# 22. Generation Integration

Генерация всегда создаёт Assets проекта.

Пример:

```
Text Fragment

↓

Generation Job

↓

Audio Asset

↓

Timeline Entry

```

---

# 23. Export Integration

Экспорт использует данные проекта.

Источники:

- Timeline;
- Audio Assets;
- Metadata;
- Cover;
- Chapters.

---

# 24. Backup

Project Service должен поддерживать:

- создание копий;
- восстановление;
- проверку целостности.

---

# 25. Corruption Handling

При повреждении проекта:

- обнаружить ошибку;
- сохранить диагностику;
- предложить восстановление.

---

# 26. Performance Requirements

Project Service должен поддерживать:

- большие книги;
- тысячи аудиофрагментов;
- десятки тысяч объектов;
- быстрый поиск данных.

---

# 27. Security

Проект может содержать:

- пользовательский текст;
- голосовые записи;
- приватные материалы.

Необходимо:

- контроль доступа;
- защита файлов;
- безопасное хранение.

---

# 28. Test Requirements

Проверяются:

- создание проекта;
- открытие;
- сохранение;
- восстановление;
- импорт;
- параллельные операции;
- повреждение данных.

---

# 29. Compliance

Любая реализация Project Service обязана соответствовать настоящему документу.

---

# Appendix A. Example

Проект аудиокниги:

```
Project:
"The Great Novel"

Sources:

book.epub


Characters:

Narrator

Hero

Villain


Voice Profiles:

Narrator → Voice A

Hero → Voice B


Workflow:

Audiobook Production


Output:

book.m4b

```

---

End of Document