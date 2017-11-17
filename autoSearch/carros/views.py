# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import render

from .forms import CarModelForm
from .models import Car
from .mixin import FormUserNeededMixin

# Create your views here.

def home(request):
	prueba="esta es una prueba"
	contexto={"prueba":prueba}
	return render(request,'home.html',contexto)

class Car_list(ListView):
	model = Car

class Car_detail(DetailView):
	model = Car

class CarCreateView(LoginRequiredMixin, FormUserNeededMixin, CreateView):
	form_class=CarModelForm
	template_name="carros/create.html"
	success_url="Crear"
	login_url="/admin"
	
class CarUpdateView(UpdateView):
	queryset= Car.objects.all()
	form_class=CarModelForm
	template_name="carros/update.html"
	success_url="/list/"

class CarDeleteView(LoginRequiredMixin,DeleteView):
	model = Car
	template_name = "carros/delete_confirm.html"
	success_url = reverse_lazy("lista")


class Car_list(ListView):
    template_name = "carros/car_list.html"
    # queryset = Car.objects.all()

    def get_queryset(self, *args, **kwargs):
        qs = Car.objects.all()
        print self.request.GET
        query = self.request.GET.get("q", None)
        if query is not None:
            qs = qs.filter(
                            Q(make__icontains=query) |
                            Q(Type__icontains=query)
                          )
        return qs

    def get_context_data(self, *args, **kwargs):
        context = super(Car_list, self).get_context_data(*args, **kwargs)
        print context
        context['create_form'] = CarModelForm()
        context['create_url'] = reverse_lazy("Crear")
        return context