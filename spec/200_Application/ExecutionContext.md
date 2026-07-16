# ExecutionContext

**Document Path:**
`spec/200_Application/ExecutionContext.md`

**Document ID:** APP-012

**Version:** 1.0.0

**Status:** Draft

**Classification:** Normative

---

# 1. Purpose

This document defines the **ExecutionContext** architectural component of the Voxarium platform.

An ExecutionContext represents the immutable runtime context associated with a single application operation. It carries execution-specific metadata required by the Application Layer while remaining independent of infrastructure implementations.

ExecutionContext SHALL describe the execution environment but SHALL NOT contain business state.

---

# 2. Scope

This specification defines:

* responsibilities;
* lifecycle;
* dependency rules;
* execution boundaries;
* interaction with Application components.

Authentication systems, transport protocols, and infrastructure-specific context propagation are outside the scope of this specification.

---

# 3. Definition

An **ExecutionContext** is an immutable object describing the runtime environment of a single UseCase execution.

Each application operation SHALL execute within exactly one ExecutionContext.

---

# 4. Responsibilities

ExecutionContext SHALL be responsible for:

* identifying the current execution;
* exposing execution metadata;
* providing request correlation;
* exposing execution timestamps;
* carrying application-scoped contextual information.

ExecutionContext SHALL NOT:

* contain Domain entities;
* modify business state;
* manage transactions;
* execute business logic.

---

# 5. Context Information

ExecutionContext MAY include:

* execution identifier;
* correlation identifier;
* request identifier;
* creation timestamp;
* initiating actor identifier;
* locale;
* timezone;
* cancellation token;
* execution metadata.

The exact representation SHALL remain implementation independent.

---

# 6. Lifecycle

The lifecycle SHALL consist of:

1. creation;
2. propagation through the Application Layer;
3. use during execution;
4. disposal after operation completion.

ExecutionContext SHALL NOT outlive the associated application operation.

---

# 7. Dependencies

ExecutionContext MAY depend upon:

* primitive types;
* Value Objects;
* application abstractions.

ExecutionContext SHALL NOT depend upon:

* Repository implementations;
* Application Services;
* Domain Aggregates;
* Infrastructure frameworks.

---

# 8. Propagation

ExecutionContext SHOULD be propagated explicitly between Application components.

Hidden global context mechanisms SHOULD be avoided.

Application components SHALL receive the ExecutionContext through dependency injection or explicit parameters.

---

# 9. Immutability

ExecutionContext SHALL be immutable.

After creation:

* identifiers SHALL remain unchanged;
* metadata SHALL remain unchanged;
* execution properties SHALL remain unchanged.

---

# 10. Thread Safety

Because ExecutionContext is immutable, it SHALL be inherently thread-safe.

Concurrent readers SHALL observe identical state throughout the execution lifetime.

---

# 11. Error Handling

ExecutionContext SHALL remain valid even when application execution fails.

Failure information SHALL be represented separately from the ExecutionContext.

---

# 12. Compliance

All Application Layer operations within Voxarium SHALL execute within an ExecutionContext conforming to this specification.

Implementations SHALL preserve immutability, deterministic propagation, execution isolation, and architectural independence.

---

# 13. References

* UseCase.md
* ApplicationService.md
* CommandHandler.md
* QueryHandler.md
* TransactionCoordinator.md
* OperationResult.md
* ApplicationDTO.md

---

**End of Document**
