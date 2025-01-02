from django.urls import path, include 
from .views import UserView,UserCreateView, GetUser


urlpatterns =[
    path('me/',UserView.as_view(), name='user-detail'),
    path('create/',UserCreateView.as_view(),name='user-create'),
    path('<id>/', GetUser.as_view(), name='user-get'),
    

]