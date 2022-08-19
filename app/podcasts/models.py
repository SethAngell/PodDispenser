import uuid

from django.db import models

from .constants import CATEGORIES, FILETYPES, LANGUAGES, TRUE_OR_FALSE, YES_OR_NO
from .utils import validate_show_art_is_optimally_sized


# Create your models here.
class Show(models.Model):
    title = models.CharField(max_length=128, null=False, blank=False, unique=True)
    description = models.TextField(max_length=3000, null=False, blank=False)
    language = models.CharField(
        max_length=5, choices=LANGUAGES, null=False, blank=False
    )
    link = models.URLField(help_text="The homepage for your podcast")
    copyright = models.CharField(max_length=128)

    # Itunes Specific Fields
    image = models.ImageField(
        null=False,
        blank=False,
        validators=[validate_show_art_is_optimally_sized],
        help_text="Should be a 3000x3000 square image",
    )
    category = models.CharField(max_length=40, choices=CATEGORIES)
    explicit = models.BooleanField(default=False)
    author = models.CharField(
        max_length=120,
        help_text="The name of this shows hosts as you'd like them displayed within a podcast directory",
    )
    owner_name = models.CharField(
        max_length=120,
        help_text="The name of this shows primary point of contact (Not displayed in podcast directories)",
    )
    owner_email = models.EmailField(
        help_text="The email of this shows primary point of contact (Not displayed in podcast directories)"
    )
    block = models.CharField(
        max_length=3,
        choices=YES_OR_NO,
        help_text="Whether this show is displayed in the Apple Itunes Directory. Set to YES if you don't want this show to be published yet",
    )
    complete = models.CharField(
        max_length=3,
        choices=YES_OR_NO,
        help_text="Whether this show is complete. Set to YES if this show has concluded and will no longer be publishing new content",
    )

    def __str__(self):
        return f"{self.title} by {self.author}"


class Episode(models.Model):
    parent_show = models.ForeignKey(Show, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    file = models.FileField()
    file_type = models.CharField(max_length=20, choices=FILETYPES)
    guid = models.UUIDField(default=uuid.uuid4, editable=False)
    published_date = models.DateTimeField(
        help_text="The publication date of this episode. Used to determine what shows to include in the RSS feed"
    )
    description = models.TextField(max_length=3000)
    link = models.URLField(
        help_text="Link to a specific page for show notes for this episode"
    )

    # Itunes Specific Fields
    duration = models.IntegerField(
        null=False, blank=False, help_text="Length of episode in seconds"
    )
    image = models.ImageField(
        null=True,
        blank=True,
        help_text="Overrides the show art for this episode in specific. Defaults to Show art if null.",
        validators=[validate_show_art_is_optimally_sized],
    )
    explicit = models.CharField(max_length=5, choices=TRUE_OR_FALSE)

    def __str__(self):
        return f"{self.parent_show} : {self.title}"
