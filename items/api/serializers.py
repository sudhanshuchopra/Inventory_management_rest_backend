from rest_framework import serializers
from items.models import Item,Category

class ItemSerializer(serializers.ModelSerializer):
	class Meta:
		model=Item
		fields=('id','category','borrower')

class CategorySerializer(serializers.ModelSerializer):
	items=serializers.PrimaryKeyRelatedField(many=True, queryset=Item.objects.all())
	class Meta:
		model=Category
		fields=('id','name','description','items')