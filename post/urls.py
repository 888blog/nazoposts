from django.urls import path
from . import views

app_name = 'post'

urlpatterns = [
    # path('', views.TopViews.as_view(), name='top')
    path('', views.IndexView.as_view(), name='index')
]
