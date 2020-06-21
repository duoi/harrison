# Generated by Django 3.0.7 on 2020-06-21 03:58

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClassificationStandard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('name', models.TextField(help_text='The name of this standard (ICD-10, ICD-9 etc)')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ClassificationCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('identifier', models.TextField(blank=True, default=None, help_text="Classification standard's code for this condition", null=True)),
                ('description', models.TextField(blank=True, default=None, help_text='The shorthand description for this condition', null=True)),
                ('standard', models.ForeignKey(blank=True, default=None, help_text='The classification standard (ICD-10, SNOMED-CT etc)', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='classification.ClassificationStandard')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
