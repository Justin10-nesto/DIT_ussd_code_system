# Generated by Django 4.1 on 2023-05-31 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=50)),
                ('registration_no', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=255)),
                ('index_number', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=15, null=True)),
            ],
            options={
                'verbose_name': 'Student',
                'db_table': 'Student',
            },
        ),
    ]
