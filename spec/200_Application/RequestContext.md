# RequestContext

**Document Path:**
`spec/200_Application/RequestContext.md`

**Document ID:** APP-020

**Version:** 1.0.0

**Status:** Draft

**Classification:** Normative

---

# 1. Purpose

This document defines the **RequestContext** architectural component of the Voxarium platform.

A RequestContext represents immutable information associated with a single incoming application request. It carries request-specific metadata required during request processing while remaining independent of transport protocols and infrastructure implementations.

RequestContext SHALL describe the request environment but SHALL NOT contain Domain state.

---

# 2. Scope

This specification defines:

* responsibilities;
* lifecycle;
* dependency rules;
* interaction with ExecutionContext;
* request metadata.

Authentication providers, HTTP frameworks, RPC protocols, and transport-specific implementations are outside the scope of this specification.

---

# 3. Definition

A **RequestContext** is an immutable Application Layer object describing a single incoming request.

Every request entering the Application Layer SHOULD have exactly one RequestContext.

---

# 4. Responsibilities

RequestContext SHALL be responsible for:

* identifying the request;
* exposing request metadata;
* carrying localization settings;
* exposing correlation information;
* supporting request tracing.

RequestContext SHALL NOT:

* execute business logic;
* contain Domain entities;
* manage transactions;
* expose infrastructure implementations.

---

# 5. Context Information

A RequestContext MAY contain:

* request identifier;
* correlation identifier;
* client identifier;
* user identifier;
* request timestamp;
* locale;
* timezone;
* preferred language;
* request metadata.

The exact representation SHALL remain implementation independent.

---

# 6. Lifecycle

The lifecycle SHALL consist of:

1. request creation;
2. validation;
3. propagation through the Application Layer;
4. disposal after request completion.

A RequestContext SHALL exist only for the duration of one request.

---

# 7. Dependencies

RequestContext MAY depend upon:

* primitive types;
* Value Objects;
* application abstractions.

RequestContext SHALL NOT depend upon:

* Repository implementations;
* Domain Aggregates;
* GUI frameworks;
* database implementations.

---

# 8. Relationship with ExecutionContext

A RequestContext SHALL describe the incoming request.

An ExecutionContext SHALL describe the execution of a UseCase.

A single RequestContext MAY produce one or more ExecutionContexts if multiple independent UseCases are executed.

---

# 9. Immutability

RequestContext SHALL be immutable.

After creation:

* identifiers SHALL remain unchanged;
* metadata SHALL remain unchanged;
* localization settings SHALL remain unchanged.

---

# 10. Error Handling

RequestContext SHALL remain available throughout request processing, including failure scenarios.

Application errors SHALL NOT modify RequestContext contents.

---

# 11. Thread Safety

Because RequestContext is immutable, it SHALL be inherently thread-safe.

Concurrent readers SHALL observe identical state.

---

# 12. Compliance

All requests processed by Voxarium SHALL use a RequestContext conforming to this specification.

Implementations SHALL preserve immutability, deterministic propagation, request isolation, dependency inversion, and architectural independence.

---

# 13. References

* ExecutionContext.md
* ApplicationPipeline.md
* PipelineBehavior.md
* ApplicationService.md
* CommandHandler.md
* QueryHandler.md
* OperationResult.md

---

**End of Document**
