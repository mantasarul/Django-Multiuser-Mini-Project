from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    item = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.item}"

    # class Meta:
    #     order_with_respect_to = 'user'