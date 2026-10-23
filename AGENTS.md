# Ecological Information umbrella instructions

Read README.md, CHANGELOG.md, DRM/README.md and REORGANISATION.json before changing domain documentation.

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
- Keep the historical federated-knowledge-systems.png byte-for-byte unchanged. Approximate sampled fills and their meanings are retained below: blue synthesis, lavender DRM/federation, green research knowledge bases, amber scientific/geographic/observational sources, grey emerging applications.
- PBCKA remains unclassified until its research scope is approved. Dashed database-card borders denote developing components; solid card borders denote published research, not scientific validation. Preserve database autonomy and the conceptual-status qualification.
- Do not treat EIRKB HA/IL/IM classifications as federation-wide schemes or introduce operational data-flow claims. Do not copy OSDS's eight-category detail into the umbrella illustration.
- Keep README image paths repository-relative. Website allowlisting, source pin updates and deployment require a separate task; do not modify the website or other research repositories during Overview work.
- Validate deterministic SVG regeneration, readable layout, internal links and scoped Git changes. Keep technical maintenance instructions here rather than in the introductory narrative.

## Retained repository research context

These contributor/reference notes preserve substantive material from the retired architecture document. They are not an additional website publication entry point. Current shared methodology remains in [DRM documentation](DRM/README.md); no taxonomy, research record or methodological decision is changed by this relocation.

### EIRKB

EIRKB concerns the history and theory of ecological information, academic
references, intellectual lineages, conceptual classifications and associated
research metadata. Its current material includes a historical and theoretical
narrative, a Markdown reference register transcribing 13 workbook sections,
two reference-register spreadsheets, and documentation of the intended
knowledge-base architecture. The protocol distinguishes identity, metadata,
classification, relationships and provenance; its classifications and research
interpretations remain provisional.

The current project README uses “Ecological Information Research Knowledge Base”.
Its citation metadata and published introduction retain “Ecological Information
Reference Knowledge Base”; older umbrella terminology used “Ecological
Interaction Reference Knowledge Base”. These names describe source editions,
not separate repositories. A canonical-name alignment remains to be approved.

It distinguishes scholarly information, disciplinary terminology and
project analytical positions. Bibliographic records and research
interpretations should retain their sources and evidence status.

### EII

Its Scientific Reference Register is the human-readable five-column catalogue
of 235 indicators across EII Domain Taxonomy v1.0.0, comprising 15 scientific
domains. Its authoritative Machine Reference contains full-length structured
records in Markdown JSON blocks, definitions, classifications, supporting
relationships, scientific references, source routes and observation schemas.
The separately curated remote-sensing subset contains 91 indicators.

The indicator inventory is work in progress, not a verified monitoring standard. GISDS routes remain candidate sources, AMRKB links remain technical context, and IoT/bioinformatics bindings are not automatically assigned. PBCKA/EIRKB interoperability and Trails4Soil practice crosswalks remain outside its active scope. Historical DRM v1.0.0 references do not establish conformance: the available DRM introduction is not an approved detailed specification. Scientific verification, bibliographic enrichment and database implementation remain further work; EII's reading interface is now published.

### AMRKB

AMRKB concerns agricultural modes, systems, methods, practices,
techniques, technologies and classifications.

Its current documentation defines scope and a proposed development
architecture, covering traditional, Indigenous, industrial, ecological,
experimental and emerging approaches. Research dimensions include historical
development, technical methods and infrastructure, ecological mechanisms,
place-specific suitability, labour and productive organisation. Modes, systems,
methods, practices, technologies and indicators are kept distinct. A populated
reference inventory, validated classification and database have not yet been
implemented. The previously configured personal-account repository returned a public 404 during this review. That does not establish whether it is private, moved or absent; no replacement link or ownership is inferred.

### GISDS and OSDS

GISDS catalogues GIS, cartography and Earth-observation sources, including
platform capabilities, analytical download routes, access conditions and
interpretation limits. Its current `GISDS.md` register, catalogue version 1.4,
contains 25 unique resources, `RS001`–`RS025`. These include data providers,
environmental platforms, geospatial computation services and map-making tools;
they are catalogue resources, not 25 completed dataset records. The README
defines dataset-level metadata, including product/version, dates, resolution,
CRS, processing, provenance and reuse conditions. Descriptions derive from
provider documentation rather than end-to-end tests of every platform.

GISDS's verified current repository is [ecological-interaction/GISDS](https://github.com/ecological-interaction/GISDS); its personal-account URL redirects there. GISDS and OSDS now have published reading pages. OSDS separates source discovery from product-level verification, keeps 62 candidate source IDs, eight disciplinary domains and eight observation categories, and distinguishes its authoritative machine reference from its human presentation. OSDS classifications are not equivalent to EII classifications merely because their codes match.

### Developing components

