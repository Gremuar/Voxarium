# Voxarium Software Architecture Specification

Document Path:
spec/100_Domain/AudioTrack.md

Document ID: DOM-015

Title: AudioTrack

Version: 1.0.0

Status: Accepted

Classification: Normative

Depends On

- SAS-000 Project Philosophy
- SAS-001 Glossary
- SAS-002 Domain Ontology
- SAS-003 Architecture Principles
- SpeechSegment
- ProductionItem

Referenced By

- Audio_Service
- Playback_Module
- Export_Service
- Production

---

# 1. Purpose

AudioTrack представляет собой логическое представление результата генерации речи.

AudioTrack связывает SpeechSegment с физическим аудиоресурсом, но не содержит сам аудиофайл.

AudioTrack является объектом предметной области.

---

# 2. Responsibilities

AudioTrack SHALL отвечать за:

- идентификацию результата генерации;
- связь со SpeechSegment;
- хранение логического состояния аудио;
- хранение технических характеристик результата;
- обеспечение ссылочной целостности.

---

# 3. Non-Responsibilities

AudioTrack SHALL NOT:

- хранить аудиоданные;
- хранить путь к файлу;
- хранить URI;
- выполнять воспроизведение;
- выполнять микширование;
- выполнять экспорт;
- выполнять обработку аудио.

---

# 4. Ownership

AudioTrack принадлежит Project.

```
Project
    │
    └── AudioTracks
            │
            └── AudioTrack
```

---

# 5. Identity

Каждый AudioTrack имеет неизменяемый Identifier.

Identifier SHALL:

- быть уникальным внутри Project;
- сохраняться при сериализации;
- никогда не изменяться.

---

# 6. Relationships

AudioTrack обязан ссылаться на один SpeechSegment.

Один SpeechSegment MAY иметь несколько AudioTrack.

Это позволяет хранить несколько вариантов генерации одного и того же сегмента.

---

# 7. Metadata

| Property | Required | Mutable |
|----------|----------|---------|
| Identifier | Yes | No |
| SpeechSegmentId | Yes | No |
| Version | Yes | Yes |
| Status | Yes | Yes |
| Duration | No | Yes |
| SampleRate | No | Yes |
| Channels | No | Yes |
| Revision | Yes | Yes |

---

# 8. Status

Поддерживаются следующие состояния.

- Pending
- Available
- Invalid
- Missing
- Archived

AudioTrack SHALL находиться только в одном состоянии.

---

# 9. Version

Version определяет порядковый номер результата генерации.

Каждая повторная генерация создает новый AudioTrack.

Предыдущие версии могут сохраняться.

Удаление старых версий определяется политикой хранения.

---

# 10. Audio Metadata

AudioTrack MAY содержать:

- продолжительность;
- частоту дискретизации;
- количество каналов;
- формат PCM.

Данные являются описательными.

Физический файл остается частью Infrastructure Layer.

---

# 11. Lifecycle

```
Created

↓

Generating

↓

Available

↓

Archived
```

При ошибке допускается переход.

```
Generating

↓

Invalid
```

---

# 12. Invariants

AudioTrack SHALL удовлетворять следующим требованиям.

- Identifier существует.
- SpeechSegment существует.
- Revision ≥ 1.
- Status определен.

---

# 13. Creation Rules

После успешной генерации SHALL:

- создать новый AudioTrack;
- присвоить новый Identifier;
- установить Version;
- опубликовать AudioTrackCreated.

---

# 14. Modification Rules

Допускается изменение:

- Status;
- технических метаданных.

Изменение SpeechSegment запрещено.

---

# 15. Persistence

AudioTrack сериализуется как часть Project.

AudioTrack SHALL NOT знать:

- путь файла;
- файловую систему;
- Blob Storage;
- Object Storage;
- формат контейнера.

---

# 16. Concurrency

Поддерживается конкурентное чтение.

Конкурентная запись запрещена.

---

# 17. Domain Events

AudioTrack публикует:

- AudioTrackCreated
- AudioTrackAvailable
- AudioTrackInvalidated
- AudioTrackArchived
- AudioTrackDeleted

---

# 18. Commands

Поддерживаются команды.

- RegisterAudioTrack
- ArchiveAudioTrack
- DeleteAudioTrack
- ValidateAudioTrack

---

# 19. AI Implementation Requirements

AudioTrack SHALL описывать исключительно логический результат генерации.

Реализация SHALL NOT хранить:

- WAV;
- MP3;
- FLAC;
- путь к файлу;
- FFmpeg;
- параметры кодека.

Все физические данные принадлежат Infrastructure Layer.

---

# 20. Test Requirements

Минимальный набор тестов.

- создание AudioTrack;
- повторная генерация;
- создание нескольких версий;
- сериализация;
- десериализация;
- проверка инвариантов;
- проверка публикации событий.

---

# 21. Compliance Checklist

Реализация соответствует настоящей спецификации только если:

- AudioTrack принадлежит Project;
- связан с одним SpeechSegment;
- не содержит аудиофайла;
- не зависит от файловой системы;
- реализованы все события;
- реализованы все команды;
- соблюдены все инварианты;
- сериализация полностью воспроизводима.

---

End of Document