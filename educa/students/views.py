from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import *
from django.urls import reverse, reverse_lazy
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.views.generic.edit import CreateView
from .forms import *

# Create your views here.
def profile(request):
    return render(request, "students/student/register.html")


class registerView(CreateView):
    form_class = SimpleUserForm
    success_url = reverse_lazy('login')
    template_name = 'students/student/user_page.html'


























# from django.urls import reverse_lazy
# from django.views.generic.edit import CreateView
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth import authenticate, login
# from django.views.generic.edit import FormView
# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.views.generic.list import ListView
# from django.views.generic.detail import DetailView
# from courses.models import Course
# from .forms import CourseEnrollForm
#
#
# class StudentRegistrationView(CreateView):
#     template_name = 'students/student/register.html'
#     form_class = UserCreationForm
#     success_url = reverse_lazy('student_course_list')
#
#     def form_valid(self, form):
#         result = super(StudentRegistrationView,
#                        self).form_valid(form)
#         cd = form.cleaned_data
#         user = authenticate(username=cd['username'],
#                             password=cd['password1'])
#         login(self.request, user)
#         return result
#
#
# class StudentEnrollCourseView(LoginRequiredMixin, FormView):
#     course = None
#     form_class = CourseEnrollForm
#
#     def form_valid(self, form):
#         self.course = form.cleaned_data['course']
#         self.course.students.add(self.request.user)
#         return super(StudentEnrollCourseView,
#                      self).form_valid(form)
#
#     def get_success_url(self):
#         return reverse_lazy('student_course_detail',
#                             args=[self.course.id])
#
#
# class StudentCourseListView(LoginRequiredMixin, ListView):
#     model = Course
#     template_name = 'students/course/list.html'
#
#     def get_queryset(self):
#         qs = super(StudentCourseListView, self).get_queryset()
#         return qs.filter(students__in=[self.request.user])
#
#
# class StudentCourseDetailView(DetailView):
#     model = Course
#     template_name = 'students/course/detail.html'
#
#     def get_queryset(self):
#         qs = super(StudentCourseDetailView, self).get_queryset()
#         return qs.filter(students__in=[self.request.user])
#
#     def get_context_data(self, **kwargs):
#         context = super(StudentCourseDetailView,
#                         self).get_context_data(**kwargs)
#         # get course object
#         course = self.get_object()
#         if 'module_id' in self.kwargs:
#             # get current module
#             context['module'] = course.modules.get(
#                                     id=self.kwargs['module_id'])
#         else:
#             # get first module
#             context['module'] = course.modules.all()[0]
#         return context
