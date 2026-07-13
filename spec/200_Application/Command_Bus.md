# Voxarium Software Architecture Specification

Document Path:
spec/200_Application/Command_Bus.md

Document ID: APP-004

Title: Command Bus

Version: 1.0.0

Status: Accepted

Classification: Normative

Depends On

- APP-001 Application Architecture
- APP-002 Command Model
- APP-003 Query Model

Referenced By

- Event_Bus.md
- Query_Bus.md
- All Command Handlers
- Presentation Layer
- CLI
- GUI
- REST API
- Plugin API

---

# 1. Purpose

Command Bus является центральным механизмом передачи команд в системе Voxarium.

Ни один компонент системы не имеет права вызывать Command Handler напрямую.

Все изменения состояния Project проходят исключительно через Command Bus.

---

# 2. Responsibilities

Command Bus отвечает за:

- получение Command;
- маршрутизацию Command;
- поиск соответствующего Handler;
- проверку структуры Command;
- запуск Pipeline;
- обработку отмены;
- журналирование;
- публикацию результатов выполнения.

Command Bus не отвечает за:

- бизнес-логику;
- выполнение Job;
- выполнение Workflow;
- взаимодействие с Domain Model.

---

# 3. General Architecture

Command проходит следующие стадии.

Presentation Layer

↓

Command Bus

↓

Pipeline

↓

Handler Resolver

↓

Command Handler

↓

Transaction

↓

Domain Events

↓

Event Bus

↓

Result

---

# 4. Single Handler Rule

Каждый тип Command имеет ровно один Handler.

Регистрация нескольких Handler для одной команды запрещена.

При нарушении данного правила приложение не должно запускаться.

---

# 5. Handler Resolution

Поиск Handler выполняется исключительно по типу Command.

Использование строковых идентификаторов запрещено.

Использование Reflection во время выполнения не рекомендуется.

Регистрация Handler выполняется на этапе инициализации приложения.

---

# 6. Pipeline

Перед передачей команды Handler Command проходит Pipeline.

Минимальный Pipeline включает:

- Structural Validation;
- Authorization;
- Logging;
- Metrics;
- Idempotency Check;
- Transaction Opening;
- Handler Execution;
- Transaction Commit;
- Event Publishing.

Порядок этапов является обязательным.

---

# 7. Validation

Command Bus выполняет только структурную проверку.

Проверяются:

- обязательные поля;
- корректность UUID;
- версия схемы;
- сериализация;
- допустимость типа Command.

Бизнес-правила проверяются только Handler.

---

# 8. Authorization

Command Bus вызывает Authorization Policy.

Если пользователь не имеет прав,

Handler не вызывается.

---

# 9. Idempotency

Перед выполнением Command Bus обязан проверить,

не была ли команда уже успешно выполнена.

Если Command уже существует,

результат предыдущего выполнения возвращается повторно.

---

# 10. Transactions

Command Bus открывает транзакцию перед вызовом Handler.

При успешном завершении выполняется Commit.

При ошибке выполняется Rollback.

---

# 11. Cancellation

Command Bus обязан поддерживать отмену выполнения.

Cancellation Token передаётся во все нижележащие компоненты.

Любой Handler обязан корректно реагировать на отмену.

---

# 12. Timeout

Command Bus может завершить выполнение Command по таймауту.

Политика таймаута определяется конфигурацией.

При превышении времени выполнение должно быть безопасно остановлено либо преобразовано в Job.

---

# 13. Event Publishing

Domain Events публикуются только после успешного Commit.

При ошибке транзакции публикация событий запрещена.

---

# 14. Result

Каждый Handler возвращает Command Result.

Result содержит:

- Success;
- Failure;
- Validation Errors;
- Domain Errors;
- Job Id (при необходимости);
- Metadata.

Result никогда не содержит Domain Entity.

---

# 15. Exception Policy

Handler не должен возвращать исключения пользователю.

Все исключения преобразуются в унифицированный Command Result.

---

# 16. Logging

Каждая команда журналируется.

Минимально фиксируются:

- Command Id;
- Correlation Id;
- Handler;
- время выполнения;
- результат;
- исключение.

---

# 17. Metrics

Command Bus публикует следующие метрики:

- Commands/sec;
- Average Execution Time;
- Failed Commands;
- Retry Count;
- Queue Time;
- Handler Time.

---

# 18. Performance

Command Bus должен поддерживать:

- пакетную обработку команд;
- параллельную обработку независимых команд;
- минимальное количество аллокаций памяти;
- высокую пропускную способность.

---

# 19. Thread Safety

Command Bus обязан быть полностью потокобезопасным.

Несколько потоков могут одновременно отправлять команды.

Каждая команда должна обрабатываться независимо.

---

# 20. Plugin Integration

Plugin могут регистрировать:

- собственные Command;
- собственные Handler;
- собственные Validation Policy;
- собственные Authorization Policy.

Plugin не могут изменять Core Pipeline.

---

# 21. Failure Recovery

Если приложение аварийно завершилось во время обработки команды,

после запуска должна существовать возможность определить:

- была ли команда завершена;
- была ли выполнена транзакция;
- были ли опубликованы события.

Повторное выполнение должно оставаться безопасным.

---

# 22. Test Requirements

Command Bus должен иметь тесты, проверяющие:

- маршрутизацию;
- Pipeline;
- идемпотентность;
- Rollback;
- публикацию событий;
- отмену;
- многопоточную работу;
- регистрацию Handler;
- обработку ошибок.

---

# 23. Compliance

Любая реализация Command Bus обязана соответствовать настоящему документу.

---

# Appendix A. Reference Pipeline

Receive Command

↓

Structural Validation

↓

Authorization

↓

Logging Begin

↓

Metrics Begin

↓

Idempotency Check

↓

Open Transaction

↓

Resolve Handler

↓

Execute Handler

↓

Commit

↓

Publish Events

↓

Logging End

↓

Metrics End

↓

Return Result

---

End of Document