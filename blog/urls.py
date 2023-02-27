from django.urls import path
from . import views
app_name='blog'
urlpatterns = [
    path('',views.bloglist,name='bloglist'),
    path('create/', views.create, name='create'),
    path('profile/', views.profile, name='profile'),
    path('logout_view',views.logout_view, name='logout_view'),
    path('politics/',views.politics,name='politics'),
    path('entertainment/',views.entertainment,name='entertainment'),
    path('sports/',views.sports,name='sports'),
    path('business/',views.business,name='business'),
    path('education/',views.education,name='education'),
    path('other/',views.other,name='other'),
    path('<str:slug>/',views.blogpost,name='blogpost'), 
   
]
