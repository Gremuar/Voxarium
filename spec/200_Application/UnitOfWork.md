# UnitOfWork

**Document Path:**
`spec/200_Application/UnitOfWork.md`

**Document ID:** APP-013

**Version:** 1.0.0

**Status:** Draft

**Classification:** Normative

---

# 1. Purpose

This document defines the **UnitOfWork** architectural component of the Voxarium platform.

A UnitOfWork coordinates changes made to Domain Aggregates during a single application operation. It tracks modified objects, ensures atomic persistence, and provides a consistent mechanism for committing or rolling back changes.

The UnitOfWork SHALL coordinate persistence but SHALL NOT implement business logic.

---

# 2. Scope

This specification defines:

* responsibilities;
* lifecycle;
* dependency rules;
* interaction with Repositories;
* interaction with TransactionCoordinator.

Persistence technology, ORM implementations, and database engines are outside the scope of this specification.

---

# 3. Definition

A **UnitOfWork** is an Application Layer component representing a single persistence session associated with one business transaction.

Each write UseCase SHOULD execute within one UnitOfWork.

---

# 4. Responsibilities

UnitOfWork SHALL be responsible for:

* tracking modified Aggregates;
* tracking newly created Aggregates;
* tracking removed Aggregates;
* coordinating Repository persistence;
* committing changes atomically;
* rolling back incomplete operations.

UnitOfWork SHALL NOT:

* execute business rules;
* validate requests;
* perform query optimization;
* expose infrastructure-specific APIs.

---

# 5. Dependencies

UnitOfWork MAY depend upon:

* Repository interfaces;
* Transaction abstractions;
* Domain Aggregates;
* Domain Events;
* TransactionCoordinator.

UnitOfWork SHALL NOT depend directly upon:

* SQL implementations;
* filesystem implementations;
* HTTP frameworks;
* GUI frameworks;
* speech synthesis providers.

---

# 6. Lifecycle

The lifecycle SHOULD follow this sequence:

1. create UnitOfWork;
2. register Aggregate changes;
3. begin transaction;
4. persist changes;
5. commit transaction;
6. publish Domain Events;
7. dispose UnitOfWork.

If persistence fails, rollback SHALL occur before disposal.

---

# 7. Change Tracking

UnitOfWork SHALL track:

* created objects;
* modified objects;
* deleted objects.

Each Aggregate SHALL appear only once within a single tracking session.

---

# 8. Repository Coordination

Repositories SHALL interact with persistence exclusively through the active UnitOfWork.

Repositories SHALL NOT commit transactions independently.

---

# 9. Transaction Integration

UnitOfWork SHALL cooperate with TransactionCoordinator.

TransactionCoordinator SHALL determine:

* transaction boundaries;
* commit timing;
* rollback behavior.

UnitOfWork SHALL execute persistence operations within those boundaries.

---

# 10. Event Collection

Domain Events produced during Aggregate execution SHOULD be accumulated by the UnitOfWork.

Collected events SHALL be forwarded to the EventDispatcher only after successful transaction commitment.

---

# 11. Error Handling

UnitOfWork SHALL:

* detect persistence failures;
* abort incomplete commits;
* perform rollback when required;
* leave Domain state consistent.

Partial persistence SHALL NOT occur.

---

# 12. Thread Safety

A UnitOfWork SHALL belong to exactly one execution context.

UnitOfWork instances SHALL NOT be shared across concurrent operations.

---

# 13. Compliance

All UnitOfWork implementations within Voxarium SHALL conform to this specification.

Implementations SHALL preserve atomic persistence, deterministic change tracking, transactional consistency, dependency inversion, and separation of concerns.

---

# 14. References

* TransactionCoordinator.md
* Repository.md
* ApplicationService.md
* CommandHandler.md
* EventDispatcher.md
* Aggregate.md
* DomainEvent.md
* ExecutionContext.md

---

**End of Document**
