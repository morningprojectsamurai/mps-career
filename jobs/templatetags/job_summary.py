import markdown
from django import template

register = template.Library()

@register.filter(is_safe=True)
def html(value):
    return markdown.markdown(value)
