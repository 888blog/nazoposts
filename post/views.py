from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, DetailView
from .models import Post
from .forms import PostForm


class PostListView(ListView):
    model = Post
    template_name = "post/index.html"
    ordering = '-created_at'


class PostCreateView(LoginRequiredMixin, CreateView):
    template_name = "post/post_create.html"
    form_class = PostForm
    success_url = reverse_lazy('post:post_create_complete')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = self.get_form()
        context = {
            'form': form,
        }
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostCreateCompleteView(TemplateView):
    template_name = "post/post_create_complete.html"


class PostQuestionView(DetailView):
    model = Post
    template_name = "post/post_question.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        count = 0
        q = Post.objects.get(uuid=self.kwargs['pk'])
        if q.q_img1:
            count += 1
        if q.q_img2:
            count += 1
        if q.q_img3:
            count += 1
        if q.q_img4:
            count += 1
        context['img_count'] = count
        return context

class PostAnswerView(DetailView):
    model = Post
    template_name = "post/post_answer.html"
