from django.db import models

# 学院表
class Academy(models.Model):
    id = models.AutoField('序号',primary_key=True)
    name = models.CharField('学院',max_length=20)

    # 修改显示的表的名字
    class Meta:
        verbose_name = '学院'
        verbose_name_plural = '学院'

    def __str__(self):
        return self.name

# 专业表
class Major(models.Model):
    id = models.AutoField('序号',primary_key=True)
    academy = models.ForeignKey(Academy,on_delete=models.CASCADE,verbose_name='学院')
    major = models.CharField('专业',max_length=30)

    # 修改显示的表的名字
    class Meta:
        verbose_name = '专业'
        verbose_name_plural = '专业'
    def __str__(self):
        return self.major

# 课程表
class Course(models.Model):
    id = models.AutoField('序号',primary_key=True)
    course_id = models.CharField('课程号',max_length=10)
    course_name = models.CharField('课程名称',max_length=30)

    class Meta:
        verbose_name = '课程'
        verbose_name_plural = '课程'

    def __str__(self):
        return self.course_name

# 学生表
class Student(models.Model):
    sid = models.CharField('学号',max_length=12,primary_key=True)
    name = models.CharField('姓名',max_length=20,unique=True)
    sex = models.BooleanField('性别',choices=((0,'女'),(1,'男')))
    age = models.IntegerField('年龄')
    academy = models.ForeignKey(Academy,on_delete=models.CASCADE,verbose_name='学院')
    major = models.ForeignKey(Major,on_delete=models.CASCADE,verbose_name='专业')
    sclass = models.CharField('班级',max_length=20,help_text='例如: 17-03')
    email = models.EmailField('邮箱',default=None)    # 默认为空   唯一值
    pwd = models.CharField('密码',max_length=20)

    # 修改显示的表的名字
    class Meta:
        verbose_name = '学生'
        verbose_name_plural = '学生信息表'

    def __str__(self):
        return self.sid

# 题库表
class QuestionBank(models.Model):
    id = models.AutoField('序号',primary_key=True)
    major = models.ForeignKey(Major,on_delete=models.CASCADE,verbose_name='专业')
    course = models.ForeignKey(Course,on_delete=models.CASCADE,verbose_name='科目')
    title = models.TextField('题目')
    qtype = models.CharField('题目类型',choices=(('单选','单选'),('多选','多选'),('判断','判断')),max_length=40)
    a = models.CharField('A选项',max_length=40)
    b = models.CharField('B选项',max_length=40)
    c = models.CharField('C选项',max_length=40)
    d = models.CharField('D选项',max_length=40)
    answer = models.CharField('答案',choices=(('A','A'),('B','B'),('C','C'),('D','D')),max_length=4)
    difficulty = models.CharField('难度',choices=(('easy','简单'),('middle','中等'),('difficult','难')),max_length=10)
    score = models.IntegerField('分值')

    class Meta:
        # 选择这个表之后显示的名字
        verbose_name = '题库'
        # 显示的表名
        verbose_name_plural = '题库'

    def __str__(self):
        return '<%s:%s>' % (self.course, self.title)

# 试卷表
class TestPaper(models.Model):
    id = models.AutoField('序号',primary_key=True)
    title = models.CharField('题目',max_length=40,unique=True)
    pid = models.ManyToManyField(QuestionBank)
    course = models.ForeignKey(Course,on_delete=models.CASCADE,verbose_name='科目')
    major = models.ForeignKey(Major,on_delete=models.CASCADE,verbose_name='考卷适合专业')
    time = models.IntegerField('考试时长',help_text='单位是分钟')
    examtime = models.DateTimeField('上次考试时间')

    class Meta:
        # 选择这个表之后显示的名字
        verbose_name = '试卷'
        verbose_name_plural = '试卷'

# # 学生成绩表
class Record(models.Model):
    id = models.AutoField('序号',primary_key=True)
    sid = models.ForeignKey(Student,on_delete=models.CASCADE,verbose_name='学号',related_name='stu_xuehao')
    course = models.ForeignKey(Course,on_delete=models.CASCADE,verbose_name='考试科目',related_name='stu_course')
    grade = models.FloatField('成绩')
    rtime = models.DateTimeField('考试时间',blank=True,null=True)

    class Meta:
        verbose_name = '学生成绩'
        verbose_name_plural = '学生成绩'

    def __str__(self):
        return '<%s:%s>' % (self.sid,self.grade)