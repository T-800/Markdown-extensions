#! /usr/bin/python

import markdown
import os
import pdfkit
from weasyprint import HTML


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


def main():
    ficIn = open("test.md", 'r')
    txt = ficIn.read()
    ficIn.close()
    ficOut = open("test.html", 'w')

    DATA_PATH, CODE_CSS_STYLE, CSS_NAME, EXTENSIONS =\
        open_config("CONFIG")

    header = '''
    <head>
        <meta charset='UTF-8'>
        <link rel='stylesheet' href="''' + DATA_PATH + "CSS/" + CSS_NAME + '''"/>
        <link rel="stylesheet" href="''' + DATA_PATH + "CSS/highlight/styles/" + CODE_CSS_STYLE + '''"/>
        <script src="''' + DATA_PATH + '''CSS/highlight/highlight.pack.js"></script>
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

    HTML('test.html').write_pdf('./ext/test.pdf')  # no Js
#    os.remove("test.html")


if __name__ == "__main__":
    main()
