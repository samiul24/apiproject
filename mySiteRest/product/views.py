"""from django.shortcuts import render, HttpResponseRedirect
from django.contrib import messages
from django.http import HttpResponse,JsonResponse
from product.models import Product,Category,Comments,CommentForm
import json"""
from product.models import Product, Category
from django.http import Http404
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView #Class Based View
from rest_framework.decorators import api_view #Function Based View
from .serializers import ProductSerializer, CategorySerializer, NewProductSerializer
import requests

# Create your views here.
class CategoryAPIView(APIView):
    def get(self, request):
        categorys=Category.objects.all().order_by('id','Title')
        serializer=CategorySerializer(categorys, many=True)
        return Response(serializer.data)  
    
    def post(self, request):
        serializer=CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CategoryDetailsAPIView(APIView):
    def get_object(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return Http404

    def get(self, request, pk):
        category=self.get_object(pk)
        serializer=CategorySerializer(category)
        return Response(serializer.data)
    
    def put(self, request, pk):
        category=self.get_object(pk)
        serializer=CategorySerializer(category, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
    
    def delete(self, request, pk):
        category=self.get_object(pk)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProductAPIView(APIView):
    def get(self, request, **kwargs):
        print(kwargs.get("id"))
        products=Product.objects.all()
        """for product in products:
            category=Category.objects.get(id=product.Category.id)
            print(category)"""
        
        serializer=NewProductSerializer(products, many=True)
        return  Response(serializer.data)
    
    def post(self, request):
        serializer=ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDeatilAPIView(APIView):
    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        product=self.get_object(pk)
        serializer=ProductSerializer(product)
        return Response(serializer.data)

    def put(self, request, pk):
        product=self.get_object(pk)
        serializer=ProductSerializer(product, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)      
    
    def delete(self, request, pk):
        product=self.get_object(pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

## Display Category Data
def display_categoryies(request):
    print('Samiul')
    categories=requests.get('http://127.0.0.1:8000/product/categorylist/')
    categories=categories.json()
    context={
        'categories':categories,
    }
    return render(request,'categories.html', context)



"""def search_auto(request):
    #print(request.GET)
    userSearching = request.GET.get('term')
    #print(userSearching)
    data = Product.objects.filter(Title__icontains=userSearching)
    productlist = []
    productlist += [x.Title for x in data]
    #print(productlist)
    return JsonResponse(productlist,safe=False)


def comment(request,id):
    url = request.META.get('HTTP_REFERER')  # get last url
    form = CommentForm()
    if request.method=='POST':
        data = Comments() # Create a relation with Comment Model
        form = CommentForm(request.POST)
        if form.is_valid():
            #print(id)
            data.Product_id = id
            data.Subject = form.cleaned_data['Subject']
            data.Comment = form.cleaned_data['Comment']
            data.Rating = form.cleaned_data['Rating']
            current_user = request.user
            #print(current_user)
            data.User_id = current_user.id
            #print(data.User_id)
            data.save()
            messages.success(request,'Thanks for your review')
            return HttpResponseRedirect(url)

    return HttpResponseRedirect(url)"""
