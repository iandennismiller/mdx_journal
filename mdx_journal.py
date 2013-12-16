from html5lib.sanitizer import HTMLSanitizer

import re
from markdown.postprocessors import Postprocessor
from markdown import Extension

class MyTokenizer(HTMLSanitizer):
    def sanitize_token(self, token):
        return token

class JournalPostprocessor(Postprocessor):
    def run(self, text):
        if re.match(r"^%d%d%d%d$", text):
            text = "<h2>%s</h2>" % text
        return text

class JournalExtension(Extension):
    def extendMarkdown(self, md, md_globals):
        md.postprocessors.add("journal", JournalPostprocessor(md), "_begin")

def makeExtension(configs=None):
    return JournalExtension(configs=configs)
