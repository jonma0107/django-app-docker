# Generated by Django 4.1.3 on 2023-02-13 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drf', '0008_alter_drf_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drf',
            name='state',
            field=models.IntegerField(choices=[(1, 'BACKLOG'), (2, 'TO DO'), (3, 'DOING'), (4, 'TEST'), (5, 'DONE')]),
        ),
    ]
