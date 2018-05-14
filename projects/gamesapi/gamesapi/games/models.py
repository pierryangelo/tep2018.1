from django.db import models


class Game(models.Model):
    created = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=200, blank=True,
                            default=True)
    release_date = models.DateTimeField()
    game_category = models.CharField(max_length=200, blank=True,
                                     default='')
    played = models.BooleanField(default=False)

    class Meta:
        ordering = ('name',)

