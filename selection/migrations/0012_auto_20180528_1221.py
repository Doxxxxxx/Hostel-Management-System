# Generated by Django 2.0.5 on 2018-05-28 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('selection', '0011_auto_20180528_1220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default=None, max_length=1, null=True),
        ),
    ]