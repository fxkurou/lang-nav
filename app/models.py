from django.db import models
from django.utils.translation import gettext_lazy as _


class Article(models.Model):
    title = models.CharField(_("title"), max_length=200)
    content = models.TextField(_("content"))
    published_date = models.DateTimeField()

    def __str__(self):
        return self.title