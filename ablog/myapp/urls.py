
from django.urls import path
#from . import views
#from views file we are importing HomeView class that we created there
from .views import HomeView
urlpatterns = [
    #path('',views.home,name="home"),
    #'' this means that we are directing it to the home page i.e. the root page
    path('',HomeView.as_view(),name="home"),
]
