# Generated by Django 5.0.4 on 2024-04-30 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=255)),
                ('make', models.CharField(max_length=255)),
                ('year', models.IntegerField()),
                ('price', models.IntegerField()),
                ('color', models.CharField(max_length=255)),
                ('type', models.CharField(max_length=255)),
            ],
        ),
    ]
