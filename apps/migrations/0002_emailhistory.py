# Generated by Django 4.1.4 on 2022-12-15 07:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailHistory',
            fields=[
                ('date_of_create', models.DateTimeField(auto_created=True, auto_now_add=True)),
                ('date_of_resend', models.DateTimeField(auto_created=True, auto_now_add=True)),
                ('date_of_send', models.DateTimeField(auto_created=True)),
                ('reference_id', models.AutoField(primary_key=True, serialize=False)),
                ('sender', models.CharField(max_length=36)),
                ('receiver', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
