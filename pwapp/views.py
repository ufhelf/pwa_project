from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import sqlite3 as sql3

def index(request):
    return render(request, 'index.html')