# Generated by Django 3.1.4 on 2021-01-30 15:53

from django.db import migrations, models
import group.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False, unique=True)),
                ('cover_image', models.ImageField(db_column='cover_image', max_length=255, upload_to=group.models.image_upload_location)),
                ('name', models.CharField(db_column='name', max_length=255, verbose_name='group_name')),
                ('description', models.CharField(db_column='description', max_length=1000, verbose_name='group_description')),
            ],
            options={
                'db_table': 'group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='GroupMember',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False, unique=True)),
            ],
            options={
                'db_table': 'group_member',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='GroupPost',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False, unique=True)),
            ],
            options={
                'db_table': 'group_post',
                'managed': False,
            },
        ),
    ]