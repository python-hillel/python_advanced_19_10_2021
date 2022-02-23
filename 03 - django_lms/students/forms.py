from django import forms

from django_filters import FilterSet

from .models import Students


class StudentCreateForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = [
            'first_name',
            'last_name',
            'phone_number',
            'birthday'
        ]

        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'})
        }

    @staticmethod
    def normalize_name(value):
        return value.lower().capitalize()

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        return self.normalize_name(first_name)

    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        return self.normalize_name(last_name)


class StudentsFilter(FilterSet):
    class Meta:
        model = Students
        fields = {
            'age': ['lt', 'gt'],
            'first_name': ['exact', 'icontains'],
            'last_name': ['exact', 'startswith'],
        }
