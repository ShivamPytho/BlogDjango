# Generated by Django 2.2 on 2019-12-23 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_signup'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='signup',
            name='timeStamp',
        ),
        migrations.AlterField(
            model_name='signup',
            name='password',
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name='signup',
            name='uname',
            field=models.CharField(max_length=10),
        ),
    ]