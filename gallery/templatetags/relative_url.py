from django import template
from django.urls import reverse

register = template.Library()

@register.simple_tag
def relative(view_name, *args, **kwargs):
    url = reverse(view_name, args=args, kwargs=kwargs)
    if url == '/':
        return 'index.html'
    if url.startswith('/'):
        return url[1:]
    return url
