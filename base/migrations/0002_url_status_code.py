# Generated by Django 2.1.2 on 2018-10-31 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='url',
            name='status_code',
            field=models.IntegerField(null=True),
        ),
    ]