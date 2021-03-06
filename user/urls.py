from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('login/', views.Login.as_view(), name = 'login'),
    path('logout/', views.Logout, name = 'logout'),
    path('signup', views.SignUpView.as_view(), name = 'signup'),
]
