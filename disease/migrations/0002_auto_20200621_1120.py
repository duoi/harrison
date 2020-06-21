# Generated by Django 3.0.7 on 2020-06-21 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('disease', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disease',
            name='name',
            field=models.TextField(blank=True, default=None, help_text='The name of the disease being referenced', null=True, unique=True),
        ),
    ]
