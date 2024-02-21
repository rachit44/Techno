# Generated by Django 4.2.10 on 2024-02-20 08:46

import TechnoCoder.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TechnoCoder', '0004_questions_snippet_alter_choice_text_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='profile_picture',
            field=models.ImageField(blank=True, default=TechnoCoder.models.default_profile_picture, upload_to='profile_pictures/'),
        ),
    ]
