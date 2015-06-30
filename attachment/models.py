from django.db import models

class File(models.Model):
    VIDEO_TYPE = 1
    TYPE_CHOICES = (
        (VIDEO_TYPE, 'video'),
    )
    type = models.IntegerField('tipo', choices=TYPE_CHOICES)
    path = models.CharField('percorso', max_length=255, help_text='a partire dalla directory media/attachment/TYPE')
    notes = models.TextField('note')

    class Meta:
        verbose_name = 'Allegato'
        verbose_name_plural = 'Allegati'

    def __unicode__(self):
        return self.path
