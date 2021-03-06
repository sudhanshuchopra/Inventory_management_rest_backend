from .serializers import UserSerializer
from rest_framework import generics
from items.models import Category,Item
from users.models import MyUser
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def get_items(request,email):
	users=MyUser.objects.filter(email=email)
	if(users.count()<0):
		return response({'invalid':'email'})
	user=users.first()
	borrowed_items=list(user.items.values())
	items=[]
	for each in borrowed_items:
		item={}
		category=Category.objects.get(id=each['category_id'])
		item['name']=category.name
		item['description']=category.description
		item['bid']=category.id
		item['pid']=each.id
		items.append(item)
	return Response(items)


@api_view(['POST'])
def add_items(request):
    request_obj=request.data
    obj_email=request_obj['email']
    users=MyUser.objects.filter(email=obj_email)
    if(users.count()<=0):
    	return Response({'invalid':'email'})
    user=users.first()
    if(user.is_superuser):
    	category_name=request_obj['product_name']
    	category_objs=Category.objects.all()
    	for each in category_objs:
    		if each.name==category_name:
    			return Response({'invalid':'item already exists pls go to update section'})
    	k=Category.objects.create(name=category_name,description=None)
    	obj_count=request_obj['quantity']
    	i=0
    	while(i<obj_count):
    		item=Item.objects.create(category=k,borrower=user)
    		i=i+1
    	return Response({'created':'objects created'})
    return Response({'invalid':'only admin can create objects'})

@api_view(['POST'])
def request_item(request):
	request_obj=request.data
	obj_id=request_obj['bid']
	obj_quantity=request_obj['quantity']
	obj_email=request_obj['email']
	users=MyUser.objects.filter(email=obj_email)
	if(users.count()<=0):
		return Response({'invalid':'user'})
	user=users.first()
	items=Item.objects.filter(borrower_id=1,category_id=obj_id)
	k=items.count()
	if(obj_quantity>k):
		return Response({'invalid':'The number of items requested is not available'})
	for item in items:
		if(obj_quantity>0):
			item.borrower=user
			item.save()
			obj_quantity=obj_quantity-1
	return Response({'message':'items provided'})


@api_view(['POST'])
def update_items(request):
    request_obj=request.data
    obj_email=request_obj['email']
    users=MyUser.objects.filter(email=obj_email)
    if(users.count()<=0):
    	return Response({'invalid':'email'})
    user=users.first()
    if(user.is_superuser):
    	category_id=request_obj['bid']
    	obj_count=request_obj['quantity']
    	category=Category.objects.filter(id=category_id).first()
    	borrower=MyUser.objects.filter(id=1).first()
    	k=Item.objects.filter(borrower_id=1,category_id=category_id)
    	k=k.count()
    	if(k<obj_count):
    		while(k<obj_count):
    			obj=Item.objects.create(category=category,borrower=borrower)
    			k=k+1
    	elif(k>obj_count):
    		items=Item.objects.filter(borrower_id=1,category_id=category_id)
    		for each in items:
    			if(k>obj_count):
    				each.delete()
    				k=k-1
    	return Response({'message':'inventory updated'})
    return Response({'invalid':'user is not a superuser'})

@api_view(['DELETE'])
def delete_item(request):
    request_obj=request.data
    category_id=request_obj['bid']
    email=request_obj['email']
    user=MyUser.objects.filter(email=email)
    if(user.count()<=0):
        return Response({'result':False})
    user=user.first()
    if not user.is_superuser:
        return Response({'result':False})
    category=Category.objects.filter(id=category_id)
    if(category.count()<=0):
        return Response({'result':False})
    category=category.first()
    category.delete()
    return Response({'result':True})