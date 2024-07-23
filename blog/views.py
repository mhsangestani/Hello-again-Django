from django.shortcuts import render, get_object_or_404
from blog.models import Post, Category, Comment
from django.utils import timezone
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib import messages
from blog.forms import CommentForm

# Create your views here.

def blog_view(request, **kwargs):
    posts=Post.objects.filter(published_date__lte=timezone.now(), status=True)

    if kwargs.get('cat_name'):
        posts = posts.filter(category__name=kwargs['cat_name'])

    if kwargs.get('author_username'):
        posts = posts.filter(author__username=kwargs['author_username'])

    if kwargs.get('tag_name'):
        posts = posts.filter(tag__name__in=[kwargs['tag_name']])
    posts = Paginator(posts, 3)

    try:
        page_number =request.GET.get('p')
        posts = posts.get_page(page_number)
    
    except PageNotAnInteger:
        posts = posts.get_page(1)
    
    except EmptyPage:
        posts = posts.get_page(1)


    context = {'posts':posts} 
    return render(request, 'blog/blog-home.html', context)


def blog_single_view(request, pid):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'your comment submited successfully')

        else:
            messages.add_message(request, messages.ERROR, 'your comment didnt submited')
    
    posts=Post.objects.filter(published_date__lte=timezone.now(), status=True)
    post = get_object_or_404(Post, pk=pid, status=1, published_date__lte=timezone.now())
    comments = Comment.objects.filter(post=post.id, approved=True)

    post.counted_views += 1
    post.save()

    context = {
        'post': post,
        'next': posts.filter(id__gt=post.id).order_by('id').first(), 
        'previous': posts.filter(id__lt=post.id).order_by('-id').first(),
        'comments': comments
        }

    return render(request, 'blog/blog-single.html', context) 


def blog_search_view(request):
    posts=Post.objects.filter(published_date__lte=timezone.now(), status=True)
    if request.method == 'GET':
        if s := request.GET.get('s'):
            posts = posts.filter(content__contains=s)
    context = {'posts':posts} 
    return render(request, 'blog/blog-home.html', context)