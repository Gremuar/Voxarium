# Voxarium Software Architecture Specification

Document Path:
spec/200_Application/Worker.md

Document ID: APP-011

Title: Worker

Version: 1.0.0

Status: Accepted

Classification: Normative

Depends On

- APP-008 Job Orchestrator
- APP-009 Scheduler
- APP-010 Queue
- DOM-114 Job
- Plugin Architecture

Referenced By

- Generation Engine
- Plugin System
- Resource Manager
- Execution Runtime
- Monitoring System

---

# 1. Purpose

Worker является исполнительным компонентом системы Voxarium.

Worker получает назначенный Job от Scheduler и выполняет его согласно контракту Job Handler.

Worker является единственным компонентом, который непосредственно запускает операции выполнения.

---

# 2. Responsibilities

Worker отвечает за:

- получение Assignment от Scheduler;
- подготовку окружения выполнения;
- загрузку необходимых ресурсов;
- выполнение Job;
- передачу прогресса;
- обработку ошибок;
- освобождение ресурсов;
- публикацию событий выполнения.

Worker не отвечает за:

- выбор следующей задачи;
- управление очередью;
- создание Job;
- изменение бизнес-состояния Project;
- принятие решений о приоритетах.

---

# 3. Architectural Position

```
Scheduler

↓

Worker Manager

↓

Worker

↓

Job Executor

↓

Plugin / Engine

↓

Hardware

```

---

# 4. Worker Model

Worker представляет собой изолированный исполнитель.

Он может существовать как:

- поток внутри приложения;
- отдельный процесс;
- отдельный сервис;
- удалённый узел.

Архитектура не должна зависеть от способа размещения.

---

# 5. Worker Lifecycle

Worker проходит следующие состояния:

Created

↓

Initializing

↓

Ready

↓

Assigned

↓

Loading Resources

↓

Running

↓

Completed / Failed

↓

Cleanup

↓

Ready

---

# 6. Worker Registration

Каждый Worker при запуске регистрируется в Worker Registry.

Регистрация содержит:

- Worker ID;
- Version;
- Capabilities;
- Hardware Information;
- Available Resources;
- Supported Plugins.

---

# 7. Capability Model

Worker сообщает поддерживаемые возможности.

Примеры:

```
TTS.XTTS.v2

TTS.StyleTTS2

Voice.Clone

Audio.Normalize

Audio.Merge

Subtitle.Parse

Document.Convert

```

Scheduler использует эти данные при выборе Worker.

---

# 8. Job Execution Contract

Каждый Job выполняется через Executor.

Worker не знает конкретную реализацию.

Общий интерфейс:

```
prepare()

execute()

reportProgress()

cancel()

cleanup()

```

---

# 9. Resource Management

Перед запуском Job Worker резервирует ресурсы.

Контролируются:

- CPU;
- RAM;
- GPU;
- VRAM;
- Disk;
- Network.

---

# 10. Model Loading

AI/TTS Job могут требовать загрузку моделей.

Worker должен поддерживать:

- загрузку модели;
- кэширование модели;
- выгрузку модели;
- проверку совместимости.

---

# 11. Model Cache

Worker может использовать локальный Model Cache.

Пример:

```
XTTS v2

↓

GPU Memory

↓

несколько последовательных генераций

```

Повторная загрузка модели должна быть минимизирована.

---

# 12. Progress Reporting

Worker обязан публиковать прогресс.

Минимально:

- Job ID;
- текущий этап;
- процент выполнения;
- сообщение состояния;
- скорость;
- оставшееся время (если возможно).

---

# 13. Cancellation

Worker обязан поддерживать безопасную отмену.

При отмене:

- новые операции не запускаются;
- текущая операция завершается безопасно;
- временные данные очищаются.

---

# 14. Pause and Resume

Worker может поддерживать:

- сохранение checkpoint;
- восстановление состояния;
- продолжение выполнения.

Поддержка определяется Job Type.

---

# 15. Error Handling

Ошибки разделяются на категории:

## Temporary

Например:

- нехватка памяти;
- временная ошибка GPU.

Возможен Retry.

---

## Permanent

Например:

- несовместимая модель;
- повреждённый файл.

Retry запрещён.

---

## User Error

Например:

- неправильные параметры.

Требуется исправление пользователя.

---

# 16. Cleanup

После любого завершения Worker обязан:

- освободить ресурсы;
- закрыть файлы;
- удалить временные данные;
- вернуть состояние Ready.

---

# 17. Isolation

Один ошибочный Job не должен повреждать Worker.

Рекомендуется:

- отдельный процесс;
- sandbox;
- ограничение памяти;
- контроль времени выполнения.

---

# 18. Plugin Execution

Worker выполняет Plugin только через Plugin Contract.

Worker не должен знать внутренний код Plugin.

---

# 19. Multi-GPU Support

Worker должен поддерживать несколько устройств.

Например:

```
Worker

GPU 0:
XTTS

GPU 1:
Voice Clone

CPU:
Audio Processing

```

---

# 20. Local and Remote Worker

Архитектура должна поддерживать:

## Local Worker

Работает внутри пользовательского приложения.

## Remote Worker

Работает на другом компьютере.

---

# 21. Security

Worker должен контролировать:

- доступ Plugin к файлам;
- доступ к ресурсам;
- выполнение внешнего кода.

---

# 22. Logging

Worker журналирует:

- запуск;
- завершение;
- используемые ресурсы;
- ошибки;
- время выполнения.

---

# 23. Metrics

Минимальные метрики:

- Jobs Completed;
- Jobs Failed;
- Average Execution Time;
- CPU Usage;
- GPU Usage;
- VRAM Usage;
- Memory Usage.

---

# 24. Performance Requirements

Worker должен:

- минимизировать простой оборудования;
- эффективно использовать GPU;
- поддерживать параллельные задачи;
- быстро переключаться между Job.

---

# 25. Test Requirements

Должны существовать тесты:

- регистрация Worker;
- выполнение Job;
- отмена;
- ошибка Plugin;
- восстановление;
- управление ресурсами;
- многопоточность.

---

# 26. Compliance

Любая реализация Worker обязана соответствовать настоящему документу.

---

# Appendix A. Example Execution

Assignment:

```
Job:
Generate Fragment

Required Capability:

TTS.XTTS.v2

Resources:

GPU
VRAM 6GB

```

Worker:

```
1. Проверить ресурсы

2. Загрузить XTTS модель

3. Получить текст

4. Выполнить генерацию

5. Сохранить результат

6. Отправить JobCompleted

7. Освободить ресурсы

```

---

End of Document