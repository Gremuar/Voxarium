# Voxarium Software Architecture Specification

Document Path:
spec/200_Application/Execution_Runtime.md

Document ID: APP-013

Title: Execution Runtime

Version: 1.0.0

Status: Accepted

Classification: Normative

Depends On

- APP-011 Worker
- APP-012 Resource Manager
- Plugin Architecture
- Domain Job Model

Referenced By

- Plugin Runtime
- TTS Engine Module
- Audio Processing Module
- AI Module
- Worker Implementation
- Sandbox System

---

# 1. Purpose

Execution Runtime является подсистемой, обеспечивающей безопасное выполнение Job внутри Voxarium.

Runtime предоставляет единый механизм запуска, контроля и завершения исполнительных модулей независимо от их внутренней реализации.

Execution Runtime является промежуточным слоем между Worker и конкретными технологиями выполнения.

---

# 2. Responsibilities

Execution Runtime отвечает за:

- создание среды выполнения;
- запуск Executor;
- передачу параметров;
- контроль состояния выполнения;
- управление временем жизни процесса;
- обработку завершения;
- сбор диагностической информации.

Execution Runtime не отвечает за:

- выбор Job;
- выбор Worker;
- бизнес-логику;
- алгоритмы генерации речи;
- обработку аудио.

---

# 3. Architectural Position

```
Scheduler

↓

Worker

↓

Execution Runtime

↓

Executor

↓

Plugin

↓

External Engine

```

---

# 4. Execution Isolation

Каждая длительная операция должна выполняться изолированно.

Поддерживаемые уровни изоляции:

## Level 0

Внутренний поток приложения.

Используется для:

- быстрых операций;
- безопасных Core задач.

---

## Level 1

Отдельный процесс.

Используется для:

- AI моделей;
- TTS;
- обработки больших файлов.

---

## Level 2

Sandbox Process.

Используется для:

- сторонних Plugin;
- экспериментальных модулей;
- неподтверждённого кода.

---

# 5. Execution Context

Каждый запуск получает Execution Context.

Содержит:

```
Execution ID

Job ID

Project ID

Plugin ID

Worker ID

Resource Allocation

Input References

Output References

Environment

Cancellation Token

```

---

# 6. Executor Contract

Каждый Executor обязан реализовывать интерфейс:

```
initialize()

validate()

execute()

pause()

resume()

cancel()

cleanup()

```

---

# 7. Initialization Stage

Перед выполнением Runtime выполняет:

- проверку Plugin;
- проверку ресурсов;
- подготовку окружения;
- создание временных директорий;
- подготовку входных данных.

---

# 8. Validation Stage

До запуска выполняется проверка:

- совместимость версий;
- наличие файлов;
- доступность моделей;
- корректность параметров.

---

# 9. Execution Stage

Во время выполнения Runtime обеспечивает:

- передачу команд управления;
- сбор прогресса;
- мониторинг ресурсов;
- обработку событий.

---

# 10. Progress Communication

Executor обязан отправлять:

```
ProgressChanged

StageChanged

Message

EstimatedTime

CurrentOperation

```

Runtime преобразует их в системные события.

---

# 11. Cancellation Model

Отмена выполняется поэтапно:

1. Отправить Cancellation Request.
2. Дать Executor время завершиться.
3. Выполнить принудительное завершение при необходимости.
4. Выполнить Cleanup.

---

# 12. Timeout Control

Каждый Executor может иметь:

- общий Timeout;
- Idle Timeout;
- Resource Timeout.

После превышения:

Runtime инициирует остановку.

---

# 13. Process Management

Для внешних процессов Runtime контролирует:

- PID;
- состояние процесса;
- потребление памяти;
- использование GPU;
- вывод логов.

---

# 14. Crash Handling

При аварийном завершении:

Runtime сохраняет:

- код ошибки;
- последние сообщения;
- состояние ресурсов;
- диагностический снимок.

После этого Job переводится в Failed.

---

# 15. Temporary Files

Runtime управляет временными данными.

Правила:

- каждый Job имеет собственную временную директорию;
- очистка выполняется автоматически;
- незавершённые данные сохраняются только при необходимости восстановления.

---

# 16. Environment Management

Runtime может создавать окружение:

- переменные окружения;
- пути моделей;
- CUDA параметры;
- настройки Plugin;
- локальные конфигурации.

---

# 17. GPU Context

Для GPU Job Runtime обеспечивает:

- выбор устройства;
- передачу GPU Context;
- контроль использования памяти;
- освобождение после завершения.

---

# 18. Plugin Execution

Plugin никогда не запускается напрямую.

Последовательность:

```
Worker

↓

Execution Runtime

↓

Plugin Adapter

↓

Plugin

```

---

# 19. Security Model

Runtime должен ограничивать:

- доступ к файловой системе;
- доступ к сети;
- доступ к системным ресурсам;
- выполнение опасных операций.

---

# 20. Remote Execution

Runtime должен поддерживать удалённое выполнение.

Архитектурно:

```
Local Worker

↓

Remote Execution Adapter

↓

Remote Worker

↓

Runtime

```

---

# 21. Logging

Runtime собирает:

- stdout;
- stderr;
- execution events;
- ошибки;
- время выполнения.

---

# 22. Metrics

Минимально:

- Execution Time;
- CPU Usage;
- GPU Usage;
- Memory Peak;
- VRAM Peak;
- Failure Rate.

---

# 23. Recovery

После сбоя:

- обнаружить незавершённые процессы;
- освободить ресурсы;
- сохранить состояние;
- передать информацию Job Orchestrator.

---

# 24. Performance Requirements

Runtime должен обеспечивать:

- минимальную задержку запуска;
- эффективное использование процессов;
- отсутствие утечек ресурсов;
- быстрый cleanup.

---

# 25. Test Requirements

Проверяются:

- запуск Executor;
- отмена;
- таймаут;
- падение процесса;
- очистка ресурсов;
- восстановление;
- изоляция Plugin.

---

# 26. Compliance

Любая реализация Execution Runtime обязана соответствовать настоящему документу.

---

# Appendix A. Example

Job:

```
Generate Speech Fragment

```

Execution:

```
Worker

↓

Runtime creates context

↓

Load XTTS Plugin

↓

Allocate GPU

↓

Start generation

↓

Receive progress

↓

Save WAV

↓

Release GPU

↓

Publish JobCompleted

```

---

End of Document