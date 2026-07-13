# Voxarium Software Architecture Specification

Document Path:
spec/200_Application/Command_Model.md

Document ID: APP-002

Title: Command Model

Version: 1.0.0

Status: Accepted

Classification: Normative

Depends On

- APP-001 Application Architecture
- Все документы раздела 100_Domain

Referenced By

- Все Command Handler
- Queue.md
- Workflow.md
- API.md
- CLI.md
- UI.md

---

# 1. Purpose

Настоящий документ определяет модель команд (Command Model), используемую в Voxarium.

Команда представляет собой намерение изменить состояние системы.

Команда не содержит бизнес-логики.

Команда не выполняет никаких вычислений.

Команда является неизменяемым объектом (Immutable DTO).

---

# 2. Responsibilities

Command отвечает исключительно за:

- передачу входных данных;
- идентификацию выполняемой операции;
- сериализацию;
- передачу информации между слоями.

Command не отвечает за:

- выполнение операции;
- проверку бизнес-правил;
- изменение Domain Model;
- взаимодействие с инфраструктурой.

---

# 3. General Rules

Каждая команда должна:

- иметь одно назначение;
- быть неизменяемой;
- иметь уникальный тип;
- быть сериализуемой;
- быть пригодной для журналирования;
- иметь версию схемы.

---

# 4. Naming Convention

Название команды должно начинаться с глагола.

Примеры.

CreateProjectCommand

ImportDocumentCommand

SplitFragmentCommand

AssignVoiceCommand

GenerateFragmentCommand

ExportProductionCommand

CloneVoiceCommand

DeleteRoleCommand

RenameProductionCommand

---

# 5. Command Structure

Каждая команда содержит только данные.

Минимальная структура.

Command Id

Schema Version

Timestamp

Correlation Id

Initiator

Payload

Metadata

---

# 6. Command Identifier

Каждая команда имеет UUID v7.

UUID используется для:

- журналирования;
- идемпотентности;
- восстановления;
- трассировки.

---

# 7. Correlation Id

Все команды, принадлежащие одной операции пользователя, имеют общий Correlation Id.

Пример.

Импорт книги

↓

Создание проекта

↓

Создание Document

↓

Создание Timeline

↓

Создание Fragment

Все команды имеют одинаковый Correlation Id.

Это позволяет полностью восстановить цепочку выполнения.

---

# 8. Initiator

Команда должна содержать информацию об инициаторе.

Минимально поддерживаются:

- User
- Workflow
- Plugin
- Automation
- System

---

# 9. Payload

Payload содержит только входные параметры.

Payload не содержит:

- сервисов;
- ссылок на объекты памяти;
- открытых файлов;
- делегатов;
- лямбда-функций.

---

# 10. Metadata

Metadata используется исключительно для служебной информации.

Например:

- версия клиента;
- язык интерфейса;
- источник команды;
- пользовательские метки.

Бизнес-данные запрещается помещать в Metadata.

---

# 11. Immutability

После создания Command изменение её содержимого запрещено.

Любое изменение создаёт новую Command.

---

# 12. Validation

Command проходит два этапа проверки.

## Stage 1

Проверка структуры DTO.

- обязательные поля;
- формат UUID;
- типы данных.

## Stage 2

Проверка бизнес-правил выполняется Handler.

---

# 13. Idempotency

Каждая команда должна поддерживать повторную отправку.

Повторное получение команды с тем же Command Id не должно приводить к повторному выполнению операции.

---

# 14. Serialization

Все команды должны сериализоваться в независимый формат.

Рекомендуемые форматы:

- JSON
- CBOR

Использование бинарной сериализации платформы запрещено.

---

# 15. Versioning

Каждая команда имеет Schema Version.

Изменение структуры команды требует увеличения версии.

Старые версии должны поддерживаться механизмом миграции.

---

# 16. Command Bus

Все команды передаются исключительно через Command Bus.

Presentation Layer не имеет права напрямую вызывать Handler.

Последовательность взаимодействия.

Presentation

↓

Command Bus

↓

Handler Resolution

↓

Handler Execution

---

# 17. Relationship with Workflow

Workflow создаёт команды.

Workflow не вызывает Handler напрямую.

---

# 18. Relationship with Job

Handler может создать Job.

Команда не содержит Job.

---

# 19. Error Handling

Если Command не прошла структурную проверку,

она отклоняется до вызова Handler.

Handler никогда не получает невалидную структуру Command.

---

# 20. Logging

Каждая команда журналируется.

Минимально фиксируются:

- Command Id;
- Correlation Id;
- время получения;
- время завершения;
- результат;
- ошибка.

---

# 21. Performance Requirements

Создание Command должно иметь минимальные накладные расходы.

Команда должна занимать минимальный объём памяти.

Передача команды между потоками должна выполняться без копирования больших данных.

---

# 22. Extensibility

Plugin могут регистрировать собственные команды.

Все пользовательские команды обязаны соответствовать настоящему документу.

---

# 23. Test Requirements

Для каждой команды должны существовать тесты, проверяющие:

- сериализацию;
- десериализацию;
- идемпотентность;
- валидацию структуры;
- версионирование.

---

# 24. Compliance

Любая команда системы Voxarium обязана соответствовать требованиям настоящего документа.

---

# Appendix A. Standard Commands

Минимальный набор команд Core.

## Project

CreateProjectCommand

OpenProjectCommand

CloseProjectCommand

SaveProjectCommand

RenameProjectCommand

DeleteProjectCommand

---

## Source

ImportSourceCommand

RemoveSourceCommand

UpdateSourceMetadataCommand

---

## Document

ImportDocumentCommand

ParseDocumentCommand

NormalizeDocumentCommand

---

## Timeline

CreateTimelineCommand

SplitFragmentCommand

MergeFragmentsCommand

MoveFragmentCommand

DeleteFragmentCommand

---

## Role

CreateRoleCommand

RenameRoleCommand

AssignRoleCommand

DeleteRoleCommand

---

## Voice

CreateVoiceProfileCommand

CloneVoiceCommand

AssignVoiceCommand

DeleteVoiceCommand

---

## Generation

GenerateFragmentCommand

GenerateSelectionCommand

GenerateTimelineCommand

GenerateProductionCommand

RegenerateFragmentCommand

CancelGenerationCommand

---

## Playback

PlayCommand

PauseCommand

StopCommand

SeekCommand

---

## Export

ExportAudioCommand

ExportProjectCommand

ExportSubtitlesCommand

---

## Workflow

CreateWorkflowCommand

ExecuteWorkflowCommand

CancelWorkflowCommand

---

End of Document