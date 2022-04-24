import os

from django.core.paginator import Paginator

from django.shortcuts import get_object_or_404, render

from django.contrib.auth.decorators import login_required

from .models import Group, Post

from django.contrib.auth.models import User

PATH_TO_INDEX = os.path.join('posts', 'index.html')
PATH_TO_GROUP_LIST = os.path.join('posts', 'group_list.html')
PATH_TO_PROFILE = os.path.join('posts', 'profile.html')
PATH_TO_POST = os.path.join('posts', 'post_detail.html')
# POST_LENGTH = 10
POSTS_IN_PAGINATOR = 10


def index(request):
    """Return main page."""
    template = PATH_TO_INDEX
    # title = 'Main page for project Yatube'
    post_list = Post.objects.all().order_by('-pub_date')
    paginator = Paginator(post_list, POSTS_IN_PAGINATOR)

    # Из URL извлекаем номер запрошенной страницы - это значение параметра page
    page_number = request.GET.get('page')

    # Получаем набор записей для страницы с запрошенным номером
    page_obj = paginator.get_page(page_number)
    # Отдаем в словаре контекста
    context = {
        'page_obj': page_obj,
    }
    return render(request, template, context)


@login_required
def group_posts(request, slug):
    """View-function for group page."""
    template = PATH_TO_GROUP_LIST
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()
    paginator = Paginator(posts, POSTS_IN_PAGINATOR)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'group': group,
        'posts': posts,
        'page_obj': page_obj,
    }
    return render(request, template, context)


def profile(request, username):
    """Code to the model and the creation of the context dict for user."""
    template = PATH_TO_PROFILE
    author = get_object_or_404(User, username=username)
    posts = author.posts.all().order_by("-pub_date")
    paginator = Paginator(posts, POSTS_IN_PAGINATOR)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'author': author,
        'posts_count': author.posts.count(),
    }
    return render(request, template, context)


def post_detail(request, post_id):
    """Code to the model and the creation of the context dict for posts."""
    template = PATH_TO_POST
    post = get_object_or_404(Post, pk=post_id)
    author = post.author
    posts_count = author.posts.count()
    context = {
        'post': post,
        'posts_count': posts_count,
    }
    return render(request, template, context)


def post_create(request):
    pass


def post_edit(request):
    pass
