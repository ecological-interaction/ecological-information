"""Render the umbrella diagram's fixed-layout Mermaid subset as portable SVG.

Adapted from the OSDS diagram method. All labels, colours, relationships and
layout hints are authoritative in federated_knowledge_systems.mmd. This small
renderer does not implement general Mermaid layout. Requires only Python 3.
"""
from pathlib import Path
from html import escape
import hashlib
import re
import xml.etree.ElementTree as ET

HERE = Path(__file__).resolve().parent
SOURCE = HERE / 'federated_knowledge_systems.mmd'
DESTINATION = HERE / 'federated_knowledge_systems.svg'


def render():
    source = SOURCE.read_text(encoding='utf-8')
    labels = dict(re.findall(r'^\s*(?:subgraph\s+)?(\w+)\["([^"\n]+)"\]', source, re.M))
    width, height = map(int, re.search(r'^%% @canvas (\d+) (\d+)$', source, re.M).groups())
    hints = re.findall(r'^%% @(box|group|region) (\w+) (\d+) (\d+) (\d+) (\d+) (\w+)$', source, re.M)
    boxes = {name: tuple(map(int, (x, y, w, h))) for _, name, x, y, w, h, _ in hints}
    styles = {name: dict(item.split(':', 1) for item in declarations.split(','))
              for name, declarations in re.findall(r'^\s*classDef (\w+) ([^\n;]+);', source, re.M)}
    developing = set(re.search(r'^\s*class ([\w,]+) developing;', source, re.M).group(1).split(','))
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title description">',
             '<title id="title">Ecological Information — federated research architecture</title>',
             '<desc id="description">Developing interdisciplinary synthesis and shared methodology connect autonomous research knowledge bases and scientific, geographic and observation-source catalogues. PBCKA remains unclassified. A lower band shows emerging analytical applications. Solid database-card borders denote published research; dashed borders denote developing components. Connections are conceptual, not operational data flows.</desc>',
             f'<!-- Derived from federated_knowledge_systems.mmd; SHA-256 {hashlib.sha256(SOURCE.read_bytes()).hexdigest()}. Do not edit this SVG directly. -->',
             '<defs><marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" fill="#637286"/></marker></defs>',
             f'<rect width="{width}" height="{height}" fill="#ffffff"/>',
             '<g font-family="Arial, Helvetica, sans-serif" text-anchor="middle">']
    for a, relationship, b in re.findall(r'^\s*(\w+) (<-->|-->) (\w+)\s*$', source, re.M):
        ax, ay, aw, ah = boxes[a]; bx, by, bw, bh = boxes[b]
        start = ' marker-start="url(#arrow)"' if relationship == '<-->' else ''
        parts.append(f'<path d="M {ax + aw / 2:g} {ay + ah + 5} L {bx + bw / 2:g} {by - 5}" fill="none" stroke="#637286" stroke-width="1.6" marker-end="url(#arrow)"{start}/>')
    for kind, name, _, _, _, _, role in hints:
        if kind == 'region':
            x, y, w, h = boxes[name]
            declarations = re.search(r'^\s*style ' + name + r' ([^\n]+)$', source, re.M).group(1)
            style = dict(item.split(':', 1) for item in declarations.split(','))
            parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="18" fill="{style["fill"]}" stroke="{style["stroke"]}" stroke-dasharray="{style["stroke-dasharray"]}"/>')
            continue
        x, y, w, h = boxes[name]; style = styles[role]
        dash = f' stroke-dasharray="{styles["developing"]["stroke-dasharray"]}"' if name in developing else ''
        stroke_width = style.get('stroke-width', '1px').removesuffix('px')
        parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="14" fill="{style["fill"]}" stroke="{style["stroke"]}" stroke-width="{stroke_width}"{dash}/>')
        lines = labels[name].split('<br/>')
        if role == 'synthesis':
            baselines, sizes = [y + 48, y + 88], [30, 22]
        elif role == 'federation':
            baselines, sizes = [y + 39, y + 74], [28, 21]
        elif kind == 'group':
            baselines, sizes = ([y + 36, y + 66], [27, 18]) if len(lines) == 2 else ([y + 36], [26])
        elif role == 'knowledgecard':
            baselines, sizes = ([y + 27, y + 50, y + 72, y + 96], [23, 16, 16, 13]) if len(lines) == 4 else ([y + 32, y + 61, y + 88], [23, 17, 13])
        elif role == 'sourcecard':
            baselines, sizes = [y + 30, y + 57], [23, 15]
        elif name == 'PBCKA':
            baselines, sizes = [y + 25, y + 48, y + 67], [22, 17, 13]
        else:
            baselines, sizes = [y + 26, y + 50], [19, 19]
        assert len(lines) == len(baselines), name
        for index, (line, baseline, size) in enumerate(zip(lines, baselines, sizes)):
            weight = '600' if index == 0 else '400'
            parts.append(f'<text x="{x + w / 2:g}" y="{baseline:g}" font-size="{size}" font-weight="{weight}" fill="{style["color"]}">{escape(line)}</text>')
    for kind in ['note', 'legend']:
        x, y, label = re.search(r'^%% @' + kind + r' (\d+) (\d+) (.+)$', source, re.M).groups()
        parts.append(f'<text x="{x}" y="{y}" font-size="17" fill="#566579">{escape(label)}</text>')
    parts.append('</g></svg>')
    svg = '\n'.join(parts) + '\n'
    ET.fromstring(svg)
    DESTINATION.write_text(svg, encoding='utf-8')


if __name__ == '__main__':
    render()
