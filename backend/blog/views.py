from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage,\
                                  PageNotAnInteger
from .models import Post
from django.views.generic import View
 
class PostListView(View):
    
    def get(self, request):
        object_list = Post.published.all()
        paginator = Paginator(object_list, 2) # по 2 поста на каждой странице
        page = request.GET.get('page')
        pagename = 'Блог'
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            # Если страница не является целым числом, отправляем первую страницу
            posts = paginator.page(1)
        except EmptyPage:
            # Если страница вне диапазона отправляем последнюю страницу результатов
            posts = paginator.page(paginator.num_pages)
        return render(request,
                      'blog/blog_post_list.html',
                      {'page': page,
                       'pagename': pagename,
                       'posts': posts})


def blog_post_list(request):
    object_list = Post.published.all()
    paginator = Paginator(object_list, 4) # по 3 поста на каждой странице
    page = request.GET.get('page')
    pagename = 'Блог'
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # Если страница не является целым числом, отправляем первую страницу
        posts = paginator.page(1)
    except EmptyPage:
        # Если страница вне диапазона отправляем последнюю страницу результатов
        posts = paginator.page(paginator.num_pages)
    return render(request,
                  'blog/blog_post_list.html',
                  {'page': page,
                   'pagename': pagename,
                   'posts': posts})

def blog_post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                                   status='published',
                                   publish__year=year,
                                   publish__month=month,
                                   publish__day=day)
    pagename = 'Блог'
    return render(request,
                  'blog/blog_post_detail.html',
                  {'pagename': pagename, 'post': post})
