
from django.urls import path
from . import views
app_name='signup'
urlpatterns = [
    path('',views.home,name='home'),
    path('login/', views.login_view, name='login_view'),
    path('signup/', views.reg, name='reg')
]
