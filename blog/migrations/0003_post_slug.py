# Generated by Django 2.2 on 2019-12-19 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20191210_0914'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.CharField(default=2, max_length=120),
            preserve_default=False,
        ),
    ]