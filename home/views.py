from django.shortcuts import render, redirect
from admin_datta.forms import RegistrationForm, LoginForm, UserPasswordChangeForm, UserPasswordResetForm, UserSetPasswordForm
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordResetConfirmView, PasswordResetView
from django.views.generic import CreateView
from django.contrib.auth import logout
from .forms import Reportingform
from .models import *
from django.core.serializers import serialize
from django.contrib.auth.decorators import login_required
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response

def index(request):
  data = Govpersonnel.objects.all()

  context = {
    'datas'  : data,
    #'products' : Product.objects.all()
  }
  return render(request, "pages/index.html", context)

def tables(request):
  context = {
    'segment': 'tables'
  }
  return render(request, "pages/dynamic-tables.html", context)

@api_view(["GET"])
def sendModel(request):
  data = Govpersonnel.objects.all()
  rendered_data=serialize("json", data)
  return Response(rendered_data)
  



# def reporting_forms(request):
#   if request.POST:
#     form = Reportingform(request.POST, request.media)

#   return render(request, "pages/reportform.html", context)
