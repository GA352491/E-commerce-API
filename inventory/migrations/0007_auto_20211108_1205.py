# Generated by Django 3.2.8 on 2021-11-08 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0006_auto_20211108_1041'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='ex_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='mf_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
