from django.shortcuts import render, get_object_or_404
from blog.models import Post
from django.utils import timezone

# Create your views here.

def blog_view(request):
    posts=Post.objects.filter(published_date__lte=timezone.now(), status=True)
    context = {'posts':posts} 
    return render(request, 'blog/blog-home.html', context)


def blog_single_view(request, pid):
    posts=Post.objects.filter(published_date__lte=timezone.now(), status=True)
    post = get_object_or_404(Post, pk=pid, status=1, published_date__lte=timezone.now())
    post.counted_views += 1
    post.save()
    context = {
          'post': post,
          'next': posts.filter(id__gt=post.id).order_by('id').first(), 
          'previous': posts.filter(id__lt=post.id).order_by('-id').first()
        }
    return render(request, 'blog/blog-single.html', context) 