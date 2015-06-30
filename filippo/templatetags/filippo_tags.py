from django import template

from filippo.models import Page

register = template.Library()

@register.inclusion_tag('filippo/archive.html')
def filippo_archive():
  pages = Page.objects.all()
  return {'pages': pages}
