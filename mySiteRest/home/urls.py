from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index_rest, name='index_rest'),
    path('indexrest/', views.IndexRest.as_view()),
]
