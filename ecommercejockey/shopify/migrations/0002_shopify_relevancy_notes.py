# Generated by Django 2.2.5 on 2019-11-05 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopify', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopifycollection',
            name='is_relevant',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='shopifycollection',
            name='notes',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='shopifyproduct',
            name='is_relevant',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='shopifyproduct',
            name='notes',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='shopifycollection',
            name='body_html',
            field=models.TextField(blank=True),
        ),
    ]
