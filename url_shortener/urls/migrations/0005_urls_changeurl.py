# Generated by Django 3.0.7 on 2020-06-18 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urls', '0004_urls_counting'),
    ]

    operations = [
        migrations.AddField(
            model_name='urls',
            name='changeurl',
            field=models.URLField(default=1),
            preserve_default=False,
        ),
    ]