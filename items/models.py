from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


# Create your models here.
class Category(models.Model):
	name=models.CharField(max_length=150)
	description=models.TextField(null=True,blank=True)


	def __str__(self):
		return self.name

class Item(models.Model):
	category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name='items')
	borrower=models.ForeignKey(User,default=1,related_name='items')