"""MealOrder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
# from django.conf.urls import url    # , include
from meals import views as meals_views
from orders import views as orders_views
from . import views

# app_name = 'meals'

urlpatterns = [
    path('admin/', admin.site.urls),

    # To define the homepage
    # url('^$', meals_views.homepage, name='homepage'),
    # path('', meals_views.homepage, name='homepage'),

    path('', meals_views.all_meals, name='all_meals'),

    # path('meals/', meals_views.all_meals, name='all_meals'),

    path('details/<int:id>/<str:slug>/', meals_views.meal_details, name='meal_details'),

    path('order/<int:id>/', orders_views.make_order, name='make_order'),

    path('admin_view/all_orders/', views.view_orders, name='view_orders'),

    path('admin_view/add_meal.html/', meals_views.add_meal, name='add_meal'),

    ]

# This is to define the Media files url, so it could be accessible from browser for example.
# This is not suitable for production use!
# https://docs.djangoproject.com/en/2.1/howto/static-files/#serving-files-uploaded-by-a-user-during-development
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


