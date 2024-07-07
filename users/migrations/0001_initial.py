# Generated by Django 5.0.4 on 2024-07-03 14:42

import django.contrib.auth.models
import django.utils.timezone
import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=35, null=True, region=None, verbose_name='phone number')),
                ('tg_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='tg name')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='users/avatars', verbose_name='avatar')),
                ('city', models.CharField(blank=True, choices=[('Moscow', 'Moscow'), ('Saint Petersburg', 'Saint Petersburg'), ('Novosibirsk', 'Novosibirsk'), ('Kazan', 'Kazan'), ('Krasnoyarsk', 'Krasnoyarsk'), ('Yekaterinburg', 'Yekaterinburg'), ('Omsk', 'Omsk'), ('Tomsk', 'Tomsk')], max_length=50, null=True, verbose_name='city')),
                ('is_active', models.BooleanField(default=False, verbose_name='is active')),
                ('verification_token', models.CharField(blank=True, max_length=50, null=True, verbose_name='Verification Token')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
