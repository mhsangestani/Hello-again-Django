from django import template
from blog.models import Post, Category
from django.utils import timezone


register = template.Library()

@register.inclusion_tag('website/websit_latestblog.html')
def latest_blog(arg=6):
    posts=Post.objects.filter(published_date__lte=timezone.now(), status=True).order_by('-published_date')[:arg]
    return {"posts":posts}