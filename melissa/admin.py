from django.contrib import admin

import melissa

class MelissaAdmin(admin.ModelAdmin):
    list_display = ['date', 'title',]
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(melissa.models.Page, MelissaAdmin)
