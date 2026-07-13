# Voxarium Software Architecture Specification

Document Path:
spec/200_Application/Query_Bus.md

Document ID: APP-005

Title: Query Bus

Version: 1.0.0

Status: Accepted

Classification: Normative

Depends On

- APP-001 Application Architecture
- APP-003 Query Model

Referenced By

- Presentation Layer
- GUI
- CLI
- REST API
- Read Model
- Plugin API

---

# 1. Purpose

Query Bus является единственной точкой входа для всех операций чтения данных.

Ни один компонент системы не имеет права вызывать Query Handler напрямую.

Все операции чтения проходят через Query Bus.

---

# 2. Responsibilities

Query Bus отвечает за:

- получение Query;
- поиск соответствующего Query Handler;
- выполнение Pipeline чтения;
- журналирование;
- публикацию метрик;
- кэширование (при необходимости);
- возврат результата.

Query Bus не отвечает за:

- изменение Domain Model;
- выполнение Command;
- создание Job;
- выполнение Workflow.

---

# 3. Architectural Principles

Каждый Query имеет один Query Handler.

Каждый Query возвращает один Result DTO.

Query Bus не знает внутреннего устройства Handler.

Handler не знает, кто инициировал запрос.

---

# 4. Processing Pipeline

Каждый Query проходит одинаковый Pipeline.

Receive Query

↓

Structural Validation

↓

Authorization

↓

Logging

↓

Metrics

↓

Cache Lookup

↓

Resolve Handler

↓

Execute Handler

↓

Cache Store

↓

Return DTO

---

# 5. Handler Resolution

Каждый тип Query регистрируется один раз.

Если зарегистрировано несколько Handler для одного Query,

приложение не должно запускаться.

---

# 6. Validation

Query проходит структурную проверку.

Проверяются:

- обязательные поля;
- корректность типов;
- версия схемы;
- сериализация.

Проверка бизнес-правил не выполняется.

---

# 7. Authorization

Перед выполнением Query проверяются права доступа.

Handler никогда не вызывается при отсутствии необходимых разрешений.

---

# 8. Read Repository

Query Handler получает данные исключительно через Read Repository.

Handler не работает напрямую:

- с файловой системой;
- с базой данных;
- с Domain Repository.

Read Repository скрывает способ хранения данных.

---

# 9. Result

Каждый Query возвращает DTO.

DTO является неизменяемым.

DTO не содержит:

- методов изменения;
- бизнес-логики;
- ссылок на Aggregate Root.

---

# 10. Caching

Query Bus может использовать кэширование.

Допускаются:

- Memory Cache;
- Disk Cache;
- Distributed Cache.

Политика кэширования определяется конфигурацией.

---

# 11. Cache Invalidation

После успешного выполнения Command

соответствующие записи кэша должны быть инвалидированы.

Query Bus самостоятельно не изменяет кэш.

---

# 12. Pagination

Query Bus поддерживает:

- Offset Pagination;
- Cursor Pagination.

Handler обязан возвращать информацию:

- об общем количестве записей (если доступно);
- о наличии следующей страницы;
- о положении курсора.

---

# 13. Streaming Queries

Для больших наборов данных Query Bus должен поддерживать потоковую выдачу результатов.

Примеры:

- список Fragment большого проекта;
- библиотека Voice Profile;
- история Job;
- журнал событий.

Потоковая выдача должна минимизировать использование памяти.

---

# 14. Consistency

По умолчанию Query работают с последним согласованным состоянием.

Если используется отдельная Read Model,

допускается Eventual Consistency.

---

# 15. Logging

Каждый Query журналируется.

Фиксируются:

- Query Id;
- тип Query;
- Handler;
- длительность выполнения;
- количество возвращённых объектов;
- ошибки.

---

# 16. Metrics

Минимальный набор метрик.

- Queries/sec
- Average Duration
- Cache Hit Rate
- Cache Miss Rate
- Read Repository Time
- Handler Time

---

# 17. Thread Safety

Query Bus обязан поддерживать многопоточную работу.

Несколько Query могут выполняться одновременно.

Операции чтения не должны блокировать друг друга.

---

# 18. Plugin Integration

Plugin могут регистрировать:

- Query;
- Query Handler;
- Read Repository Adapter;
- Read DTO.

Plugin не могут изменять Core Pipeline.

---

# 19. Error Handling

Все ошибки преобразуются в единый Query Result.

Минимально поддерживаются:

- Validation Error;
- Access Denied;
- Not Found;
- Timeout;
- Infrastructure Error.

Исключения не должны покидать Query Bus.

---

# 20. Performance Requirements

Query Bus должен поддерживать:

- десятки тысяч Query в минуту;
- потоковую обработку больших коллекций;
- минимальное количество аллокаций памяти;
- эффективное кэширование.

---

# 21. Test Requirements

Должны существовать тесты, проверяющие:

- маршрутизацию Query;
- регистрацию Handler;
- работу Pipeline;
- кэширование;
- пагинацию;
- потоковую выдачу;
- многопоточную работу;
- обработку ошибок.

---

# 22. Compliance

Любая реализация Query Bus обязана соответствовать настоящему документу.

---

# Appendix A. Reference Query Flow

Presentation

↓

Query Bus

↓

Validation

↓

Authorization

↓

Logging

↓

Metrics

↓

Cache

↓

Query Handler

↓

Read Repository

↓

DTO

↓

Presentation

---

End of Document