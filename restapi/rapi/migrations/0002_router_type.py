# Generated by Django 3.2.3 on 2021-06-12 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rapi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='router',
            name='type',
            field=models.CharField(default='CSS', max_length=4),
        ),
    ]
