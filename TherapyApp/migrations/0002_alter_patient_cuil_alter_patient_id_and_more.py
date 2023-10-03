# Generated by Django 4.2.5 on 2023-10-03 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TherapyApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='cuil',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='patient',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='profesional',
            name='cuil',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='profesional',
            name='fee',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='profesional',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='profesional',
            name='score',
            field=models.IntegerField(),
        ),
    ]