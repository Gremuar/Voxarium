# Voxarium Software Architecture Specification

Document Path:
spec/300_Contracts/IVoiceService.md

Document ID: CTR-004

Title: IVoiceService

Version: 1.0.0

Status: Accepted

Classification: Normative

Depends On

- CTR-000 IService
- VoiceProfile
- Role
- Emotion
- PronunciationDictionary
- GenerationPreset

Referenced By

- Voice_Service
- Generation_Service
- Workflow_Engine
- User_Interface_Architecture

---

# 1. Purpose

IVoiceService определяет публичный контракт управления голосовыми профилями и их назначением ролям проекта.

Контракт отвечает исключительно за конфигурацию голосов.

Фактическая генерация речи данным контрактом не выполняется.

---

# 2. Responsibilities

Контракт SHALL обеспечивать:

- управление VoiceProfile;
- назначение голосов ролям;
- управление словарями произношений;
- управление настройками эмоций;
- проверку совместимости конфигурации.

---

# 3. Non-Responsibilities

Контракт SHALL NOT:

- выполнять генерацию речи;
- выполнять клонирование голоса;
- выполнять инференс моделей;
- управлять AudioTrack;
- изменять Timeline.

---

# 4. Lifecycle Operations

## 4.1 CreateVoiceProfile

### Signature

CreateVoiceProfile(ProjectId, Name)

### Purpose

Создает новый VoiceProfile.

### Parameters

- ProjectId
- Name

### Returns

- VoiceProfile

### Preconditions

- Project существует.
- Имя уникально.

### Postconditions

- Создан новый VoiceProfile.

### Published Events

- VoiceProfileCreated

### Exceptions

- ProjectNotFound
- DuplicateVoiceProfile

---

## 4.2 DeleteVoiceProfile

### Signature

DeleteVoiceProfile(VoiceProfileId)

### Purpose

Удаляет VoiceProfile.

### Preconditions

- VoiceProfile существует.
- Профиль не используется активной генерацией.

### Postconditions

- VoiceProfile удален.

### Published Events

- VoiceProfileDeleted

### Exceptions

- VoiceProfileNotFound
- VoiceProfileInUse

---

## 4.3 UpdateVoiceProfile

### Signature

UpdateVoiceProfile(VoiceProfile)

### Purpose

Изменяет параметры VoiceProfile.

### Published Events

- VoiceProfileUpdated

---

# 5. Assignment Operations

## 5.1 AssignVoiceToRole

### Signature

AssignVoiceToRole(RoleId, VoiceProfileId)

### Purpose

Назначает VoiceProfile выбранной роли.

### Preconditions

- Role существует.
- VoiceProfile существует.

### Postconditions

- Role использует указанный VoiceProfile.

### Published Events

- VoiceAssignedToRole

---

## 5.2 RemoveVoiceAssignment

### Signature

RemoveVoiceAssignment(RoleId)

### Purpose

Удаляет назначение голоса роли.

### Published Events

- VoiceAssignmentRemoved

---

# 6. Pronunciation Operations

Контракт SHALL предоставлять операции:

- AttachPronunciationDictionary
- DetachPronunciationDictionary
- ValidatePronunciationDictionary

---

# 7. Emotion Operations

Контракт SHALL предоставлять операции:

- AssignEmotion
- RemoveEmotion
- ValidateEmotionConfiguration

---

# 8. Validation Operations

Контракт SHALL предоставлять:

- ValidateVoiceProfile
- ValidateAssignments
- ValidateGenerationCompatibility

---

# 9. Query Operations

Контракт SHALL предоставлять:

- GetVoiceProfile
- GetVoiceProfiles
- GetAssignedVoice
- GetVoiceStatistics
- FindVoiceProfiles

Query SHALL NOT изменять состояние системы.

---

# 10. Transaction Rules

Все операции изменения SHALL выполняться в пределах одной прикладной транзакции.

---

# 11. Thread Safety

Операции чтения допускается выполнять параллельно.

Изменение одного VoiceProfile SHALL сериализоваться.

---

# 12. Dependencies

Контракт SHALL зависеть только от Domain Model и IService.

---

# 13. AI Implementation Rules

Реализация SHALL:

- не выполнять генерацию речи;
- не обращаться напрямую к AI Runtime;
- использовать Aggregate Root VoiceProfile;
- публиковать события после успешного завершения транзакции.

---

# 14. Test Requirements

Для каждой операции SHALL существовать:

- позитивный сценарий;
- негативный сценарий;
- проверка Preconditions;
- проверка Postconditions;
- проверка публикации событий.

---

# 15. Compliance Checklist

Контракт соответствует настоящей спецификации только если:

- управляет исключительно конфигурацией голосов;
- не выполняет генерацию речи;
- поддерживает назначение ролям;
- поддерживает словари произношений;
- поддерживает настройки эмоций;
- соответствует IService.

---

End of Document