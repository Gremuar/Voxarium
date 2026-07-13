# Voxarium Software Architecture Specification

Document Path:
spec/100_Domain/Asset.md

<<<<<<< HEAD
Document ID: DOM-109

Title: Asset

Version: 1.0.0
=======
Document ID: DOM-010

Title: Asset

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

- Source.md
- VoiceProfile.md
- SpeechSegment.md
- Export_Module.md
- Asset_Manager.md
- Project_Format.md
=======
- SAS-000 Project Philosophy
- SAS-001 Glossary
- SAS-002 Domain Ontology
- SAS-003 Architecture Principles
- Project

Referenced By

- VoiceProfile
- Workflow
- Production
- Audio_Service
- Export_Service
- Plugin_Runtime
>>>>>>> c975edf (t)

---

# 1. Purpose

<<<<<<< HEAD
Asset представляет собой универсальное описание любого бинарного ресурса, принадлежащего Project.

Asset является единственным способом хранения файлов внутри проекта.

Ни одна доменная сущность не должна обращаться к файлам напрямую.

Все ссылки на физические данные выполняются исключительно через Asset.

---

# 2. Responsibility

Asset отвечает исключительно за:

- идентификацию файла;
- хранение информации о файле;
- проверку целостности;
- управление версиями ресурсов;
- связь между предметной моделью и файловым хранилищем.

Asset не отвечает за:

- обработку содержимого;
- генерацию данных;
- интерпретацию формата;
- кэширование.

---

# 3. Aggregate

Asset является самостоятельным агрегатом.

Asset принадлежит одному Project.

Asset может использоваться несколькими сущностями одновременно.

---

# 4. Business Motivation

Использование единой модели Asset позволяет:

- избежать дублирования файлов;
- выполнять дедупликацию;
- контролировать целостность;
- заменить физическое расположение файлов без изменения предметной модели;
- реализовать переносимые проекты.
=======
Asset представляет собой логический ресурс проекта.

Asset описывает наличие ресурса, его назначение и принадлежность проекту.

Asset не определяет способ хранения ресурса.

Asset не содержит содержимое ресурса.

Asset является Domain Entity.

---

# 2. Responsibilities

Asset SHALL отвечать за:

- идентификацию ресурса;
- описание назначения ресурса;
- хранение логического типа ресурса;
- хранение пользовательских метаданных;
- хранение состояния ресурса;
- обеспечение ссылочной целостности.

---

# 3. Non-Responsibilities

Asset SHALL NOT:

- хранить бинарные данные;
- хранить путь к файлу;
- хранить URI;
- знать расположение ресурса;
- выполнять загрузку;
- выполнять сохранение;
- выполнять обработку.

Все операции над физическими ресурсами принадлежат Infrastructure Layer.

---

# 4. Ownership

Asset принадлежит Project.

```
Project
    │
    └── Assets
            │
            └── Asset
```

Asset SHALL NOT существовать вне Project.
>>>>>>> c975edf (t)

---

# 5. Identity

<<<<<<< HEAD
Каждый Asset обладает постоянным UUID v7.

UUID никогда не изменяется.

---

# 6. Required Attributes

| Name | Type | Required | Mutable |
|------|------|----------|----------|
| id | UUIDv7 | Yes | No |
| assetType | AssetType | Yes | No |
| checksum | SHA-256 | Yes | No |
| size | UInt64 | Yes | No |
| storagePath | RelativePath | Yes | No |
| createdAt | UTC DateTime | Yes | No |

---

# 7. Optional Attributes

| Name | Type |
|------|------|
| originalFilename | String |
| mimeType | String |
| compression | CompressionType |
| encryption | EncryptionType |
| metadata | Map<String, Value> |

---

# 8. Asset Types

Минимально поддерживаются:

- Audio
- Image
- Voice Model
- Embedding
- Lexicon
- Subtitle
- Temporary File
- Export File
- Cache File
- Plugin Resource
- User Resource
- Binary Blob

Plugin могут регистрировать собственные типы.

---

# 9. Physical Storage

Asset не содержит бинарных данных.

