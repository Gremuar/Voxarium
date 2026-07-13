# Voxarium Software Architecture Specification

Document Path:
spec/000_Foundation/SAS-008_Document_Template.md

Document ID: SAS-008

Title: Architecture Document Template

Version: 1.0.0

Status: Accepted

Classification: Normative

---

# 1. Purpose

Настоящий документ определяет обязательную структуру архитектурных документов спецификации Voxarium.

Все документы SHALL соответствовать настоящему шаблону, если иное не определено отдельной нормативной спецификацией.

---

# 2. Goals

Шаблон обеспечивает:

- единообразную структуру документации;
- возможность автоматической обработки документации;
- однозначную интерпретацию ИИ-агентами;
- упрощение сопровождения;
- снижение дублирования.

---

# 3. Document Categories

Допускаются следующие категории документов.

- Foundation
- Domain
- Module
- Contract
- Command
- Query
- Event
- Project Format
- Plugin
- GUI
- Testing
- ADR

Каждая категория MAY использовать специализированные разделы.

---

# 4. Mandatory Header

Каждый документ SHALL содержать следующий заголовок.

```
Title

Document Path

Document ID

Version

Status

Classification

Depends On

Referenced By
```

Поля SHALL быть заполнены.

---

# 5. Required Sections

Документ SHOULD содержать следующие разделы.

```
Purpose

Responsibilities

Non-Responsibilities

Relationships

Lifecycle

Invariants

Commands

Events

Persistence

Concurrency

Extension Rules

Implementation Notes

Test Requirements

Compliance Checklist
```

Допускается исключение разделов, не применимых к конкретному типу документа.

---

# 6. Section Ordering

Разделы SHALL располагаться в следующем порядке.

```
Header

Purpose

Responsibilities

Non-Responsibilities

Structure

Relationships

Lifecycle

Rules

Persistence

Events

Commands

Implementation

Testing

Compliance
```

Нарушение порядка допускается только при наличии обоснования.

---

# 7. Language Rules

Нормативные требования SHALL использовать RFC 2119 терминологию.

Допускаются только следующие ключевые слова.

- SHALL
- SHALL NOT
- SHOULD
- SHOULD NOT
- MAY

Использование разговорных форм запрещено.

---

# 8. Cross References

Все документы SHOULD ссылаться только на Document ID.

Например.

```
Depends On

DOM-004
DOM-012
SAS-003
```

Использование имен документов допускается только для повышения читаемости.

---

# 9. Diagrams

Диаграммы SHALL использовать только ASCII.

Допускаются:

- деревья;
- DAG;
- конечные автоматы;
- последовательности;
- агрегаты.

Использование изображений запрещено.

---

# 10. Tables

Таблицы SHALL использовать Markdown.

Допускаются только простые таблицы.

Сложные объединения ячеек запрещены.

---

# 11. Examples

Документы MAY содержать примеры.

Пример SHALL быть явно помечен как ненормативный.

Нормативные требования не должны зависеть от примеров.

---

# 12. Extension Rules

Расширения документации SHALL:

- сохранять структуру шаблона;
- не изменять обязательные разделы;
- использовать собственные Document ID.

---

# 13. Versioning

Каждый документ обязан иметь Version.

Изменение SHALL сопровождаться:

- увеличением версии;
- обновлением списка зависимостей при необходимости.

---

# 14. AI Readability

Документы SHALL быть ориентированы на автоматический анализ.

Следует избегать:

- неоднозначных формулировок;
- скрытых предположений;
- ссылок вида "см. выше";
- неявных зависимостей.

---

# 15. Compliance Checklist

Архитектурный документ соответствует настоящему шаблону только если:

- содержит обязательный заголовок;
- использует единую терминологию;
- содержит нормативные требования;
- имеет явные зависимости;
- имеет проверяемые требования;
- допускает автоматическую обработку.

---

End of Document