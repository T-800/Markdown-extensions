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
##All
* graphviz (voir: http://www.graphviz.org/)
* latex

Module a installer (pip install):
* markdown
* weasyprint
* MarkdownHighlight

##Mac
* html5lib
* tinyCSS
* CSSselect
* LXML


```
    git clone https://github.com/T-800/Markdown-extensions.git

    cp -r data ~/.data

    sudo cp ./mdx.py /usr/bin/mdx

    sudo cp extensions/* /usr/lib/python3.4/site-packages/markdown/extensions/

```
# Usage

## Mode pdf

```
    mdx fichier.md [out.pdf]
```

Le fichier ```out.pdf``` est optionnel. s'il n'est pas mentioné le fichier de sortie aura le meme nom que le fichier d'entré


## Mode html

```
    mdx -w fichier.md [out.html]
```


```
    mdx --html fichier.md [out.html]
```
