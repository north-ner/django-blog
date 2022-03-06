
from django.urls import path
#from . import views
#from views file we are importing HomeView class that we created there
from .views import HomeView, ArticleDetailView
urlpatterns = [
    #path('',views.home,name="home"),
    #'' this means that we are directing it to the home page i.e. the root page
    path('',HomeView.as_view(),name="home"),
#int:pk wis for the prinmary key of the post in the database
    path('article/<int:pk>',ArticleDetailView.as_view(),name='article-detail'),
]
