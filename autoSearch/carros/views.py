# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

def home(request):
	prueba="esta es una prueba"
	contexto={"prueba":prueba}
	return render(request,'home.html',contexto) 
