from django.db import models


# Create your models here.
class Tasks(models.Model):
    """ Tasks Model Class
        Description tasks table """
    id = models.AutoField(primary_key=True)
    task_name = models.CharField(max_length=150)
    task_abbreviation = models.CharField(
        max_length=10, null=True, default=None)
    task_description = models.CharField(
        max_length=2000, null=True, default=None)
    points = models.IntegerField(null=False, default=None)

    class Meta:
        db_table = 'tasks'
