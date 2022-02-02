from django.shortcuts import render
from django.views.generic import TemplateView

class TopView(TemplateView):
    template_name = "post/top.html"


class IndexView(TemplateView):
    template_name = "post/index.html"

