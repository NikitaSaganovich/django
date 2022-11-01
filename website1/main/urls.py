from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('about-us', views.about),
    path('new',views.new),
    path('exampleHTML',views.exampleHTML),
]
