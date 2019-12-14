from django.urls import path
from django.views.decorators.cache import cache_page
from . import views
from django.contrib.auth.views import auth_login

app_name = 'students'

urlpatterns = [
    # login page
    path('', auth_login, name="login"),

    path("register", views.registerView.as_view(), name="registration"),

    path("user/", views.profile, name="profile"),
]
# urlpatterns = [
#     path('register/',
#          views.StudentRegistrationView.as_view(),
#          name='student_registration'),
#     path('enroll-course/',
#          views.StudentEnrollCourseView.as_view(),
#          name='student_enroll_course'),
#     path('courses/',
#          views.StudentCourseListView.as_view(),
#          name='student_course_list'),
#     path('course/<pk>/',
#          cache_page(60 * 15)(views.StudentCourseDetailView.as_view()),
#          name='student_course_detail'),
#     path('course/<pk>/<module_id>/',
#          cache_page(60 * 15)(views.StudentCourseDetailView.as_view()),
#          name='student_course_detail_module'),
# ]
