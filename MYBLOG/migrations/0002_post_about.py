# Generated by Django 2.1.2 on 2018-11-01 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MYBLOG', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='about',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]