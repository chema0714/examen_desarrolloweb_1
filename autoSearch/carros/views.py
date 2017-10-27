# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.views.generic import ListView
from .models import Car
from django.views.generic.detail import DetailView
# Create your views here.

def home(request):
	prueba="esta es una prueba"
	contexto={"prueba":prueba}
	return render(request,'home.html',contexto)

class Car_list(ListView):
	model = Car

class Car_detail(DetailView):
	model = Car
