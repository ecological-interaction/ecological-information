# Changelog

This repository-level record summarises documentation changes and their provenance. It is not a research release register or a website publication entry point. Dates below are supported by the cited Git history; the current targeted edit remains uncommitted.

## [Unreleased]

### Targeted editorial revision

- Moved the existing Research database directory above the Introduction in README.md, preserving both sections verbatim and retaining the complete diagram block unchanged.
- Removed the Research resources and Database Reference Methodology sections from the public Overview without adding replacements. Repository, attribution, citation and historical references are retained in AGENTS.md. Existing DRM/README.md already covers the removed methodological explanation; no methodology changes or transfers were required.
- Retired ARCHITECTURE.md from the active documentation structure. Its substantive research boundaries, federation responsibilities, technical directions and citation references are preserved in AGENTS.md; dated history is summarised below. Its exact earlier text remains in source commit `78795d7ac4de670ff56921b8aa4638cab4a40eec`.
- The historical PNG, Mermaid source, SVG, renderer, DRM documentation and REORGANISATION.json remain unchanged. Website removal of the architecture route requires a separate, future publication update; no manifest or website file is changed here.

## 2026-10-23 — Overview and diagram revision

Source commit `78795d7ac4de670ff56921b8aa4638cab4a40eec` shortened the Overview, added the nine-component directory, introduced editable Mermaid and derived SVG assets with a renderer, and relocated detailed notes into ARCHITECTURE.md. Sampled colours retained the earlier PNG's conceptual groupings. IRKB synthesis was distinguished from source-database authority; EIRKB's HA/IL/IM classifications were not adopted as universal schemes. PBCKA remained unclassified pending a defined scope.

Website commit `0f0cc932e9ce2b564c2314ade8db81448b7e43e7`, dated 23 October 2026, integrated that source edition, its SVG and architecture page. This records the Git publication milestone, not a newly inferred deployment timestamp. The earlier preparation note described Information source pin `c10e39b29dda883272b3ae501e8dfcf0f332c494` and pre-revision local HEAD `0a5afde92e0a0e96192a69aea099ad256c579931`; those are historical edition references, not instructions to change the current publication pin.

The relocated notes recorded EIRKB naming differences among “Ecological Information Research Knowledge Base”, “Ecological Information Reference Knowledge Base” and older “Ecological Interaction Reference Knowledge Base”. These describe documentation editions, not different repositories. No canonical-name change is made by this editorial revision.

## 2026-10-22 — DRM documentation

Source commit `0a5afde92e0a0e96192a69aea099ad256c579931` expanded DRM/README.md with working methodology, glossary and a conceptual example. The material remains qualified as developing guidance, not an approved detailed specification or implemented federation.

## 2026-10-21 — Shared documentation and illustration

Source commits `1a09476`, `b71c304` and `c10e39b` added the original federation illustration and revised shared documentation and publication references. The original federated-knowledge-systems.png remains a historical visual source; no binary asset is replaced by this edit.

## 2026-10-13 — Catalogue additions

Source commits `e0b778e` and `bb44b7c` added GISDS and PBCKA to the project catalogue respectively. The GISDS personal-account URL was later documented as redirecting to the organisation repository; AMRKB's configured personal-account location was recorded as publicly unverified, without inferring a replacement or ownership change.

## 2026-10-12 — Repository reorganisation

Source commits `d77e3ab` and `abaff3d` preserved the original domain documentation and established the umbrella documentation. EIRKB, EII and AMRKB were organised as independent local repositories. REORGANISATION.json retains the original five-file mapping, sizes and checksums; its paths remain relative to the original organisational directory and must not be rebased.

The approved mapping placed EIRKB_README.md at EIRKB/README.md despite the document's older filename instruction. Spreadsheet names were retained. The manifest does not describe all earlier Understanding history; that repository separately retains historical research provenance. No earlier history is rewritten here.
