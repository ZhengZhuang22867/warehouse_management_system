from django.db import models

# Create your models here.
class Manager(models.Model):
    manager_name = models.CharField(primary_key=True, max_length=255)
    manager_pw = models.CharField(max_length=255)
    manager_age = models.IntegerField(blank=True, null=True)
    manager_email = models.CharField(max_length=255, blank=True, null=True)
    manager_telephone = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'manager'