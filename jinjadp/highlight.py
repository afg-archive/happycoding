from pygments import highlight as _highlight
from pygments.lexers import CppLexer
from pygments.formatters import HtmlFormatter

from .utils import safe_rendering


@safe_rendering
def highlight(code):
    return _highlight(code, CppLexer(), HtmlFormatter())
