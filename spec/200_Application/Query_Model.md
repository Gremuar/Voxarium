# Voxarium Software Architecture Specification

Document Path:
spec/200_Application/Query_Model.md

Document ID: APP-003

Title: Query Model

Version: 1.0.0

Status: Accepted

Classification: Normative

Depends On

- APP-001 Application Architecture
- APP-002 Command Model
- Все документы раздела 100_Domain

Referenced By

- Query Bus
- Presentation Layer
- UI
- CLI
- REST API
- Read Models

---

# 1. Purpose

Настоящий документ определяет модель запросов (Query Model), используемую в Voxarium.

Query представляет собой запрос на получение информации.

Query никогда не изменяет состояние системы.

Query не создаёт Domain Events.

Query не создаёт Job.

---

# 2. Responsibilities

Query отвечает исключительно за:

- описание требуемых данных;
- параметры поиска;
- параметры сортировки;
- параметры фильтрации;
- параметры пагинации.

Query не отвечает за:

- изменение состояния Project;
- выполнение бизнес-логики;
- запуск Workflow;
- выполнение генерации.

---

# 3. Architectural Principles

Для всех Query действуют следующие правила.

Каждый Query имеет собственный Handler.

Каждый Query возвращает DTO.

Query никогда не возвращает доменные сущности напрямую.

Query не обращается к Infrastructure напрямую.

---

# 4. CQRS Separation

Command Side

↓

Domain Model

↓

Persistence

↓

Read Projection

↓

Query Side

Query всегда работает с Read Model.

При отсутствии Read Projection допускается чтение Domain Model через Read Repository.

---

# 5. Naming Convention

Название Query начинается с Get, Find, Search или List.

Примеры.

GetProjectOverviewQuery

GetTimelineQuery

GetFragmentQuery

FindVoiceProfilesQuery

SearchDictionaryQuery

ListProjectsQuery

---

# 6. Query Structure

Каждый Query содержит:

Query Id

Schema Version

Timestamp

Payload

Metadata

---

# 7. Payload

Payload может содержать:

- идентификаторы;
- строки поиска;
- фильтры;
- параметры сортировки;
- параметры отображения;
- ограничения количества результатов.

Payload не должен содержать ссылки на объекты памяти.

---

# 8. Read DTO

Каждый Query возвращает специализированный DTO.

DTO не должен содержать:

- методы изменения;
- бизнес-логику;
- ссылки на Domain Aggregate.

DTO является исключительно структурой данных.

---

# 9. Read Models

Application Layer может использовать специализированные Read Model.

Например.

Project Overview

↓

Production Summary

↓

Timeline View

↓

Voice Library

↓

Job Monitor

↓

Plugin Catalog

Read Model может отличаться от структуры Domain Model.

---

# 10. Filtering

Все Query должны поддерживать фильтрацию, если это применимо.

Примеры.

по языку

по роли

по голосу

по состоянию Job

по дате

по тегам

---

# 11. Sorting

Если порядок результатов имеет значение,

Query должен поддерживать сортировку.

Минимально:

- по имени;
- по времени создания;
- по времени изменения;
- по длительности;
- по пользовательскому порядку.

---

# 12. Pagination

Для больших наборов данных должна использоваться пагинация.

Поддерживаются:

Offset Pagination

Cursor Pagination

Конкретный способ определяется реализацией Read Repository.

---

# 13. Performance

Query должны оптимизироваться независимо от Command Side.

Допускается:

- денормализация;
- индексы;
- кэширование;
- специальные представления.

Domain Layer не должен знать об этих оптимизациях.

---

# 14. Caching

Query могут использовать кэш.

Кэш не должен нарушать согласованность данных.

Инвалидация выполняется после успешного завершения соответствующих Command.

---

# 15. Consistency

Read Side допускает Eventual Consistency.

После выполнения Command допускается небольшая задержка обновления Read Projection.

Для локального режима рекомендуется Strong Consistency.

---

# 16. Query Bus

Все Query передаются исключительно через Query Bus.

Presentation Layer не вызывает Handler напрямую.

Последовательность взаимодействия.

Presentation

↓

Query Bus

↓

Handler Resolution

↓

Query Handler

↓

Read Repository

↓

DTO

---

# 17. Security

Query проходят проверку прав доступа.

Handler обязан возвращать только разрешённые данные.

Скрытые объекты не должны попадать в DTO.

---

# 18. Error Handling

Query может завершиться следующими результатами.

Success

Not Found

Access Denied

Validation Error

Timeout

Infrastructure Error

Ошибки представляются в едином формате.

---

# 19. Logging

Каждый Query журналируется.

Минимально фиксируются:

- Query Id;
- время выполнения;
- длительность;
- количество возвращённых объектов;
- ошибка.

---

# 20. Extensibility

Plugin могут регистрировать:

- собственные Query;
- собственные DTO;
- собственные Read Projection;
- собственные Query Handler.

Core взаимодействует с ними только через Query Bus.

---

# 21. Test Requirements

Для каждого Query должны существовать:

- Unit Tests;
- Contract Tests;
- Performance Tests (при необходимости);
- Tests на фильтрацию;
- Tests на сортировку;
- Tests на пагинацию.

---

# 22. Compliance

Любая реализация Query обязана соответствовать настоящему документу.

---

# Appendix A. Standard Queries

Минимальный набор Query Core.

## Project

GetProjectOverviewQuery

GetProjectStatisticsQuery

ListProjectsQuery

---

## Production

GetProductionQuery

ListProductionsQuery

---

## Timeline

GetTimelineQuery

GetFragmentQuery

ListFragmentsQuery

---

## Role

GetRoleQuery

ListRolesQuery

---

## Voice

GetVoiceProfileQuery

ListVoiceProfilesQuery

SearchVoiceProfilesQuery

---

## Speech

GetSpeechSegmentQuery

ListSpeechSegmentsQuery

---

## Assets

GetAssetQuery

FindAssetsQuery

---

## Jobs

GetJobQuery

ListJobsQuery

GetQueueStateQuery

---

## Workflow

GetWorkflowQuery

ListWorkflowsQuery

---

## Plugins

ListPluginsQuery

GetPluginCapabilitiesQuery

---

End of Document