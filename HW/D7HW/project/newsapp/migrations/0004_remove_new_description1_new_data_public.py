# Generated by Django 4.1.5 on 2023-02-14 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0003_new_description1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='new',
            name='description1',
        ),
        migrations.AddField(
            model_name='new',
            name='data_public',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]