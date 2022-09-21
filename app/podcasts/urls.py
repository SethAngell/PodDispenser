from django.conf import settings
from django.urls import path

from . import views

if settings.MULTI_SHOW_HOST:
    urlpatterns = [
        path("rss/<str:show_title>/", views.RSSFeed.as_view(), name="rss_index"),
    ]
else:
    urlpatterns = [path("rss/", views.RSSFeed.as_view(), name="rss_index")]
