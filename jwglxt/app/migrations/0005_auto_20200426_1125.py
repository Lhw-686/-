# Generated by Django 2.2.11 on 2020-04-26 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20200426_1113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='teacher_come_year',
            field=models.DateTimeField(null=True, verbose_name='入职日期'),
        ),
    ]
