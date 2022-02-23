from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import UpdateView, ListView, CreateView, DeleteView

from students.models import Students

from .forms import GroupCreateForm
from .forms import GroupUpdateForm
from .models import Group


def create_group(requests):
    pass


def delete_group(requests):
    pass


def get_groups(requests):
    groups = Group.objects.all()

    return render(requests, 'groups/list.html', {'groups': groups})


class GroupListView(ListView):
    model = Group
    template_name = 'groups/list.html'


class GroupCreateView(CreateView):
    model = Group
    form_class = GroupCreateForm
    success_url = reverse_lazy('groups:list')
    template_name = 'groups/create.html'


class GroupUpdateView(UpdateView):
    model = Group
    form_class = GroupUpdateForm
    success_url = reverse_lazy('groups:list')
    template_name = 'groups/update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['students'] = self.get_object().students.prefetch_related('headman_group')

        return context

    def get_initial(self):
        initial = super().get_initial()
        try:
            initial['headman_field'] = self.object.headman.id
        except AttributeError:
            pass

        return initial

    def form_valid(self, form):
        response = super().form_valid(form)
        pk = form.cleaned_data['headman_field']
        if pk:
            form.instance.headman = Students.objects.get(id=form.cleaned_data['headman_field'])
        form.instance.save()

        return response


class GroupDeleteView(DeleteView):
    model = Group
    success_url = reverse_lazy('groups:list')
