# Generated by Django 4.1.4 on 2022-12-30 14:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecommandLink',
            fields=[
                ('reference_id', models.AutoField(primary_key=True, serialize=False)),
                ('sub_domain', models.CharField(max_length=36, verbose_name='sub_domain')),
                ('domain', models.CharField(max_length=36, verbose_name='domain')),
                ('top_level_domain', models.CharField(max_length=36, verbose_name='top_level_domain')),
                ('rate', models.IntegerField(verbose_name='rate')),
                ('like', models.IntegerField(verbose_name='like')),
                ('hit', models.IntegerField(verbose_name='hit count')),
                ('register', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'recommand_link',
            },
        ),
    ]
