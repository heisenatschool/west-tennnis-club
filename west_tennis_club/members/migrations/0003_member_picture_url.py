# Generated by Django 5.0.6 on 2024-06-25 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_member_birthdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='picture_url',
            field=models.CharField(default='#', max_length=255),
        ),
    ]
