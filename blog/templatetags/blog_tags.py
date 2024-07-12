from django import template
from blog.models import Post, Category
from django.utils import timezone

register = template.Library()


@register.inclusion_tag('blog/blog_popular.html')
def latestposts(arg=4):
    posts=Post.objects.filter(published_date__lte=timezone.now(), status=True).order_by('published_date')[:arg]
    return {"posts":posts}

@register.inclusion_tag('blog/blog_Catgories.html')
def postcatgories():
    posts=Post.objects.filter(published_date__lte=timezone.now(), status=True)
    catgories=Category.objects.all()
    cat_dict = dict()
    for name in catgories:
        cat_dict[name.name] = posts.filter(category=name).count()
    return {'catgories':cat_dict}