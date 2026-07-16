# AuthorizationContext

**Document Path:**
`spec/200_Application/AuthorizationContext.md`

**Document ID:** APP-024

**Version:** 1.0.0

**Status:** Draft

**Classification:** Normative

---

# 1. Purpose

This document defines the **AuthorizationContext** abstraction of the Voxarium platform.

An AuthorizationContext represents the immutable authorization information associated with an application execution. It provides the Application Layer with the information required to perform authorization decisions while remaining independent of authentication providers, transport protocols, and infrastructure implementations.

AuthorizationContext SHALL describe authorization state only.

---

# 2. Scope

This specification defines:

* responsibilities;
* lifecycle;
* dependency rules;
* interaction with Application components;
* authorization metadata.

Authentication mechanisms, identity providers, access token formats, and security infrastructure are outside the scope of this specification.

---

# 3. Definition

An **AuthorizationContext** is an immutable Application Layer object representing the permissions and authorization attributes available during a single application execution.

AuthorizationContext SHALL exist independently of any specific authentication technology.

---

# 4. Responsibilities

AuthorizationContext SHALL be responsible for:

* exposing the current principal identity;
* exposing granted permissions;
* exposing assigned roles;
* exposing authorization metadata;
* supporting deterministic authorization decisions.

AuthorizationContext SHALL NOT:

* authenticate users;
* validate credentials;
* access identity providers;
* execute business logic.

---

# 5. Context Information

AuthorizationContext MAY include:

* principal identifier;
* assigned roles;
* granted permissions;
* authentication method identifier;
* tenant identifier;
* security claims;
* authorization timestamp;
* additional authorization metadata.

The representation SHALL remain implementation independent.

---

# 6. Lifecycle

The lifecycle SHALL consist of:

1. creation;
2. validation;
3. propagation through the Application Layer;
4. disposal after request completion.

AuthorizationContext SHALL remain immutable throughout its lifetime.

---

# 7. Dependencies

AuthorizationContext MAY depend upon:

* primitive types;
* Value Objects;
* authorization abstractions.

AuthorizationContext SHALL NOT depend upon:

* Repository implementations;
* Domain Aggregates;
* GUI frameworks;
* database implementations;
* identity provider SDKs.

---

# 8. Authorization Decisions

Application components MAY consult AuthorizationContext before executing protected operations.

Authorization decisions SHOULD be deterministic for identical context information.

Business authorization rules SHALL remain separate from authentication mechanisms.

---

# 9. Relationship with RequestContext

A RequestContext describes the incoming application request.

An AuthorizationContext describes the security characteristics associated with that request.

Both contexts MAY coexist during a single application execution while remaining independent.

---

# 10. Error Handling

Authorization failures SHOULD result in standardized application-level failures.

AuthorizationContext SHALL remain unchanged even when authorization is denied.

Authorization errors SHALL NOT expose sensitive security information.

---

# 11. Thread Safety

AuthorizationContext SHALL be immutable.

Immutable implementations SHALL be inherently thread-safe.

Concurrent readers SHALL observe identical authorization information.

---

# 12. Compliance

All authorization-aware application operations within Voxarium SHALL use an AuthorizationContext conforming to this specification.

Implementations SHALL preserve immutability, deterministic authorization behavior, dependency inversion, transport independence, and complete separation from authentication infrastructure.

---

# 13. References

* RequestContext.md
* ExecutionContext.md
* ApplicationPipeline.md
* PipelineBehavior.md
* ApplicationException.md
* OperationResult.md
* UseCase.md

---

**End of Document**
