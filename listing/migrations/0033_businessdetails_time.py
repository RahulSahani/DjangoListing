# Generated by Django 4.1.1 on 2022-09-24 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0032_rename_time_contactus_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='businessdetails',
            name='time',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
    ]