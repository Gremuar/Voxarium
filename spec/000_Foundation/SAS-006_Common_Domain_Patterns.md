# Voxarium Software Architecture Specification

Document Path:
spec/000_Foundation/SAS-006_Common_Domain_Patterns.md

Document ID: SAS-006

Title: Common Domain Patterns

Version: 1.0.0

Status: Accepted

Classification: Normative

---

# 1. Purpose

Настоящий документ определяет базовые шаблоны Domain Model, обязательные для использования всеми сущностями системы Voxarium.

Ни один Domain Document не должен повторно определять описанные здесь концепции.

---

# 2. Entity

Entity представляет собой объект предметной области, обладающий собственной идентичностью.

Entity SHALL:

- иметь Identifier;
- иметь жизненный цикл;
- обладать собственной идентичностью независимо от состояния.

Entity SHALL NOT сравниваться по значениям всех полей.

Entity сравнивается исключительно по Identifier.

---

# 3. Aggregate Root

Aggregate Root представляет единственную точку изменения агрегата.

Только Aggregate Root имеет право:

- создавать дочерние Entity;
- удалять дочерние Entity;
- изменять состав агрегата;
- публиковать Aggregate Events.

Все остальные Entity изменяются исключительно через Aggregate Root.

---

# 4. Value Object

Value Object представляет неизменяемое значение.

Value Object SHALL:

- быть immutable;
- сравниваться по значениям;
- не иметь Identifier.

Изменение Value Object выполняется созданием нового экземпляра.

---

# 5. Identifier

Каждая Entity обязана иметь Identifier.

Identifier SHALL:

- быть глобально уникальным;
- быть неизменяемым;
- использоваться во всех ссылках;
- сохраняться после сериализации.

Identifier никогда не переиспользуется.

---

# 6. Revision

Каждая изменяемая Entity обязана содержать Revision.

Revision SHALL:

- начинаться с 1;
- увеличиваться при каждом изменении;
- использоваться для optimistic concurrency.

Revision никогда не уменьшается.

---

# 7. Audit Metadata

Изменяемые Entity SHOULD содержать:

- CreatedUtc;
- ModifiedUtc.

Immutable Entity MAY содержать только:

- CreatedUtc.

Audit Metadata используется исключительно для истории изменений.

---

# 8. Lifecycle

Каждая Entity обязана иметь жизненный цикл.

Lifecycle SHALL быть конечным автоматом.

Все допустимые переходы должны быть явно описаны в документе соответствующей Entity.

Неописанные переходы запрещены.

---

# 9. Status

Status представляет текущее логическое состояние Entity.

Status SHALL:

- принимать одно значение;
- соответствовать Lifecycle;
- изменяться только допустимыми переходами.

---

# 10. Domain Event

Каждая существенная бизнес-операция SHALL публиковать Domain Event.

Domain Event обязан:

- описывать завершившийся факт;
- быть неизменяемым;
- содержать Identifier источника;
- содержать Timestamp.

Domain Event никогда не изменяется после публикации.

---

# 11. Commands

Команда представляет намерение изменить состояние системы.

Command SHALL:

- описывать намерение;
- валидироваться до выполнения;
- приводить либо к изменению состояния, либо к ошибке.

Command не является событием.

---

# 12. Invariants

Каждая Entity обязана определять собственные инварианты.

Инварианты SHALL выполняться:

- после создания;
- после каждой модификации;
- после десериализации.

Нарушение инвариантов делает Entity недействительной.

---

# 13. Ownership

Каждая Entity обязана иметь владельца.

Владелец определяет:

- жизненный цикл;
- сериализацию;
- транзакционные границы.

Entity SHALL NOT иметь нескольких владельцев.

---

# 14. References

Все ссылки между Entity являются логическими.

Entity SHALL хранить только Identifier другой Entity.

Прямые объектные ссылки запрещены.

---

# 15. Serialization

Domain Model сериализуется полностью.

После десериализации SHALL восстанавливаться:

- идентичность;
- инварианты;
- связи;
- Revision.

---

# 16. Immutability

Следующие объекты SHOULD быть immutable:

- Domain Event;
- Value Object;
- GenerationResult;
- Snapshot.

Immutable объекты не изменяются после создания.

---

# 17. Dependency Rule

Domain Layer SHALL NOT зависеть от:

- Application Layer;
- Infrastructure Layer;
- GUI;
- Runtime;
- AI Engine;
- Database;
- Filesystem.

Все зависимости направлены только внутрь Domain.

---

# 18. Thread Safety

Domain Model не отвечает за многопоточность.

Все механизмы синхронизации принадлежат Application Layer.

---

# 19. Extension Rules

Plugin SHALL NOT изменять фундаментальные правила настоящего документа.

Plugin MAY:

- добавлять новые Entity;
- добавлять новые Value Object;
- добавлять новые Domain Event.

---

# 20. Compliance Checklist

Любая Domain Entity соответствует архитектуре Voxarium только если:

- имеет Identifier;
- определён владелец;
- определены инварианты;
- определён жизненный цикл;
- определены Domain Event;
- определены Command;
- определены правила сериализации;
- отсутствует зависимость от Infrastructure;
- отсутствует зависимость от GUI;
- отсутствует зависимость от Runtime.

---

End of Document