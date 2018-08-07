from django.shortcuts import render,HttpResponse
from rest_framework.views import APIView

# Create your views here.

from api.models import CourseCategory,Course,DegreeCourse,Teacher,Scholarship,OftenAskedQuestion,CourseOutline,CourseChapter,CourseSection,Homework,PricePolicy,CourseDetail,CourseSubCategory

class Check(APIView):
    def get(self,request):

        # a.查看所有学位课并打印学位课名称以及授课老师
        # DegreeCourse_list1 = DegreeCourse.objects.all().values('name',"teachers__name")
        # print(DegreeCourse_list1)

        # b.查看所有学位课并打印学位课名称以及学位课的奖学金

        # DegreeCourse_list2 = DegreeCourse.objects.all().values("name","total_scholarship")
        # print(DegreeCourse_list2)

        # c.展示所有的专题课
        # course_list = Course.objects.filter(degree_course__isnull=True)
        # print(course_list)

        # d.查看id = 1的学位课对应的所有模块名称

        # course_list1 = Course.objects.filter(degree_course__id=1).values("name")
        # print(course_list1)

        # e.获取id = 1的专题课，并打印：课程名、级别(中文)、why_study、what_to_study_brief、所有recommend_courses
        # course_obj = Course.objects.filter(id=1).first()
        # print(course_obj.name,course_obj.get_level_display(),
        #       course_obj.coursedetail.why_study,
        #       course_obj.coursedetail.what_to_study_brief,
        #       course_obj.coursedetail.recommend_courses)


        # f.获取id = 1的专题课，并打印该课程相关的所有常见问题
        # course_obj2 = Course.objects.filter(id=1).

        # g.获取id = 1的专题课，并打印该课程相关的课程大纲
        # course_obj3 = Course.objects.filter(id=1).values("coursedetail__courseoutline__content")
        # print(course_obj3)

        # h.获取id = 1的专题课，并打印该课程相关的所有章节
        # course_obj4 = Course.objects.filter(id=1).values("coursechapters__chapter")
        # print(course_obj4)

        # i.获取id = 1的专题课，并打印该课程相关的所有课时
        # course_obj5 = Course.objects.filter(id=1).values("coursechapters__coursesections__name").all()
        # print(course_obj5)

        # j.获取id = 1的专题课，并打印该课程相关的所有的价格策略
        # course_obj6 = Course.objects.filter(id=1).values("price_policy__valid_period")
        # print(course_obj6)

        return HttpResponse("ok")














# i.获取id = 1
# 的专题课，并打印该课程相关的所有课时

