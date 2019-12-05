# Generated by Django 2.2.5 on 2019-12-05 06:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_relevancy_and_notes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vendor',
            name='slug',
        ),
        migrations.AlterField(
            model_name='vendor',
            name='shopify_vendor',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='vendor', to='shopify.ShopifyVendor'),
        ),
    ]
