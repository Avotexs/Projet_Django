# Generated by Django 5.0.4 on 2024-05-02 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VoyageEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('date', models.DateField()),
                ('location', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='voyage_events/')),
            ],
        ),
    ]
