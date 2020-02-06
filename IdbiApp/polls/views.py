from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello IDBI Users, You're at the polls index.")
