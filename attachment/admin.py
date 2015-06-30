from django.contrib import admin

import attachment

class FileAdmin(admin.ModelAdmin):
    list_display = ['type', 'path',]

admin.site.register(attachment.models.File, FileAdmin)
