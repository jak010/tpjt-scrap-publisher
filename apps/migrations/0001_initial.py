# Generated by Django 4.1.4 on 2022-12-17 11:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=36, unique=True, verbose_name='user_email')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('date_of_join', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=True)),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'member',
            },
        ),
        migrations.CreateModel(
            name='GroupSubScribe',
            fields=[
                ('reference_id', models.AutoField(primary_key=True, serialize=False)),
                ('author', models.CharField(max_length=36, verbose_name='author')),
                ('sub_domain', models.CharField(max_length=36, verbose_name='sub_domain')),
                ('domain', models.CharField(max_length=36, verbose_name='domain')),
                ('top_level_domain', models.CharField(max_length=36, verbose_name='top_level_domain')),
                ('date_of_create', models.DateTimeField(auto_now=True)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.group', verbose_name='group')),
            ],
            options={
                'db_table': 'group_subscribe',
            },
        ),
        migrations.CreateModel(
            name='PublishMemberHistory',
            fields=[
                ('reference_id', models.AutoField(primary_key=True, serialize=False)),
                ('receiver', models.CharField(max_length=128)),
                ('title', models.CharField(max_length=256)),
                ('content', models.TextField()),
                ('description', models.CharField(max_length=512)),
                ('date_of_create', models.DateTimeField(auto_now_add=True)),
                ('sender', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'publish_member_history',
            },
        ),
        migrations.CreateModel(
            name='PublishGroupHistory',
            fields=[
                ('reference_id', models.AutoField(primary_key=True, serialize=False)),
                ('date_of_create', models.DateTimeField(auto_now_add=True)),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='auth.group')),
                ('member', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('subscribe', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='apps.groupsubscribe')),
            ],
            options={
                'db_table': 'publish_group_history',
            },
        ),
    ]
