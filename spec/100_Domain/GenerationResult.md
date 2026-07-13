# Voxarium Software Architecture Specification

Document Path:
spec/100_Domain/GenerationResult.md

Document ID: DOM-018

Title: GenerationResult

Version: 1.0.0

Status: Accepted

Classification: Normative

Depends On

- SAS-000 Project Philosophy
- SAS-001 Glossary
- SAS-002 Domain Ontology
- SAS-003 Architecture Principles
- GenerationSession
- AudioTrack

Referenced By

- Generation_Service
- Export_Service
- Workflow
- Job

---

# 1. Purpose

GenerationResult представляет собой неизменяемый результат завершения GenerationSession.

GenerationResult фиксирует факт выполнения генерации.

GenerationResult никогда не изменяется после создания.

GenerationResult не является процессом.

GenerationResult не является AudioTrack.

---

# 2. Responsibilities

GenerationResult SHALL отвечать за:

- фиксацию результата выполнения;
- хранение итогового статуса;
- хранение диагностической информации;
- хранение ссылок на созданные объекты;
- обеспечение воспроизводимости истории.

---

# 3. Non-Responsibilities

GenerationResult SHALL NOT:

- выполнять генерацию;
- выполнять повторную генерацию;
- хранить аудиофайлы;
- обращаться к Runtime;
- выполнять обработку ошибок.

---

# 4. Ownership

GenerationResult принадлежит GenerationSession.

```
GenerationSession
        │
        └── GenerationResult
```

GenerationResult SHALL NOT существовать самостоятельно.

---

# 5. Identity

Каждый GenerationResult имеет неизменяемый Identifier.

Identifier SHALL:

- быть уникальным;
- никогда не изменяться;
- сохраняться при сериализации.

---

# 6. Metadata

| Property | Required | Mutable |
|----------|----------|---------|
| Identifier | Yes | No |
| SessionId | Yes | No |
| Status | Yes | No |
| StartedUtc | Yes | No |
| FinishedUtc | Yes | No |
| Duration | Yes | No |

После создания все свойства становятся неизменяемыми.

---

# 7. Result Status

Допустимые состояния.

- Success
- Failed
- Cancelled
- Skipped
- PartialSuccess

Status определяется один раз.

Изменение запрещено.

---

# 8. Diagnostics

GenerationResult MAY содержать:

- список ошибок;
- список предупреждений;
- список информационных сообщений.

Диагностические сообщения являются частью истории выполнения.

---

# 9. Produced Objects

GenerationResult MAY ссылаться на:

- AudioTrack;
- Asset;
- Report.

GenerationResult не владеет этими объектами.

---

# 10. Metrics

GenerationResult MAY содержать:

- длительность выполнения;
- количество обработанных сегментов;
- количество успешных операций;
- количество ошибок;
- количество предупреждений.

Метрики являются информационными.

---

# 11. Lifecycle

```
Created

↓

Stored
```

Других состояний не существует.

GenerationResult является immutable.

---

# 12. Invariants

GenerationResult SHALL удовлетворять следующим требованиям.

- Identifier существует.
- Session существует.
- Status определён.
- StartedUtc ≤ FinishedUtc.
- Duration ≥ 0.

---

# 13. Creation Rules

GenerationResult создаётся автоматически после завершения GenerationSession.

После создания SHALL:

- вычислить Duration;
- сохранить Diagnostics;
- сохранить ссылки на созданные объекты;
- опубликовать GenerationResultCreated.

---

# 14. Modification Rules

Любая модификация запрещена.

GenerationResult является immutable Entity.

---

# 15. Persistence

GenerationResult сериализуется как часть Project.

GenerationResult SHALL NOT знать:

- Runtime;
- Worker;
- файловую систему;
- GPU;
- параметры AI Engine.

---

# 16. Concurrency

Поддерживается только конкурентное чтение.

Запись допускается исключительно во время создания объекта.

---

# 17. Domain Events

GenerationResult публикует:

- GenerationResultCreated

Других событий не существует.

---

# 18. Commands

Поддерживаются команды.

- CreateGenerationResult

После создания команды изменения отсутствуют.

---

# 19. AI Implementation Requirements

GenerationResult SHALL быть полностью независимым от технологии синтеза.

Запрещается хранить:

- параметры CUDA;
- параметры XTTS;
- параметры Piper;
- параметры Kokoro;
- параметры ONNX Runtime.

---

# 20. Test Requirements

Минимальный набор тестов.

- успешное создание;
- создание после ошибки;
- сериализация;
- десериализация;
- неизменяемость;
- проверка инвариантов.

---

# 21. Compliance Checklist

Реализация соответствует настоящей спецификации только если:

- Result принадлежит Session;
- является immutable;
- содержит итоговый статус;
- не зависит от AI Runtime;
- реализованы события;
- соблюдены все инварианты;
- сериализация полностью воспроизводима.

---

End of Document