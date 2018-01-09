"""meme_making URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from index import views as iv
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', iv.index,name='index'),
    url(r'^upload/',iv.upload,name='upload'),
    url(r'^upload_info/',iv.upload_pic,name='upload_info'),
    url(r'^img_list/',iv.listImg,name='img_list'),
    url(r'^chosedImg/',iv.chosedImg,name='chosedImg'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
