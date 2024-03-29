# Generated by Django 4.0.5 on 2022-08-07 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_blogslist_modifieddate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogslist',
            old_name='content',
            new_name='description',
        ),
        migrations.AddField(
            model_name='blogslist',
            name='html_blog_post',
            field=models.FileField(blank=True, default=None, null=True, upload_to='blog_html_files'),
        ),
    ]
