# Generated by Django 4.2 on 2023-04-30 15:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviewService', '0002_rename_image_review_attachments_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='attachments',
        ),
    ]