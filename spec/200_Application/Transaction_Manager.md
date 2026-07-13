# Voxarium Software Architecture Specification

Document Path:
spec/200_Application/Transaction_Manager.md

Document ID: APP-030

Title: Transaction Manager

Version: 1.0.0

Status: Accepted

Classification: Normative

Depends On

- Application_Architecture
- Command_Bus
- Event_Bus
- Query_Bus

Referenced By

- Project_Service
- Timeline_Service
- Voice_Service
- Generation_Service
- Workflow_Engine
- Job_Orchestrator

---

# 1. Purpose

Transaction Manager обеспечивает атомарное выполнение прикладных операций.

Он является единственной точкой управления жизненным циклом транзакций Application Layer.

---

# 2. Responsibilities

Transaction Manager SHALL:

- открывать транзакцию;
- завершать транзакцию;
- выполнять откат;
- координировать публикацию событий;
- обеспечивать согласованность изменений;
- предотвращать частичное выполнение операций.

---

# 3. Non-Responsibilities

Transaction Manager SHALL NOT:

- выполнять бизнес-логику;
- выполнять валидацию;
- выполнять генерацию;
- управлять пользовательским интерфейсом;
- выполнять сохранение проекта.

---

# 4. Transaction Lifecycle

Каждая транзакция SHALL проходить следующие стадии.

```
Created

↓

Started

↓

Executing

↓

Committing

↓

Committed

или

Rolling Back

↓

Rolled Back
```

---

# 5. Transaction Scope

Транзакция охватывает выполнение одной команды.

Одна команда SHALL соответствовать одной транзакции.

Вложенные транзакции не допускаются.

---

# 6. Event Publication

Domain Events SHALL публиковаться только после успешного завершения транзакции.

При откате публикация событий запрещена.

---

# 7. Consistency Rules

Transaction Manager SHALL гарантировать:

- отсутствие частично применённых изменений;
- согласованность Aggregate Root;
- публикацию только подтверждённых событий.

---

# 8. Failure Handling

При возникновении ошибки Transaction Manager SHALL:

- остановить выполнение;
- выполнить откат;
- освободить ресурсы;
- вернуть информацию об ошибке.

---

# 9. Concurrency

Transaction Manager SHALL поддерживать выполнение нескольких независимых транзакций.

Одновременное изменение одного Aggregate регулируется механизмом конкурентного доступа.

---

# 10. Dependencies

Transaction Manager MAY использовать:

- Command Bus;
- Event Bus;
- Repository;
- Unit of Work.

Transaction Manager SHALL NOT зависеть от GUI, AI Runtime или Storage Backend.

---

# 11. AI Implementation Rules

Реализация SHALL:

- гарантировать атомарность операций;
- публиковать события только после Commit;
- не выполнять бизнес-логику;
- быть независимой от механизма хранения данных.

---

# 12. Test Requirements

Минимальный набор тестов.

- успешное завершение транзакции;
- откат при ошибке;
- отсутствие публикации событий при Rollback;
- выполнение нескольких независимых транзакций;
- конкурентное изменение Aggregate.

---

# 13. Compliance Checklist

Transaction Manager соответствует настоящей спецификации только если:

- обеспечивает атомарность операций;
- выполняет Commit и Rollback;
- публикует события только после Commit;
- не содержит бизнес-логики;
- допускает независимое тестирование.

---

End of Document