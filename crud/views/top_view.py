from django.shortcuts import render
from django.views.generic import TemplateView

#TemplateViewを継承したクラスを定義する
class TopView(TemplateView):
    template_name = "top.html"
