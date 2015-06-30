from django.db import models

from ckeditor.fields import RichTextField

class Page(models.Model):
    """ Diary Page
    """
    date = models.DateField('data', auto_now=False, auto_now_add=False)
    title = models.CharField('titolo', max_length=128)
    slug = models.SlugField('slug', max_length=255)
    text = RichTextField('testo')

    class Meta:
        verbose_name = 'Pagina'
        verbose_name_plural = 'Pagine'
        ordering = ('-date', '-id',)

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('filippo-page-detail', None, { 
          'slug': self.slug, 
          'year': self.date.year, 
          'month': self.date.strftime("%m"), 
          'day': self.date.strftime("%d") 
        })

