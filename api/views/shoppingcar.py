import redis
from rest_framework.viewsets import ViewSetMixin
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser,FormParser

from api import models

CONN= redis.Redis(host="192.168.0.107",port=6379)   #全局变量要大写
class ShoppingCarView(ViewSetMixin,APIView):
    # parser_classes = [JSONParser,FormParser]    #帮助解析请求头是否带了json(或者对应的数据类型，只能解析中括号里的数据类型
    # def list(self,request,*args,**kwargs):
    #     conn.hset("xx","k1","于超")
    #     conn.hset("xx","k2","彭静")
    #     n1 = conn.hget("xx","k1")
    #     n2 = conn.hget("xx","k2")
    #     print(n1,n2)
    #     return Response("111")
    #
    # def create(self,request,*args,**kwargs):
    #     print("create")
    #     conn.hset("xx","k1","zhao")
    #     conn.hset("xx","k2","yuahn")
    #     n1 = conn.hget("xx","k1")
    #     n2 = conn.hget("xx","k2")
    #     print(n1,n2)    #取出来的值是byte类型 ，用json格式传输数据
    #     return Response("222")
    #

    #购物车
    parser_classes = [JSONParser]
    def list(self,request,*args,**kwargs):
        '''
        查看购物车信息
        :param request:
        :param args:
        :param kwargs:
        :return:
        '''

    def create(self,request,*args,**kwargs):
      '''
        1,接收用户选中的课程id和价格策略id
        2,判断合法性
            课程是否存在？
            价格策略是否合法？
        3，把商品和价格策略信息放入购物车
      :param request:
      :param args:
      :param kwargs:
      :return:
      '''
      # 1, 接收用户选中的课程id和价格策略id
      print('加入购物车')
      # ret = request.body
      course_id = request.data.get("course_id")    #可以直接取数据
      policy_id = request.data.get("policy_id")
      print(course_id)
      #request是rest_framework封装的request,原始的用request._request

      # 2判断数据的合法性
      #   课程是否存在
      #价格策略是否存在
      course = models.Course.objects.filter(id=course_id).first()   #还要判断是否是线上status=0
      if not course:
          return Response({"code":1000,"error":"课程不存在"})
      price_policy_list = course.price_policy.all()
      for item in price_policy_list:
          print(item)






      return Response({"code":"111"})







