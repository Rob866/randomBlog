from django import template
from django.db.models import Count
from ..models import Post


register = template.Library()

@register.simple_tag
def total_posts():
    return Post.published.count()

@register.simple_tag
def get_most_commented_posts(count=3):
    return Post.published.annotate(total_comments=Count('comments')).order_by('-total_comments')[:count]



@register.inclusion_tag('blog/post/lastest_post.html')
def show_lastest_posts(count=3):
    lastest_posts= Post.published.order_by('-publish')[:count]
    return {'lastest_posts': lastest_posts }