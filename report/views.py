from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout
from .forms import IngredientUpdateForm, ReportUpdateForm
from .models import Ingredients, Report
from django.urls import reverse
from django.views.generic import TemplateView
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView
)
# Import PDF Stuff
from django.http import HttpResponse

from django.template.loader import get_template

from xhtml2pdf import pisa


def home(request):
    return render(request, 'report/tester.html')


def production_view(request):
    return render(request, 'report/Production_view.html')


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
    form_class = IngredientUpdateForm
    template_name = 'ingredients_form.html'
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def get_success_url(self):
        return reverse('report:New Entry')

    def get(self, request, *args, **kwargs):
        form = self.form_class
        return render(request, 'report/ingredients_form.html', {'form': form})


class ReportCreateView(CreateView, LoginRequiredMixin, TemplateView):
    model = Report
    form_class = ReportUpdateForm
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def get_success_url(self):
        return reverse('report:New Report')

    def get(self, request, *args, **kwargs):
        form = self.form_class
        return render(request, 'report/report_form.html', {'form': form})


class UpdateEntryView(UpdateView, LoginRequiredMixin, TemplateView):
    model = Report
    form_class = ReportUpdateForm
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def get_success_url(self):
        return reverse('report:View Report')

    def get(self, request, *args, **kwargs):
        form = self.form_class
        return render(request, 'report/report_form.html', {'form': form})


# Generate a PDF File Venue List
def report_pdf(request):
    entries = Report.objects.all()

    template_path = 'report/pdf_Report.html'

    context = {'entries': entries}

    response = HttpResponse(content_type='application/pdf')

    response['Content-Disposition'] = 'filename="pdf_report.pdf"'

    template = get_template(template_path)

    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('report:Home')


def logout_view(request):
    logout(request)
