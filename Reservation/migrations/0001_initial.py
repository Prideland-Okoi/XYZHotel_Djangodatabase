# Generated by Django 4.0.4 on 2022-06-17 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lodge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_number', models.IntegerField()),
                ('room_type', models.CharField(max_length=1500)),
                ('amount', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Lodging',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1500)),
                ('email', models.EmailField(max_length=1500)),
                ('occupation', models.CharField(max_length=1500)),
                ('room_number', models.PositiveIntegerField()),
                ('ammount_paid', models.IntegerField()),
                ('number_of_night', models.PositiveIntegerField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
            ],
        ),
    ]