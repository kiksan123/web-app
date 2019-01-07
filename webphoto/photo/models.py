from django.db import models


class Post(models.Model):
	title = models.CharField(max_length=255)
	text = models.TextField()
	tag1 = models.CharField(max_length=255)
	tag2 = models.CharField(max_length=255)
	tag3 = models.CharField(max_length=255)
	author = models.CharField(max_length=255)
	images = models.ImageField(upload_to="images")
