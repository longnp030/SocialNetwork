# Generated by Django 3.1.4 on 2021-02-02 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupAdmin',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False, unique=True)),
                ('was', models.DateTimeField(auto_now_add=True, db_column='was')),
            ],
            options={
                'db_table': 'group_admin',
                'managed': False,
            },
        ),
    ]