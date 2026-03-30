from django.urls import include, path
from . import views

urlpatterns = [
    path('',views.home_page),
    path('entry/',views.entry_page),
    path('home/',views.home_page)
]