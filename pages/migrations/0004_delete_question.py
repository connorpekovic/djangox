# Generated by Django 3.1.4 on 2021-08-22 22:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_remove_response_the_question'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Question',
        ),
    ]
