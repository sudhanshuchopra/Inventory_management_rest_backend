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
		item['count']=category.items.filter(borrower=user).count()
		var=0
		for i in items:
			if(i['name']==item['name']):
				var=1
		if var==0:
			items.append(item)
	return Response(items)




