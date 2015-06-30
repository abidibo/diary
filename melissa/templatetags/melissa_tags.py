from django import template

from melissa.models import Page

register = template.Library()

@register.inclusion_tag('melissa/archive.html')
def melissa_archive():
  pages = Page.objects.all()
  return {'pages': pages}
