
from django.contrib import admin
from django.urls import path
from mydemoproject.views import demo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('demo/', demo),
]

