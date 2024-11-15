from django.shortcuts import render
from django.views.generic import ListView
from .models import UserData

# Create your views here.
class UserDataList(ListView):
    model = UserData