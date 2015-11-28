from jinja2 import Markup


def safe_rendering(function):
    def _safe_renderer(*args, **kwargs):
        return Markup(function(*args, **kwargs))
    return _safe_renderer
