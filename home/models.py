from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class media(models.Model):
	title = models.CharField(max_length=100)
	description=models.TextField(max_length=200)
	date_uploaded=models.DateTimeField()
	data=models.FileField(upload_to='uploads/%Y/%m/%d/',null=True)
	author = models.ForeignKey(User,on_delete=models.CASCADE,)
	media_type=models.CharField(max_length=50,null=True)