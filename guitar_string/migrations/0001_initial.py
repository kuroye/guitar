# Generated by Django 4.0.4 on 2022-06-02 12:53

from django.db import migrations, models
import guitar_string.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('guitar_string', models.JSONField(default=guitar_string.models.Song.string_default, verbose_name='StringInfo')),
            ],
        ),
    ]
