from datetime import datetime

from django.conf import settings
from django.shortcuts import render
from django.views import generic

from .models import Episode, Show

# Create your views here.


class RSSFeed(generic.TemplateView):
    template_name = "podcasts/show_rss_feed.html"
    content_type = "application/rss+xml"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if settings.MULTI_SHOW_HOST:
            current_show = Show.objects.get(slug_title=self.kwargs["show_title"])
        else:
            current_show = Show.objects.get(title=settings.SHOW_TITLE)

        episodes = (
            Episode.objects.filter(parent_show=current_show)
            .filter(published_date__lt=datetime.now())
            .order_by("published_date")
        )

        context["show"] = current_show
        context["episodes"] = episodes

        return context
