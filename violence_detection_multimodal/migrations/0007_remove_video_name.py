# Generated by Django 4.0.2 on 2022-02-22 16:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('colorapp', '0006_alter_audio_audiofile_alter_audio_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='name',
        ),
    ]
