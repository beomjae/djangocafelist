# Generated by Django 2.1.5 on 2019-01-17 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_cafe_mainphoto'),
    ]

    operations = [
        migrations.AddField(
            model_name='cafe',
            name='modifiedDate',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='cafe',
            name='publishedDate',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
