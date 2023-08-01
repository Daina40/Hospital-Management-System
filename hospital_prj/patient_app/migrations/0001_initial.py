# Generated by Django 4.2.3 on 2023-07-31 04:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dr_details_app', '0002_remove_doctors_hospital_name_alter_doctors_contact'),
        ('hospital_app', '0003_delete_doctors'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specialized', models.CharField(max_length=200, null=True)),
                ('patient_name', models.CharField(max_length=100)),
                ('patient_age', models.CharField(max_length=20)),
                ('patient_contact', models.CharField(max_length=20)),
                ('appointment_sl', models.IntegerField(default=1)),
                ('appointment_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dr_details_app.doctors')),
                ('hospital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital_app.hospital')),
            ],
        ),
    ]