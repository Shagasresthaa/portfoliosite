from django.db import models

# Create your models here.

class projectsList(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=10)
    url = models.URLField()
    
    class Meta:
        db_table = "projects"