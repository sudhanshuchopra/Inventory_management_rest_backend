from rest_framework import serializers
from users.models import MyUser
from items.models import Item


class UserSerializer(serializers.ModelSerializer):
	items=serializers.PrimaryKeyRelatedField(many=True, queryset=Item.objects.all())
	class Meta:
		model=MyUser
		fields=('id','username','email','items')