# Voxarium Software Architecture Specification

Document Path:
spec/300_Contracts/IGenerationService.md

Document ID: CTR-005

Title: IGenerationService

Version: 1.0.0

Status: Accepted

Classification: Normative

Depends On

- CTR-000 IService
- Project
- Production
- Timeline
- SpeechSegment
- VoiceProfile
- GenerationPreset
- Job

Referenced By

- Generation_Service
- Workflow_Engine
- Job_Orchestrator
- User_Interface_Architecture

---

# 1. Purpose

IGenerationService определяет публичный контракт запуска, управления и мониторинга процессов генерации речи.

Контракт является единственной точкой входа для операций генерации на уровне Application Layer.

---

# 2. Responsibilities

Контракт SHALL обеспечивать:

- запуск генерации;
- запуск пакетной генерации;
- повторную генерацию;
- отмену генерации;
- получение состояния генерации;
- получение результатов генерации.

---

# 3. Non-Responsibilities

Контракт SHALL NOT:

- выполнять инференс моделей;
- управлять GPU;
- выполнять воспроизведение;
- выполнять экспорт;
- управлять очередями выполнения.

---

# 4. Lifecycle Operations

## 4.1 GenerateSegment

### Signature

GenerateSegment(SpeechSegmentId, GenerationPresetId)

### Purpose

Запускает генерацию одного SpeechSegment.

### Parameters

- SpeechSegmentId
- GenerationPresetId

### Returns

- Job

### Preconditions

- SpeechSegment существует.
- VoiceProfile назначен.
- GenerationPreset существует.

### Postconditions

- Создан новый Job.
- Job поставлен в очередь выполнения.

### Published Events

- GenerationRequested

### Exceptions

- SpeechSegmentNotFound
- MissingVoiceProfile
- InvalidGenerationPreset

---

## 4.2 GenerateSelection

### Signature

GenerateSelection(SegmentIds, GenerationPresetId)

### Purpose

Запускает генерацию выбранного набора сегментов.

### Returns

- Job

### Published Events

- GenerationRequested

---

## 4.3 GenerateDocument

### Signature

GenerateDocument(DocumentId, GenerationPresetId)

### Purpose

Запускает генерацию всего документа.

### Returns

- Job

---

## 4.4 GenerateProduction

### Signature

GenerateProduction(ProductionId)

### Purpose

Запускает генерацию Production.

### Returns

- Job

---

## 4.5 RetryGeneration

### Signature

RetryGeneration(JobId)

### Purpose

Повторно запускает завершившуюся неудачей генерацию.

### Returns

- Job

### Published Events

- GenerationRetryRequested

---

## 4.6 CancelGeneration

### Signature

CancelGeneration(JobId)

### Purpose

Отменяет выполняющуюся генерацию.

### Returns

Нет.

### Published Events

- GenerationCancellationRequested

---

# 5. Query Operations

Контракт SHALL предоставлять:

- GetJob
- GetGenerationStatus
- GetGenerationProgress
- GetGenerationResult
- ListActiveJobs
- ListCompletedJobs

Запросы SHALL NOT изменять состояние системы.

---

# 6. Progress Reporting

Контракт SHALL обеспечивать получение информации о ходе выполнения генерации.

Минимальный набор данных:

- состояние Job;
- процент выполнения;
- текущий этап;
- предполагаемое оставшееся время (если доступно).

---

# 7. Result Model

После успешного завершения генерации SHALL быть доступен результат, содержащий:

- идентификатор Job;
- созданные AudioTrack;
- время выполнения;
- диагностическую информацию.

---

# 8. Transaction Rules

Создание Job SHALL выполняться атомарно.

Фактическое выполнение генерации может происходить вне границ транзакции.

---

# 9. Thread Safety

Контракт SHALL поддерживать параллельный запуск нескольких независимых Job.

---

# 10. Dependencies

Контракт SHALL зависеть только от:

- Domain Model;
- IService.

Контракт SHALL NOT зависеть от:

- GUI;
- AI Runtime;
- Infrastructure.

---

# 11. AI Implementation Rules

Реализация SHALL:

- создавать Job для каждой операции генерации;
- не выполнять синхронный инференс внутри публичных методов;
- обеспечивать возможность отмены длительных операций;
- публиковать события после изменения состояния Job.

---

# 12. Test Requirements

Для каждой операции SHALL существовать тесты:

- успешный запуск;
- отмена;
- повторный запуск;
- получение состояния;
- получение результата;
- обработка ошибочных параметров.

---

# 13. Compliance Checklist

Контракт соответствует настоящей спецификации только если:

- предоставляет единый API запуска генерации;
- не зависит от конкретного AI Engine;
- поддерживает мониторинг выполнения;
- поддерживает отмену операций;
- использует Job как единицу выполнения;
- соответствует IService.

---

End of Document