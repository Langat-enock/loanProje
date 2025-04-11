"""
URL configuration for Enock project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from main_app import views
from main_app.views import approve_loan, apply_loan

# from .views import apply_loan

# app_name = 'main_app'  # Add this line

urlpatterns = [
    path('', views.home, name='home'),
    path('apply-loan/', apply_loan, name='apply_loan'),
    path('', views.loan, name='loan'),
    path('approve-loan/<int:loan_id>/', approve_loan, name='approve-loan'),
    path('admin/', admin.site.urls)
]


# urlpatterns = [
#
#     path('', views.home, name='home'),
#
#
#     # path('approve-loan/<int:loan_id>/', approve_loan, name='approve-loan'),
#     path('', views.apply_loan, name='apply-loan'),
#
#     path('admin/', admin.site.urls),
# ]