IRKB concerns comparative, interdisciplinary synthesis. SSKB and DPRKB are developing systems-science/SES and design-practice research directions, not verified populated databases. PBCKA has no confirmed expansion or defined research scope. No disciplinary grouping is assigned to PBCKA in the reconstructed diagram. AMRKB is a scope/architecture project; its inclusion does not imply a populated or publicly accessible database.

## Federation responsibilities

This umbrella contains layer documentation, a project catalogue,
coordination instructions and the historical reorganisation record.
It can maintain shared methodologies, database architecture guidance,
cross-database mappings and shared research diagrams. Individual databases
retain authority over their research documents, classifications, schemas,
identifiers and evidence. The umbrella does not duplicate their authoritative
research documents, registers, datasets or databases.

The databases are intended to operate as an interoperable federation,
retaining independent version control and explicit, evidenced relationships.
This is a research direction, not an implemented federation service.

IRKB synthesises across independent resources without ownership or control. EIRKB's Historical Arc (HA), Intellectual Lineages (IL) and Intellectual Map (IM) remain project analytical classifications; they are not universal codes inherited by the federation. The lower analysis/application band describes potential uses, not an operational service.

## Interoperability and technical directions

Planned conventions include:

- Stable project and entity identifiers with explicit cross-project mappings.
- Bibliographic metadata, citation keys and mappings to external identifiers.
- Dataset descriptions, provenance, versions, checksums and reuse conditions.
- Indicator definitions, units, measurement methods and interpretation limits.
- Agricultural classifications with documented evidence and provisional status.
- Spatial metadata identifying places, geometry sources and coordinate
  reference systems.
- Versioned schemas and documented exchange formats.

Zotero interoperability is intended to support literature management
and bibliographic exchange. EIRKB should complement Zotero rather than
replace it or directly modify its internal database.

SQLite is the planned canonical structured store for EIRKB.
AMRKB also anticipates later SQLite development. These databases are
not currently implemented.

QGIS compatibility is a future development direction for spatial
information and validated exchanges. EIRKB documentation identifies
GeoPackage and GeoJSON as intended spatial formats.

Future knowledge-graph development should preserve existing entity
identifiers, relationship meanings and assertion-level provenance.
JSON-LD and RDF are prospective representations, not current
implemented capabilities.

Shared conventions do not require identical project schemas or a
shared runtime dependency.

## Retained citation and repository references

EIRKB, EII, GISDS and OSDS provide `CITATION.cff` metadata for Jonathan Minchin, Ecological Interaction, ORCID 0000-0001-8152-1796:

- [EIRKB citation metadata](https://github.com/ecological-interaction/EIRKB/blob/main/CITATION.cff)
- [EII citation metadata](https://github.com/ecological-interaction/EII/blob/main/CITATION.cff)
- [GISDS citation metadata](https://github.com/ecological-interaction/GISDS/blob/main/CITATION.cff)
- [OSDS citation metadata](https://github.com/ecological-interaction/OSDS/blob/main/CITATION.cff)

Use the metadata and commit/version of the resource actually consulted. No umbrella-wide licence, DOI or new authorship is assigned by this revision. Referenced datasets retain their own conditions.

The [umbrella repository](https://github.com/ecological-interaction/ecological-information) maintains this introduction and shared documentation. Individual repositories retain the authoritative research registers; the website presents approved editions rather than independently edited academic copies. Consult each project's research guide for definitions, methods, evidence limitations and current development status.

Use project-level citation metadata when citing a resource and identify the version or commit consulted. EIRKB, EII, GISDS and OSDS provide citation files linked in these repository notes. Academic resources identify their named authors; [Jonathan Minchin's ORCID](https://orcid.org/0000-0001-8152-1796) supports attribution. Public access and citation metadata do not replace project-specific licences or third-party reuse conditions.

These repository notes preserve detailed research boundaries, technical directions and naming questions. The [historical reorganisation record](REORGANISATION.json) remains unchanged. Future shared conventions should make relationships explicit without duplicating authoritative records or claiming integrations that have not been implemented.

## Retained colour-reference notes

The principal fill samples below were extracted from interior regions of the original 1536 × 1024 PNG. Raster gradients and antialiasing produce nearby values; these are approximate representative fills, not claims of an original vector palette.

| Meaning | Sampled approximate fill | Reconstructed use |
|---|---|---|
| Interdisciplinary synthesis | Pale blue `#CCE3F9` | IRKB |
| Federation and methodology | Lavender `#E1DAF0` | DRM and shared conventions |
| Research knowledge bases | Green `#E1F0E6` | EIRKB, SSKB, DPRKB, AMRKB |
| Scientific/geographic sources | Amber `#FEEEC9` (light panels also `#FEF6E3`) | EII, GISDS, OSDS |
| Analysis and applications | Grey `#EAEDF1` | Emerging analytical/applied uses |

PBCKA uses an unclassified neutral card, not a new disciplinary category. Solid database-card borders identify published research resources; dashed borders identify developing components. Public availability is not evidence of scientific verification.
