import markdown
import base64
import markdown.preprocessors
import subprocess


# Defines our basic inline image
IMG_EXPR = "<img " + \
    " src='data:image/svg+xml;base64,%s'>"


class GraphvizPostprocessor(markdown.postprocessors.Postprocessor):
        """This post processor extension just allows us to further
        refine, if necessary, the document after it has been parsed."""
        def run(self, text):
            return text


class GraphvizExtension(markdown.Extension):
    def __init__(self, configs):
        self.config = {'FORMAT': 'svg'}
        for key, value in configs:
            self.config[key] = value

    def reset(self):
        pass

    def extendMarkdown(self, md, md_globals):
        "Add GraphvizExtension to the Markdown instance."
        md.registerExtension(self)
        self.parser = md.parser
        md.preprocessors.add('graphviz', GraphvizPreprocessor(self), '_begin')

        # Our cleanup postprocessing extension
        md.postprocessors.add('graphviz',
                              GraphvizPostprocessor(self), ">amp_substitute")


class GraphvizPreprocessor(markdown.preprocessors.Preprocessor):
    """
    Find all graphviz blocks, generate images and inject
    image link to generated images.
    """

    def __init__(self, graphviz):
        self.graphviz = graphviz
        self.formatters = ["dot", "neato", "lefty", "dotty"]

    def run(self, lines):
        start_tags = ["<%s>" % x for x in self.formatters]
        end_tags = ["</%s>" % x for x in self.formatters]
        graph_n = 0
        new_lines = []
        block = []
        in_block = None
        for line in lines:
            if line in start_tags:
                assert(block == [])
                in_block = self.extract_format(line)
            elif line in end_tags:
                new_lines.append(self._graphviz_to_base64(in_block, block))
                graph_n = graph_n + 1
                block = []
                in_block = None
            elif in_block in self.formatters:
                block.append(line)
            else:
                new_lines.append(line)
        assert(block == [])
        return new_lines

    def extract_format(self, tag):
        format = tag[1:-1]
        assert(format in self.formatters)
        return format

    def _graphviz_to_base64(self, typed, lines):
        """Generates a base64 representation of Graphviz string"""

        cmd = "%s -T%s" % (typed, self.graphviz.config["FORMAT"])
        p = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE,
                             stdout=subprocess.PIPE, close_fds=True)
        p.stdin.write(bytes("\n".join(lines), 'UTF-8'))
        p.stdin.close()
        p.wait()
        pp = p.stdout.read()
        data = base64.b64encode(pp)
        return IMG_EXPR % data.decode("utf-8")


def makeExtension(configs=None):
    return GraphvizExtension(configs=configs)
