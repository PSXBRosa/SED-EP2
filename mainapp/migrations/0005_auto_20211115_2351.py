# Generated by Django 3.2.9 on 2021-11-16 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_auto_20211115_2349'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='categories',
            field=models.ManyToManyField(to='mainapp.Category'),
        ),
        migrations.DeleteModel(
            name='Post_Category',
        ),
    ]