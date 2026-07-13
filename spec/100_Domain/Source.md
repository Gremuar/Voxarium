# Voxarium Software Architecture Specification

Document Path:
spec/100_Domain/Source.md

<<<<<<< HEAD
Document ID: DOM-102

Title: Source

Version: 1.0.0
=======
Document ID: DOM-002

Title: Source

Version: 2.0.0
>>>>>>> c975edf (t)

Status: Accepted

Classification: Normative

Depends On

<<<<<<< HEAD
- SAS-001 Glossary
- SAS-002 Domain Ontology
- SAS-003 Architecture Principles
- Project.md

Referenced By

- Document.md
- Import_Module.md
- IImporter.md
- Project_Format.md
- Asset.md
=======
- SAS-000 Project Philosophy
- SAS-001 Glossary
- SAS-002 Domain Ontology
- SAS-003 Architecture Principles
- Project

Referenced By

- Document
- Import_Service
- Project_Service
- Search_Index_Service
>>>>>>> c975edf (t)

---

# 1. Purpose

<<<<<<< HEAD
Source представляет собой неизменяемое представление исходного материала, импортированного пользователем в Project.

Source является единственным официальным источником происхождения данных (Source of Origin).

Source используется исключительно как источник данных для построения одного или нескольких Document.

После успешного импорта Source никогда не изменяется.

---

# 2. Responsibility

Source отвечает исключительно за:

- хранение информации об оригинальном материале;
- хранение происхождения данных;
- хранение контрольной информации;
- обеспечение повторного импорта;
- обеспечение воспроизводимости процесса импорта.

Source не отвечает за:

- разбиение текста;
- анализ структуры;
- определение ролей;
- генерацию речи;
- хранение результатов обработки.

---

# 3. Aggregate

Source является самостоятельным агрегатом.

Source принадлежит одному Project.

Document может ссылаться одновременно на несколько Source.

---

# 4. Identity

Каждый Source обладает постоянным UUID v7.

Изменение идентификатора запрещается.

---

# 5. Source Types

Архитектура не ограничивает перечень допустимых типов Source.

Поддержка конкретного типа определяется установленными Import Plugin.

Примеры типов:

- Plain Text
- DOCX
- ODT
- PDF
- EPUB
- FB2
- HTML
- Markdown
- SRT
- WebVTT
- ASS
- SSA
- XML
- JSON
- CSV
- ZIP Archive
- Audio Transcript
- Clipboard
- URL
- Directory

Core не содержит встроенной логики обработки конкретных форматов.

---

# 6. Required Attributes

| Name | Type | Required | Mutable |
|----------|----------|----------|----------|
| id | UUIDv7 | Yes | No |
| type | SourceType | Yes | No |
| importerId | PluginId | Yes | No |
| importedAt | UTC DateTime | Yes | No |
| originalName | String | Yes | No |
| checksum | Hash | Yes | No |
| size | Integer | Yes | No |

---

# 7. Optional Attributes

| Name | Type |
|----------|----------|
| originalPath | String |
| mediaType | MIME Type |
| encoding | String |
| language | LanguageCode |
| author | String |
| metadata | Map<String, Value> |

Наличие необязательных атрибутов зависит от Import Plugin.

---

# 8. Binary Content

Source может содержать:

- текст;
- бинарные данные;
- изображения;
- архивы;
- служебные файлы.

Core рассматривает содержимое Source как неизменяемые данные.

Интерпретация содержимого выполняется Import Plugin.

---

# 9. Immutability

После завершения импорта изменение Source запрещено.

Не допускается изменение:

- содержимого;
- имени;
- размера;
- контрольной суммы;
- времени импорта.

Любое изменение исходного файла вне Project не влияет на уже импортированный Source.

---

# 10. Origin Tracking

Каждый Source обязан хранить информацию о происхождении.

Минимальный набор:

- способ получения;
- идентификатор Import Plugin;
- дата импорта;
- контрольная сумма;
- оригинальное имя.

Дополнительная информация может сохраняться Plugin.

---

# 11. Relationship with Document

Document создаётся исключительно на основании одного или нескольких Source.

Source не содержит ссылок на Document.

Связь хранится на стороне Document.

Один Source может использоваться несколькими Document.

---

# 12. Relationship with Asset

Если импорт требует сохранения дополнительных файлов, они должны оформляться как Asset.

Source хранит только ссылки на соответствующие Asset.

---

# 13. Commands

Следующие команды работают с Source.

ImportSource

ValidateSource

RemoveSource

ReimportSource

ExtractMetadata

Удаление Source запрещается при наличии зависимых Document.

---

# 14. Domain Events

SourceImported

