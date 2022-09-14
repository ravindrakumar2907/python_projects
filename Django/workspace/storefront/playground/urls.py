## Map urls to view functions

from django.urls import path

from . import views

# url config
urlpatterns = [
    path('hello/', views.hellow),
    path('index/', views.myView),
    path('index1/', views.index1),
    path('data/', views.data)
]