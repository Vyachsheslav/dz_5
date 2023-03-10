# Generated by Django 4.1.5 on 2023-01-30 09:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Measurement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('sensor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='measurement', to='measurement.sensor')),
            ],
        ),
    ]
