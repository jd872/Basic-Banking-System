# Generated by Django 3.1.2 on 2020-11-04 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0002_auto_20201103_2041'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='reg_id',
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
        ),
    ]
