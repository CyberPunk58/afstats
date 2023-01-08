# Generated by Django 4.1.5 on 2023-01-08 19:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_1', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='teams.team')),
            ],
        ),
    ]