from xml.dom.minidom import Document
from django.urls import path 
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import static 
urlpatterns = [
  path('', views.inicio, name="inicio"),
  path('resultados', views.resultados, name="resultados"),
  path('index', views.index, name="index"),
]+ static(settings.MEDIA_URL, Document_root=settings.MEDIA_ROOT)