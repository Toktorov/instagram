# Generated by Django 2.2.6 on 2021-06-04 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0002_remove_tag_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
