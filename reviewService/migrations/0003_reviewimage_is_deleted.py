# Generated by Django 4.2.1 on 2023-08-01 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviewService', '0002_alter_review_feedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviewimage',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]