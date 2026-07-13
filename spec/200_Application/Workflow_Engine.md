# Voxarium Software Architecture Specification

Document Path:
spec/200_Application/Workflow_Engine.md

Document ID: APP-016

Title: Workflow Engine

Version: 1.0.0

Status: Accepted

Classification: Normative

Depends On

- DOM-113 Workflow
- DOM-114 Job
- APP-008 Job Orchestrator
- APP-015 Application Event Model
- APP-004 Command Bus

Referenced By

- Project Module
- Production Module
- Audio Generation Module
- Export Module
- Plugin System

---

# 1. Purpose

Workflow Engine является подсистемой управления сценариями обработки проекта Voxarium.

Workflow Engine определяет:

- последовательность операций;
- зависимости между этапами;
- условия выполнения;
- автоматический запуск Job;
- обработку результатов.

Workflow Engine является механизмом автоматизации пользовательских сценариев.

---

# 2. Main Concept

Главная задача Voxarium:

преобразовать пользовательский проект в готовый аудиопродукт.

Этот процесс состоит из множества этапов:

```
Источник текста

↓

Импорт

↓

Анализ

↓

Подготовка

↓

Назначение голосов

↓

Генерация

↓

Обработка аудио

↓

Экспорт

```

Workflow Engine управляет этим процессом.

---

# 3. Responsibilities

Workflow Engine отвечает за:

- создание Workflow;
- выполнение Workflow;
- управление состояниями;
- запуск Job;
- обработку событий;
- ветвление;
- повторение операций;
- сохранение прогресса.

Workflow Engine не отвечает за:

- выполнение TTS;
- обработку аудио;
- работу GPU;
- хранение файлов;
- выбор моделей.

---

# 4. Architectural Position

```
User Action

↓

Command

↓

Workflow Engine

↓

Job Orchestrator

↓

Scheduler

↓

Worker

↓

Plugin

```

---

# 5. Workflow Definition

Workflow является описанием процесса.

Он содержит:

```
Workflow ID

Name

Version

Steps

Dependencies

Conditions

Parameters

Error Policy

```

---

# 6. Workflow Instance

Каждый запущенный Workflow создаёт Instance.

Instance содержит:

```
Workflow Instance ID

Project ID

Current State

Started At

Progress

Created Jobs

Variables

```

---

# 7. Workflow Lifecycle

Состояния:

```
Created

↓

Ready

↓

Running

↓

Paused

↓

Completed

↓

Failed

↓

Cancelled

```

---

# 8. Workflow Step

Каждый Workflow состоит из Step.

Step является логической операцией.

Примеры:

```
Import Document

Parse Text

Detect Characters

Assign Voices

Generate Audio

Merge Audio

Export

```

---

# 9. Step Types

Минимальные типы:

---

## Command Step

Выполнение команды.

Пример:

```
Create Project Metadata

```

---

## Job Step

Создание Job.

Пример:

```
Generate Speech

```

---

## Event Wait Step

Ожидание события.

Пример:

```
Wait GenerationCompleted

```

---

## Condition Step

Условное выполнение.

Пример:

```
If contains characters:

    Detect Roles

else:

    Continue

```

---

## Parallel Step

Параллельное выполнение.

Пример:

```
Generate Chapter 1

Generate Chapter 2

Generate Chapter 3

```

---

## Loop Step

Повторение.

Пример:

```
For every chapter:

Generate Audio

```

---

# 10. Workflow Graph

Workflow представляет собой DAG.

Пример:

```
Import

 |

Parse

 |

 ├─────────────┐

 ▼             ▼

Roles       Chapters

 |

 ▼

Voices

 |

 ▼

Generation

 |

 ▼

Merge

 |

 ▼

Export

```

---

# 11. Workflow Execution

Основной цикл:

```
1. Load Workflow

2. Validate

3. Create Instance

4. Execute Ready Steps

5. Create Jobs

6. Wait Events

7. Continue

8. Complete

```

---

# 12. Workflow Variables

Workflow поддерживает переменные.

Примеры:

```
language = ru

voice = narrator

chapter_count = 25

output_format = mp3

```

---

# 13. Parameter Binding

Параметры могут поступать из:

- Project;
- User Settings;
- Plugin;
- Previous Step Result.

---

# 14. Parallel Execution

Workflow должен эффективно использовать параллелизм.

Пример:

Книга:

```
100 глав

```

Workflow:

```
Chapter 1 Job

Chapter 2 Job

...

Chapter 100 Job

```

Scheduler самостоятельно распределяет выполнение.

---

# 15. Error Handling

Каждый Step имеет Error Policy.

Поддерживаются:

---

## Stop

Остановить Workflow.

---

## Retry

Повторить Step.

---

## Skip

Пропустить.

---

## Compensation

Выполнить обратную операцию.

---

# 16. Resume

Workflow должен поддерживать продолжение после:

- закрытия приложения;
- перезагрузки компьютера;
- ошибки Worker.

---

# 17. Checkpoint

После каждого Step сохраняется состояние:

```
Step Completed

Output Stored

Next Step Ready

```

---

# 18. User Control

Пользователь может:

- запустить Workflow;
- поставить на паузу;
- отменить;
- изменить параметры;
- перезапустить этап.

---

# 19. Dynamic Workflow

Некоторые Workflow могут изменяться во время выполнения.

Пример:

Добавление новой главы в книгу.

Workflow должен уметь:

- добавить новые Job;
- перестроить граф;
- продолжить выполнение.

---

# 20. Plugin Integration

Plugin могут предоставлять:

- новые Step Types;
- новые Workflow Templates;
- новые Actions.

---

# 21. Workflow Templates

Система должна поддерживать шаблоны.

Примеры:

---

## Audiobook Full Production

```
Import

↓

Analyze

↓

Assign Voices

↓

Generate

↓

Master

↓

Export

```

---

## Subtitle Voiceover

```
Import SRT

↓

Parse Timings

↓

Generate Voices

↓

Mix

↓

Export Video Audio Track

```

---

## Voice Clone Workflow

```
Import Voice Sample

↓

Analyze Voice

↓

Create Profile

↓

Generate

```

---

# 22. Workflow Storage

Workflow хранится отдельно от реализации.

Поддерживаются:

- JSON;
- YAML;
- Database;
- Plugin Templates.

---

# 23. Event Integration

Workflow реагирует на:

```
JobCompleted

JobFailed

DocumentImported

VoiceCreated

PluginReady

```

---

# 24. Logging

Workflow журналирует:

- запуск;
- шаги;
- переходы;
- ошибки;
- результаты.

---

# 25. Performance Requirements

Workflow Engine должен поддерживать:

- большие проекты;
- тысячи шагов;
- параллельное выполнение;
- восстановление состояния.

---

# 26. Test Requirements

Проверяются:

- создание Workflow;
- граф зависимостей;
- параллельность;
- ошибки;
- восстановление;
- отмена;
- динамические изменения.

---

# 27. Compliance

Любая реализация Workflow Engine обязана соответствовать настоящему документу.

---

# Appendix A. Main Voxarium Workflow

```
Create Project

↓

Import Source

↓

Normalize Text

↓

Analyze Structure

↓

Detect Characters

↓

Assign Voices

↓

Generate Speech

↓

Process Audio

↓

Build Timeline

↓

Export Result

```

---

End of Document