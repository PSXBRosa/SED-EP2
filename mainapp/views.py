from django.db.models import Q
from .models import Category, Post, Comment
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from .forms import PostForm, CommentForm
from django.views import generic

def create_comment(request, post_id):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            author = form.cleaned_data['author']
            id = post_id
            content = form.cleaned_data['content']
            post = Comment(author=author,
                        post_id=id,
                        content=content)
            post.save()
            post_slug = get_object_or_404(Post, pk=post_id).slug
            return HttpResponseRedirect(f'../../{post_slug}')
    else:
        form = CommentForm()
    context = {'form':form}
    return render(request, 'comment.html', context)

def search(request):
    context = {"categories":Category.objects.all}
    post_list = Post.objects.all()

    if request.GET.get('query',False):
        search_term = request.GET['query'].lower()
        post_list = post_list.filter(title__icontains=search_term)

    if request.GET.get('category', False):
        ids = request.GET.getlist('category')
        for id in ids:
            post_list = post_list.filter(categories__id=id)

    context['post_list'] = post_list
    return render(request, 'index.html', context)
    
class IndexListView(generic.ListView):
    model = Post
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all
        return context

class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comments"] = Comment.objects.filter(post=self.object.id).order_by('-created_on')
        return context

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
