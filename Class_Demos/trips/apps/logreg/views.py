# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import HttpResponse, redirect, render
from django.views import View

# Create your views here.
# def index(request):
#     response = "Placeholder to verify logreg creation."
#     return HttpResponse(response)

class LandingView(View):
    def get(self, request):
        """Takes us to logreg"""
        template = 'logreg/index.html'
        context = {}
        return render(request, template, context)
