from django.urls import path
from . import views

app_name = 'post'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('create/', views.PostCreateView.as_view(), name='post_create'),
    path('create/complete', views.PostCreateCompleteView.as_view(), name='post_create_complete')

]
