from django.shortcuts import render
from .models import Post
from django.http import Http404,HttpResponseRedirect
from django.urls import reverse

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
        name = request.POST['title']
        slug = request.POST['slug']
        html = request.POST['content']
        post = Post(title=name,
                    slug=slug,
                    content=html)
        post.save()
        return HttpResponseRedirect(f'../{slug}/')
    else:
        return render(request, 'create.html', {})

def update(request, slug):
    post = Post.objects.filter(slug=slug)[0]

    if request.method == "POST":
        post.title = request.POST['title']
        post.slug = request.POST['slug']
        post.content = request.POST['content']
        post.save()

        s = request.POST['slug']
        return HttpResponseRedirect(f'/{s}/')
    context = {'post': post}
    return render(request, 'update.html', context)

def delete(request,slug):
    post = Post.objects.filter(slug=slug)[0]

    if request.method == "POST":
        post.delete()
        return HttpResponseRedirect('/')
    context = {'post': post}
    return render(request, 'delete.html', context)
