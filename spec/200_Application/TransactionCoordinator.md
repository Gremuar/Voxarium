# TransactionCoordinator

**Document Path:**
`spec/200_Application/TransactionCoordinator.md`

**Document ID:** APP-008

**Version:** 1.0.0

**Status:** Draft

**Classification:** Normative

---

# 1. Purpose

This document defines the **TransactionCoordinator** architectural component of the Voxarium platform.

A TransactionCoordinator is responsible for establishing, controlling, and completing transactional boundaries for application use cases. It ensures that modifications to Domain Aggregates are committed atomically and that Domain Events are published only after successful transaction completion.

The TransactionCoordinator manages transaction lifecycle but SHALL NOT contain business logic.

---

# 2. Scope

This specification defines:

* responsibilities;
* transaction lifecycle;
* dependency rules;
* interaction with Application Services;
* interaction with Repository interfaces.

Database-specific transaction implementations are outside the scope of this specification.

---

# 3. Definition

A **TransactionCoordinator** is an Application Layer component responsible for managing transactional execution of application use cases.

Each transaction SHALL represent one logical business operation.

---

# 4. Responsibilities

TransactionCoordinator SHALL be responsible for:

* beginning transactions;
* committing transactions;
* rolling back failed transactions;
* coordinating Repository consistency;
* coordinating post-commit event publication;
* ensuring atomic execution.

TransactionCoordinator SHALL NOT:

* execute business rules;
* validate requests;
* load Aggregates directly;
* access infrastructure-specific APIs.

---

# 5. Dependencies

TransactionCoordinator MAY depend upon:

* transaction abstractions;
* Repository interfaces;
* Event Publisher interfaces;
* Unit of Work abstractions.

TransactionCoordinator SHALL NOT depend directly upon:

* SQL implementations;
* ORM frameworks;
* filesystem implementations;
* HTTP frameworks;
* GUI frameworks.

---

# 6. Transaction Lifecycle

A transaction SHOULD follow this lifecycle:

1. begin transaction;
2. execute application workflow;
3. persist Aggregate changes;
4. commit transaction;
5. publish Domain Events.

If any step fails before commit, the transaction SHALL be rolled back.

---

# 7. Atomicity

A TransactionCoordinator SHALL guarantee:

* all modifications succeed together; or
* all modifications are discarded.

Partial commits SHALL NOT occur.

---

# 8. Aggregate Consistency

Multiple Aggregates MAY participate in a single transaction.

Aggregate invariants SHALL remain the responsibility of the Domain Layer.

The TransactionCoordinator SHALL preserve consistency across all modified Aggregates.

---

# 9. Event Publication

Domain Events SHALL be published only after successful transaction commitment.

If commit fails:

* no Domain Events SHALL be published;
* application state SHALL remain unchanged.

---

# 10. Error Handling

TransactionCoordinator SHALL:

* detect transaction failures;
* perform rollback;
* report transactional errors;
* preserve application consistency.

Rollback operations SHOULD be idempotent whenever supported by the underlying infrastructure.

---

# 11. Thread Safety

Each transaction SHALL belong to exactly one execution context.

TransactionCoordinator implementations SHOULD remain stateless outside the active transaction scope.

---

# 12. Compliance

All TransactionCoordinator implementations within Voxarium SHALL conform to this specification.

Implementations SHALL preserve atomicity, consistency, deterministic transaction behavior, dependency inversion, and separation of concerns.

---

# 13. References

* ApplicationService.md
* CommandHandler.md
* Repository.md
* UnitOfWork.md
* DomainEvent.md
* Aggregate.md
* ValidationJob.md

---

**End of Document**
