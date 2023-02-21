from django.shortcuts import render
from django.http import HttpResponse


def home_page_view(require):
    return HttpResponse('hi welcome to home')
