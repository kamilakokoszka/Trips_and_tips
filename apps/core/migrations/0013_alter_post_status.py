# Generated by Django 4.2.6 on 2023-11-18 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_alter_comment_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[(0, 'Draft'), (1, 'Publish')]),
        ),
    ]
