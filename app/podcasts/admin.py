from django.contrib import admin

from .models import Episode, Show


# Register your models here.
class ShowAdmin(admin.ModelAdmin):
    pass


class EpisodeAdmin(admin.ModelAdmin):
    pass


admin.site.register(Show, ShowAdmin)
admin.site.register(Episode, EpisodeAdmin)
