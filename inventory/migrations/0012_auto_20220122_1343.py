# Generated by Django 3.2.8 on 2022-01-22 08:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0011_alter_product_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('contact_name', models.CharField(blank=True, max_length=100, null=True)),
                ('contact_number', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.company'),
        ),
    ]
