Markdown-extensions
===================

Script Python qui utilise le module markdown de python3 pour tranformer un fichier mardown en pdf

Module ajouter :
* latex
* graphviz
* table des matières
* tables
* definition
* highlight"

# Install

* graphviz (voir: http://www.graphviz.org/)
* latex

Module a installer (pip install):
* markdown
* weasyprint
* MarkdownHighlight.highlight

```
    git clone https://github.com/T-800/Markdown-extensions.git

    cp data ~/.data

    sudo cp ./main.py /usr/bin/mdx

    sudo extensions/* /usr/lib/python3.4/site-packages/markdown/extensions/

```
# Usage
```
    mdx fichier.md fichier.pdf
```
