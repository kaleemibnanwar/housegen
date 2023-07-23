# Generated by Django 4.2.2 on 2023-07-16 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='New Project', max_length=255)),
                ('number_of_rooms', models.IntegerField()),
                ('input_data_json', models.CharField(max_length=2048)),
                ('output_data_json', models.CharField(max_length=2048)),
            ],
        ),
    ]
