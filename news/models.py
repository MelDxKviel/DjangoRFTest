from django.db import models


class Type(models.Model):
    name = models.CharField(max_length=25)
    color = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=120)
    short_description = models.TextField()
    description = models.TextField()
    type = models.ForeignKey(Type, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.title
