# Generated by Django 4.1.3 on 2022-12-04 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("board", "0006_auto_20221203_2021"),
    ]

    operations = [
        migrations.AlterField(
            model_name="board",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="category",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="reply",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]