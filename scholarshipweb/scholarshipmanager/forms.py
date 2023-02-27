from django.forms import ModelForm
from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__' #('field','field'])
        labels = '__all__' #{'':''}
        widgets = {
            'title': forms.Select(attrs={'class':'form-control'}),
            'firstname': forms.TextInput(attrs={'class':'form-control'}),
            'lastname': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'student_id': forms.TextInput(attrs={'class':'form-control'}),
            'major': forms.Select(attrs={'class':'form-control'}),
            'year': forms.Select(attrs={'class':'form-control'}),
            'gpax': forms.TextInput(attrs={'class':'form-control'}),
            'phone': forms.TextInput(attrs={'class':'form-control'}),
            'phone_brand': forms.TextInput(attrs={'class':'form-control'}),
            'income': forms.TextInput(attrs={'class':'form-control'}),
            'income_from': forms.TextInput(attrs={'class':'form-control'}),
            'abroad': forms.TextInput(attrs={'class':'form-control'}),
            'address1': forms.Textarea(attrs={'class':'form-control','placeHolder':'ที่อยู่ตามทะเบียนบ้าน'}),
            'address_type': forms.Select(attrs={'class':'form-control'}),
            'dormitory': forms.TextInput(attrs={'class':'form-control'}),
            'address2': forms.Textarea(attrs={'class':'form-control','placeHolder':'ที่อยู่ปัจจุบัน'}),
            'father_job': forms.TextInput(attrs={'class':'form-control'}),
            'avg_father_salary': forms.TextInput(attrs={'class':'form-control'}),
            'phone_father': forms.TextInput(attrs={'class':'form-control'}),
            'mother_job': forms.TextInput(attrs={'class':'form-control'}),
            'avg_mother_salary': forms.TextInput(attrs={'class':'form-control'}),
            'phone_mother': forms.TextInput(attrs={'class':'form-control'}),
            'status_parent': forms.Select(attrs={'class':'form-control'}),
            'case_separated': forms.Select(attrs={'class':'form-control'}),
            'parents_relationship': forms.TextInput(attrs={'class':'form-control'}),
            'parent_job': forms.TextInput(attrs={'class':'form-control'}),
            'avg_parent_salary': forms.TextInput(attrs={'class':'form-control'}),
            'phone_parent': forms.TextInput(attrs={'class':'form-control'}),
            'num_sibling': forms.TextInput(attrs={'class':'form-control'}),
            'num_working_sib': forms.TextInput(attrs={'class':'form-control'}),
            'other_income': forms.TextInput(attrs={'class':'form-control'}),
            'other_income_from': forms.TextInput(attrs={'class':'form-control'}),
            'debt_amount': forms.TextInput(attrs={'class':'form-control'}),
            'source_of_debt': forms.TextInput(attrs={'class':'form-control'}),
            'reason_of_apply': forms.Textarea(attrs={'class':'form-control','placeHolder':'เหตุผลการขอทุน'}),
            'level_necessity': forms.Select(attrs={'class':'form-control'}),
            'picture': forms.FileInput(attrs={'class':'form-control','style': 'height:36px;'}),
            'schorlarship_doc': forms.FileInput(attrs={'class':'form-control','style': 'height:36px;'}),
            'other_doc': forms.FileInput(attrs={'class':'form-control','style': 'height:36px;'}),
        }
        exclude  = ['user']

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1','password2']