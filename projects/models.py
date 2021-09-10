from django.db import models
from django_resized import ResizedImageField

# Create your models here.

class projectsList(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=10)
    img = ResizedImageField(size=[800, 800], upload_to='project_pics', default='default.jpg', quality=75, force_format='JPEG')
    url = models.URLField()
    
    class Meta:
        db_table = "projects"

    def __str__(self):
        return f'{self.name} projectsList'