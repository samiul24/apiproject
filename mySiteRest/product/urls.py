from django.urls import path, include
from . import views
#from product import views

app_name='Product'

urlpatterns = [
    #path('', views.index, name='index'),
    path('productlist/', views.ProductAPIView.as_view()),
    path('productlist/<int:pk>/', views.ProductDeatilAPIView.as_view()),
    path('categorylist/', views.CategoryAPIView.as_view()),
    path('display_categories/',views.display_categoryies),
    path('categorylist/<int:pk>/', views.CategoryDetailsAPIView.as_view())
    #path('search_auto/', views.search_auto, name='search_auto'),
    #path('comment/<int:id>/', views.comment, name='comment'),
]
