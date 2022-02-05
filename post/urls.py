from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'post'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('create/', views.PostCreateView.as_view(), name='post_create'),
    path('create/complete', views.PostCreateCompleteView.as_view(), name='post_create_complete')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)