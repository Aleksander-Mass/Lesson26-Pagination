# Generated by Django 3.0.3 on 2020-03-26 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0003_auto_20200312_2042'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='rating',
            field=models.PositiveSmallIntegerField(default=1),
        ),
    ]