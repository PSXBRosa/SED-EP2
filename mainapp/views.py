from django.shortcuts import render
from .models import Post
from django.http import Http404,HttpResponseRedirect
from django.urls import reverse
from .forms import PostForm

def index(request):
    post_list = Post.objects.all
    context = {'post_list': post_list}
    return render(request, "index.html", context)

def detail(request, slug):
    post = Post.objects.filter(slug=slug)
    if len(post) == 0:
        raise Http404("page does not exist")
    context = {'post':post[0]}
    return render(request, "detail.html", context)

def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['title']
            slug = form.cleaned_data['slug']
            html = form.cleaned_data['content']
            post = Post(title=name,
                        slug=slug,
                        content=html)
            post.save()
            return HttpResponseRedirect(f'../{slug}/')
    else:
        form = PostForm()
    context = {'form':form}
    return render(request, 'create.html', context)

def update(request, slug):
    post = Post.objects.filter(slug=slug)[0]

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post.title = form.cleaned_data['title']
            post.slug = form.cleaned_data['slug']
            post.content = form.cleaned_data['content']
            post.save()

            s = form.cleaned_data['slug']
            return HttpResponseRedirect(f'/{s}/')
    else:
        form = PostForm(
            initial={
                'title': post.title,
                'slug': post.slug,
                'content': post.content
            }
        )
    context = {'post':post, 'form':form}
    return render(request, 'update.html', context)

def delete(request,slug):
    post = Post.objects.filter(slug=slug)[0]

    if request.method == "POST":
        post.delete()
        return HttpResponseRedirect('/')
    context = {'post': post}
    return render(request, 'delete.html', context)
