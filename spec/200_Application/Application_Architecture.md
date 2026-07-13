# Voxarium Software Architecture Specification

Document Path:
spec/200_Application/Application_Architecture.md

Document ID: APP-001

Title: Application Architecture

Version: 1.0.0

Status: Accepted

Classification: Normative

Depends On

- SAS-003 Architecture Principles
- Все документы раздела 100_Domain

Referenced By

- Все документы раздела 200_Application
- Все документы разделов 300-900

---

# 1. Purpose

Настоящий документ определяет архитектуру прикладного уровня (Application Layer) системы Voxarium.

Application Layer реализует сценарии использования системы (Use Cases), координирует работу доменной модели и инфраструктуры, но не содержит бизнес-правил предметной области и не зависит от реализации внешних сервисов.

---

# 2. Position in Hexagonal Architecture

Архитектура Voxarium состоит из следующих слоёв.

Presentation Layer

↓

Application Layer

↓

Domain Layer

↓

Ports

↓

Infrastructure Layer

Application Layer является единственной точкой входа в доменную модель.

Ни один пользовательский интерфейс, плагин или инфраструктурный модуль не имеет права напрямую изменять Domain Model.

---

# 3. Responsibilities

Application Layer отвечает за:

- выполнение пользовательских сценариев;
- управление транзакциями;
- координацию доменных объектов;
- запуск Workflow;
- создание Job;
- публикацию Domain Events;
- вызов внешних портов;
- обработку ошибок прикладного уровня;
- контроль выполнения операций.

Application Layer не отвечает за:

- бизнес-правила предметной области;
- работу TTS Engine;
- работу с базой данных;
- отображение интерфейса;
- сериализацию файлов проекта.

---

# 4. Architectural Principles

Application Layer строится по следующим принципам.

## 4.1 Один Use Case — один класс

Каждый сценарий использования реализуется отдельным классом.

Пример:

CreateProjectHandler

ImportBookHandler

GenerateSpeechHandler

ExportAudiobookHandler

AssignVoiceHandler

Никакие универсальные сервисы, объединяющие десятки сценариев, не допускаются.

---

## 4.2 CQRS

Все операции разделяются на две категории.

Commands

изменяют состояние системы.

Queries

только читают данные.

Query никогда не изменяет Domain Model.

---

## 4.3 Command Handler

Каждая команда имеет собственный обработчик.

Команда содержит только входные данные.

Вся логика находится внутри Handler.

Пример.

GenerateSpeechCommand

↓

GenerateSpeechHandler

↓

Domain

↓

Ports

---

## 4.4 Query Handler

Каждый запрос имеет отдельный обработчик.

Пример.

GetProjectOverviewQuery

↓

GetProjectOverviewHandler

↓

Read Model

---

## 4.5 Thin Application Layer

Application Layer не содержит сложной бизнес-логики.

Все правила принадлежат Domain Layer.

Application Layer только организует выполнение.

---

## 4.6 Explicit Dependencies

Каждый Handler получает зависимости через Dependency Injection.

Использование Service Locator запрещено.

---

## 4.7 Idempotency

Все команды должны поддерживать повторный вызов.

Повторное выполнение не должно приводить к повреждению Project.

---

## 4.8 Asynchronous Operations

Все длительные операции должны выполняться посредством Job System.

Запрещается выполнять генерацию речи непосредственно внутри Handler.

---

# 5. Use Case Structure

Каждый Use Case имеет одинаковую структуру.

Input DTO

↓

Validation

↓

Load Aggregate

↓

Execute Domain Logic

↓

Persist Changes

↓

Publish Events

↓

Return Result

---

# 6. Transaction Boundaries

Один Use Case соответствует одной прикладной транзакции.

Все изменения должны быть либо полностью применены, либо полностью отменены.

Частично завершённые изменения запрещены.

---

# 7. Communication Rules

Взаимодействие компонентов разрешено только по следующей схеме.

Presentation

↓

Application

↓

Domain

↓

Ports

↓

Infrastructure

Обратные зависимости запрещены.

---

# 8. Domain Events

Application Layer обязан публиковать все Domain Events после успешного завершения транзакции.

До фиксации изменений события не должны быть доступны подписчикам.

---

# 9. Integration with Job System

Если выполнение операции занимает продолжительное время, Handler обязан:

1. создать Job;
2. зарегистрировать Job;
3. поставить Job в очередь;
4. вернуть пользователю идентификатор Job.

Handler не ожидает завершения выполнения Job.

---

# 10. Validation

Application Layer выполняет:

- проверку DTO;
- проверку прав доступа;
- проверку существования объектов;
- проверку корректности входных параметров.

Проверка бизнес-инвариантов выполняется Domain Layer.

---

# 11. Error Handling

Ошибки подразделяются на:

- Validation Error;
- Domain Error;
- Infrastructure Error;
- User Cancelled;
- Timeout;
- Plugin Error.

Application Layer преобразует внутренние исключения в единый формат ошибок.

---

# 12. Logging

Каждый Use Case обязан журналировать:

- начало выполнения;
- окончание выполнения;
- длительность;
- результат;
- ошибку (при наличии).

Журналирование выполняется через Logging Port.

---

# 13. Metrics

Каждый Use Case публикует:

- время выполнения;
- количество созданных Job;
- количество обработанных объектов;
- успешность выполнения.

---

# 14. Security

Application Layer не должен доверять входным данным.

Все входные параметры проходят обязательную проверку.

---

# 15. Performance Requirements

Application Layer должен:

- не блокировать UI;
- поддерживать параллельное выполнение независимых Use Case;
- минимизировать удержание транзакций;
- избегать длительных операций в памяти.

---

# 16. Extensibility

Плагины могут регистрировать собственные:

- Commands;
- Queries;
- Handlers;
- Validators;
- Policies.

Core взаимодействует с ними только через публичные интерфейсы.

---

# 17. Test Requirements

Для каждого Use Case должны существовать:

- Unit Tests;
- Integration Tests;
- Contract Tests (для Ports);
- Performance Tests (при необходимости).

---

# 18. Compliance

Любая реализация Application Layer обязана соответствовать настоящему документу.

Изменение архитектурных принципов допускается только через новый Architecture Decision Record (ADR).

---

End of Document