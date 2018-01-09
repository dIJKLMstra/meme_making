from django.db import models

# Create your models here.
class Image(models.Model):
	#pic_label = models.CharField(max_length=30)
	pic = models.ImageField(upload_to="pic_folder/")