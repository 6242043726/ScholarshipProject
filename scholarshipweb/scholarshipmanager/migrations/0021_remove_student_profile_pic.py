# Generated by Django 4.1.4 on 2022-12-15 13:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scholarshipmanager', '0020_student_source_of_debt'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='profile_pic',
        ),
    ]