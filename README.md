# Ecological Information

Ecological Information is the research information and knowledge-base
domain of the Ecological Interaction ecosystem.

Its purpose is to organise research references, academic positions,
ecological indicators, classifications, datasets and associated metadata
while preserving evidence, attribution and provenance.

## Relationship to the six domains

Ecological Interaction comprises six complementary domains:

- Understanding communicates ecological knowledge through education,
  teaching and learning resources.
- Information organises references, indicators, classifications,
  datasets and research knowledge.
- Computing provides reusable methods for processing ecological data.
- Intelligence develops interpretation, inference and analytical systems.
- Infrastructure supports access, integration and deployment.
- Generation supports the design and evaluation of ecological interventions.

These are logical domains. Listing them does not imply that every domain
already has implemented software or an established repository.

Information provides resources that other domains can use through
documented identifiers, metadata and exchange formats.

## Current project catalogue

### EIRKB — Ecological Interaction Reference Knowledge Base

EIRKB concerns academic references, research knowledge and associated
metadata. Its current material includes a historical and theoretical
narrative, two reference-register spreadsheets, and documentation of
the intended knowledge-base architecture.

It distinguishes scholarly information, disciplinary terminology and
project analytical positions. Bibliographic records and research
interpretations should retain their sources and evidence status.

### EII — Ecological Indicators Inventory

EII concerns ecological variables, indicators and indices, including
their definitions, observations, measurements, interpretation and
relationships.

Its current material is an exploratory Markdown inventory. Scientific
verification, bibliographic enrichment and database implementation
remain later development stages.

### AMRKB — Agricultural Modes Reference Knowledge Base

AMRKB concerns agricultural modes, systems, methods, practices,
techniques, technologies and classifications.

Its current documentation defines scope and a proposed development
architecture. A populated reference inventory and database have not
yet been implemented.

## Repository boundaries

EIRKB, EII and AMRKB are independent sibling repositories.

This umbrella contains domain documentation, a project catalogue,
coordination instructions and the historical reorganisation record.
It does not duplicate authoritative research documents, registers,
datasets or databases from the individual projects.

The containing `ecological-information/` directory is an ordinary
organisational directory.

Permanent project links can be added after repository publication
has been verified.

## Interoperability direction

The projects should remain separate while developing compatible
identifiers, source metadata and explicit relationships.

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

## Research quality and current status

The current projects are local research and development resources.
They are not complete, validated databases or established integration
services.

Distinguish documented evidence, inference and project interpretation.
Keep provisional classifications and exploratory inventory entries
clearly labelled.

The canonical project names in this catalogue are the agreed domain
terminology. Older project documents retain historical names pending
separately approved documentation updates.

Licensing, repository citation metadata and GitHub publication remain
to be agreed. No remote is configured for this umbrella.

## Historical reorganisation

The reorganisation dated 12 October 2026 established EIRKB, EII and
AMRKB as independent local repositories.

[REORGANISATION.json](REORGANISATION.json) preserves the original
five-file mapping, byte sizes and SHA-256 checksums.

Its paths are relative to the original `ecological-information/`
organisational directory. Moving the record into this umbrella does
not rebase or change those historical paths.

The original EIRKB document included an instruction to retain the
filename `EIRKB_README.md`. The approved repository mapping instead
placed it at `EIRKB/README.md`; the historical document text was
preserved unchanged. Both reference-register spreadsheet filenames
were also preserved.

The manifest describes that reorganisation from an ordinary directory.
It is not a complete account of earlier Understanding Git history.
The Understanding umbrella separately records the provenance of
historical research material now maintained in EIRKB.

This umbrella's first commit preserves the original domain README
and reorganisation manifest unchanged. Subsequent documentation
clarifies the domain architecture without changing the independent
research repositories.
