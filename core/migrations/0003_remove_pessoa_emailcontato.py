# Generated by Django 2.2.7 on 2019-11-13 13:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20191113_1022'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pessoa',
            name='emailContato',
        ),
    ]
