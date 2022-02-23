from django.urls import path

from .views import StudentUpdateView
from .views import StudentsListView
from .views import create_student
from .views import delete_student

app_name = 'students'

urlpatterns = [
    path('', StudentsListView.as_view(), name='list'),                        # R
    path('create/', create_student, name='create'),                           # C
    path('update/<int:ppk>/', StudentUpdateView.as_view(), name='update'),    # U
    path('delete/<int:pk>/', delete_student, name='delete'),                  # D
]
