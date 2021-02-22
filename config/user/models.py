from django.db import models

# Create your models here.
class User(models.Model):
    u_no = models.IntegerField(primary_key=True)
    user_id = models.CharField(unique=True, max_length=50)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'user'