# Generated by Django 5.0.4 on 2024-04-10 12:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('just_menu', '0005_remove_third_level_two_rename_first_country_brand_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='brand',
            old_name='level_one',
            new_name='brand_fk',
        ),
        migrations.RenameField(
            model_name='brand',
            old_name='second_level',
            new_name='brand_name',
        ),
        migrations.RenameField(
            model_name='country',
            old_name='first_level',
            new_name='country',
        ),
        migrations.RenameField(
            model_name='model',
            old_name='level_two',
            new_name='model_fk',
        ),
        migrations.RenameField(
            model_name='model',
            old_name='third_level',
            new_name='model_name',
        ),
    ]
