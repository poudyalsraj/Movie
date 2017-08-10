from django.db import models
from django.urls import reverse


class MovieGenre(models.Model):
	name =models.CharField(max_length= 50)
	image=models.FileField(blank=True)
	discription=models.TextField(max_length=500)

	def __str__ (self):
		return self.name


class Movie(models.Model):

	title =models.CharField(max_length=50)
	genre=models.ForeignKey(MovieGenre, on_delete=models.CASCADE)
	language= models.CharField(max_length=30)
	release_date=models.DateField()
	synopsisa=models.TextField(max_length=300 ,blank=True)
	logo=models.FileField(blank=True)
	trailer=models.TextField(max_length=300)

	def __str__(self):
		return self.title 


class PageView(models.Model):
	hits=models.IntegerField(default=0)

# class BookingSeat(models.Model):
# 	movie=models.ForeignKey(Movie, on_delete=models.CASCADE)
# 	email_id= models.CharField(max_length=50, default='poudyalsraj@gmail.com')
# 	seat_num= models.IntegerField(default=0)
# 	show_num= models.IntegerField(default=1)

# 	def __str__(self):
# 		return self.email_id+self.movies