# Generated by Django 4.1.4 on 2022-12-25 10:30

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='id',
            field=models.UUIDField(default=uuid.UUID('1da6af7b-ce29-443d-9ebd-e8947ac66460'), primary_key=True, serialize=False),
        ),
    ]