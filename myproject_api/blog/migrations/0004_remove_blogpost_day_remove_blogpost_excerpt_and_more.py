# Generated by Django 4.0.4 on 2022-05-28 11:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_blogpost_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='day',
        ),
        migrations.RemoveField(
            model_name='blogpost',
            name='excerpt',
        ),
        migrations.RemoveField(
            model_name='blogpost',
            name='month',
        ),
    ]
