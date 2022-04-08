# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Post, Group
import os

PATH_TO_INDEX = os.path.join('posts', 'index.html')
PATH_TO_GROUP_LIST = os.path.join('posts', 'group_list.html')


def index(request) -> None:
    """Return main page."""
    template = PATH_TO_INDEX
    title_dict = 'Main page for project Yatube'
    posts = Post.objects.order_by('-pub_date')[:10]
    context = {
        'title_dict': title_dict,
        'posts': posts
    }
    return render(request, template, context)


def group_posts(request, slug) -> None:
    """View-function for group page."""
    template = PATH_TO_GROUP_LIST
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, template, context)
