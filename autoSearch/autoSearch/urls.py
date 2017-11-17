"""autoSearch URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from carros.views import home, Car_list, Car_detail, CarCreateView, CarUpdateView, CarDeleteView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home, name='home'),
    url(r'^list/', Car_list.as_view() , name='lista'),
    url(r'^detail/(?P<pk>\d+)/', Car_detail.as_view() , name='detalle'),
    url(r'^create/',CarCreateView.as_view(),name="Crear"),
    url(r'^update/(?P<pk>\d+)/',CarUpdateView.as_view(), name="Actualizar"),
    url(r'^delete/(?P<pk>\d+)/',CarDeleteView.as_view(),name="BorrarElemento"),
]
