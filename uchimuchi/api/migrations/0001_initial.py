# Generated by Django 4.2.18 on 2025-02-05 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BaseVocab',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('char', models.CharField(max_length=200)),
                ('phen', models.CharField(max_length=200)),
                ('trans', models.CharField(max_length=200)),
            ],
        ),
    ]
