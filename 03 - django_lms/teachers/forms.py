from django.forms import ModelForm

from .models import Teacher


class TeacherBaseForm(ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'


class TeacherCreateForm(TeacherBaseForm):
    pass
