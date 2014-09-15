#! /usr/bin/python

import markdown
import sys
import os
import pdfkit
from weasyprint import HTML
from MarkdownHighlight.highlight import HighlightExtension


def file_exist(fichier):

    return (os.path.exists(os.path.expanduser(fichier)) and not os.path.isdir(os.path.expanduser(fichier)))



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


def main(pathIn, pathOut):
    ficIn = open(pathIn, 'r')
    txt = ficIn.read()
    ficIn.close()
    ficOut = open("test.html", 'w')
    DATA_PATH, CODE_CSS_STYLE, CSS_NAME, EXTENSIONS =\
        open_config(os.path.expanduser('~/.data/CONFIG'))

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
    ficOut.write(header)

    md = markdown.Markdown(extensions=EXTENSIONS)

    ficOut.write(md.convert(txt))
    ficOut.write('''</body>''')
    ficOut.close()

    # htmltopdf
    options = {
        'quiet': '',
        'enable-internal-links': '',
        'enable-external-links': ''
    }

    # pdfkit.from_file('test.html', './ext/test1.pdf',
    #                    options=options)  # no click link
    HTML('test.html').write_pdf(pathOut)  # no Js
    os.remove("test.html")

if __name__ == "__main__":
    if(len(sys.argv) == 3):
        if (file_exist(sys.argv[1]) and sys.argv[2].endswith(".pdf")):
            main(sys.argv[1], sys.argv[2])
        else:
            print("Le fichier"+sys.argv[1]+" n'éxiste pas ")
    else:
        print("Entrer un fichier en argument")
