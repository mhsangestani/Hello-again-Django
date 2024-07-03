from django.shortcuts import render, get_object_or_404
from blog.models import Post
from django.utils import timezone

# Create your views here.

def blog_view(request):
    Post.objects.filter(published_date__lte=timezone.now()).update(status=True)
    posts=Post.objects.filter(status=True)
    context = {'posts':posts} 
    return render(request, 'blog/blog-home.html', context)


def blog_single_view(request, pid):
    post = get_object_or_404(Post, pk=pid)

    post.counted_views += 1
    post.save()
    context = {'post':post}
    return render(request, 'blog/blog-single.html', context) 