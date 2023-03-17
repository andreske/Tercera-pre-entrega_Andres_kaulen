from django.http import HttpResponse
from django.shortcuts import render
from AppWeb.models import Home

def home(request):
    return render(request, "index.html")

