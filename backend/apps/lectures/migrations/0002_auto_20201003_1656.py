# Generated by Django 3.1.1 on 2020-10-03 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lectures', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lecture',
            name='duration',
            field=models.IntegerField(default=2, help_text='Enter number of hours'),
        ),
        migrations.AddField(
            model_name='lecture',
            name='is_required',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='lecture',
            name='lecturer_name',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]
