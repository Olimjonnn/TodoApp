from django.contrib import admin
from django.urls import path
from main.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path("works/", WorksView.as_view()),
    path("works/true/", WorkTrue.as_view()),
    path("works/false/", WorkFalse.as_view()),
]


