# Generated by Django 3.0b1 on 2020-03-21 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_profile_date_of_account_creation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Paytm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.IntegerField()),
            ],
        ),
    ]
