# Repository Structure

**Document Path:**
`spec/000_Foundation/Repository_Structure.md`

**Document ID:** FOUND-013

**Version:** 1.0.0

**Status:** Draft

**Classification:** Normative

---

# 1. Purpose

This document defines the canonical directory structure of the Voxarium repository.

Its purpose is to establish a stable organization for source code, architecture documentation, project resources, testing infrastructure, tooling, and build artifacts.

Every file within the repository SHALL belong to a clearly defined architectural area.

---

# 2. Scope

This specification applies to:

* source code;
* architecture documentation;
* project resources;
* plugins;
* tests;
* build scripts;
* development tools;
* generated artifacts.

---

# 3. Design Principles

The repository SHALL satisfy the following principles:

* predictable organization;
* separation of concerns;
* minimal coupling between directories;
* scalability;
* discoverability;
* deterministic structure.

Directory names SHALL remain stable over time.

---

# 4. Top-Level Repository Layout

The repository SHOULD follow the conceptual structure below.

```text
/
├── docs/
├── spec/
├── src/
├── plugins/
├── resources/
├── tests/
├── tools/
├── scripts/
├── examples/
├── build/
├── dist/
└── README.md
```

Additional top-level directories SHALL require architectural review.

---

# 5. Specification Directory

The `spec/` directory contains the complete architectural specification.

Its internal organization SHALL follow the approved documentation index.

```text
spec/
├── 000_Foundation/
├── 100_Domain/
├── 200_Application/
├── 300_Contracts/
├── 400_Commands/
├── 500_Events/
├── 600_Project_Format/
├── 700_Plugins/
├── 800_GUI/
├── 900_Testing/
└── 999_ADR/
```

No specification document SHALL exist outside this hierarchy.

---

# 6. Source Code Directory

The `src/` directory contains the production implementation.

Its internal organization SHOULD reflect the architectural layers defined in the specification.

Implementation-specific subdivision MAY evolve independently of the specification, provided architectural boundaries remain intact.

---

# 7. Plugin Directory

The `plugins/` directory contains installable plugins and related resources.

Each plugin SHALL reside in its own directory.

Plugins SHALL NOT modify files outside their own directory except through documented extension mechanisms.

---

# 8. Resources Directory

The `resources/` directory stores static assets used by the application.

Examples include:

* icons;
* themes;
* translations;
* templates;
* embedded media.

Generated resources SHALL be clearly distinguished from manually maintained assets.

---

# 9. Test Directory

The `tests/` directory contains automated tests.

Test organization SHOULD mirror the production code structure whenever practical.

Test utilities MAY be placed in dedicated shared directories.

Production code SHALL NOT depend upon test code.

---

# 10. Documentation Directory

The `docs/` directory contains non-normative documentation.

Examples include:

* user manuals;
* tutorials;
* migration guides;
* release notes;
* contributor documentation.

Architecture specifications SHALL remain exclusively within `spec/`.

---

# 11. Tools Directory

The `tools/` directory contains developer utilities.

Examples include:

* code generators;
* validation tools;
* migration utilities;
* diagnostic applications.

Tools SHALL remain independent from production runtime whenever practical.

---

# 12. Scripts Directory

The `scripts/` directory contains automation scripts supporting development and maintenance.

Examples include:

* build scripts;
* formatting scripts;
* packaging scripts;
* continuous integration helpers.

Scripts SHALL avoid embedding business logic.

---

# 13. Build Artifacts

Generated output SHALL reside outside manually maintained source directories.

Typical locations include:

* `build/`
* `dist/`

Generated artifacts SHALL NOT be committed unless explicitly required.

---

# 14. Naming Rules

Repository directories SHALL:

* use descriptive names;
* avoid abbreviations where possible;
* remain stable across releases.

Directory names SHALL correspond to architectural responsibilities.

---

# 15. Ownership

Every directory SHALL have a clearly defined responsibility.

Files SHALL belong to exactly one architectural area.

Cross-directory ownership is prohibited.

---

# 16. Dependency Direction

Repository organization SHALL reinforce architectural dependencies.

Physical directory layout SHALL NOT encourage violations of the architectural layering defined elsewhere in the specification.

---

# 17. Evolution

Repository restructuring SHALL:

* preserve repository integrity;
* minimize disruption;
* maintain architectural clarity.

Major restructuring SHALL require an Architecture Decision Record.

---

# 18. Compliance

Every file added to the repository SHALL have an appropriate location consistent with this specification.

Architecture reviews SHALL verify compliance with the repository structure.

---

# 19. References

* Documentation_Index.md
* Architecture_Principles.md
* Layered_Architecture.md
* Component_Model.md
* Naming_Conventions.md
* 999_ADR/

---

**End of Document**
