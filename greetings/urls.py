from django.urls import path
from . import views
urlpatterns = [
    path('',views.home, name='home'),
    path('add',views.add, name="add"),
    path('exam',views.exam, name="exam"),
    path('user_info',views.user_info,name="user_info"),
    path('password',views.password, name="password")
]
