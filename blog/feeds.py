from django.contrib.syndication.views import Feed
from django.urls import reverse
from blog.models import Post
from django.utils import timezone


class LatestEntriesFeed(Feed):
    title = "blog beat site news"
    link = "rss/feed"
    description = "best blog."

    def items(self):
        return Post.objects.filter(published_date__lte=timezone.now(), status=True)

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content[:20]
