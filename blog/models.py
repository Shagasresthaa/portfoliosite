from django.db import models
from django_resized import ResizedImageField

# Create your models here.

class blogsList(models.Model):
    postId = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=150)
    blogHeaderImage = ResizedImageField(size=[500, 500], upload_to='blog_pics', default='default.jpg', quality=85, force_format='JPEG')
    description = models.TextField()
    publishedDate = models.DateTimeField()
    isModified = models.BooleanField(default=False)
    html_blog_post = models.FileField(upload_to='blog_html_files', blank=True, null=True, default=None)
    modifiedDate = models.DateTimeField()

    class Meta:
        db_table = "blogs"

    def __str__(self):
        return f'{self.title} blogsList'
