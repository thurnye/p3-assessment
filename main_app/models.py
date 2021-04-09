from django.db import models
from django.urls import reverse

# Create your models here.
class WackyWidget(models.Model):
    description = models.CharField(max_length=70)
    quantity = models.IntegerField(default=0)

    # def __str__(self):
    #     return self.description

    # def __int__(self):
    #     return self.quantity

    def get_absolute_url(self):
        return reverse('index', kwargs={'pk': self.id})