from django.urls import path
from .views import *

urlpatterns = [
       path('', homepage, name='home'),
       path('upload/', upload, name='upload'),
]
