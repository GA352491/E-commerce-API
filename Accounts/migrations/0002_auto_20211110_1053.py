# Generated by Django 3.2.8 on 2021-11-10 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shipping',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='shipping',
            name='pincode',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
