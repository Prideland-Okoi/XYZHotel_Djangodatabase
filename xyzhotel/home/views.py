from django.shortcuts import render, redirect

from .forms import CommentForm
from .models import Post
# Create your views here.


def books(request):
    posts=Post.objects.all()
    return render(request, 'home/index.html', {'posts':posts})

def post_details(request, slug):
    post=Post.objects.get(slug=slug)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment =form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect('post_detail', slug=post.slug)
        else:
            form = CommentForm()
        return render(request, 'home/post_detail.html', {'post': post, 'form': form})