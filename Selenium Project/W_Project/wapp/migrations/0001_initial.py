# Generated by Django 4.2.2 on 2024-06-21 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('artist_name', models.CharField(max_length=255)),
                ('program_name', models.CharField(max_length=255)),
                ('artist_role', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('auditorium', models.CharField(max_length=255)),
            ],
        ),
    ]
