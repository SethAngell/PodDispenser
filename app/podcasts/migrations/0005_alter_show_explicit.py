# Generated by Django 4.0.2 on 2022-08-23 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("podcasts", "0004_episode_html_description_alter_show_title"),
    ]

    operations = [
        migrations.AlterField(
            model_name="show",
            name="explicit",
            field=models.CharField(
                choices=[("True", "True"), ("False", "False")],
                default="False",
                max_length=5,
            ),
        ),
    ]
