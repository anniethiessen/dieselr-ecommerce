# Generated by Django 2.2.5 on 2019-10-27 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sema', '0029_semacategory_notes'),
    ]

    operations = [
        migrations.AddField(
            model_name='semaproduct',
            name='notes',
            field=models.TextField(blank=True),
        ),
    ]
