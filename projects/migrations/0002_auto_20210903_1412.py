# Generated by Django 3.2.6 on 2021-09-03 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectslist',
            name='end_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='projectslist',
            name='start_date',
            field=models.DateField(),
        ),
    ]