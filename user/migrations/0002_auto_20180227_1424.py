# Generated by Django 2.0.2 on 2018-02-27 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='funds',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=8),
        ),
    ]