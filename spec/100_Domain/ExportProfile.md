# Voxarium Software Architecture Specification

Document Path:
spec/100_Domain/ExportProfile.md

Document ID: DOM-013

Title: ExportProfile

Version: 1.0.0

Status: Accepted

Classification: Normative

Depends On

- SAS-000 Project Philosophy
- SAS-001 Glossary
- SAS-003 Architecture Principles
- Project

Referenced By

- Production
- Export_Service

---

# 1. Purpose

ExportProfile представляет собой именованный набор правил экспорта итогового произведения.

ExportProfile определяет требования к результату экспорта, но не определяет способ реализации конкретного экспортного движка.

ExportProfile является объектом предметной области.

---

# 2. Responsibilities

ExportProfile SHALL отвечать за:

- описание формата итогового результата;
- описание структуры выходных файлов;
- описание политики именования;
- описание требований к качеству;
- хранение пользовательских настроек;
- обеспечение воспроизводимости экспорта.

---

# 3. Non-Responsibilities

ExportProfile SHALL NOT:

- выполнять экспорт;
- хранить путь назначения;
- знать файловую систему;
- знать кодеки;
- выполнять кодирование;
- выполнять запись файлов.

---

# 4. Ownership

ExportProfile принадлежит Project.

```
Project
    │
    └── ExportProfiles
            │
            └── ExportProfile
```

---

# 5. Identity

Каждый ExportProfile имеет неизменяемый Identifier.

Identifier SHALL:

- быть уникальным внутри Project;
- сохраняться при сериализации;
- никогда не изменяться.

---

# 6. Metadata

| Property | Required | Mutable |
|----------|----------|---------|
| Identifier | Yes | No |
| Name | Yes | Yes |
| Description | No | Yes |
| Category | No | Yes |
| Revision | Yes | Yes |
| CreatedUtc | Yes | No |
| ModifiedUtc | Yes | Yes |

---

# 7. Export Rules

ExportProfile MAY определять следующие логические правила.

- Single Output
- Multiple Files
- Chapter Split
- Preserve Document Order
- Include Metadata
- Include Cover
- Include Chapter Markers
- Normalize Audio
- Generate Manifest

Правила являются декларативными.

---

# 8. Output Format

ExportProfile определяет логический формат результата.

Например:

- Audiobook
- Podcast
- Voice Pack
- Archive
- Raw Audio Set

Domain не определяет расширения файлов.

---

# 9. Naming Policy

ExportProfile MAY определять политику именования.

Примеры.

- By Document Name
- By Chapter Number
- Sequential
- Custom Template

Интерпретация шаблонов принадлежит Export Service.

---

# 10. Relationships

ExportProfile MAY использоваться:

- Production;
- Workflow.

ExportProfile никем не владеет.

---

# 11. Lifecycle

```
Created

↓

Active

↓

Archived
```

---

# 12. Invariants

ExportProfile SHALL удовлетворять следующим требованиям.

- Identifier существует.
- Name существует.
- Revision ≥ 1.

---

# 13. Creation Rules

При создании SHALL:

- создать Identifier;
- установить Revision = 1;
- опубликовать ExportProfileCreated.

---

# 14. Modification Rules

Любое изменение SHALL:

- увеличивать Revision;
- публиковать ExportProfileModified.

---

# 15. Deletion Rules

Удаление допускается только если отсутствуют ссылки со стороны Production.

При наличии ссылок рекомендуется архивирование.

---

# 16. Persistence

ExportProfile сериализуется как часть Project.

ExportProfile SHALL NOT знать:

- файловую систему;
- кодеки;
- контейнеры;
- путь назначения;
- Runtime.

---

# 17. Concurrency

Поддерживается конкурентное чтение.

Конкурентная запись запрещена.

---

# 18. Domain Events

ExportProfile публикует:

- ExportProfileCreated
- ExportProfileModified
- ExportProfileArchived
- ExportProfileDeleted

---

# 19. Commands

Поддерживаются команды.

- CreateExportProfile
- UpdateExportProfile
- ArchiveExportProfile
- DeleteExportProfile

---

# 20. AI Implementation Requirements

ExportProfile SHALL описывать исключительно пользовательские намерения.

Реализация SHALL NOT содержать:

- MP3;
- FLAC;
- WAV;
- AAC;
- Opus;
- FFmpeg;
- параметры кодеков.

Все подобные сведения принадлежат Infrastructure Layer.

---

# 21. Test Requirements

Минимальный набор тестов.

- создание;
- изменение;
- сериализация;
- десериализация;
- проверка инвариантов;
- проверка событий.

---

# 22. Compliance Checklist

Реализация соответствует настоящей спецификации только если:

- ExportProfile принадлежит Project;
- Identifier неизменяем;
- отсутствует зависимость от файловой системы;
- отсутствует зависимость от кодеков;
- реализованы все события;
- реализованы все команды;
- соблюдены все инварианты;
- сериализация полностью воспроизводима.

---

End of Document