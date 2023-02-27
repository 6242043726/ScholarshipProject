from typing import ClassVar
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Student(models.Model):
    user        = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    TITLE = (
        ('นาย','นาย'),
        ('นางสาว','นางสาว')
    )
    title       = models.CharField(max_length=255, null=True, choices=TITLE)
    firstname   = models.CharField(max_length=255, null=True,)
    lastname    = models.CharField(max_length=255, null=True)
    email       = models.CharField(max_length=255, null=True)
    student_id  = models.CharField(max_length=255, null=True)
    MAJOR = (
        ('การบัญชี (Accounting)','การบัญชี (Accounting)'),
        ('บริหาร-การจัดการเพื่อเป็นผู้ประกอบการธุรกิจ (Entrepreneurial Management)','บริหาร-การจัดการเพื่อเป็นผู้ประกอบการธุรกิจ (Entrepreneurial Management)'),
        ('บริหาร-ระบบสารสนเทศทางการจัดการ (Management Information Systems)','บริหาร-ระบบสารสนเทศทางการจัดการ (Management Information Systems)'),
        ('บริหาร-การธนาคารและการเงิน (Banking and Finance)','บริหาร-การธนาคารและการเงิน (Banking and Finance)'),
        ('บริหาร-การตลาด (Marketing)','บริหาร-การตลาด (Marketing)'),
        ('บริหาร-การจัดการโลจิสติกส์ระหว่างประเทศ (International Logistics Management)','บริหาร-การจัดการโลจิสติกส์ระหว่างประเทศ (International Logistics Management)'),
        ('สถิติ-สถิติประยุกต์ (Applied Statistics)','สถิติ-สถิติประยุกต์ (Applied Statistics)'),
        ('สถิติ-เทคโนโลยีสารสนเทศเพื่อธุรกิจ (Information Technology for Business)','สถิติ-เทคโนโลยีสารสนเทศเพื่อธุรกิจ (Information Technology for Business)'),
        ('สถิติ-ประกันภัย (Insurance)','สถิติ-ประกันภัย (Insurance)'),
        ('ป.โท','ป.โท'),
    )
    major       = models.CharField(max_length=255, null=True, choices=MAJOR)
    YEAR = (
        ('ปี1','ปี1'),
        ('ปี2','ปี2'),
        ('ปี3','ปี3'),
        ('ปี4','ปี4'),
        ('ปี5','ปี5'),
    )
    year        = models.CharField(max_length=255, null=True, choices=YEAR)
    gpax        = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    phone       = models.CharField(max_length=255, null=True)
    phone_brand = models.CharField(max_length=255, null=True)
    income      = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    income_from = models.CharField(max_length=255, null=True, blank=True)
    abroad      = models.CharField(max_length=255, null=True, blank=True)
    address1        = models.TextField(null=True)
    ADDRESS_TYPE = (
        ('หอพักนิสิตจุฬาฯ','หอพักนิสิตจุฬาฯ'),
        ('หอพักเอกชน','หอพักเอกชน'),
        ('บ้าน','บ้าน'),
    )
    address_type    = models.CharField(max_length=255, null=True, choices=ADDRESS_TYPE)
    dormitory       = models.CharField(max_length=255, null=True, blank=True)
    address2            = models.TextField(null=True)
    father_job          = models.CharField(max_length=255, null=True)
    avg_father_salary   = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    phone_father        = models.CharField(max_length=255, null=True)
    mother_job          = models.CharField(max_length=255, null=True)
    avg_mother_salary   = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    phone_mother        = models.CharField(max_length=255, null=True)
    STATUS_PARENT = (
        ('อยู่ด้วยกัน','อยู่ด้วยกัน'),
        ('หย่าร้าง','หย่าร้าง'),
        ('แยกกันอยู่','แยกกันอยู่ *ตอบข้อถัดไป'),
        ('บิดาถึงแก่กรรม','บิดาถึงแก่กรรม'),
        ('มารดาถึงแก่กรรม','มารดาถึงแก่กรรม'),
    )
    status_parent        = models.CharField(max_length=255, null=True, choices=STATUS_PARENT)
    CASE_SEPARATED = (
        ('บิดา','บิดา'),
        ('มารดา','มารดา'),
    )
    case_separated       = models.CharField(max_length=255, null=True, blank=True, choices=CASE_SEPARATED)
    parents_relationship = models.CharField(max_length=255, null=True, blank=True)
    parent_job = models.CharField(max_length=255, null=True, blank=True)
    avg_parent_salary = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    phone_parent = models.CharField(max_length=255, null=True, blank=True)
    num_sibling = models.IntegerField(null=True)
    num_working_sib = models.IntegerField(null=True)
    other_income = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    other_income_from = models.CharField(max_length=255, null=True)
    debt_amount = models.CharField(max_length=255, null=True)
    source_of_debt = models.CharField(max_length=255, null=True)
    reason_of_apply = models.TextField(null=True)
    LEVEL_NECESSITY = (
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5'),
        ('6','6'),
        ('7','7'),
        ('8','8'),
        ('9','9'),
        ('10','10'),
    )
    level_necessity = models.CharField(max_length=255, null=True, choices=LEVEL_NECESSITY)
    picture = models.ImageField(default="images/default_profile_pic.png",null=True, blank=True, upload_to='images/')
    schorlarship_doc = models.FileField(null=True, upload_to='schorlarship_doc/')
    other_doc = models.FileField(null=True, blank=True, upload_to='other_doc/')

    def __str__(self):
        return str(self.student_id)


