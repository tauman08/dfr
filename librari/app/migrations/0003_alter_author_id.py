# Generated by Django 4.1.4 on 2023-01-15 12:14

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_author_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='id',
            field=models.UUIDField(default=uuid.UUID('e055d7e9-f2f0-42d0-89e4-4fff6d60d27e'), primary_key=True, serialize=False),
        ),
    ]
