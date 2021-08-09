from django.shortcuts import render

# Create your views here.
from django.urls import path

from commentapp.urls import CommentCreateView

app_name = 'commentapp'


urlpatterns = [
    path('create/', CommentCreateView.as_view(), name='create'),
]