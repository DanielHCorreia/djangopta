# Generated by Django 2.2.7 on 2019-11-13 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serie', models.CharField(max_length=100, verbose_name='Series')),
                ('hobbie', models.CharField(max_length=100, verbose_name='Hobbies')),
                ('emailContato', models.EmailField(max_length=254, null=True, verbose_name='Email')),
            ],
            options={
                'verbose_name': 'Pessoa',
                'verbose_name_plural': 'Pessoas',
                'ordering': ['serie'],
            },
        ),
    ]