Asset содержит только описание.

Физическое хранение определяется Storage Layer.

Core не знает расположения файлов.

---

# 10. Content Addressing

Контрольная сумма является обязательной.

Основной алгоритм:

SHA-256

Контрольная сумма используется для:

- проверки целостности;
- дедупликации;
- обнаружения повреждений.

---

# 11. Deduplication

Если два Asset имеют одинаковую контрольную сумму, Storage Layer может использовать один физический файл.

Предметная модель не должна зависеть от способа хранения.

Удаление одного Asset не должно приводить к удалению физического файла, пока существуют другие ссылки.

---

# 12. Reference Counting

Storage Layer обязан поддерживать механизм подсчёта ссылок.

Физическое удаление ресурса допускается только после удаления последней ссылки.

---

# 13. Relationship with Domain

Следующие сущности могут ссылаться на Asset:

- Source
- VoiceProfile
- SpeechSegment
- Export
- Plugin Data

Asset не содержит обратных ссылок.

---

# 14. Commands

RegisterAsset

ImportAsset

ValidateAsset

ArchiveAsset

DeleteAsset

RestoreAsset

---

# 15. Domain Events

AssetRegistered

AssetImported

AssetValidated

AssetDeleted

AssetRestored

AssetCorrupted

---

# 16. Validation

При регистрации проверяются:

- существование файла;
- контрольная сумма;
- размер;
- корректность типа;
- отсутствие повреждений.

---

# 17. Recovery

При восстановлении проекта должна выполняться повторная проверка всех Asset.

Отсутствующий Asset не должен приводить к повреждению всей модели.

Зависимые сущности переводятся в состояние Missing Resource.

---

# 18. Performance Requirements

Проверка контрольных сумм должна выполняться потоковым способом.

Работа с большими файлами должна исключать их полную загрузку в память.

Storage Layer обязан поддерживать ленивое открытие файлов.

---

# 19. Security

Core запрещается автоматически выполнять содержимое Asset.

Все бинарные данные рассматриваются как недоверенные.

Plugin получают доступ к Asset только через публичные интерфейсы.

---

# 20. Extensibility

Storage Layer может использовать:

- локальную файловую систему;
- ZIP-контейнер;
- объектное хранилище;
- облачное хранилище;
- распределённое хранилище.

Предметная модель не должна зависеть от выбранного способа хранения.

---

# 21. Test Requirements

Должны существовать автоматические тесты, проверяющие:

- регистрацию Asset;
- дедупликацию;
- проверку контрольной суммы;
- обнаружение повреждений;
- удаление;
- восстановление;
- работу нескольких ссылок на один ресурс;
- проверку ссылочной целостности.

---

# 22. Future Compatibility

Архитектура должна поддерживать:

- прозрачное сжатие;
- шифрование;
- внешние хранилища;
- облачные репозитории;
- потоковое хранение;
- CDN для удалённых ресурсов.

Настоящий документ определяет только логическую модель.

---

# 23. Compliance

Любая реализация Asset обязана соответствовать требованиям настоящего документа.

Изменение модели Asset допускается исключительно посредством изменения настоящей спецификации и оформления соответствующего Architecture Decision Record.
=======
Каждый Asset обязан иметь неизменяемый Identifier.

Identifier SHALL:

- быть уникальным внутри Project;
- использоваться всеми ссылками;
- сохраняться после сериализации;
- никогда не изменяться.

---

# 6. Metadata

Asset содержит следующие свойства.

| Property | Required | Mutable |
|----------|----------|---------|
| Identifier | Yes | No |
| Name | Yes | Yes |
| Type | Yes | No |
| Description | No | Yes |
| Status | Yes | Yes |
| Tags | No | Yes |
| Revision | Yes | Yes |
| CreatedUtc | Yes | No |
| ModifiedUtc | Yes | Yes |

---

# 7. Asset Type

Поддерживаются следующие логические типы.

- Audio
- VoiceSample
- Image
- Cover
- Music
- SoundEffect
- PronunciationDictionary
- Subtitle
- PluginResource
- UserData
- Temporary

