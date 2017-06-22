from .serializers import CategorySerializer,ItemSerializer
from rest_framework import generics
from items.models import Category,Item
from rest_framework.decorators import api_view
from rest_framework.response import Response


class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ItemList(generics.ListCreateAPIView):
	queryset=Item.objects.all()
	serializer_class=ItemSerializer


class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset=Item.objects.all()
	serializer_class=ItemSerializer

@api_view(['GET'])
def stock_status(request):
    category_list=Category.objects.all()
    categories=[]
    for each in category_list:
    	category={}
    	category['name']=each.name
    	category['description']=each.description
    	free_objects=0
    	obj_list=list(each.items.values())
    	for every in obj_list:
    		print(every)
    		if every['borrower_id']==1:
    			free_objects=free_objects+1
    	category['count']=free_objects
    	categories.append(category)

    return Response(categories)
