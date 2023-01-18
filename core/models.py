from django.db import models
from django.contrib.auth.models import User

class Url(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    url = models.URLField()
    unique_id = models.CharField(max_length=7, blank=True, null=True)
    clicks = models.PositiveBigIntegerField(null=True)

    def __str__(self):
        return self.url

class Click(models.Model):
    url = models.ForeignKey(Url, on_delete=models.CASCADE)
    ip_address = models.GenericIPAddressField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return f'{self.url.url}: {self.ip_address}'

    

