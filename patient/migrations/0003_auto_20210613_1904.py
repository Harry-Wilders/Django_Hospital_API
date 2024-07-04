# Generated by Django 3.0.3 on 2021-06-13 19:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0001_initial'),
        ('patient', '0002_patient_history'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient_history',
            name='assigned_doctor',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='doctor.doctor'),
        ),
        migrations.AlterField(
            model_name='patient_history',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.patient'),
        ),
        migrations.AlterField(
            model_name='patient_history',
            name='release_date',
            field=models.DateField(blank=True, verbose_name='Release Date'),
        ),
        migrations.CreateModel(
            name='patient_discharge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_charge', models.PositiveIntegerField(verbose_name='Room charge')),
                ('medicine_cost', models.PositiveIntegerField(verbose_name='Medicine cost')),
                ('doctor_fee', models.PositiveIntegerField(verbose_name='Doctor Fee')),
                ('Other_charge', models.PositiveIntegerField(verbose_name='Other charges')),
                ('patient_details', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='patient.patient_history')),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appontment_date', models.DateField(verbose_name='Appointment date')),
                ('appointment_time', models.TimeField(verbose_name='Appointement time')),
                ('status', models.BooleanField(default=False)),
                ('doctor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='doctor.doctor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.patient_history')),
            ],
        ),
    ]