SourceValidated

SourceRemoved

SourceReimported

SourceValidationFailed

SourceMetadataUpdated

---

# 15. Validation

После импорта должны быть проверены:

- корректность контрольной суммы;
- корректность структуры;
- успешность чтения;
- соответствие заявленному типу;
- отсутствие повреждений.

Validation выполняется Import Plugin.

---

# 16. Reimport

Source поддерживает повторный импорт.

Повторный импорт создаёт новый Source.

Исходный Source сохраняется.

Document не должен автоматически переключаться на новый Source.

Решение о миграции принимает пользователь.

---

# 17. Multiple Sources

Project может содержать произвольное количество Source.

Document может использовать:

- один Source;
- несколько Source.

Архитектура должна поддерживать объединение нескольких Source в один Document.

Пример:

Том 1

+

Том 2

+

Том 3

↓

Document

---

# 18. Duplicate Sources

Допускается импорт нескольких одинаковых файлов.

Совпадение контрольной суммы не считается ошибкой.

Пользователь может получить предупреждение о наличии идентичного Source.

Окончательное решение принимает пользователь.

---

# 19. Storage Requirements

Source должен храниться таким образом, чтобы обеспечить:

- неизменяемость;
- проверку целостности;
- резервное копирование;
- переносимость проекта;
- независимость от исходного расположения файла.

После успешного импорта проект не должен зависеть от расположения оригинального файла на компьютере пользователя.

---

# 20. Security

Source не должен автоматически исполняться.

Core не должен:

- выполнять макросы;
- выполнять сценарии;
- открывать встроенные ссылки;
- запускать исполняемые файлы.

Любая активная обработка выполняется исключительно соответствующим Plugin.

---

# 21. Extensibility

Поддержка новых форматов Source осуществляется исключительно посредством Import Plugin.

Core не требует изменения при добавлении нового типа Source.

Plugin может вводить собственные специализированные SourceType без изменения Core.

---

# 22. Performance Requirements

Импорт больших файлов не должен требовать полной загрузки файла в оперативную память, если формат допускает потоковую обработку.

Архитектура должна поддерживать импорт файлов размером в несколько гигабайт.

Контрольная сумма должна вычисляться потоковым способом.

---

# 23. Test Requirements

Должны существовать автоматические тесты, проверяющие:

- импорт нового Source;
- импорт повреждённого файла;
- импорт неподдерживаемого формата;
- повторный импорт;
- проверку неизменяемости;
- проверку контрольной суммы;
- обнаружение повреждений;
- работу с несколькими Source.

---

# 24. Compliance

Любая реализация сущности Source обязана соответствовать настоящему документу.

Изменение модели Source допускается только посредством изменения настоящей спецификации и оформления соответствующего Architecture Decision Record.
=======
Source представляет собой первичный источник данных, импортированный в проект.

Source описывает происхождение информации, но не содержит результатов её обработки.

Source является единственной точкой происхождения пользовательских данных.

Все объекты Document обязаны ссылаться на Source, из которого были созданы.

---

# 2. Responsibilities

Source SHALL отвечать за:

- описание происхождения данных;
- хранение информации об исходном файле;
- хранение контрольных сумм;
- хранение информации об импорте;
- хранение информации о кодировке;
- хранение информации о языке;
- обеспечение воспроизводимости импорта.

---

# 3. Non-Responsibilities

Source SHALL NOT:

- содержать текст документа;
- хранить структуру документа;
- хранить Timeline;
- хранить Fragment;
- хранить результаты генерации;
- хранить Audio;
- выполнять импорт.

Импорт выполняется Import Service.

---

# 4. Ownership

Source принадлежит Project.

```
Project
    │
    └── Sources
            │
            └── Source
```

Source SHALL NOT существовать вне Project.

---

# 5. Identity

Каждый Source обязан иметь неизменяемый Identifier.

Identifier SHALL:

- быть уникальным внутри Project;
- использоваться всеми ссылками;
- сохраняться после сериализации;
- никогда не изменяться.

---

# 6. Metadata

Source содержит следующие обязательные свойства.

| Property | Required | Mutable |
|------------|----------|---------|
| Identifier | Yes | No |
| DisplayName | Yes | Yes |
| OriginalFileName | Yes | No |
| OriginalPath | No | Yes |
| ImportDateUtc | Yes | No |
| FileSize | Yes | No |
| Checksum | Yes | No |
| Encoding | Yes | No |
| Language | Yes | Yes |
| ImporterId | Yes | No |
| ImporterVersion | Yes | No |
| SourceType | Yes | No |

---

# 7. SourceType

Допустимые типы источников.

