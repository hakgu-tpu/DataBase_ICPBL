# Generated by Django 3.1.3 on 2022-12-05 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0004_auto_20221205_1533'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_building_num',
            field=models.IntegerField(default=0, max_length=16, verbose_name='동정보'),
        ),
    ]