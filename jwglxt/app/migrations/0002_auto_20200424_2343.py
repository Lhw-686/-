# Generated by Django 2.2.11 on 2020-04-24 15:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursearrangement',
            name='course_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.Course', verbose_name='课程号'),
        ),
        migrations.AlterField(
            model_name='coursearrangement',
            name='teacher_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.Teacher', verbose_name='工号'),
        ),
        migrations.AlterField(
            model_name='message',
            name='student_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.Student', verbose_name='学号'),
        ),
        migrations.AlterField(
            model_name='selectcourse',
            name='course_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.Course', verbose_name='课程号'),
        ),
        migrations.AlterField(
            model_name='selectcourse',
            name='student_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.Student', verbose_name='学号'),
        ),
        migrations.AlterField(
            model_name='selectlist',
            name='course_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.Course', verbose_name='课程号'),
        ),
    ]
