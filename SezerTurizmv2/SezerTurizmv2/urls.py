"""
URL configuration for SezerTurizmv2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from core.models import Section

def generate_dynamic_urls():
    urlpatterns = []
    for section in Section.objects.all():
        try:
            app_name = section.name
            urlpatterns.append(path(app_name.lower() + '/', include(f'{app_name}.urls')))
        except Exception:
            # Handle the error or log it
            pass
    return urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
] + generate_dynamic_urls()