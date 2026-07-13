# Voxarium Software Architecture Specification

Document Path:
spec/100_Domain/GenerationSession.md

Document ID: DOM-016

Title: GenerationSession

Version: 1.0.0

Status: Accepted

Classification: Normative

Depends On

- SAS-000 Project Philosophy
- SAS-001 Glossary
- SAS-002 Domain Ontology
- SAS-003 Architecture Principles
- SpeechSegment
- GenerationPreset
- VoiceProfile

Referenced By

- Generation_Service
- Workflow
- Job
- AudioTrack

---

# 1. Purpose

GenerationSession представляет собой единичную попытку генерации речи.

Каждый запуск синтеза создает новую GenerationSession.

GenerationSession описывает процесс выполнения генерации независимо от ее результата.

GenerationSession не является Job.

GenerationSession не является AudioTrack.

---

# 2. Responsibilities

GenerationSession SHALL отвечать за:

- идентификацию запуска генерации;
- ссылку на генерируемый SpeechSegment;
- хранение конфигурации генерации;
- хранение состояния выполнения;
- хранение итогового результата;
- обеспечение воспроизводимости процесса.

---

# 3. Non-Responsibilities

GenerationSession SHALL NOT:

- выполнять синтез речи;
- хранить аудиофайлы;
- выполнять обработку аудио;
- управлять очередью;
- управлять Worker;
- содержать параметры конкретного AI Engine.

---

# 4. Ownership

GenerationSession принадлежит Project.

```
Project
    │
    └── GenerationSessions
            │
            └── GenerationSession
```

---

# 5. Identity

Каждая GenerationSession имеет неизменяемый Identifier.

Identifier SHALL:

- быть уникальным внутри Project;
- сохраняться после сериализации;
- никогда не изменяться.

---

# 6. Relationships

GenerationSession обязана ссылаться на:

- SpeechSegment.

GenerationSession MAY ссылаться на:

- VoiceProfile;
- GenerationPreset;
- AudioTrack.

После успешной генерации создается новый AudioTrack.

---

# 7. Metadata

| Property | Required | Mutable |
|----------|----------|---------|
| Identifier | Yes | No |
| SpeechSegmentId | Yes | No |
| Status | Yes | Yes |
| StartedUtc | No | No |
| FinishedUtc | No | Yes |
| Revision | Yes | Yes |

---

# 8. Status

Допустимые состояния.

- Pending
- Queued
- Running
- Completed
- Failed
- Cancelled
- Expired

В каждый момент времени GenerationSession SHALL находиться только в одном состоянии.

---

# 9. Lifecycle

```
Pending

↓

Queued

↓

Running

↓

Completed
```

Допускаются переходы.

```
Running → Failed

Running → Cancelled
```

---

# 10. Effective Configuration

Перед запуском SHALL вычисляться Effective Generation Configuration.

Полученная конфигурация сохраняется как неизменяемый Snapshot.

После начала генерации изменение конфигурации запрещено.

---

# 11. Retry Policy

Повторная генерация SHALL создавать новую GenerationSession.

Повторное использование существующей Session запрещено.

История запусков сохраняется.

---

# 12. Invariants

GenerationSession SHALL удовлетворять следующим требованиям.

- Identifier существует.
- SpeechSegment существует.
- Status определен.
- Revision ≥ 1.

---

# 13. Creation Rules

При создании SHALL:

- создать Identifier;
- установить Revision = 1;
- установить состояние Pending;
- вычислить Effective Configuration;
- опубликовать GenerationSessionCreated.

---

# 14. Completion Rules

После успешного завершения SHALL:

- создать AudioTrack;
- связать его с Session;
- изменить состояние на Completed;
- опубликовать GenerationCompleted.

---

# 15. Failure Rules

При ошибке SHALL:

- сохранить диагностическую информацию;
- изменить состояние на Failed;
- опубликовать GenerationFailed.

Ошибки не удаляются автоматически.

---

# 16. Persistence

GenerationSession сериализуется как часть Project.

GenerationSession SHALL NOT знать:

- Worker;
- Thread;
- Queue;
- Runtime;
- GPU;
- файловую систему.

---

# 17. Concurrency

Допускается конкурентное чтение.

Одновременное изменение одной GenerationSession запрещено.

---

# 18. Domain Events

GenerationSession публикует:

- GenerationSessionCreated
- GenerationStarted
- GenerationCompleted
- GenerationFailed
- GenerationCancelled

---

# 19. Commands

Поддерживаются команды.

- CreateGenerationSession
- StartGeneration
- CancelGeneration
- RetryGeneration

---

# 20. AI Implementation Requirements

GenerationSession SHALL описывать исключительно бизнес-факт выполнения генерации.

Запрещается хранить:

- параметры CUDA;
- параметры ONNX Runtime;
- параметры PyTorch;
- параметры XTTS;
- параметры Piper;
- параметры Kokoro;
- ссылки на внутренние объекты AI Runtime.

Все подобные сведения принадлежат Infrastructure Layer.

---

# 21. Test Requirements

Минимальный набор тестов.

- создание Session;
- успешная генерация;
- ошибка генерации;
- повторная генерация;
- сериализация;
- десериализация;
- проверка инвариантов;
- публикация событий.

---

# 22. Compliance Checklist

Реализация соответствует настоящей спецификации только если:

- Session принадлежит Project;
- представляет единственную попытку генерации;
- не содержит AI Runtime;
- не содержит аудиофайлов;
- реализованы все события;
- реализованы все команды;
- соблюдены все инварианты;
- сериализация полностью воспроизводима.

---

End of Document