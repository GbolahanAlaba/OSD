# Generated by Django 4.2.1 on 2023-05-22 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp24', '0003_inventory_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventory',
            name='Type',
            field=models.CharField(blank=True, choices=[('New', 'New'), ('Used', 'Used')], default='', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='inventory',
            name='Vendor',
            field=models.CharField(blank=True, choices=[('China', 'China'), ('Dubai', 'Dubai')], default='', max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='Comments',
            field=models.TextField(blank=True, default='', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='Product',
            field=models.CharField(blank=True, default='', max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='Quantity',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
