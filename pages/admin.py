from django.contrib import admin

# Register your models here.
from django.utils.html import format_html

from pages.models import Team


class TeamAdmin(admin.ModelAdmin):

    def thumbnail(self, object):
        return format_html('<img src="{}" style="border-radius:50%" width="40" />'.format(object.photo.url))

    list_display = ('id', 'thumbnail', 'first_name', 'designation',)
    list_display_links = ('id', 'thumbnail', 'first_name')
    search_fields = ('first_name', 'last_name', 'designation',)
    list_filter = ('designation',)


admin.site.register(Team, TeamAdmin)
