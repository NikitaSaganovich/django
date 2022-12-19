from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name = 'home'),
    path('about-us', views.about, name = 'about'),
    path('new',views.new, name = 'new'),
    path('primer',views.exampleHTML, name = 'example'),
    path('create', views.create, name='create'),

]
