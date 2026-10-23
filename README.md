# Ecological Information

![Ecological Information federation: interdisciplinary synthesis, shared methodology, autonomous research databases and emerging applications](assets/diagrams/federated_knowledge_systems.svg)

*Conceptual research architecture; relationships do not necessarily represent completed technical integrations.* [View full-size diagram](assets/diagrams/federated_knowledge_systems.svg).

## Introduction

Ecological Information organises research references, scientific indicators, geographic resources, observational systems and the evidence needed to interpret them. It is the research information and knowledge-base layer of Ecological Interaction, alongside Understanding, Computation, Intelligence, Infrastructure and Generation. Its resources support researchers, designers, students and collaborators working across ecological questions and disciplinary traditions.

These resources answer different questions. Research references explain ideas and methods; indicators describe measurements and qualified interpretations; geographic catalogues identify spatial resources; observation-source catalogues locate monitoring systems and data routes. Keeping these responsibilities distinct makes their relationships easier to examine without treating a provider, an indicator and a verified measurement dataset as interchangeable.

Separate databases allow specialised research to develop while retaining its own definitions and evidence. Federation is the developing framework for connecting that work. The directory distinguishes public reading resources from components whose scope or implementation is still being developed. Publication makes a research edition accessible; it does not establish that every record, classification or data source has been scientifically verified.

## Research database directory

| Database | Research responsibility | Current status | Reading resource | Repository |
|---|---|---|---|---|
| **EIRKB — Ecological Information Research Knowledge Base** | History and theory of ecological information, references and conceptual research. | Published research; classifications remain provisional. | [Research pages](https://ecological-interaction.github.io/information/EIRKB/) | [EIRKB](https://github.com/ecological-interaction/EIRKB) |
| **EII — Ecological Indicator Inventory** | Ecological variables, indicators, measurements and qualified inferences. | Published catalogue of 235 indicators; not a validated monitoring standard. | [Scientific catalogue](https://ecological-interaction.github.io/information/EII/) | [EII](https://github.com/ecological-interaction/EII) |
| **GISDS — GIS and Remote Sensing Database Sources** | Geographic and Earth-observation resources, access routes and interpretation limits. | Published catalogue of 25 resources; product-level review remains necessary. | [Resource catalogue](https://ecological-interaction.github.io/information/GISDS/) | [GISDS](https://github.com/ecological-interaction/GISDS) |
| **OSDS — Observational Systems and Data Sources** | Observation networks, monitoring infrastructure and physical data-source discovery. | Published catalogue of 62 candidate sources, not 62 verified datasets. | [Scientific catalogue](https://ecological-interaction.github.io/information/OSDS/) | [OSDS](https://github.com/ecological-interaction/OSDS) |
| **AMRKB — Agricultural Modes Reference Knowledge Base** | Agricultural modes, systems, methods, practices and technologies. | Scope and architecture defined; public repository access unverified. | Not verified | Not publicly verified |
| **PBCKA** | Research responsibility and full name remain to be defined. | Local project scaffolding. | Not published | Not verified |
| **IRKB — Interdisciplinary Research Knowledge Base** | Comparative synthesis and interdisciplinary research across independent resources. | Developing research direction. | Not published | Not verified |
| **SSKB — Systems Science and SES** | Proposed systems-science and socio-ecological-systems research. | Developing direction; detailed scope requires definition. | Not published | Not verified |
| **DPRKB — Design Practice Research** | Proposed design-practice research and related knowledge. | Developing direction; detailed scope requires definition. | Not published | Not verified |

## Database Reference Methodology

The [Database Reference Methodology (DRM)](DRM/README.md) develops shared conventions for describing and connecting these resources. Stable identifiers distinguish records over time. Shared entity references help establish when records concern the same thing. Classifications organise research within a particular framework; mappings state how meanings correspond across frameworks. Relationships describe connections between entities, while provenance records the evidence and reasoning supporting a claim. These functions complement one another and should not be conflated.

Each database remains authoritative over its own records, classifications and evidence. Interoperability does not require identical schemas or the removal of disciplinary differences. A connection between resources must preserve their original meanings, scope and uncertainty. Scholarly evidence, inference and project interpretation must remain distinguishable, including where a proposed relationship is plausible but not yet established.

DRM provides methodological guidance under development, not a completed ontology, conformance standard or fully implemented software layer. IRKB has a different responsibility: interdisciplinary comparison and synthesis. It does not own the underlying databases or impose one project's analytical classifications on all others. The diagram also identifies possible analytical and applied uses; it does not assert the existence of an operational platform.

## Research resources

The [umbrella repository](https://github.com/ecological-interaction/ecological-information) maintains this introduction and shared documentation. Individual repositories retain the authoritative research registers; the website presents approved editions rather than independently edited academic copies. Consult each project's research guide for definitions, methods, evidence limitations and current development status.

Use project-level citation metadata when citing a resource and identify the version or commit consulted. EIRKB, EII, GISDS and OSDS provide citation files linked in the [architecture and history notes](ARCHITECTURE.md). Academic resources identify their named authors; [Jonathan Minchin's ORCID](https://orcid.org/0000-0001-8152-1796) supports attribution. Public access and citation metadata do not replace project-specific licences or third-party reuse conditions.

The [architecture and history notes](ARCHITECTURE.md) preserve detailed research boundaries, technical directions and naming questions. The [historical reorganisation record](REORGANISATION.json) remains unchanged. Future shared conventions should make relationships explicit without duplicating authoritative records or claiming integrations that have not been implemented.
