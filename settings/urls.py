'''
Root directories URLs file for the entire project
'''
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('base.urls')),
]
