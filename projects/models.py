from django.db import models
from django_resized import ResizedImageField

# Create your models here.

class projectsList(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    short_description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True, default=None)
    status = models.CharField(max_length=20)
    img = ResizedImageField(size=[800, 800], upload_to='project_pics', default='default.jpg', quality=75, force_format='JPEG')
    html_files = models.FileField(upload_to='html_files', blank=True, null=True, default=None)
    url = models.URLField()
    
    class Meta:
        db_table = "projects"

    def __str__(self):
        return f'{self.name} projectsList'