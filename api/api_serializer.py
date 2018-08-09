from api import models
from rest_framework import serializers    #序列化


# class CourseSerializer(serializers.Serializer):
    # level = serializers.CharField(source="get_level_display")


    #
    # class Meta:
    #     model = models.Course
    # #     fields = "__all__"
    #     fields = ["title"]
        # depth = 1

    # id = serializers.IntegerField()
    # name = serializers.CharField()

    #
    # def get_courseoutline_list(self,row):
    #     courseoutline_list = row.coursedetail.courseoutline_set.all()
    #     return [{'title': item.title} for item in courseoutline_list]


# class CourseModelSerializer(serializers.ModelSerializer):
    # level_name = serializers.CharField(source="get_level_display")
    # hours = serializers.CharField(source="coursedetail.hours")
    # course_slogan = serializers.CharField(source="coursedetail.course_slogan")
    #
    # recommend_courses = serializers.SerializerMethodField()
    # question = serializers.SerializerMethodField()  # F
    # title = serializers.SerializerMethodField()
    # name = serializers.SerializerMethodField()
    # def get_question(self):
    # class Meta:
    #     model = models.Course
        # fields = ["id","name","level_name","hours","course_slogan","recommend_courses"]
        # fields = ["name"]
        # fields = ["question"]

    # def get_recommend_courses(self, row):
    #     recommend_list = row.coursedetail.recommend_courses.all()
        # print(recommend_list)

        # return [{'id': item.id, 'name': item.name} for item in recommend_list]
        # return [11]

    # f.获取id = 1的专题课，并打印该课程相关的所有常见问题
    # def get_questin(self, row):
    #     ask_list = row.asked_question.all()
    #     return [{'question': item.question} for item in ask_list]
    # g.获取id = 1的专题课，并打印该课程相关的课程大纲
    # def get_courseoutline_list(self,row):
    #     courseoutline_list = row.coursedetail.courseoutline_set.all()
    #     return [{'title': item.title} for item in courseoutline_list]

    # h.获取id = 1的专题课，并打印该课程相关的所有章节
    # def get_coursechapter(self,row):
    #     coursechapter_list = row.scholarship_set.all()
    #     return [{'name': item.name} for item in coursechapter_list]


# class DegreeCourseModelSerializer(serializers.ModelSerializer):
    # teachers = serializers.SerializerMethodField()   #a

    # time_percent = serializers.SerializerMethodField()   #b

    # name = serializers.SerializerMethodField()   #d







    # class Meta:
    #     model = models.DegreeCourse
    #     # fields = ["name", "teachers"]
    #     fields = ["question"]
    #
    # def get_teachers(self, row):
    #     teacher_list = row.teachers.all()

        # return [{'name': item.name} for item in teacher_list]

    # def get_time_percent(self,row):
    #     time_percent_list = row.scholarship_set.all()

        # return [{'time_percent': item.time_percent} for item in time_percent_list]

    # def get_name(self,row):
    #     name_list = row.course_set.all()

        # return [{'name': item.name} for item in name_list]



# ------------------------------------day99---------------------------------------------

class CourseModelSerializer(serializers.ModelSerializer):
    level_name = serializers.CharField(source="get_level_display")
    hours = serializers.CharField(source="coursedetail.hours")
    course_slogan = serializers.CharField(source="coursedetail.course_slogan")
    recommend_courses = serializers.SerializerMethodField()

    class Meta:
        model = models.Course
        fields = ["id","name","level_name","hours","course_slogan","recommend_courses"]

    def get_recommend_courses(self, row):
        recommend_list = row.coursedetail.recommend_courses.all()
        print(recommend_list)
        return [{'id': item.id, 'name': item.name} for item in recommend_list]







