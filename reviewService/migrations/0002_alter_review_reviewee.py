# Generated by Django 4.2 on 2023-05-07 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviewService', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='reviewee',
            field=models.CharField(default='Anonymous', max_length=200),
        ),
    ]
