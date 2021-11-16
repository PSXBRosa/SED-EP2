from .models import Post, Comment
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from .forms import PostForm, CommentForm
from django.views import generic

def create_comment(request, post_id):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            author = form.cleaned_data['author']
            post = post_id
            content = form.cleaned_data['content']
            post = Comment(author=author,
                        post_id=post,
                        content=content)
            post.save()
            post_slug = get_object_or_404(Post, pk=post_id)
            return HttpResponseRedirect(f'../../{post_slug}')
    else:
        form = CommentForm()
    context = {'form':form}
    return render(request, 'comment.html', context)

class IndexListView(generic.ListView):
    model = Post
    template_name = 'index.html'

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
