# Generated by Django 4.1 on 2022-08-05 17:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_rename_choices_choice'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='choices_text',
            new_name='choice_text',
        ),
    ]
