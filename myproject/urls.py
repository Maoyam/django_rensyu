"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from crud.views.top_view import TopView
from crud.views.product_list_view import ProductListView
from crud.views.product_create_view import ProductCreateView
from crud.views.product_update_view import ProductUpdateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TopView.as_view(), name="top"),
    path('crud/', ProductListView.as_view(), name="list"),
    path('crud/new/', ProductCreateView.as_view(), name="new"),
    path('crud/edit/<int:pk>', ProductUpdateView.as_view(), name="edit"),
]
