from django.conf import settings
from django.db import models

# Create your models here.

USER_MODEL = settings.AUTH_USER_MODEL


class Post(models.Model):
    author = models.ForeignKey(
        USER_MODEL, verbose_name="Autor", on_delete=models.CASCADE
    )
    creation_date = models.DateTimeField("Erstellungsdatum", auto_now_add=True)
    edit_date = models.DateTimeField("Bearbeitungsdatum", auto_now=False)
    text = models.CharField("Text", max_length=1024)
    title = models.CharField("Titel", max_length=255)

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, verbose_name="Post", on_delete=models.CASCADE)
    author = models.ForeignKey(
        USER_MODEL, verbose_name="Autor", on_delete=models.CASCADE
    )
    creation_date = models.DateTimeField("Erstellungsdatum", auto_now_add=True)
    text = models.CharField("Text", max_length=512)

    class Meta:
        verbose_name = "Kommentar"
        verbose_name_plural = "Kommentare"

    def __str__(self):
        return self.text[:50]
