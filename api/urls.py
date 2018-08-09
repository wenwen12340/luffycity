from django.conf.urls import url
from api.views import course,shoppingcar

urlpatterns = [
    # url(r"courses/$",course.CoursesView.as_view()),
    # url(r'courses/(?P<pk>\d+)/$',course.CourseDetailView.as_view()),
    # url(r"degreecourse/",course.DegreeCourseView.as_view()),
    # url(r"degreecourse/(?P<pk>\d+)/$",course.DegreeCourseDetailView.as_view())


    # -------------------------------------day99--------------------------------------------------
    #第二版
    # url(r'course/$',course.CoursesView.as_view({"get":"list","post":"create"})),
    # url(r'course/(?P<pk>\d+)/$',course.CoursesView.as_view({"get":"retrieve","put":"updata","delete":"destroy"}))

    #第三版
    url(r'shoppingcar/$', shoppingcar.ShoppingCarView.as_view({"get": "list",'post':"create"})),
    # url(r'courses/$',course.CourseView.as_view({"get":"list"})),
    # url(r'courses/(?P<pk>\d+/$)',course.CourseView.as_view({"get":"retrieve"}))
]
# from rest_framework.routers import DefaultRouter
# router = DefaultRouter()
# router.register(r"course",views.Course)
# urlpatterns += router.urls