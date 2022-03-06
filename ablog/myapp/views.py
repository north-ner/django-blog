from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post
#def home(request):
#	return render(request,'home.html',{})
# Create your views here.
class HomeView(ListView):
	#this we have created in the mdoels.py
	model = Post
	template_name='home.html'
class ArticleDetailView(DetailView):
	model =Post
	template_name='articles_details.html'
