from django.db import models

# Create your models here.
class Owner(models.Model):
    first_name = models.CharField("First name", max_length=50)
    last_name = models.CharField("Last name", max_length=50)
    age = models.IntegerField("Age", null=True, blank=True)
    adoption = models.BooleanField("Adoption", default=False)
