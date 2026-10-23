# Ecological Information umbrella instructions

Read README.md, ARCHITECTURE.md and REORGANISATION.json before changing domain documentation.

- This repository contains domain coordination material and historical migration records.
- EIRKB, EII, GISDS, OSDS, AMRKB and PBCKA are independent sibling repositories at different research/publication stages. Read their own instructions before explicitly authorised project work.
- Do not duplicate authoritative research documents, registers, datasets or databases in this umbrella.
- Preserve issued identifiers, academic attribution, provenance and distinctions between evidence, inference and project interpretation.
- Keep existing capabilities separate from proposed databases, integrations and knowledge graphs.
- Preserve REORGANISATION.json unchanged. Its paths are relative to the original ecological-information organisational directory.
- Keep documentation portable; do not invent publication URLs or add filesystem-relative links to sibling repositories.
- Cross-project changes require explicit scope. Preserve Git history and avoid submodules, subtrees and unnecessary shared dependencies.
- Do not select licences, configure remotes or publish without explicit approval.

## Diagram maintenance

- The authoritative editable source is assets/diagrams/federated_knowledge_systems.mmd. Labels, conceptual relationships, colours, status styles and fixed-layout hints belong there.
- Regenerate assets/diagrams/federated_knowledge_systems.svg with `python3 assets/diagrams/render_federated_knowledge_systems.py`. The renderer is adapted from the OSDS diagram-specific Mermaid-subset renderer, not a general Mermaid implementation. Never independently edit the SVG.
- Keep the historical federated-knowledge-systems.png byte-for-byte unchanged. Approximate sampled fills and their meanings are documented in ARCHITECTURE.md: blue synthesis, lavender DRM/federation, green research knowledge bases, amber scientific/geographic/observational sources, grey emerging applications.
- PBCKA remains unclassified until its research scope is approved. Dashed database-card borders denote developing components; solid card borders denote published research, not scientific validation. Preserve database autonomy and the conceptual-status qualification.
- Do not treat EIRKB HA/IL/IM classifications as federation-wide schemes or introduce operational data-flow claims. Do not copy OSDS's eight-category detail into the umbrella illustration.
- Keep README image paths repository-relative. Website allowlisting, source pin updates and deployment require a separate task; do not modify the website or other research repositories during Overview work.
- Validate deterministic SVG regeneration, readable layout, internal links and scoped Git changes. Keep technical maintenance instructions here rather than in the introductory narrative.
