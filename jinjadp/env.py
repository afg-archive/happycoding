from django.contrib.staticfiles.storage import staticfiles_storage
from django.core.urlresolvers import reverse
from django.utils.timezone import localtime
from django.contrib import messages

from jinja2 import Environment, Markup, contextfunction

from jinjadp.bootstrap import bootstrap
from jinjadp.highlight import highlight


@contextfunction
def navli(context, url, display, active=None, disabled=False, _blank=False):
    if active is None:
        active = context['request'].path_info == url
    classes = []
    if active:
        classes.append('active')
    if disabled:
        classes.append('disabled')
    return Markup(
        '<li class="{classes}"><a{aattr}{url}>{display}</a></li>'
    ).format(
        classes=' '.join(classes),
        url=Markup(' href="{}"').format(url) if url else '',
        display=display,
        aattr=Markup(' target="_blank"') if _blank else ''
    )


def localftime(time):
    return localtime(time).strftime('%Y/%m/%d %H:%M:%S')


def url(name, *args, **kwargs):
    return reverse(name, args=args, kwargs=kwargs)


@contextfunction
def get_messages(context):
    return messages.get_messages(context['request'])


message_classes = {
    messages.DEBUG: 'info',
    messages.INFO: 'info',
    messages.SUCCESS: 'success',
    messages.WARNING: 'warning',
    messages.ERROR: 'danger',
}


def environment(**options):
    env = Environment(**options)
    env.globals.update({
        'static': staticfiles_storage.url,
        'url': url,
        'navli': navli,
        'localtime': localtime,
        'bootstrap': bootstrap,
        'get_messages': get_messages,
        'message_classes': message_classes,
    })
    env.filters.update({
        'localftime': localftime,
        'highlight': highlight,
    })
    return env
