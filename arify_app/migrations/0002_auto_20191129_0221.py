# Generated by Django 2.2.7 on 2019-11-29 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arify_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ar_object',
            name='pos_offset_x',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=3),
        ),
        migrations.AddField(
            model_name='ar_object',
            name='pos_offset_y',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=3),
        ),
        migrations.AddField(
            model_name='ar_object',
            name='pos_offset_z',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=3),
        ),
    ]
