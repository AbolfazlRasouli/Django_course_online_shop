from django.shortcuts import render
from django.views.generic import TemplateView


class Homepage(TemplateView):
    template_name = 'home.html'


class AboutUsPageView(TemplateView):
    template_name = 'pages/abouts.html'

