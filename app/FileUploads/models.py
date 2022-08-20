from django.db import models


# Create your models here.
class EpisodeFile(models.Model):
    name = models.CharField(max_length=128)
    episode_file = models.FileField()

    def __str__(self):
        return self.name
