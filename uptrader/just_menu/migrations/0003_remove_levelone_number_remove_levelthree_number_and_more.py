# Generated by Django 5.0.4 on 2024-04-09 17:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('just_menu', '0002_alter_levelone_options_alter_levelthree_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='levelone',
            name='number',
        ),
        migrations.RemoveField(
            model_name='levelthree',
            name='number',
        ),
        migrations.RemoveField(
            model_name='leveltwo',
            name='number',
        ),
    ]
