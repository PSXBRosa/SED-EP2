from typing import SupportsComplex
from django.shortcuts import render
from .models import Post
from django.http import Http404,HttpResponseRedirect
from .forms import PostForm
from django.views import generic

class IndexListView(generic.ListView):
    model = Post
    template_name = 'index.html'

class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'detail.html'

class PostCreateView(generic.CreateView):
    model = Post
    template_name = 'create.html'
    form_class = PostForm
    def get_success_url(self) -> str:
        return '/' + self.object.slug

class PostUpdateView(generic.UpdateView):
    model = Post
    template_name = 'update.html'
    form_class = PostForm
    def get_success_url(self) -> str:
        return '/'+ self.object.slug

class PostDeleteView(generic.DeleteView):
    model = Post
    template_name = 'delete.html'
    success_url = '/'