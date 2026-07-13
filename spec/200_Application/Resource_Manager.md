# Voxarium Software Architecture Specification

Document Path:
spec/200_Application/Resource_Manager.md

Document ID: APP-012

Title: Resource Manager

Version: 1.0.0

Status: Accepted

Classification: Normative

Depends On

- APP-009 Scheduler
- APP-011 Worker
- Plugin Architecture
- Hardware Abstraction Layer

Referenced By

- Scheduler
- Worker
- AI Engine
- TTS Engine
- Audio Processing Module
- Plugin System

---

# 1. Purpose

Resource Manager является подсистемой управления вычислительными ресурсами Voxarium.

Он отвечает за учёт, резервирование, освобождение и мониторинг ресурсов, необходимых для выполнения Job.

Resource Manager обеспечивает эффективное использование локального оборудования пользователя и будущих распределённых Worker.

---

# 2. Responsibilities

Resource Manager отвечает за:

- обнаружение доступного оборудования;
- ведение состояния ресурсов;
- резервирование ресурсов;
- освобождение ресурсов;
- контроль лимитов;
- предоставление информации Scheduler;
- контроль конфликтов использования.

Resource Manager не отвечает за:

- запуск Job;
- выбор Job;
- выполнение AI-моделей;
- управление Plugin.

---

# 3. Architectural Position

```
Hardware

↓

Hardware Abstraction Layer

↓

Resource Manager

↓

Scheduler

↓

Worker

↓

Executor

```

---

# 4. Resource Types

Минимально поддерживаются следующие ресурсы.

---

## CPU

Параметры:

- количество ядер;
- количество потоков;
- текущая загрузка;
- доступное время CPU.

---

## RAM

Параметры:

- общий объём;
- свободная память;
- зарезервированная память;
- лимиты.

---

## GPU

Параметры:

- количество устройств;
- модель GPU;
- вычислительная способность;
- текущая загрузка.

---

## VRAM

Параметры:

- общий объём;
- свободная память;
- занятая память;
- используемые модели.

---

## Storage

Параметры:

- доступное место;
- скорость;
- временное пространство;
- рабочие директории.

---

## Network

Параметры:

- скорость;
- задержка;
- доступность.

---

# 5. Resource Model

Каждый ресурс представлен объектом:

```
Resource

ID

Type

Capacity

Available

Reserved

Owner

State

Metadata

```

---

# 6. Resource Discovery

При запуске приложения Resource Manager выполняет обнаружение:

- CPU;
- RAM;
- GPU;
- VRAM;
- дисков;
- доступных ускорителей.

Информация обновляется динамически.

---

# 7. Resource States

Минимальные состояния:

Available

Reserved

Allocated

Busy

Overloaded

Unavailable

Error

---

# 8. Reservation Model

Перед запуском Job Worker резервирует ресурсы.

Пример:

```
GenerateSpeechJob

Need:

GPU:
RTX 4070 Ti

VRAM:
5 GB

RAM:
8 GB

```

Resource Manager:

```
Reserve:

GPU VRAM 5GB

RAM 8GB

```

После завершения:

```
Release

```

---

# 9. Resource Locking

Ресурсы должны поддерживать блокировку.

Цель:

- предотвращение конфликтов;
- защита от переполнения VRAM;
- исключение одновременной загрузки несовместимых моделей.

---

# 10. GPU Management

Resource Manager должен поддерживать:

- несколько GPU;
- выбор GPU;
- мониторинг загрузки;
- распределение моделей.

Пример:

```
GPU 0

XTTS Model

6GB VRAM


GPU 1

Whisper Model

4GB VRAM

```

---

# 11. VRAM Awareness

Для AI-моделей VRAM является критическим ресурсом.

Перед запуском Job необходимо проверить:

- размер модели;
- текущие загруженные модели;
- свободную VRAM;
- возможность выгрузки.

---

# 12. Model Residency

Resource Manager должен поддерживать понятие:

Model Residency

Это означает:

модель уже загружена и может быть использована повторно.

Пример:

```
XTTS v2

Loaded

GPU 0

Reuse allowed

```

---

# 13. Resource Pressure

Система должна определять состояние нехватки ресурсов.

Примеры:

Low Memory

Low VRAM

Disk Almost Full

GPU Overload

---

# 14. Resource Policies

Поддерживаются политики:

## Performance First

Максимальная скорость.

---

## Memory Saving

Минимальное потребление памяти.

---

## Energy Saving

Минимальная нагрузка.

---

## Balanced

Баланс производительности и ресурсов.

---

# 15. Scheduler Integration

Scheduler получает от Resource Manager:

- доступные ресурсы;
- возможные назначения;
- ограничения;
- рекомендации.

Scheduler не изменяет ресурсы напрямую.

---

# 16. Worker Integration

Worker сообщает:

- начало использования ресурса;
- изменение нагрузки;
- завершение использования.

---

# 17. Plugin Integration

Plugin должны описывать требования:

Пример:

```
Capability:

TTS.XTTS.v2


Requirements:

GPU=true

VRAM>=6GB

CUDA=true

RAM>=8GB

```

---

# 18. Dynamic Resource Usage

Некоторые Job имеют изменяемые требования.

Например:

Начало:

```
VRAM 4GB

```

Во время генерации:

```
VRAM 7GB

```

Resource Manager должен поддерживать изменение резерва.

---

# 19. Monitoring

Resource Manager публикует события:

ResourceDetected

ResourceReserved

ResourceReleased

ResourcePressureDetected

ResourceUnavailable

---

# 20. Recovery

После сбоя приложения:

- снять старые блокировки;
- проверить активные процессы;
- восстановить состояние ресурсов.

---

# 21. Security

Resource Manager должен предотвращать:

- превышение лимитов;
- неконтролируемое потребление памяти;
- повреждение системы Plugin.

---

# 22. Performance Requirements

Resource Manager должен:

- обновлять состояние без заметной нагрузки;
- быстро отвечать Scheduler;
- поддерживать большое количество Worker;
- работать в реальном времени.

---

# 23. Test Requirements

Тестируются:

- обнаружение ресурсов;
- резервирование;
- освобождение;
- конфликт ресурсов;
- несколько GPU;
- нехватка VRAM;
- восстановление после сбоя.

---

# 24. Compliance

Любая реализация Resource Manager обязана соответствовать настоящему документу.

---

# Appendix A. Example

Система:

```
CPU:
16 cores


RAM:
64GB


GPU:
RTX 4070 Ti

VRAM:
12GB

```

Running:

```
XTTS Generation

VRAM:
6GB


Whisper Analysis

VRAM:
3GB


Available:

VRAM:
3GB

```

Scheduler:

```
Reject:

Large Voice Clone Job

Need:
8GB VRAM

```

---

End of Document