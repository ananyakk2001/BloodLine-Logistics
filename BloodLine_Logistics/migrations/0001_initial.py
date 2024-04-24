# Generated by Django 2.0.9 on 2023-12-28 07:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blood_name', models.CharField(default=1, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Blood_bank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock', models.CharField(max_length=100)),
                ('BLOOD_ID', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='BloodLine_Logistics.Blood')),
            ],
        ),
        migrations.CreateModel(
            name='Donor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('house', models.CharField(max_length=100)),
                ('pin', models.CharField(max_length=100)),
                ('post', models.CharField(max_length=100)),
                ('gender', models.CharField(default=1, max_length=100)),
                ('BLOOD_ID', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='BloodLine_Logistics.Blood')),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=100)),
                ('feedback', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('usertype', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
                ('BLOOD_ID', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='BloodLine_Logistics.Blood')),
            ],
        ),
        migrations.CreateModel(
            name='Request_allocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=100)),
                ('DONOR', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='BloodLine_Logistics.Donor')),
                ('REQUEST', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='BloodLine_Logistics.Request')),
            ],
        ),
        migrations.CreateModel(
            name='Seeker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=100)),
                ('BLOOD_ID', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='BloodLine_Logistics.Blood')),
                ('LOGIN', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='BloodLine_Logistics.Login')),
            ],
        ),
        migrations.AddField(
            model_name='request',
            name='SEEKER',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='BloodLine_Logistics.Seeker'),
        ),
        migrations.AddField(
            model_name='feedback',
            name='LOGIN',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='BloodLine_Logistics.Login'),
        ),
        migrations.AddField(
            model_name='donor',
            name='LOGIN',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='BloodLine_Logistics.Login'),
        ),
    ]
