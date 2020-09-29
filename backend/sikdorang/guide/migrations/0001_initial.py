# Generated by Django 2.2.7 on 2020-09-29 02:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TripItemModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_img', models.ImageField(blank=True, upload_to='guide/%Y/%m/%d')),
                ('title', models.CharField(max_length=100)),
                ('area', models.CharField(max_length=50)),
                ('start_date', models.CharField(max_length=30)),
                ('end_date', models.CharField(max_length=30)),
                ('price', models.IntegerField()),
                ('start_point', models.CharField(max_length=50)),
                ('start_time', models.CharField(max_length=30)),
                ('content', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='GuideTour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trip_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='guide.TripItemModel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
