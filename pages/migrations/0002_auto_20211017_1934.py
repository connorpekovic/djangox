# Generated by Django 3.1.13 on 2021-10-17 19:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='response',
            old_name='Stregthen_social_safety_nets',
            new_name='Question1',
        ),
        migrations.RenameField(
            model_name='response',
            old_name='Nationalize_healthcare',
            new_name='Question2',
        ),
        migrations.RenameField(
            model_name='response',
            old_name='Climate_response',
            new_name='Question3',
        ),
        migrations.RenameField(
            model_name='response',
            old_name='Should_we_limit_urban_sprall',
            new_name='Question4',
        ),
        migrations.RenameField(
            model_name='response',
            old_name='Do_you_support_or_oppose_globalization',
            new_name='Question5',
        ),
    ]
