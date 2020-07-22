from django.db import models

class BlogModel(models.Model):
    title = models.CharField(max_length=1000)
    content = models.TextField(blank=True)

    def __str__(self):
        return self.title