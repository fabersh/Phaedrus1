
from django.contrib import admin
from django.urls import  include, path

urlpatterns = [
    path('phaedrus/', include('phaedrus.urls')),
    path('admin/', admin.site.urls)
]
