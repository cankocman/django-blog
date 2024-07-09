from django.shortcuts import render, get_object_or_404, redirect
from .models import BlogPost
from .forms import CommentForm


def blog_list(request):
    posts = BlogPost.objects.all()
    return render(request, 'blog/blog_list.html', {'posts': posts})


def blog_detail(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    comments = post.comments.all()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('blog_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/blog_detail.html', {'post': post, 'comments': comments, 'form': form})
