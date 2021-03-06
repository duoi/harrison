"""harrison URL Configuration

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
from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, re_path, include

from imaging.viewsets import login_required_files

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^', include(('harrison.api', 'api'), namespace='api', )),
    url(r'^media/(?P<path>.*)$', login_required_files,
        {'document_root': settings.MEDIA_ROOT}),
]
