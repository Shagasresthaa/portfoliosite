# Generated by Django 3.2.7 on 2021-09-10 08:49

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_projectslist_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectslist',
            name='img',
            field=django_resized.forms.ResizedImageField(crop=None, default='default.jpg', force_format=None, keep_meta=True, quality=0, size=[800, 800], upload_to='project_pics'),
        ),
    ]
