# Generated by Django 5.1.1 on 2024-09-25 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0002_patient'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_name', models.CharField(max_length=100)),
                ('appointment_date', models.DateField(unique=True)),
                ('appointment_time', models.TimeField()),
                ('description', models.TextField()),
            ],
        ),
    ]
