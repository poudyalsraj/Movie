from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import MovieGenre, Movie,  PageView
from django.contrib.auth import authenticate 
from django.core.urlresolvers import reverse_lazy,reverse


#This class will display the listview of movigenre objects
class MovieGenreListView(ListView):
	
	model = MovieGenre
	template_name= 'managemovie/home.html'
	def get_context_data(self, **kwargs):
		context = super(MovieGenreListView, self).get_context_data(**kwargs)
		
		x=PageView.objects.all()[0]
		x.hits=x.hits+1
		x.save()

		context1={
		'page':x.hits,

		}

		context.update(context1)
		return context
		
#This class will display the Detail of movigenre objects that includes all the movies related to that genre
class MovieGenreDetailView(DetailView):
	
	model=MovieGenre
	def get_context_data(self, **kwargs):

		context = super(MovieGenreDetailView, self).get_context_data(**kwargs)
		context['movies'] = Movie.objects.all()
		return context


#this class will create form field of the genres
class MovieGenreCreateView(CreateView):
		
		model = MovieGenre
		fields= [
			'name',
			'image',
			'discription'
			]
		success_url = reverse_lazy('managemovie:home')


#this class will render the form field with field value to update the genre objects
class MovieGenreUpdateView(UpdateView):
		
		model = MovieGenre
		fields= [
			'name',
			'image',
			'discription'
			]
		success_url = reverse_lazy('managemovie:home')

#this class will delete the genre objects
class MovieGenreDeleteView(DeleteView):
		
		model = MovieGenre
		success_url = reverse_lazy('managemovie:home')


#******************************************************************************************
#following this codes are for movie 

#this class will display the listview of the movie objects
class MovieListView(ListView):

	model = Movie
	def get_context_data(self, **kwargs):
		context = super(MovieListView, self).get_context_data(**kwargs)
		
		x=PageView.objects.all()[0]
		x.hits=x.hits+1
		x.save()

		context1={
		'page':x.hits,

		}

		context.update(context1)
		return context


#this class will display the detailview of the movie objects
class MovieDetailView(DetailView):
	
	model=Movie
	def get_context_data(self, **kwargs):
		context = super(MovieDetailView, self).get_context_data(**kwargs)
		return context
	

#this class will create and display the form field for the movie objects to add new objects
class MovieCreateView(CreateView):
		
		model = Movie
		fields= [
			'title',
			'genre',
			'language',
			'release_date',
	
			'synopsisa',
			'logo','trailer'
			]
		success_url = reverse_lazy('managemovie:home')

#this class will create and display the form field with field value 
class MovieUpdateView(UpdateView):
		
		model = Movie
		fields= [
			'title',
			'genre',
			'language',
			'release_date',
			'synopsisa',
			'logo','trailer'
			]
		def get_success_url(self):
			return reverse('managemovie:moviegenre-detail', args=(self.object.genre.id,))


#this class will delete the movie objects
class MovieDeleteView(DeleteView):
		model = Movie
		def get_success_url(self):
			return reverse('managemovie:moviegenre-detail', args=(self.object.genre.id,))




#*********************************Raw Codes****************************************

# # class UserCreateView(CreateView):
# # 		model = User
# # 		fields= ['email_id', 'mobile_num', 'first_name', 'last_name','password']
# # 		success_url='add_user_success'

# #to book seat
# class BookingSeatCreateView(CreateView):
# 		model = BookingSeat
# 		fields= ['movie', 'email_id', 'seat_num', 'show_num']
# 		success_url='add/add_user_success'

# def addUserSucess(request):
# 	template='managemovie/a.html'
# 	return render(request, template)


# def userAuthentication(request):
# 	template1='managemovie/movie_list.html'
# 	template2='managemovie/loginfailed.html'
# 	all_users= User.objects.all()
# 	emailid = request.POST.get('emailid')
# 	password = request.POST.get('password')
# 	for user in all_users:
# 		if user.email_id == emailid and user.password == password:
# 			return redirect('managemovie:movie-list')
# 		# else: 
# 		# 	return render(request, template2)
			
# def login(request):
#    if request.method == 'POST':
#       form = LoginForm(request.POST)
#       if form.is_valid():
#          username = request.POST['username']
#          password = request.POST['password']
#          user = authenticate(request, username=username, password=password)
#          if request.user.is_authenticated():
#             if user is not None:
#                return redirect('managemovie:movie-list' )
#             else:
#                return HttpResponse('Invalid Username or password. Please try again')
#          else:
#                return render(request, "login.html")
#    else:
#          form = LoginForm()
#    return render(request, "login.html", {'form':form})


# # #this function is for counting the num of visitors
# # def Home(request):

# #     if(PageView.objects.count()<=0):
# #         x=PageView.objects.create()
# #         x.save()
# #     else:
# #         x=PageView.objects.all()[0]
# #         x.hits=x.hits+1
# #         x.save()
# #     context={'page':x.hits}
# #     return  render(request,'managemovie/movie_list.html',context=context)

# # class MovieFilterView(ListView):

# # 	def get_queryset(self):
# # 		self.publisher = get_object_or_404(Movie, name=self.args[0])
# # 		return Movie.objects.filter(publisher=self.publisher)

# # 	def get_context_data(self, **kwargs):

		
# # 		context = super(MovieListView, self).get_context_data(**kwargs)
		
# # 		return context