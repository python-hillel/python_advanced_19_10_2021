from django.urls import path

from .views import GroupCreateView
from .views import GroupDeleteView
from .views import GroupListView
from .views import GroupUpdateView

app_name = 'groups'

urlpatterns = [
    path('', GroupListView.as_view(), name='list'),                        # R
    path('create/', GroupCreateView.as_view(), name='create'),             # C
    path('update/<int:pk>/', GroupUpdateView.as_view(), name='update'),    # U
    path('delete/<int:pk>/', GroupDeleteView.as_view(), name='delete'),    # D
]
