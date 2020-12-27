"""myfood URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.contrib.auth.views import LogoutView
from foodapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('', include('social_django.urls', namespace='social')),
    path('logout/', LogoutView.as_view(template_name=settings.LOGOUT_REDIRECT_URL), name='logout'),
    path('product/', views.add_product, name='product'),
    path('category/', views.add_category, name='category'),
    path('delete_cat/', views.delete_category, name='delete_cat'),
    path('delete_prod/', views.delete_product, name='delete_prod'),
    path('purchase/', views.make_purchase, name='purchase'),
    path('delete_purch', views.delete_purchase, name='delete_purch'),
    path('date_filter/', views.date_filter, name='date_filter'),
    path('date_cat_filter/', views.date_and_cat_filter, name='date_cat_filter'),
    path('date_prod_filter/', views.date_and_prod_filter, name='date_prod_filter')
]
