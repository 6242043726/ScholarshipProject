# Generated by Django 4.1.4 on 2022-12-18 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scholarshipmanager', '0022_alter_student_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='picture',
            field=models.ImageField(blank=True, default='images/default_profile_pic.png', null=True, upload_to='images/'),
        ),
    ]
