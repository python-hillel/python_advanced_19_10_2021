from copy import copy

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView
from django.views.generic import UpdateView


from .forms import StudentCreateForm
from .forms import StudentsFilter
from .models import Students


def get_students(request, args):
    students = Students.objects.all().select_related('group', 'headman_group')

    filter_students = StudentsFilter(data=request.GET, queryset=students)

    return render(
        request=request,
        template_name='students/list.html',
        context={
            'test': 'Hello World!',
            'students': students,
            'filter_students': filter_students,
        }
    )


def create_student(request):
    if request.method == 'GET':
        form = StudentCreateForm()
    elif request.method == 'POST':
        form = StudentCreateForm(data=request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('students:list'))

    return render(
        request=request,
        template_name='students/create.html',
        context={'form': form}
    )


@login_required
def delete_student(request, pk):
    student = get_object_or_404(Students, id=pk)
    if request.method == 'POST':
        student.delete()
        return HttpResponseRedirect(reverse('students:list'))

    return render(request, 'students/delete.html', {'student': student})


class StudentUpdateView(LoginRequiredMixin, UpdateView):
    model = Students
    form_class = StudentCreateForm
    success_url = reverse_lazy('students:list')
    template_name = 'students/update.html'

    pk_url_kwarg = 'ppk'


class StudentsListView(ListView):
    paginate_by = 10
    model = Students
    template_name = 'students/list.html'

    def get_filter(self):
        return StudentsFilter(
            data=self.request.GET,
            queryset=self.model.objects.all().select_related('group', 'headman_group')
        )

    def get_queryset(self):
        return self.get_filter().qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter_form'] = self.get_filter().form

        # params = self.request.GET
        # if 'page' in params:
        #     params = copy(params)
        #     del params['page']
        #
        # context['get_params'] = '&' + params.urlencode() if params else ''  # convert dict to str

        return context


