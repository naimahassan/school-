# Generated by Django 2.2.1 on 2019-05-28 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_course_trainer'),
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='courses',
            field=models.ManyToManyField(to='course.Course'),
        ),
    ]
