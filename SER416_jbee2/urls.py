"""SER416_jbee2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

from SER416_jbee2.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('login/', login),
    path('create_user/', create_user),
    path('customer_portal/', customer_portal),
    path('admin_portal/', admin_portal),
    path('make_donation/', make_donation),
    path('book_event/', book_event),
    path('class_signup/', class_signup),
    path('volunteer/', volunteer),
    path('request_homecare/', request_homecare),
    path('request_shuttle/', request_shuttle),
    path('confirmation/', confirmation),
    path('view_events/', view_events),
    path('view_equipment/', view_equipment),
    path('view_classes/', view_classes),
]
