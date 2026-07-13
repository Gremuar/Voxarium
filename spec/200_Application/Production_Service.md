# Voxarium Software Architecture Specification

Document Path:
spec/200_Application/Production_Service.md

Document ID: APP-031

Title: Production Service

Version: 1.0.0

Status: Accepted

Classification: Normative

Depends On

- SAS-003 Architecture Principles
- SAS-006 Common Domain Patterns
- Project
- Production
- Timeline
- AudioTrack
- Workflow

Referenced By

- Generation_Service
- Audio_Service
- Export_Service
- Timeline_Service
- Workflow_Engine

---

# 1. Purpose

Production Service является прикладным сервисом, управляющим жизненным циклом Production.

Сервис отвечает за формирование готового материала, предназначенного для последующего прослушивания, проверки или экспорта.

Production Service не выполняет генерацию речи, обработку аудио и экспорт.

---

# 2. Responsibilities

Production Service SHALL:

- создавать Production;
- удалять Production;
- изменять свойства Production;
- управлять составом Production;
- синхронизировать Production с Timeline;
- отслеживать актуальность Production;
- публиковать события приложения.

---

# 3. Non-Responsibilities

Production Service SHALL NOT:

- выполнять генерацию речи;
- выполнять микширование;
- выполнять экспорт;
- воспроизводить аудио;
- изменять Document;
- изменять SpeechSegment.

---

# 4. Public Operations

Production Service предоставляет следующие операции.

- CreateProduction
- DeleteProduction
- RenameProduction
- DuplicateProduction
- RebuildProduction
- SynchronizeProduction
- ValidateProduction

---

# 5. Production Composition

Production SHALL состоять из упорядоченного набора элементов.

Элемент Production может ссылаться на:

- Timeline;
- AudioTrack;
- Asset.

Production Service определяет порядок этих элементов.

---

# 6. Synchronization

Production Service SHALL отслеживать изменения:

- Timeline;
- AudioTrack;
- Workflow.

При обнаружении изменений состояние Production должно быть пересчитано.

---

# 7. State Model

Production SHALL поддерживать состояния:

- Draft;
- Ready;
- Outdated;
- Building;
- Valid;
- Invalid.

Изменение состояния производится только сервисом.

---

# 8. Validation

Перед переводом в состояние Ready SHALL проверяться:

- наличие всех AudioTrack;
- отсутствие поврежденных ссылок;
- корректность структуры Timeline;
- отсутствие конфликтов Workflow.

---

# 9. Rebuild

Rebuild SHALL:

- повторно вычислять состав Production;
- сохранять Identifier;
- увеличивать Revision;
- публиковать событие ProductionRebuilt.

---

# 10. Event Publication

Production Service публикует:

- ProductionCreated;
- ProductionDeleted;
- ProductionUpdated;
- ProductionRebuilt;
- ProductionValidated;
- ProductionStateChanged.

---

# 11. Dependencies

Production Service MAY использовать:

- Timeline Service;
- Workflow Engine;
- Event Bus;
- Query Bus.

Production Service SHALL NOT зависеть от:

- GUI;
- Playback Service;
- AI Runtime;
- Storage.

---

# 12. Error Handling

Поддерживаются категории ошибок:

- MissingTimeline;
- MissingAudioTrack;
- InvalidWorkflow;
- ValidationError;
- InternalError.

Ошибки SHALL возвращаться вызывающему компоненту.

---

# 13. Concurrency

Все изменения SHALL выполняться через Aggregate Root Production.

При конкурентных изменениях используется механизм Revision.

---

# 14. AI Implementation Rules

Реализация SHALL:

- не изменять Timeline напрямую;
- не изменять AudioTrack;
- использовать Domain Events;
- быть независимой от способа хранения проекта.

---

# 15. Test Requirements

Обязательные тесты.

- создание Production;
- удаление Production;
- перестроение;
- синхронизация;
- проверка состояний;
- публикация событий;
- проверка конкурентных изменений.

---

# 16. Compliance Checklist

Production Service соответствует настоящей спецификации только если:

- является единственной точкой изменения Production;
- не зависит от GUI;
- не зависит от AI Runtime;
- публикует события;
- поддерживает пересборку;
- обеспечивает синхронизацию с Timeline;
- соблюдает правила Domain.

---

End of Document