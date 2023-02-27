# Generated by Django 4.1.4 on 2022-12-14 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scholarshipmanager', '0018_student_dormitory_alter_student_address_type_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='other_doc',
            field=models.FileField(blank=True, null=True, upload_to='other_doc/'),
        ),
        migrations.AddField(
            model_name='student',
            name='picture',
            field=models.ImageField(blank=True, default='images/target.jpg', null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='student',
            name='schorlarship_doc',
            field=models.FileField(blank=True, null=True, upload_to='schorlarship_doc/'),
        ),
        migrations.AlterField(
            model_name='student',
            name='case_separated',
            field=models.CharField(blank=True, choices=[('บิดา', 'บิดา'), ('มารดา', 'มารดา')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='level_necessity',
            field=models.CharField(blank=True, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='status_parent',
            field=models.CharField(blank=True, choices=[('อยู่ด้วยกัน', 'อยู่ด้วยกัน'), ('หย่าร้าง', 'หย่าร้าง'), ('แยกกันอยู่', 'แยกกันอยู่ *ตอบข้อถัดไป'), ('บิดาถึงแก่กรรม', 'บิดาถึงแก่กรรม'), ('มารดาถึงแก่กรรม', 'มารดาถึงแก่กรรม')], max_length=255, null=True),
        ),
    ]
