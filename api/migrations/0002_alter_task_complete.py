# Generated by Django 3.2.9 on 2021-11-27 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='complete',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
