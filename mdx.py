#! /usr/bin/python

import markdown
import sys
import os
from MarkdownHighlight.highlight import HighlightExtension
from weasyprint import HTML


def file_exist(fichier):

    return (os.path.exists(os.path.expanduser(fichier)) and not
            os.path.isdir(os.path.expanduser(fichier)))


def open_config(path=""):
    conf = []

    ficConf = open(path)
    fic = [ligne.strip() for ligne in ficConf.readlines()]

    for ligne in fic[::]:
        if ligne and not ligne.startswith("#"):
            conf += [ligne]

    for line in conf:
        line = line.split("=", 1)
        if line[0] == "DATA_PATH":
            DATA_PATH = line[1]
        elif line[0] == "CODE_CSS_STYLE":
            CODE_CSS_STYLE = line[1]
        elif line[0] == "CSS_NAME":
            CSS_NAME = line[1]
        elif line[0] == "EXTENSIONS":
            EXTENSIONS = eval(line[1])
    return DATA_PATH, CODE_CSS_STYLE, CSS_NAME, EXTENSIONS


def modepdf(fichiers):
    if not fichiers[0].endswith(".md"):
        aide()
        return

    tmp = modehtml([fichiers[0], "tmp.html"])

    ficIn = open(tmp, 'r')
    txt = ficIn.read()
    ficIn.close()

    if (len(fichiers) > 1):
        pathOut = fichiers[1]
    else:
        pathOut = fichiers[0][:-3]+".pdf"

    HTML(tmp).write_pdf(pathOut)
    os.remove(tmp)


def modehtml(fichiers):
    if not fichiers[0].endswith(".md"):
        aide()
        return

    DATA_PATH, CODE_CSS_STYLE, CSS_NAME, EXTENSIONS =\
        open_config(os.path.expanduser('~/.data/CONFIG'))

    ficIn = open(fichiers[0], 'r')
    txt = ficIn.read()
    ficIn.close()

    header = '''
    <head>
        <meta charset='UTF-8'>
        <link rel='stylesheet' href="''' + os.path.expanduser(DATA_PATH) + "CSS/" + CSS_NAME + '''"/>
        <link rel="stylesheet" href="''' + os.path.expanduser(DATA_PATH) + "CSS/highlight/styles/" + CODE_CSS_STYLE + '''"/>
        <script src="''' + os.path.expanduser(DATA_PATH) + '''CSS/highlight/highlight.pack.js"></script>
        <script>hljs.initHighlightingOnLoad();</script>
    </head>
    <body>
        '''
    if (len(fichiers) > 1):
        pathOut = fichiers[1]
    else:
        pathOut = fichiers[0][:-3]+".html"
    ficOut = open(pathOut, 'w')
    ficOut.write(header)

    md = markdown.Markdown(extensions=EXTENSIONS)

    ficOut.write(md.convert(txt))
    ficOut.write('''</body>''')
    ficOut.close()
    if file_exist("latex.cache"):
        os.remove("latex.cache")
    return pathOut


def args(arg):
    if len(arg) < 0:
        aide()
        return
    print(arg)
    if arg[0].startswith("-") and len(arg) > 1:
        if arg[0] == "-h" or arg[0] == "--help":
            aide()
        elif arg[0] == "-w" or arg[0] == "--html":
            modehtml(arg[1:])

    elif not arg[0].startswith("-"):
        modepdf(arg)

    else:
        aide()


if __name__ == "__main__":
    args(sys.argv[1:])
