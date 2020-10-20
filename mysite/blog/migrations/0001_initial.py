# Generated by Django 3.1.2 on 2020-10-18 00:44

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('postDate', models.DateField(default=datetime.datetime(2020, 10, 18, 0, 44, 8, 621913, tzinfo=utc))),
                ('post_update', models.DateField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]