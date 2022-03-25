from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'report'
urlpatterns = [
    path('home/', views.home, name='home'),
    path('new_report/', views.new_report, name='new_report'),
    path('login/', auth_views.LoginView.as_view(template_name='report/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='report/logout.html'), name='logout'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
