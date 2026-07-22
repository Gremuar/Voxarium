# ApplicationContext

**Document Path:**
`spec/200_Application/ApplicationContext.md`

**Document ID:** APP-036

**Version:** 1.0.0

**Status:** Draft

**Classification:** Normative

---

# 1. Purpose

This document defines the **ApplicationContext** abstraction of the Voxarium Application Layer.

ApplicationContext represents the execution context of a single Application operation. It provides a unified container for execution-scoped information required during Use Case execution while remaining independent of Infrastructure and Presentation implementations.

ApplicationContext SHALL exist only for the lifetime of a single logical operation.

---

# 2. Scope

This specification defines:

* responsibilities;
* lifecycle;
* contained information;
* propagation rules;
* dependency rules.

Persistence, authentication providers, dependency injection containers, and transport protocols are outside the scope of this specification.

---

# 3. Definition

ApplicationContext is an immutable execution-scoped object shared between Application components participating in a single operation.

The context SHALL provide access to execution metadata without introducing coupling between services.

---

# 4. Responsibilities

ApplicationContext SHALL be responsible for providing:

* operation identifier;
* execution timestamp;
* cancellation information;
* locale information;
* current project identifier where applicable;
* correlation identifier;
* user/session identifier where available;
* arbitrary execution metadata.

ApplicationContext SHALL NOT:

* contain Domain entities;
* contain Infrastructure services;
* expose Repository implementations;
* perform business logic.

---

# 5. Lifecycle

An ApplicationContext SHALL be:

1. created at the beginning of an Application operation;
2. propagated through Application services;
3. available during the complete execution flow;
4. destroyed after operation completion.

Contexts SHALL NOT be reused between independent operations.

---

# 6. Immutability

ApplicationContext SHOULD be immutable.

When modifications are required, a new context instance SHOULD be created rather than mutating an existing instance.

Implementations SHALL avoid shared mutable state.

---

# 7. Context Propagation

ApplicationContext SHALL be propagated through:

* Use Cases;
* Application Services;
* Command Handlers;
* Query Handlers;
* Event Handlers where applicable.

Propagation SHALL remain transparent to Domain objects.

---

# 8. Stored Information

Typical information MAY include:

* OperationId;
* CorrelationId;
* RequestId;
* Timestamp;
* Locale;
* ProjectId;
* UserId;
* SessionId;
* CancellationToken;
* custom execution metadata.

Implementations MAY extend the context while preserving backward compatibility.

---

# 9. Error Handling

ApplicationContext SHALL remain available during exception handling.

Errors SHALL NOT corrupt or invalidate the execution context.

Context disposal SHALL occur regardless of successful or failed execution.

---

# 10. Thread Safety

ApplicationContext SHOULD be immutable and therefore inherently thread-safe.

Concurrent readers SHALL observe identical state throughout operation execution.

---

# 11. Compliance

All Application workflows within Voxarium SHALL execute within an ApplicationContext or an equivalent abstraction conforming to this specification.

Implementations SHALL preserve immutability, deterministic propagation, dependency inversion, execution isolation, and architectural independence from Infrastructure and Presentation layers.

---

# 12. References

* ApplicationService.md
* UseCase.md
* CommandHandler.md
* QueryHandler.md
* EventHandler.md
* CommandBus.md

---

**End of Document**
