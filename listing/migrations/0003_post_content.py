# Generated by Django 4.1.1 on 2022-09-10 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0002_category_rename_countrypages_countrypage_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='content',
            field=models.TextField(max_length=500, null=True),
        ),
    ]