Plugin MAY регистрировать дополнительные типы.

Тип определяет исключительно назначение ресурса.

---

# 8. Asset Status

Поддерживаются состояния.

- Registered
- Available
- Missing
- Invalid
- Archived

Asset SHALL находиться только в одном состоянии.

---

# 9. Relationships

Asset MAY использоваться:

- VoiceProfile;
- Production;
- Workflow;
- Plugin.

Asset никем не владеет.

Asset не владеет другими объектами.

---

# 10. Resource Reference

Asset SHALL хранить только логическую ссылку на ресурс.

Физическое расположение определяется Infrastructure.

Domain SHALL NOT зависеть:

- от файловой системы;
- от URL;
- от облачного хранилища;
- от базы данных.

---

# 11. Lifecycle

```
Registered

↓

Available

↓

InUse

↓

Archived
```

При отсутствии физического ресурса допускается состояние:

```
Available

↓

Missing
```

---

# 12. Invariants

Asset SHALL удовлетворять следующим требованиям.

- Identifier существует.
- Name существует.
- Name не пустой.
- Type определён.
- Status определён.
- Revision ≥ 1.

---

# 13. Creation Rules

Asset создаётся через Project Service либо соответствующий Application Service.

Во время создания SHALL:

- создать Identifier;
- установить Status = Registered;
- установить Revision = 1;
- опубликовать AssetRegistered.

---

# 14. Modification Rules

Допускается изменение.

- Name;
- Description;
- Tags;
- Status.

Изменение Type запрещено.

Изменение Identifier запрещено.

Любое изменение SHALL публиковать AssetModified.

---

# 15. Deletion Rules

Asset MAY быть удалён только если отсутствуют ссылки со стороны других Domain Entity.

При наличии зависимостей удаление SHALL завершаться ошибкой.

Рекомендуется перевод в состояние Archived.

---

# 16. Persistence

Asset сериализуется как часть Project.

Asset SHALL NOT знать:

- файловую систему;
- формат хранения;
- способ загрузки;
- облачное хранилище;
- Runtime.

---

# 17. Concurrency

Поддерживается:

- конкурентное чтение.

Не допускается:

- конкурентная запись.

---

# 18. Domain Events

Asset публикует:

- AssetRegistered
- AssetModified
- AssetAvailable
- AssetMissing
- AssetArchived
- AssetDeleted

---

# 19. Commands

Поддерживаются команды.

- RegisterAsset
- UpdateAsset
- ArchiveAsset
- DeleteAsset
- ValidateAsset

---

# 20. Usage Rules

Asset может использоваться несколькими объектами одновременно.

Удаление Asset SHALL NOT выполнять автоматическое удаление зависимых объектов.

Проверка зависимостей выполняется Application Layer.

---

# 21. Extension Rules

Plugin MAY:

- регистрировать новые Asset Type;
- добавлять пользовательские свойства;
- хранить дополнительные метаданные.

Plugin SHALL NOT:

- изменять обязательные свойства;
- изменять Identifier;
- нарушать модель владения.

---

# 22. AI Implementation Requirements

Asset SHALL оставаться полностью независимым от способа хранения ресурсов.

Реализация SHALL NOT содержать:

- абсолютные пути;
- относительные пути;
- URL;
- сетевые протоколы;
- параметры облачного хранения.

Все подобные сведения принадлежат Infrastructure Layer.

---

# 23. Test Requirements

Минимальный набор тестов.

- регистрация Asset;
- изменение имени;
- изменение статуса;
- архивирование;
- удаление;
- сериализация;
- десериализация;
- проверка инвариантов;
- проверка публикации событий.

---

# 24. Compliance Checklist

Реализация соответствует настоящей спецификации только если:

- Asset принадлежит Project;
- Identifier неизменяем;
- отсутствует зависимость от файловой системы;
- отсутствует способ хранения;
- отсутствует скрытое состояние;
- реализованы все события;
- реализованы все команды;
- соблюдены все инварианты;
- сериализация полностью воспроизводима.
>>>>>>> c975edf (t)

---

End of Document