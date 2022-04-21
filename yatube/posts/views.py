import os

from django.core.paginator import Paginator

from django.shortcuts import get_object_or_404, render

from .models import Group, Post

PATH_TO_INDEX = os.path.join('posts', 'index.html')
PATH_TO_GROUP_LIST = os.path.join('posts', 'group_list.html')
POST_LENGTH = 10


def index(request) -> None:
    """Return main page."""
    template = PATH_TO_INDEX
    # title = 'Main page for project Yatube'
    post_list = Post.objects.all().order_by('-pub_date')
    paginator = Paginator(post_list, 10)

    # Из URL извлекаем номер запрошенной страницы - это значение параметра page
    page_number = request.GET.get('page')

    # Получаем набор записей для страницы с запрошенным номером
    page_obj = paginator.get_page(page_number)
    # Отдаем в словаре контекста
    context = {
        'page_obj': page_obj,
    }
    return render(request, template, context)


def group_posts(request, slug) -> None:
    """View-function for group page."""
    template = PATH_TO_GROUP_LIST
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()[:POST_LENGTH]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, template, context)
