from django.conf.urls import url
from api import views
from api.views import course

urlpatterns = [
    url(r"courses/$",course.CoursesView.as_view()),
    url(r'courses/(?P<pk>\d+)/$',course.CourseDetailView.as_view()),
    url(r"degreecourse/",course.DegreeCourseView.as_view()),
    # url(r"degreecourse/(?P<pk>\d+)/$",course.DegreeCourseDetailView.as_view())
]
# from rest_framework.routers import DefaultRouter
# router = DefaultRouter()
# router.register(r"course",views.Course)
# urlpatterns += router.urls