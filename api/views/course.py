import json
from django.shortcuts import HttpResponse



from rest_framework.versioning import URLPathVersioning   #版本  在setting里配置
from rest_framework.views import APIView    #视图
from  rest_framework.viewsets import ViewSetMixin,GenericViewSet,ModelViewSet  #视图
from rest_framework.response import Response  #响应
from rest_framework.pagination import PageNumberPagination  #分页 在setting里配置
from rest_framework.mixins import ListModelMixin,CreateModelMixin,\
    RetrieveModelMixin,DestroyModelMixin,UpdateModelMixin


from api import models
from api.api_serializer import CourseModelSerializer
from api.utils.response import BaseResponse


# class CoursesView(APIView):


     # def get(self,request,*args,**kwargs):
     #     result = ""
     #     if request.version == "v1":
     #         result = "v1"
     #     else:
     #         result = "其他"
     #     return HttpResponse(result)
    # def get(self,request,*args,**kwargs):


         # 阶段一
         #方式一
         # course_list = list(models.Course.objects.all().values("id","name"))
         # print(course_list)
         # return HttpResponse(json.dumps(course_list,ensure_ascii= False))
     # ensure_ascii = False,编码方式改为utf8

        #方式二
        # course_list = models.Course.objects.all()
        # print(course_list)
        # ser = CourseSerializer(instance=course_list,many=True)
        #  # many=True  因为coutse_list是个queryset,有多个
        # return Response(ser.data)   #序列化要取.data值

        # 阶段二
        # ret = BaseResponse()  #实例化一个对象
        #  #从数据库取出数据
        # try:
        #     queryset = models.Course.objects.all()
        #     print(queryset)
        #
        #      #分页    在setting里配置
        #     page = PageNumberPagination()
        #     course_list = page.paginate_queryset(queryset,request,self)
        #     print(course_list)
        #      # self  当前对象
        #
        #     #分页之后结果执行序列化
        #     ser = CourseSerializer(instance=course_list,many=True)
        #     print(ser)
        #     ret.data = ser.data   #更改对象的属性
        #     print(ret.data)
        # except Exception:
        #     ret.code = 500
        #     ret.error = "获取数据失败"
        #
        # return Response(ret.dict)   #调用对象的静态方法，把对象转化成字典的形式

    #阶段三
        # c展示所有的专题课
        # ret = BaseResponse()
        # # try:
        # # queryset = models.Course.objects.filter(degree_course__isnull=True)
        # queryset = models.Course.objects.filter(id=1).first()
        #
        #
        # ser = CourseModelSerializer(queryset)
        # print(ser)
        # ret.data = ser.data
        # print(ret.data)
        # # except Exception:
        # #     ret.code = 500
        # #     ret.error = "获取数据失败"
        # return Response(ret.dict)




# class CourseDetailView(APIView):
#     # c. 展示所有的专题课
#     def get(self,request,*args,pk,**kwargs):
        #第一阶段
        # course = models.Course.objects.filter(id = pk).first()
        # print(course)   #对象，也可以直接用get取
        # ser = CourseSerializer(course)   #只有单个对象
        # return Response(ser.data)


        # 第二阶段
        # ret = BaseResponse()
        # try:
        #     course_obj = models.Course.objects.filter(id=pk).first()
        #     ser = CourseSerializer(course_obj)
        #     ret.data = ser.data
        # except Exception:
        #     ret.data = 500
        #     ret.error = "获取数据失败"
        # return Response(ret.dict)

        #第三阶段
        # ret = BaseResponse()
        # try:
        #     course_obj = models.Course.objects.get(id=pk)
        #     print(course_obj)
        #     ser = CourseModelSerializer(course_obj)
        #     print(ser)
        #     ret.data = ser.data
        # except Exception:
        #     ret.code = 500
        #     ret.error = "获取数据失败"
        # return Response(ret.data)


# class DegreeCourseView(APIView):
    # a.查看所有学位课并打印学位课名称以及授课老师
    # b.查看所有学位课并打印学位课名称以及学位课的奖学金
    # d. 查看id=1的学位课对应的所有模块名称
    # f.获取id = 1的专题课，并打印该课程相关的所有常见问题

    # def get(self, request, *args, **kwargs):
    #
    #     ret = BaseResponse()
    #     # try:
    #     queryset = models.DegreeCourse.objects.filter(id=1)
    #     page = PageNumberPagination()
    #     course_list = page.paginate_queryset(queryset, request, self)
    #     ser = DegreeCourseModelSerializer(course_list, many=True)
    #     ret.data = ser.data
    #     print(ret.data)


        # except Exception:
        #     ret.code = 500
        #     ret.error = "获取数据失败"

        # return Response(ret.dict)

# class DegreeCourseDetailView(APIView):



# ————————————————————day99——————————————————————————------------

# class CoursesView(ViewSetMixin,APIView):
#     #第二版
#
#     def list(self,request,*args,**kwargs):
#         ret = BaseResponse()
#         # try:
#         queryset = models.Course.objects.all()
#         print(queryset)
#         # page = PageNumberPagination()
#         # course_list = page.paginate_queryset(queryset,request,self)
#         ser = CourseModelSerializer(queryset,many=True)
#         ret.data = ser.data
#         # except Exception:
#         #     ret.code = 500
#         #     ret.error = "数据获取失败"
#         return Response(ret.dict)
#
#     def create(self,request,*args,**kwargs):
#         '''
#
#         :param request:
#         :param args:
#         :param kwargs:
#         :return:
#         '''
#
#     def retrieve(self,request,pk,*args,**kwargs):
#         ret = BaseResponse()
#         course = models.Course.objects.get(id=pk)
#         ser = CourseModelSerializer(course)
#         ret.code = 500
#         ret.error = "数据获取失败"
#         return Response(ret.dict)
#
#     def updata(self,request,pk,*args,**kwargs):
#         '''
#         修改
#         :param request:
#         :param pk:
#         :param args:
#         :param kwargs:
#         :return:
#         '''
#
#     def destroy(self,request,pk,*args,**kwargs):
#         '''
#         删除
#         :param request:
#         :param pk:
#         :param args:
#         :param kwargs:
#         :return:
#         '''


#第三版

# class CourseView(ListModelMixin,RetrieveModelMixin,GenericViewSet):
    # queryset = models.Course.objects.all()
    # serializer_class = CourseModelSerializer
    #
    # def list(self,request,*args,**kwargs):
    #     return Response()


    # 坑
    # queryset = models.Course.objects.all()
    # def list(self,request,*args,**kwargs):
    #
    #     course_list = models.Course.objects.all()
    #     ser = CourseModelSerializer(course_list,many=True)
    #     return Response(ser.data)










