from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users
from .models import *
from django.db import connection, models
from .forms import *
from django.http import HttpResponseRedirect
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
# Create your views here.

#===========================models=========================================>
#login & register
@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        group = None
        if user is not None:
            login(request, user)
            return redirect('main_menu/')
        else:
            messages.info(request, 'Email หรือ Password ไม่ถูกต้อง')
    context = {}
    return render(request, 'scholarship_template/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

def RegisterUser(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            
            messages.success(request,'Account was created for ' + username)
            return redirect('login')
        else:
            messages.info(request, 'Register Failed, Try again!')

    context = {'form':form}
    return render(request, 'scholarship_template/register.html', context)

@login_required(login_url='login')
def Main_menu(request):
    return render(request, 'scholarship_template/main_menu.html')

# student
@login_required(login_url='login')
@allowed_users(allowed_roles=['student'])
def StudentUpdate(request):
    student = request.user.student
    form = StudentForm(instance=student)

    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES,instance=student)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'scholarship_template/student_update.html', context)


#========================================mysql===============================================>
#student
@login_required(login_url='login')
@allowed_users(allowed_roles=['student'])
def StudentTime(request):
    context = {}
    user = request.user.id
    # ตัวแปร student_id ของ user ที่ login อยู่ เอาไว้ add เข้าตาราง interview_session
    student_id = Student.objects.get(user_id=user)
    context = {'student_id': student_id}
    with connection.cursor() as myCursor:
        myCursor.execute(
            "SELECT * FROM interview_session where student_id = %s", [student_id])
        myFetchData = myCursor.fetchall()
        if len(myFetchData) > 0:
            print('คุณได้ลงทะเบียนไปแล้ว')
            context['returnMessage'] = 'เลือกเวลาสัมภาษณ์เรียบร้อยแล้ว'
            myCursor.callproc('getstudenttime', [student_id,])
            # คําสั่งในส่วนนี้จะจัดผลการ Query ให้อยู่ในรูปแบบ Dictionary
            columns = [col[0] for col in myCursor.description]
            myFetchData = [dict(zip(columns, row))
                           for row in myCursor.fetchall()]
            context['returnMessage2'] = myFetchData

        else:
            if request.method == 'POST':
                myData = request.POST.copy()
                myDate = myData.get('date')
                myTime = myData.get('time')
                if myDate == '19dec':
                    if myTime == '10-11':
                        mySession = 1
                    elif myTime == '11-12':
                        mySession = 2
                    elif myTime == '13-14':
                        mySession = 3
                    elif myTime == '14-15':
                        mySession = 4

                elif myDate == '20dec':
                    if myTime == '10-11':
                        mySession = 5
                    elif myTime == '11-12':
                        mySession = 6
                    elif myTime == '13-14':
                        mySession = 7
                    elif myTime == '14-15':
                        mySession = 8

                elif myDate == '21dec':
                    if myTime == '10-11':
                        mySession = 9
                    elif myTime == '11-12':
                        mySession = 10
                    elif myTime == '13-14':
                        mySession = 11
                    elif myTime == '14-15':
                        mySession = 12

                elif myDate == '22dec':
                    if myTime == '10-11':
                        mySession = 13
                    elif myTime == '11-12':
                        mySession = 14
                    elif myTime == '13-14':
                        mySession = 15
                    elif myTime == '14-15':
                        mySession = 16

                with connection.cursor() as myCursor:
                    myCursor.execute("INSERT INTO interview_session(student_id, session_id) VALUES (%s, %s)", [
                        student_id, mySession])
                    context['returnMessage'] = 'เลือกเวลาสัมภาษณ์เรียบร้อยแล้ว'
                    myCursor.callproc('getstudenttime', [student_id,])
                    # คําสั่งในส่วนนี้จะจัดผลการ Query ให้อยู่ในรูปแบบ Dictionary
                    columns = [col[0] for col in myCursor.description]
                    myFetchData = [dict(zip(columns, row))
                                   for row in myCursor.fetchall()]
                    context['returnMessage2'] = myFetchData

    return render(request, 'scholarship_template/student_time.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['student'])
def StudentResult(request):
    context = {}
    user = request.user.id
    # ตัวแปร student_id ของ user ที่ login อยู่ เอาไว้ add เข้าตาราง interview_session
    student_id = Student.objects.get(user_id=user)
    context = {'student_id': student_id}
    with connection.cursor() as myCursor:
        myCursor.execute(
            "select * from interview_session where student_id = %s", [student_id])
        myFetchData = myCursor.fetchall()
        if len(myFetchData) > 0:
                myCursor.execute("SELECT * FROM interview_session where student_id = %s", [student_id])
                columns = [col[0] for col in myCursor.description]
                myFetchData = [dict(zip(columns, row)) for row in myCursor.fetchall()]
                context['result'] = myFetchData
        else:
            context['returnMessage'] = 'ยังไม่เลือกเวลาสัมภาษณ์'
    return render(request, 'scholarship_template/student_result.html', context)


#interviewer
@login_required(login_url='login')
@allowed_users(allowed_roles=['interviewer'])
def InterviewerHistory(request):
    # ตารางรายชื่อ นร ที่ลทบมาสัมภาษณ์ เพื่อกดดูข้อมมูลแต่ละคน InterviewerDisplay
    context = {}
    interviewer_name = request.user.first_name #ตัวแปร interviewer_name ของ user ที่ login อยู่ เอาไว้เทียบแล้วดึงเฉพาะแถวที่มีชื่อ อ.คนนี้
    context = {'interviewer_name': interviewer_name}
    with connection.cursor() as myCursor:
        myCursor.callproc('getstudentinterview', [interviewer_name,])
        columns = [col[0] for col in myCursor.description]
        myFetchData = [dict(zip(columns, row)) for row in myCursor.fetchall()]
        context['studentDataList'] = myFetchData
    return render(request, 'scholarship_template/interviewer_history.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['interviewer'])
def InterviewerHistoryDetail(request,studentID):
    context = {}
    student_data = Student.objects.get(student_id=studentID)
    context = {'student_data':student_data}
    with connection.cursor() as myCursor:
        myCursor.execute(
            "select * from interview_session as t1 inner join interview_session_list as t2 on t1.session_id = t2.session_id where student_id = %s", [studentID])
        columns = [col[0] for col in myCursor.description]
        myFetchData = [dict(zip(columns, row)) for row in myCursor.fetchall()]
        context['interviewDataList'] = myFetchData
    
    print(context)
    return render(request, 'scholarship_template/interviewer_historydetail.html',context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['interviewer'])
def InterviewerDisplay(request,studentID):
    context = {}
    student_doc = Student.objects.get(student_id=studentID)
    context = {'student_doc':student_doc}
    with connection.cursor() as myCursor:
        myCursor.execute(
            "select * from scholarshipmanager_student where student_id = %s", [studentID])
        columns = [col[0] for col in myCursor.description]
        myFetchData = [dict(zip(columns, row)) for row in myCursor.fetchall()]
        context['studentDataList'] = myFetchData
    return render(request, 'scholarship_template/interviewer_display.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['interviewer'])
def InterviewerSelect(request):
    context = {}
    interviewer_name = request.user.first_name #ตัวแปร interviewer_name ของ user ที่ login อยู่ เอาไว้เทียบแล้วดึงเฉพาะแถวที่มีชื่อ อ.คนนี้
    context = {'interviewer_name': interviewer_name}
    with connection.cursor() as myCursor:
        myCursor.callproc('getstudentinterview', [interviewer_name,])
        columns = [col[0] for col in myCursor.description]
        myFetchData = [dict(zip(columns, row)) for row in myCursor.fetchall()]
        context['studentDataList'] = myFetchData
    return render(request, 'scholarship_template/interviewer_select.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['interviewer'])
def InterviewerResult(request, studentID):
    context = {}
    student_data = Student.objects.get(student_id=studentID)
    context = {'student_data':student_data}
    with connection.cursor() as myCursor:
        myCursor.execute(
            "select * from interview_session where student_id = %s", [studentID])
        columns = [col[0] for col in myCursor.description]
        myFetchData = [dict(zip(columns, row)) for row in myCursor.fetchall()]
        context['interviewDataList'] = myFetchData
    if request.method == 'POST':
        myData = request.POST.copy()
        myInformation = myData.get('myInformation')
        myResult = myData.get('myResult')
        myUni_ss_b1 = myData.get('myUni_ss_b1') or 0
        myUni_ss_b2 = myData.get('myUni_ss_b2') or 0
        myUni_ss_c = myData.get('myUni_ss_c') or 0
        myFac_ss_b1 = myData.get('myFac_ss_b1') or 0
        myFac_ss_b2 = myData.get('myFac_ss_b2') or 0
        myFac_ss_c = myData.get('myFac_ss_c') or 0
        myExt_ss_b1 = myData.get('myExt_ss_b1') or 0
        myExt_ss_b2 = myData.get('myExt_ss_b2') or 0
        myExt_ss_c = myData.get('myExt_ss_c') or 0
        
        myAdditional_comments = myData.get('myAdditional_comments')
        myStatus = 1
        with connection.cursor() as myCursor:
            myCursor.callproc('getupdatesession', [myInformation, myResult, myUni_ss_b1, myUni_ss_b2, myUni_ss_c, myFac_ss_b1, myFac_ss_b2, myFac_ss_c, myExt_ss_b1, myExt_ss_b2, myExt_ss_c, myAdditional_comments, myStatus, studentID,])
            context['returnMessage'] = 'กรอกผลการสัมภาษณ์เรียบร้อย'
    return render(request, 'scholarship_template/interviewer_result.html', context)




# approver
@login_required(login_url='login')
@allowed_users(allowed_roles=['approver'])
def Approve_process(request):
#หน้าตารางรายชื่อนักเรียนที่มีผลสัมภาษณ์แล้ว
    context = {}
    with connection.cursor() as myCursor:
        myCursor.execute(
            "select * from interview_session_student where status = 1")
        columns = [col[0] for col in myCursor.description]
        myFetchData = [dict(zip(columns, row)) for row in myCursor.fetchall()]
        context['approveList'] = myFetchData
    return render(request, 'scholarship_template/approve_process.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['approver'])
def Approve_detail(request,studentID):
#หน้ารายละเอียดผลการสัมภาษณ์ เพื่อconfirm
    context = {}
    student_data = Student.objects.get(student_id=studentID)
    context = {'student_data':student_data}
    with connection.cursor() as myCursor:
        myCursor.execute(
            "select * from interview_session as t1 inner join interview_session_list as t2 on t1.session_id = t2.session_id where student_id = %s", [studentID])
        columns = [col[0] for col in myCursor.description]
        myFetchData = [dict(zip(columns, row)) for row in myCursor.fetchall()]
        context['interviewDataList'] = myFetchData
    
    if request.method == 'POST':
        myData = request.POST.copy()
        myInformation = myData.get('myInformation')
        myResult = myData.get('myResult')
        myUni_ss_b1 = myData.get('myUni_ss_b1')
        myUni_ss_b2 = myData.get('myUni_ss_b2')
        myUni_ss_c = myData.get('myUni_ss_c')
        myFac_ss_b1 = myData.get('myFac_ss_b1')
        myFac_ss_b2 = myData.get('myFac_ss_b2')
        myFac_ss_c = myData.get('myFac_ss_c')
        myExt_ss_b1 = myData.get('myExt_ss_b1')
        myExt_ss_b2 = myData.get('myExt_ss_b2')
        myExt_ss_c = myData.get('myExt_ss_c')
        myAdditional_comments = myData.get('myAdditional_comments')
        myStatus = myData.get('myStatus')
        with connection.cursor() as myCursor:
            myCursor.callproc('getupdatesession', [myInformation, myResult, myUni_ss_b1, myUni_ss_b2, myUni_ss_c, myFac_ss_b1, myFac_ss_b2, myFac_ss_c, myExt_ss_b1, myExt_ss_b2, myExt_ss_c, myAdditional_comments, myStatus, studentID,])
            context['returnMessage'] = 'ประเมินการอนุมัติทุนเรียบร้อย'
    print(context)
    return render(request, 'scholarship_template/approve_detail.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['approver'])
def Approve_history(request):
#หน้าตาราางประวัติการให้ทุน
    context = {}
    with connection.cursor() as myCursor:
        myCursor.execute(
            "select *, total_ss from interview_session_student as t1 inner join interview_session as t2 on t1.student_id = t2.student_id where t2.status = 2 or t2.status = 3;")
        columns = [col[0] for col in myCursor.description]
        myFetchData = [dict(zip(columns, row)) for row in myCursor.fetchall()]
        context['approveList'] = myFetchData
    return render(request, 'scholarship_template/approve_history.html',context) 

@login_required(login_url='login')
@allowed_users(allowed_roles=['approver'])
def Approve_result(request,studentID):
    context = {}
    student_data = Student.objects.get(student_id=studentID)
    context = {'student_data':student_data}
    with connection.cursor() as myCursor:
        myCursor.execute(
            "select * from interview_session where student_id = %s", [studentID])
        columns = [col[0] for col in myCursor.description]
        myFetchData = [dict(zip(columns, row)) for row in myCursor.fetchall()]
        context['interviewDataList'] = myFetchData
    print(context)
    return render(request, 'scholarship_template/approve_result.html',context) 




