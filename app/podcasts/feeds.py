# from django.contrib.syndication.views import Feed

# from .models import Episode, Show


# class ITunesElements(object):
#     def add_root_elements(self, handler):
#         """Add additional elements to the show object"""
#         super(ITunesElements, self).add_root_elements(handler)

#         show = self.feed["show"]

#         if show.original_image:
#             if imagekit:
#                 itunes_sm_url = show.img_itunes_sm.url
#                 itunes_lg_url = show.img_itunes_lg.url
#             elif photologue:
#                 site = Site.objects.get_current()
#                 itunes_sm_url = "%s%s" % (
#                     site.domain,
#                     show.original_image.get_img_itunes_sm_url(),
#                 )
#                 itunes_lg_url = "%s%s" % (
#                     site.domain,
#                     show.original_image.get_img_itunes_lg_url(),
#                 )
#             elif easy_thumbnails:
#                 aliases = settings.THUMBNAIL_ALIASES["podcasting.Show.original_image"]
#                 thumbnailer = easy_thumbnails.files.get_thumbnailer(show.original_image)
#                 try:
#                     itunes_sm_url = thumbnailer.get_thumbnail(aliases["itunes_sm"]).url
#                     itunes_lg_url = thumbnailer.get_thumbnail(aliases["itunes_lg"]).url
#                 except easy_thumbnails.exceptions.InvalidImageFormatError:
#                     easy_thumbnails.signal_handlers.generate_aliases_global(
#                         show.original_image
#                     )
#                     itunes_sm_url = thumbnailer.get_thumbnail(aliases["itunes_sm"]).url
#                     itunes_lg_url = thumbnailer.get_thumbnail(aliases["itunes_lg"]).url
#                 except AttributeError:
#                     itunes_sm_url = None
#                     itunes_lg_url = None
#             elif sorl:
#                 itunes_sm_url = sorl.thumbnail.get_thumbnail(
#                     show.original_image, "144x144"
#                 ).url
#                 itunes_lg_url = sorl.thumbnail.get_thumbnail(
#                     show.original_image, "1400x1400"
#                 ).url
#             else:
#                 itunes_sm_url = show.original_image.url
#                 itunes_lg_url = show.original_image.url
#             if itunes_sm_url and itunes_lg_url:
#                 handler.addQuickElement("itunes:image", attrs={"href": itunes_lg_url})
#                 handler.startElement("image", {})
#                 handler.addQuickElement("url", itunes_sm_url)
#                 handler.addQuickElement("title", self.feed["title"])
#                 handler.addQuickElement("link", self.feed["link"])
#                 handler.endElement("image")

#         handler.addQuickElement("guid", str(show.uuid), attrs={"isPermaLink": "false"})
#         handler.addQuickElement("itunes:subtitle", self.feed["subtitle"])
#         handler.addQuickElement("itunes:author", show.author_text)
#         handler.startElement("itunes:owner", {})
#         handler.addQuickElement("itunes:name", show.owner.get_full_name())
#         handler.addQuickElement("itunes:email", show.owner.email)
#         handler.endElement("itunes:owner")
#         handler.addQuickElement(
#             "itunes:category", attrs={"text": self.feed["categories"][0]}
#         )
#         handler.addQuickElement("itunes:summary", show.description)
#         handler.addQuickElement("itunes:explicit", show.get_explicit_display())
#         if show.redirect:
#             handler.addQuickElement("itunes:new-feed-url", show.redirect)
#         handler.addQuickElement("keywords", show.keywords)
#         if show.editor_email:
#             handler.addQuickElement("managingEditor", show.editor_email)
#         if show.webmaster_email:
#             handler.addQuickElement("webMaster", show.webmaster_email)
#         try:
#             handler.addQuickElement(
#                 "lastBuildDate", rfc2822_date(show.episode_set.published()[1].published)
#             )
#         except IndexError:
#             pass
#         handler.addQuickElement("generator", "Django Web Framework")
#         handler.addQuickElement("docs", "http://blogs.law.harvard.edu/tech/rss")

#     def add_item_elements(self, handler, item):
#         """Add additional elements to the episode object"""
#         super(ITunesElements, self).add_item_elements(handler, item)

#         show = item["show"]
#         episode = item["episode"]
#         if episode.original_image:
#             if imagekit:
#                 itunes_sm_url = episode.img_itunes_sm.url
#                 itunes_lg_url = episode.img_itunes_lg.url
#             elif photologue:
#                 itunes_sm_url = episode.original_image.get_img_itunes_sm_url()
#                 itunes_lg_url = episode.original_image.get_img_itunes_lg_url()
#             elif easy_thumbnails:
#                 aliases = settings.THUMBNAIL_ALIASES[
#                     "podcasting.Episode.original_image"
#                 ]
#                 thumbnailer = easy_thumbnails.files.get_thumbnailer(
#                     episode.original_image
#                 )
#                 try:
#                     itunes_sm_url = thumbnailer.get_thumbnail(aliases["itunes_sm"]).url
#                     itunes_lg_url = thumbnailer.get_thumbnail(aliases["itunes_lg"]).url
#                 except easy_thumbnails.exceptions.InvalidImageFormatError:
#                     easy_thumbnails.signal_handlers.generate_aliases_global(
#                         episode.original_image
#                     )
#                     itunes_sm_url = thumbnailer.get_thumbnail(aliases["itunes_sm"]).url
#                     itunes_lg_url = thumbnailer.get_thumbnail(aliases["itunes_lg"]).url
#                 except AttributeError:
#                     itunes_sm_url = None
#                     itunes_lg_url = None
#             elif sorl:
#                 itunes_sm_url = sorl.thumbnail.get_thumbnail(
#                     episode.original_image, "144x144"
#                 ).url
#                 itunes_lg_url = sorl.thumbnail.get_thumbnail(
#                     episode.original_image, "1400x1400"
#                 ).url  # noqa
#             else:
#                 itunes_sm_url = episode.original_image.url
#                 itunes_lg_url = episode.original_image.url
#             if itunes_sm_url and itunes_lg_url:
#                 handler.addQuickElement("itunes:image", attrs={"href": itunes_lg_url})
#                 handler.startElement("image", {})
#                 handler.addQuickElement("url", itunes_sm_url)
#                 handler.addQuickElement("title", episode.title)
#                 handler.addQuickElement("link", episode.get_absolute_url())
#                 handler.endElement("image")

#         handler.addQuickElement(
#             "guid", str(episode.uuid), attrs={"isPermaLink": "false"}
#         )
#         if licenses:
#             handler.addQuickElement(
#                 "copyright",
#                 "{0} {1} {2}".format(
#                     show.license.name, show.license.url, datetime.date.today().year
#                 ),
#             )
#         else:
#             handler.addQuickElement(
#                 "copyright", "{0} {1}".format(show.license, datetime.date.today().year)
#             )
#         handler.addQuickElement("itunes:author", episode.author_text)
#         handler.addQuickElement("itunes:subtitle", episode.subtitle)
#         handler.addQuickElement("itunes:summary", episode.description)
#         handler.addQuickElement(
#             "itunes:duration",
#             "%02d:%02d:%02d" % (episode.hours, episode.minutes, episode.seconds),
#         )
#         handler.addQuickElement("itunes:keywords", episode.keywords)
#         handler.addQuickElement("itunes:explicit", episode.get_explicit_display())
#         if episode.block:
#             handler.addQuickElement("itunes:block", "yes")

#     def namespace_attributes(self):
#         return {"xmlns:itunes": "http://www.itunes.com/dtds/podcast-1.0.dtd"}
