# Generated by Django 4.1.4 on 2023-01-18 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinemaapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cinema',
            name='img',
            field=models.ImageField(default='addjyy', upload_to='gallery'),
            preserve_default=False,
        ),
    ]