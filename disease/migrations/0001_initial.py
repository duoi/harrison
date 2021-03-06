# Generated by Django 3.0.7 on 2020-06-22 03:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('classification', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Disease',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('name', models.TextField(blank=True, default=None, help_text='The name of the disease being referenced', null=True, unique=True)),
                ('created_by', models.ForeignKey(editable=False, help_text='The user that created this disease entry', on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('icd_10_reference', models.ForeignKey(blank=True, default=None, help_text='The ICD-10 code for this disease', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='icd_10_disease', to='classification.ClassificationCode')),
                ('icd_9_reference', models.ForeignKey(blank=True, default=None, help_text='The ICD-9 code for this disease', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='icd_9_disease', to='classification.ClassificationCode')),
                ('snomed_ct_reference', models.ForeignKey(blank=True, default=None, help_text='The SNOMED-CT code for this disease', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='snomed_ct_disease', to='classification.ClassificationCode')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
