from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import TeacherCreateForm
from .models import Teacher


class TeacherCreateView(CreateView):
    model = Teacher
    form_class = TeacherCreateForm
    success_url = reverse_lazy('teacher:list')
    template_name = 'teachers/create.html'
