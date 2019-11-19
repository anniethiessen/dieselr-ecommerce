# Generated by Django 2.2.5 on 2019-11-15 22:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shopify', '0018_shopifyproductcalculator'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopifycollection',
            name='handle',
            field=models.SlugField(blank=True, help_text='Populated by Shopify', max_length=150),
        ),
        migrations.AddField(
            model_name='shopifycollection',
            name='parent_collection',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='child_collections', to='shopify.ShopifyCollection'),
        ),
        migrations.CreateModel(
            name='ShopifyCollectionCalculator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collection', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='calculator', to='shopify.ShopifyCollection')),
            ],
        ),
    ]
