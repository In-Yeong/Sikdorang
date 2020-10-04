# Generated by Django 2.2.7 on 2020-10-04 08:06

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
                ('start_date', models.IntegerField()),
                ('end_date', models.IntegerField()),
                ('price', models.IntegerField()),
                ('start_point', models.CharField(max_length=50)),
                ('start_time', models.CharField(max_length=30)),
                ('content', models.TextField()),
                ('limit_person', models.IntegerField()),
                ('departure_person', models.IntegerField()),
                ('now_person', models.IntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='GuideTour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=10)),
                ('phone_number', models.CharField(max_length=20)),
                ('trip_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='guide.TripItemModel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
