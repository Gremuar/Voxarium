# Voxarium Software Architecture Specification

Document Path:
spec/100_Domain/Asset.md

Document ID: DOM-109

Title: Asset

Version: 1.0.0

Status: Accepted

Classification: Normative

Depends On

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

---

# 1. Purpose

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

---

# 5. Identity

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

---

End of Document