# Generated by Django 4.2.3 on 2023-08-12 17:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0010_newsout_data_public_from_site_newsout_site'),
    ]

    operations = [
        migrations.RenameField(
            model_name='new',
            old_name='data_public',
            new_name='data_public_from_site',
        ),
    ]
