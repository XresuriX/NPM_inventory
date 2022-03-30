from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    EntryView,
    IngredientCreateView,
    ReportCreateView,
    #ReportUpdateView,
    #ReportDeleteView
)


app_name = 'report'
urlpatterns = [
    path('', views.home, name='home'),
    path('ingredient/new', IngredientCreateView.as_view(), name='New Entry'),
    path('report/new', ReportCreateView.as_view(), name='New Report'),
    path('view_report', EntryView.as_view(), name='View Report'),
    path('login/', auth_views.LoginView.as_view(template_name='report/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='report/logout.html'), name='logout'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

