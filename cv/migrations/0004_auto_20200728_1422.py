# Generated by Django 2.2.12 on 2020-07-28 12:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0003_auto_20200727_1452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cv',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
