# Generated by Django 2.0.5 on 2018-05-28 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('selection', '0010_auto_20180527_1445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='dob',
            field=models.DateField(help_text='format : YYYY-MM-DD', max_length=10, null=True),
        ),
    ]