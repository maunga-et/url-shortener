# Generated by Django 4.1.4 on 2022-12-21 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='url',
            name='unique_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]