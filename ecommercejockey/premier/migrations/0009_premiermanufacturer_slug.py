# Generated by Django 2.2.5 on 2019-12-05 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('premier', '0008_relevancy_and_notes'),
    ]

    operations = [
        migrations.AddField(
            model_name='premiermanufacturer',
            name='slug',
            field=models.CharField(blank=True, null=True, max_length=20, unique=True),
        ),
    ]
