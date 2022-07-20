from django.urls import path,include
from allauth import urls

from . import views

app_name = 'authentication'

urlpatterns = [
    path('home/', views.Home.as_view(), name='home'),
    path('', include('allauth.urls')),
    # path('', views.index, name='index'),
    # path('', views.index, name='index'),  
    
    # path('', views.IndexView.as_view(), name='index'),
    # path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    
    # path('<int:question_id>/vote/', views.vote, name='vote'),
]