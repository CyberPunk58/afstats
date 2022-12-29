# Generated by Django 4.1 on 2022-12-25 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=30)),
                ('team_logo', models.ImageField(upload_to='teams/logo')),
                ('color', models.CharField(max_length=30)),
                ('reserve_color', models.CharField(max_length=30)),
                ('url', models.URLField(blank=True)),
            ],
        ),
    ]
