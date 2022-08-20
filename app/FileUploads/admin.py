from django.contrib import admin

from .models import EpisodeFile


# Register your models here.
class EpisodeFileAdmin(admin.ModelAdmin):
    pass


admin.site.register(EpisodeFile, EpisodeFileAdmin)
