from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .forms import IngredientUpdateForm, ReportUpdateForm
from .models import Ingredients, Report
from django.urls import reverse
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.views.generic import TemplateView


def home(request):
    return render(request, 'report/home.html')


class EntryView(ListView, LoginRequiredMixin, TemplateView):
    model = Report
    template_name = 'report/view_report.html'
    context_object_name = 'entry'

    def __init__(self):
        super().__init__()
        self.object_list = self.get_queryset()

    def entry(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return render(request, self.template_name, context)


class IngredientCreateView(CreateView, LoginRequiredMixin, TemplateView):
    model = Ingredients
    fields = ['id', 'name', 'discription']
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def get_success_url(self):
        return reverse('report:New Entry')

    def __init__(self, *args, **kwargs):
        super(IngredientCreateView, self).__init__(*args, **kwargs)
        self.object_list = self.get_queryset()


class ReportCreateView(CreateView, LoginRequiredMixin, TemplateView):
    model = Report
    fields = ['id', 'opening_bgs', 'opening_kgs', 'recieved', 'bags_used_bin', 'bags_used_Th3', 'kgs_used_Th3',
              'lot_number', 'current_bgs', 'current_kgs', 'total_used_kgs', 'expiry_date']
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def get_success_url(self):
        return reverse('report:New Report')

    def __init__(self):
        super().__init__()
        self.object_list = self.get_queryset()

    def entry(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return render(request, self.template_name, context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('report:Home')


def logout_view(request):
    logout(request)
