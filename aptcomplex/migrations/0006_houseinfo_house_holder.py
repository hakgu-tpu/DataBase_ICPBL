# Generated by Django 3.1.3 on 2022-12-05 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aptcomplex', '0005_remove_houseinfo_house_holder'),
    ]

    operations = [
        migrations.AddField(
            model_name='houseinfo',
            name='house_holder',
            field=models.CharField(blank=True, max_length=16),
        ),
    ]
