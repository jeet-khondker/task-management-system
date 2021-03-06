# Generated by Django 3.1.6 on 2021-02-04 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('email', models.EmailField(max_length=60, unique=True, verbose_name='Email Address')),
                ('full_name', models.CharField(max_length=30, verbose_name='Full Name')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='Member Since')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='Last Logged In')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
