# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(verbose_name='last login', null=True, blank=True)),
                ('is_superuser', models.BooleanField(verbose_name='superuser status', default=False, help_text='Designates that this user has all permissions without explicitly assigning them.')),
                ('email', models.EmailField(max_length=255, verbose_name='email address', db_index=True, unique=True)),
                ('is_staff', models.BooleanField(verbose_name='staff status', default=False, help_text='Designates whether the user can log into this admin site.')),
                ('is_active', models.BooleanField(verbose_name='active', default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.')),
                ('date_joined', models.DateTimeField(verbose_name='date joined', default=django.utils.timezone.now)),
                ('avatar', models.ImageField(verbose_name='Profile Image', upload_to='users/%Y/%m/%d', blank=True)),
                ('full_name', models.CharField(max_length=100, verbose_name='Full name', default='', null=True, blank=True)),
                ('groups', models.ManyToManyField(verbose_name='groups', to='auth.Group', help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_query_name='user', blank=True, related_name='user_set')),
                ('user_permissions', models.ManyToManyField(verbose_name='user permissions', to='auth.Permission', help_text='Specific permissions for this user.', related_query_name='user', blank=True, related_name='user_set')),
                ('user_type', models.ForeignKey(null=True, to='contenttypes.ContentType', editable=False)),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
                'ordering': ('email',),
            },
        ),
    ]
