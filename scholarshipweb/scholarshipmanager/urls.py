from django.urls import path
from .views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('', loginPage, name="login"),
    path('logout/', logoutUser, name="logout"),
    path('register/', RegisterUser, name="register"),
    path('main_menu/', Main_menu, name="mainMenu"),

    path('student_update/', StudentUpdate, name='studentUpdatePage'),
    path('student_result/', StudentResult, name='studentResultPage'),
    path('student_time/', StudentTime, name='studentTimePage'),
    
    path('interviewer_history/',InterviewerHistory, name='interviewerHistoryPage' ),
    path('interviewer_historydetail/<int:studentID>/',InterviewerHistoryDetail, name='interviewerHistoryDetailPage' ),
    path('interviewer_select/',InterviewerSelect, name='interviewSelectPage' ),
    path('interviewer_result/<int:studentID>/',InterviewerResult, name='interviewResultPage' ),
    path('interviewer_display/<int:studentID>/',InterviewerDisplay, name='interviewDisplayPage' ),
    
    path('approve_process/', Approve_process, name="approveProcess"),
    path('approve_history/', Approve_history, name="approveHistory"),
    path('approve_detail/<int:studentID>/', Approve_detail, name="approveDetail"),
    path('approve_result/<int:studentID>/', Approve_result, name='approveResult'),
]

urlpatterns += staticfiles_urlpatterns()
