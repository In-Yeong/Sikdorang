# Generated by Django 2.2.7 on 2020-10-04 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='done_cup',
            field=models.IntegerField(default=0),
        ),
    ]