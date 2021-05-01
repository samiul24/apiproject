from rest_framework import serializers
from .models import Category, Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=[
                'id','Category','Title','Keywords',
                'Description','Variant','Image',
                'Price','Amount','MinAmount',
                'Details','Slug','Status',
                ]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=[
                'id','parent','Title',
                'Keywords','Description','Image',
                'Status','Slug',
               ]

class NewProductSerializer(serializers.ModelSerializer):
    Category=CategorySerializer(many=True)
    class Meta:
        many=True
        model=Product
        fields=['id','Category']
        