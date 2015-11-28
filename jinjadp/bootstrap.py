import bootstrap3.forms
from jinja2 import Markup

from jinjadp.utils import safe_rendering


@object.__new__
class bootstrap:

    def __getattr__(self, name):
        setattr(
            self,
            name,
            safe_rendering(
                getattr(
                    bootstrap3.forms,
                    'render_' + name
                )
            )
        )
        return getattr(self, name)

    def button(
        self,
        text,
        class_='primary',
        layout='horizontal',
        type='submit'
    ):
        assert layout == 'horizontal'
        return Markup(
            '<div class="form-group">'
                '<div class="col-md-9 col-md-offset-3">'
                    '<button type="{type}" class="btn btn-{class_}">'
                        '{text}'
                    '</button>'
                '</div>'
            '</div>'
        ).format(
            text=text,
            class_=class_,
            layout=layout,
            type=type,
        )
