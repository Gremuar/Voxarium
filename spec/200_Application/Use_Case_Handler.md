# Voxarium Software Architecture Specification

Document Path:
spec/200_Application/Use_Case_Handler.md

Document ID: APP-007

Title: Use Case Handler

Version: 1.0.0

Status: Accepted

Classification: Normative

Depends On

- APP-001 Application Architecture
- APP-002 Command Model
- APP-003 Query Model
- APP-004 Command Bus
- APP-005 Query Bus
- APP-006 Event Bus

Referenced By

- All Application Modules
- GUI
- CLI
- REST API
- Plugin API

---

# 1. Purpose

Use Case Handler представляет собой реализацию одного конкретного сценария использования системы.

Каждый Handler реализует только один сценарий.

Handler является единственной точкой, где координируется выполнение конкретной пользовательской операции.

---

# 2. Responsibility

Use Case Handler отвечает исключительно за:

- получение Command;
- загрузку необходимых Aggregate;
- координацию доменных объектов;
- вызов Domain Services;
- сохранение изменений;
- публикацию Domain Events;
- возврат результата.

Handler не отвечает за:

- бизнес-правила;
- отображение интерфейса;
- выполнение Job;
- работу с файлами;
- работу с TTS Engine.

---

# 3. Architectural Principles

Каждый Handler должен:

- реализовывать один Use Case;
- быть максимально коротким;
- быть детерминированным;
- быть легко тестируемым;
- не содержать скрытых зависимостей.

---

# 4. Standard Execution Flow

Каждый Handler обязан выполнять операции в следующем порядке.

Receive Command

↓

Load Aggregate

↓

Execute Domain Logic

↓

Persist Aggregate

↓

Publish Events

↓

Return Result

Нарушение данного порядка не допускается.

---

# 5. Aggregate Access

Handler имеет право изменять только те Aggregate,

которые относятся к текущему сценарию.

Не допускается массовое изменение большого количества Aggregate без необходимости.

---

# 6. Repository Usage

Handler получает Aggregate исключительно через Repository.

Запрещается:

- создавать Aggregate вручную;
- работать напрямую с файловой системой;
- обращаться к базе данных;
- использовать Infrastructure Adapter напрямую.

---

# 7. Domain Services

Если операция требует сложной предметной логики,

Handler обязан использовать Domain Service.

Handler не должен дублировать бизнес-правила.

---

# 8. External Services

Для взаимодействия с внешними компонентами используются исключительно Ports.

Например:

Speech Engine Port

Plugin Port

Audio Processing Port

AI Port

Storage Port

Handler никогда не знает реализацию этих компонентов.

---

# 9. Transactions

Один Handler соответствует одной прикладной транзакции.

При успешном завершении выполняется Commit.

При ошибке выполняется Rollback.

---

# 10. Job Creation

Если операция является длительной,

Handler создаёт Job.

После регистрации Job Handler немедленно завершает выполнение.

Дальнейшая работа выполняется Worker.

---

# 11. Validation

Handler выполняет:

- проверку существования Aggregate;
- проверку бизнес-инвариантов;
- проверку состояния Project;
- проверку совместимости операций.

Структурная проверка Command уже выполнена Command Bus.

---

# 12. Error Handling

Handler не должен генерировать необработанные исключения.

Все ошибки преобразуются в Result.

Минимально поддерживаются:

- Validation Error;
- Domain Error;
- Infrastructure Error;
- Plugin Error;
- Cancelled.

---

# 13. Cancellation

Если Command отменена,

Handler обязан безопасно завершить выполнение.

Частично изменённое состояние запрещено.

---

# 14. Logging

Каждый Handler обязан журналировать:

- начало выполнения;
- окончание выполнения;
- длительность;
- результат.

---

# 15. Metrics

Каждый Handler публикует:

- Execution Time;
- Aggregate Count;
- Created Jobs;
- Published Events.

---

# 16. Dependency Injection

Все зависимости передаются через конструктор.

Использование глобальных объектов запрещено.

Использование Service Locator запрещено.

---

# 17. Thread Safety

Handler не должен хранить внутреннее состояние между вызовами.

Каждый экземпляр должен быть безопасен для многократного использования.

---

# 18. Testability

Каждый Handler должен тестироваться изолированно.

Все внешние зависимости заменяются Mock или Fake.

Тесты не должны обращаться к инфраструктуре.

---

# 19. Naming Convention

Название Handler должно соответствовать Command.

Например.

CreateProjectHandler

ImportDocumentHandler

AssignVoiceHandler

GenerateFragmentHandler

ExportProductionHandler

CloneVoiceHandler

---

# 20. Performance Requirements

Handler должен:

- минимизировать время удержания транзакции;
- избегать тяжёлых вычислений;
- минимизировать использование памяти;
- делегировать длительные операции Job System.

---

# 21. Extensibility

Plugin могут регистрировать собственные Handler.

Каждый Plugin Handler обязан соответствовать требованиям настоящего документа.

---

# 22. Compliance

Любая реализация Use Case Handler обязана соответствовать настоящему документу.

---

# Appendix A. Reference Handler Flow

Command

↓

Load Aggregate

↓

Domain Logic

↓

Repository Save

↓

Commit

↓

Publish Events

↓

Return Result

---

# Appendix B. Standard Core Handlers

## Project

CreateProjectHandler

OpenProjectHandler

SaveProjectHandler

CloseProjectHandler

DeleteProjectHandler

---

## Source

ImportSourceHandler

UpdateSourceHandler

RemoveSourceHandler

---

## Document

ImportDocumentHandler

ParseDocumentHandler

NormalizeDocumentHandler

---

## Timeline

SplitFragmentHandler

MergeFragmentsHandler

MoveFragmentHandler

DeleteFragmentHandler

---

## Role

CreateRoleHandler

AssignRoleHandler

DeleteRoleHandler

---

## Voice

CreateVoiceProfileHandler

AssignVoiceHandler

CloneVoiceHandler

DeleteVoiceProfileHandler

---

## Generation

GenerateFragmentHandler

GenerateSelectionHandler

GenerateTimelineHandler

GenerateProductionHandler

RegenerateFragmentHandler

---

## Export

ExportAudioHandler

ExportProjectHandler

ExportSubtitlesHandler

---

## Workflow

CreateWorkflowHandler

ExecuteWorkflowHandler

CancelWorkflowHandler

---

End of Document