Markdown-extensions
===================

Script Python qui utilise le module markdown de python3 pour tranformer un fichier mardown en pdf

Module ajouter :
* Table des matière
* Graph
* Math

# Install

* graphviz (voir: http://www.graphviz.org/)
* latex

Module a installer (pip install):
* markdown
* weasyprint
* MarkdownHighlight.highlight



Copier le dossier data dans le home sous le nom .data et mettre le fichier config

    cp CONFIG data/

    cp data ~/.data

    sudo cp ./main.py /usr/bin/mdx

    sudo extensions/* /usr/lib/python3.4/site-packages/markdown/extensions/


# Usage

    mdx fichier.md fichier.pdf
