from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from .models import Post
from .forms import PostForm

class IndexView(TemplateView):
    template_name = "post/index.html"


class PostCreateView(LoginRequiredMixin, CreateView):
    template_name = "post/post_create.html"
    form_class = PostForm
    success_url = reverse_lazy('post:post_create_complete')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostCreateCompleteView(TemplateView):
    template_name = "post/post_create_complete.html"
