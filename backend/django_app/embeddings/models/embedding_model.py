from django.contrib.postgres.fields import ArrayField
from django.db import models

class EmbeddingModel(models.Model):
    text = models.TextField()
    embedding = ArrayField(models.FloatField(null=False, blank=True), blank=True)
    time = models.DateTimeField(auto_now_add=True)
    comment = models.TextField(blank=True, null=True)
