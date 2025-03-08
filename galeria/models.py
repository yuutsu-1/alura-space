from django.db import models

class NASAImage(models.Model):
    date = models.DateField(primary_key=True, null=False)
    explanation = models.TextField(null=False)
    media_type = models.CharField(max_length=20, null=False)
    service_version = models.CharField(max_length=10, null=False)
    title = models.CharField(max_length=225, null=False)
    url = models.URLField(null=False)
    hdurl = models.URLField()
    descricao = models.CharField(max_length=20, null=False)
    
    def __str__(self):
            return f"{self.date}: {self.title}"