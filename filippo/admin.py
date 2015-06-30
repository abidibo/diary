from django.contrib import admin

import filippo

class FilippoAdmin(admin.ModelAdmin):
    list_display = ['date', 'title',]
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(filippo.models.Page, FilippoAdmin)
