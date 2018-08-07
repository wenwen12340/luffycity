from django.contrib import admin

# Register your models here.
from api.models import CourseCategory,Course,DegreeCourse,Teacher,Scholarship,OftenAskedQuestion,CourseOutline,CourseChapter,CourseSection,Homework,PricePolicy,CourseDetail,CourseSubCategory

admin.site.register(CourseCategory)
admin.site.register(Course)
admin.site.register(DegreeCourse)
admin.site.register(Teacher)
admin.site.register(Scholarship)
admin.site.register(OftenAskedQuestion)
admin.site.register(CourseOutline)
admin.site.register(CourseChapter)
admin.site.register(CourseSection)
admin.site.register(Homework)
admin.site.register(PricePolicy)
admin.site.register(CourseDetail)
admin.site.register(CourseSubCategory)

