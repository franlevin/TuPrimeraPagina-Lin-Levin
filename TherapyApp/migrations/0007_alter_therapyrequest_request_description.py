# Generated by Django 4.2.5 on 2023-10-23 03:09

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TherapyApp', '0006_delete_patient_delete_profesional'),
    ]

    operations = [
        migrations.AlterField(
            model_name='therapyrequest',
            name='request_description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
