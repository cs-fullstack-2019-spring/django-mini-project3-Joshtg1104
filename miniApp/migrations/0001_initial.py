# Generated by Django 2.2 on 2019-03-01 16:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TeacherTimeModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher_name', models.CharField(default='', max_length=50)),
                ('school_name', models.CharField(default='', max_length=100)),
                ('subject_teaching', models.CharField(default='', max_length=100)),
                ('hours_taught', models.IntegerField(default=1, max_length=2)),
                ('date_of_work', models.DateField()),
                ('date_of_entry', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]