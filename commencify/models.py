from django.db import models

# Create your models here.
class employee(models.Model):
    name=models.CharField(max_length=50)
    phone = models.PositiveBigIntegerField()
    email=models.EmailField(unique=True)
    department=models.CharField(max_length=50)
    password=models.CharField(max_length=50)

    emp_id = models.CharField(null=True, max_length=50)
    # COMMENCIFY
    grant = models.BooleanField(null=True, default=False)
    revoke = models.BooleanField(null=True, default=False)
    # FIBROANALYSIS
    accept = models.BooleanField(null=True, default=False)
    decline = models.BooleanField(null=True, default=False)
    # ECOTOXIFY
    admit = models.BooleanField(null=True, default=False)
    deny = models.BooleanField(null=True, default=False)