- PlainText
- Markdown
- EPUB
- FB2
- DOCX
- PDF
- HTML
- WebPage
- Clipboard
- Subtitle
- Plugin

Добавление новых типов SHALL сохранять обратную совместимость.

---

# 8. Import Information

Source обязан хранить информацию об импорте.

Минимальный состав:

- Importer Identifier;
- Importer Version;
- Import Timestamp;
- Original Encoding;
- Import Options;
- Warnings;
- Errors.

Эта информация используется для повторного импорта.

---

# 9. Original Resource

Source MAY ссылаться на исходный ресурс.

Допустимые варианты:

- локальный файл;
- URL;
- Plugin Resource;
- Clipboard;
- Generated Resource.

Отсутствие исходного ресурса не делает Source некорректным.

---

# 10. Checksum

Каждый Source SHALL содержать контрольную сумму.

Checksum используется для:

- обнаружения изменений;
- проверки целостности;
- повторного импорта;
- обнаружения дубликатов.

Алгоритм вычисления определяется Infrastructure.

---

# 11. Relationships

Source имеет следующие отношения.

```
Project
    │
    └── Source
            │
            └──────► Document
```

Один Source MAY использоваться несколькими Document.

Каждый Document SHALL ссылаться ровно на один Source.

---

# 12. Lifecycle

```
Imported

↓

Validated

↓

Indexed

↓

Referenced

↓

Archived
```

Удаление Source допускается только при отсутствии связанных Document.

---

# 13. State Rules

Imported

- объект создан;
- импорт завершён.

Validated

- проверена структура;
- определён язык;
- определена кодировка.

Indexed

- построен поисковый индекс.

Referenced

- существует хотя бы один Document.

Archived

- источник больше не используется.

---

# 14. Invariants

Source SHALL удовлетворять следующим требованиям.

- Identifier существует.
- ImportDate существует.
- Checksum существует.
- SourceType определён.
- Importer определён.
- Размер файла не отрицателен.
- Кодировка определена.
- Language определён.
- Все ссылки корректны.

---

# 15. Creation Rules

Source создаётся исключительно Import Service.

Во время создания SHALL быть выполнены:

- генерация Identifier;
- вычисление Checksum;
- определение Encoding;
- определение Language;
- заполнение Import Metadata;
- публикация события SourceImported.

---

# 16. Modification Rules

Допускается изменение только следующих полей.

- DisplayName;
- Language;
- OriginalPath.

Все остальные свойства являются неизменяемыми.

---

# 17. Deletion Rules

Source MAY быть удалён только если:

- отсутствуют связанные Document;
- отсутствуют активные Workflow;
- отсутствуют блокировки.

Удаление SHALL публиковать событие SourceDeleted.

---

# 18. Persistence

Source сериализуется как часть Project.

Source не знает:

- файловую систему;
- JSON;
- SQLite;
- ZIP;
- XML.

---

# 19. Concurrency

Допускается:

- конкурентное чтение.

Не допускается:

- конкурентное изменение;
- частичное обновление.

---

# 20. Domain Events

Source публикует:

- SourceImported
- SourceValidated
- SourceUpdated
- SourceArchived
- SourceDeleted

---

# 21. Commands

Допустимые команды.

- ImportSource
- RenameSource
- ValidateSource
- ArchiveSource
- DeleteSource

---

# 22. Extension Rules

Plugin MAY:

- добавлять собственные Import Metadata;
- реализовывать новые SourceType;
- реализовывать новые Importer.

Plugin SHALL NOT:

- изменять обязательные свойства;
- нарушать инварианты;
- изменять Identifier.

---

# 23. AI Implementation Requirements

Реализация SHALL гарантировать:

- неизменяемость происхождения данных;
- воспроизводимость импорта;
- отсутствие потери Import Metadata;
- сохранение ссылочной целостности;
- детерминированную сериализацию.

---

# 24. Test Requirements

Обязательные тесты.

- импорт Source;
- повторный импорт;
- проверка Checksum;
- проверка уникальности Identifier;
- проверка инвариантов;
- сериализация;
- десериализация;
- удаление;
- публикация Domain Events;
- создание нескольких Document из одного Source.

---

# 25. Compliance Checklist

Реализация соответствует настоящему документу только если:

- Source принадлежит Project;
- происхождение данных неизменно;
- Import Metadata полностью сохраняются;
- реализованы все обязательные события;
- реализованы все команды;
- соблюдены все инварианты;
- отсутствуют скрытые зависимости;
- отсутствует доступ к Infrastructure;
- сериализация полностью воспроизводима;
- реализованы все обязательные тесты.
>>>>>>> c975edf (t)

---

End of Document