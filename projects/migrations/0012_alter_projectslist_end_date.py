# Generated by Django 3.2.7 on 2021-11-02 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0011_alter_projectslist_end_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectslist',
            name='end_date',
            field=models.DateField(blank=True, default=None, null=True),
        ),
    ]
