from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from exam import models

# Create your views here.

# 学生登录
def studentLogin(request):
    if request.method == 'POST':
        # 获取表单信息
        sid = request.POST.get('sid')
        password = request.POST.get('password')
        print("sid", sid, "password", password)
        # 通过学号获取该学生实体
        student = models.Student.objects.get(sid=sid)
        print(student)
        if password == student.pwd:  # 登录成功
            request.session['username']=sid    #user的值发送给session里的username
            request.session['is_login']=True   #认证为真
            # 查询考试信息
            paper = models.TestPaper.objects.filter(major=student.major)
            # 查询成绩信息
            grade = models.Record.objects.filter(sid=student.sid)

            # 渲染index模板
            return render(request, 'index.html', {'student': student, 'paper': paper, 'grade': grade})
        else:
            return render(request,'login.html',{'message':'密码不正确'})
    elif request.method == 'GET':
        return render(request, 'login.html')
    else:
        return HttpResponse("请使用GET或POST请求数据")


# 首页
def index(request):
    if request.session.get('is_login',None):  #若session认证为真
        username = request.session.get('username',None)
        print(username )
        student = models.Student.objects.get(sid=username)
        # 查询考试信息
        paper = models.TestPaper.objects.filter(major=student.major)
        return render(request, 'index.html',{'student': student,'paper': paper})
    else:
        return render(request, 'index.html')



def userfile(request):
    if request.session.get('is_login',None):  #若session认证为真
        username = request.session.get('username',None)
        print(username )
        student = models.Student.objects.get(sid=username)
        # 查询考试信息
        paper = models.TestPaper.objects.filter(major=student.major)
        return render(request, 'userfile.html',{'student': student})



#学生退出登录
def stulogout(request):
    # logout(request)
    request.session.clear()
    url = reverse('index')
    return redirect(url)

# 考试信息
def startExam(request):
    sid = request.GET.get('sid')
    title = request.GET.get('title')  # 试卷名字 唯一
    subject1 = request.GET.get('subject')  # 考试科目
    # 获取学生信息
    student = models.Student.objects.get(sid=sid)
    # 试卷信息
    paper = models.TestPaper.objects.filter(title=title,course__course_name=subject1)
    context = {
        'student': student,
        'paper': paper,
        'title': title,
        'subject':subject1,
        'count': paper.count()   # 数据表中数据的条数
    }
    return render(request, 'exam.html', context=context)

def examinfo(request):
    if request.session.get('is_login',None):  #若session认证为真
        username = request.session.get('username',None)
        student = models.Student.objects.get(sid=username)
        # 查询成绩信息
        grade = models.Record.objects.filter(sid=student.sid)
        return render(request, 'examinfo.html',{'student': student,'grade': grade})
    else:
        return render(request, 'examinfo.html')

# 计算考试成绩
def calculateGrade(request):
    if request.method == 'POST':
        sid = request.POST.get('sid')
        subject1 = request.POST.get('subject')
        student = models.Student.objects.get(sid=sid)
        paper = models.TestPaper.objects.filter(major=student.major)
        grade = models.Record.objects.filter(sid=student.sid)
        course = models.Course.objects.filter(course_name=subject1).first()
        now =  datetime.now()
        # 计算考试成绩
        questions = models.TestPaper.objects.filter(course__course_name=subject1).\
            values('pid').values('pid__id','pid__answer','pid__score')

        stu_grade = 0  # 初始化一个成绩
        for p in questions:
            qid = str(p['pid__id'])
            stu_ans = request.POST.get(qid)
            cor_ans = p['pid__answer']
            if stu_ans == cor_ans:
                stu_grade += p['pid__score']
        models.Record.objects.create(sid_id=sid, course_id=course.id, grade=stu_grade,rtime=now)
        context = {
            'student': student,
            'paper': paper,
            'grade': grade
        }
        return render(request, 'index.html', context=context)