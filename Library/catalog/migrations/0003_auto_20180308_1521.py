# Generated by Django 2.0 on 2018-03-08 15:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20180306_2155'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='writer',
            new_name='author',
        ),
    ]