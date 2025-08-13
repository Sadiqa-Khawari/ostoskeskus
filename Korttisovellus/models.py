from django.db import models


class Kortti(models.Model):
    otsikko = models.CharField(max_length=100)
    kuvaus = models.TextField()

    def __str__(self):
        return self.otsikko

