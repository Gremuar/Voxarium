# Voxarium Software Architecture Specification

Document Path:
spec/200_Application/Scheduler.md

Document ID: APP-009

Title: Scheduler

Version: 1.0.0

Status: Accepted

Classification: Normative

Depends On

- APP-008 Job Orchestrator
- DOM-114 Job
- APP-006 Event Bus

Referenced By

- Queue.md
- Worker.md
- Resource_Manager.md
- Generation_Module.md
- Plugin_System.md

---

# 1. Purpose

Scheduler является компонентом Application Infrastructure, отвечающим за принятие решения о том, какой Job должен быть выполнен следующим.

Scheduler преобразует набор ожидающих Job в конкретные назначения для Worker.

Scheduler не выполняет Job.

---

# 2. Responsibilities

Scheduler отвечает за:

- анализ доступных Job;
- проверку зависимостей;
- выбор оптимального Job;
- назначение Job Worker;
- контроль ограничений ресурсов;
- соблюдение приоритетов;
- управление очередностью выполнения.

Scheduler не отвечает за:

- реализацию Job;
- генерацию речи;
- обработку аудио;
- загрузку моделей;
- работу Plugin.

---

# 3. Architectural Position

```
Job Orchestrator

↓

Queue

↓

Scheduler

↓

Worker Pool

↓

Plugin / Engine

```

---

# 4. Scheduling Principles

Scheduler должен обеспечивать:

- предсказуемость;
- справедливость;
- максимальное использование ресурсов;
- возможность отмены;
- возможность восстановления;
- независимость от конкретного Job Type.

---

# 5. Scheduler Input

Scheduler получает:

- список ожидающих Job;
- состояние Worker;
- доступные ресурсы;
- приоритеты;
- зависимости;
- ограничения пользователя.

---

# 6. Scheduler Output

Результатом работы Scheduler является Assignment.

Assignment содержит:

- Job ID;
- Worker ID;
- необходимые ресурсы;
- параметры запуска;
- время назначения.

---

# 7. Job Selection Algorithm

Минимальная версия Scheduler должна учитывать:

1. Готовность Job.
2. Приоритет Job.
3. Время ожидания.
4. Доступность ресурсов.
5. Возможность выполнения на Worker.

---

# 8. Priority Handling

Поддерживаются уровни:

Critical

High

Normal

Low

Background

При одинаковом приоритете используется FIFO.

---

# 9. Fairness Policy

Scheduler не должен допускать:

- вечного ожидания низкоприоритетных задач;
- блокировки проекта одной большой задачей;
- монополизации GPU одним Job.

---

# 10. Resource Awareness

Scheduler обязан учитывать:

CPU

GPU

VRAM

RAM

Disk

Network

Plugin Capability

---

# 11. GPU Scheduling

Для TTS и AI Job Scheduler должен учитывать:

- доступную VRAM;
- загруженность GPU;
- используемые модели;
- необходимость загрузки модели.

---

# 12. Model Affinity

Некоторые Job могут иметь предпочтительный Worker.

Например:

- модель уже загружена;
- используется конкретный GPU;
- присутствует необходимый Plugin.

Scheduler должен учитывать такие предпочтения.

---

# 13. Parallel Execution

Scheduler должен поддерживать параллельное выполнение независимых Job.

Пример:

```
Generate Chapter 1
        │
        ├── Fragment 1
        ├── Fragment 2
        ├── Fragment 3
        └── Fragment 4
```

Все Fragment могут выполняться одновременно при наличии ресурсов.

---

# 14. Dependency Check

Job может быть назначен только если:

- все зависимости завершены;
- отсутствуют блокирующие ошибки;
- необходимые данные доступны.

---

# 15. Worker Selection

Scheduler выбирает Worker на основании:

- Capability;
- загрузки;
- доступных ресурсов;
- предпочтения модели;
- состояния Worker.

---

# 16. Worker States

Минимально:

Offline

Starting

Idle

Busy

Paused

Error

Stopping

---

# 17. Scheduling Cycle

Стандартный цикл:

1. Получить состояние системы.
2. Найти готовые Job.
3. Рассчитать кандидатов.
4. Выбрать лучший Job.
5. Назначить Worker.
6. Обновить состояние.
7. Опубликовать событие.

---

# 18. Failure Handling

Если Worker недоступен:

Scheduler обязан:

- снять назначение;
- вернуть Job в Queue;
- увеличить счётчик попыток;
- выбрать другой Worker.

---

# 19. Cancellation Handling

Если Job отменён:

Scheduler обязан:

- удалить его из очереди;
- отменить Assignment;
- уведомить Worker.

---

# 20. Recovery

После перезапуска Scheduler:

- восстанавливает очередь;
- проверяет активные Assignment;
- обнаруживает потерянные Worker;
- восстанавливает выполнение.

---

# 21. Plugin Integration

Plugin могут предоставлять:

- новые Capability;
- новые Resource Requirements;
- новые правила совместимости.

Scheduler не должен знать внутреннюю реализацию Plugin.

---

# 22. Performance Requirements

Scheduler должен поддерживать:

- десятки тысяч ожидающих Job;
- быстрый поиск готовых задач;
- минимальную задержку назначения;
- работу в реальном времени.

---

# 23. Thread Safety

Scheduler должен поддерживать параллельные операции:

- добавление Job;
- завершение Job;
- изменение ресурсов;
- регистрацию Worker.

---

# 24. Test Requirements

Должны существовать тесты:

- выбора Job;
- приоритетов;
- ресурсов;
- параллелизма;
- восстановления;
- отказа Worker;
- справедливости планирования.

---

# 25. Compliance

Любая реализация Scheduler обязана соответствовать настоящему документу.

---

# Appendix A. Example Scheduling

Available:

GPU RTX 4070 Ti

VRAM:
8 GB

Workers:

Worker A:
- XTTS Plugin
- 6 GB free VRAM

Worker B:
- CPU only

Queue:

Job 1:
Generate Voice Fragment
Requirement:
XTTS + GPU

Job 2:
Normalize Audio
Requirement:
CPU

Result:

Job 1 → Worker A

Job 2 → Worker B

---

End of Document