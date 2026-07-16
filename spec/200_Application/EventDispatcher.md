# EventDispatcher

**Document Path:**
`spec/200_Application/EventDispatcher.md`

**Document ID:** APP-009

**Version:** 1.0.0

**Status:** Draft

**Classification:** Normative

---

# 1. Purpose

This document defines the **EventDispatcher** architectural component of the Voxarium platform.

An EventDispatcher is responsible for delivering Domain Events to their registered handlers after successful completion of an application transaction. It provides a centralized event distribution mechanism while preserving loose coupling between application components.

The EventDispatcher coordinates event delivery but SHALL NOT implement business behavior.

---

# 2. Scope

This specification defines:

* responsibilities;
* event dispatching lifecycle;
* dependency rules;
* ordering guarantees;
* delivery semantics.

Event transport technologies, messaging infrastructure, and broker implementations are outside the scope of this specification.

---

# 3. Definition

An **EventDispatcher** is an Application Layer component responsible for dispatching Domain Events to interested subscribers.

Event dispatching SHALL occur only after successful transaction completion.

---

# 4. Responsibilities

EventDispatcher SHALL be responsible for:

* receiving published Domain Events;
* determining subscribed handlers;
* dispatching events;
* preserving event ordering;
* reporting dispatch failures;
* preventing duplicate delivery within the same dispatch operation.

EventDispatcher SHALL NOT:

* generate Domain Events;
* execute business rules;
* modify Aggregates;
* manage transaction boundaries.

---

# 5. Dependencies

EventDispatcher MAY depend upon:

* DomainEvent abstractions;
* EventHandler interfaces;
* EventPublisher interfaces;
* logging abstractions.

EventDispatcher SHALL NOT depend directly upon:

* message brokers;
* database implementations;
* HTTP frameworks;
* GUI frameworks.

---

# 6. Dispatch Lifecycle

Event dispatch SHOULD follow this sequence:

1. receive committed Domain Events;
2. resolve subscribed handlers;
3. dispatch events;
4. collect handler results;
5. report dispatch outcome.

Dispatch SHALL begin only after transaction commitment.

---

# 7. Event Ordering

For events produced within a single transaction:

* publication order SHALL be preserved;
* handlers SHALL receive events in deterministic order.

Ordering guarantees across independent transactions are implementation-dependent.

---

# 8. Delivery Semantics

Each registered handler SHOULD receive every applicable event exactly once within a single dispatch operation.

Duplicate dispatches SHALL be prevented whenever possible.

---

# 9. Error Handling

EventDispatcher SHALL:

* detect handler failures;
* isolate failing handlers where appropriate;
* report dispatch errors;
* preserve application stability.

Handler failures SHALL NOT invalidate an already committed transaction.

---

# 10. Handler Resolution

EventDispatcher SHALL dispatch events only to compatible EventHandlers.

Handler discovery MAY be:

* static;
* dependency-injection based;
* registry-based.

The resolution mechanism SHALL remain transparent to callers.

---

# 11. Thread Safety

EventDispatcher implementations SHOULD support concurrent event processing where ordering guarantees are preserved.

Internal mutable state SHOULD be minimized.

---

# 12. Compliance

All EventDispatcher implementations within Voxarium SHALL conform to this specification.

Implementations SHALL preserve deterministic dispatch, architectural decoupling, transaction safety, and dependency inversion.

---

# 13. References

* DomainEvent.md
* EventHandler.md
* EventPublisher.md
* TransactionCoordinator.md
* ApplicationService.md
* CommandHandler.md
* UnitOfWork.md

---

**End of Document**
