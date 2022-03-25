from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.http import HttpResponse,  HttpResponseRedirect


def home(request):
    return render(request, 'report/home.html')


def new_report(request):
    return HttpResponseRedirect(request, 'report/new_report.html')


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')


def logout_view(request):
    logout(request)


