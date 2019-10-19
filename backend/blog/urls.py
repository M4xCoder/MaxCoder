"""settings_maxjournal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import blog_post_list, blog_post_detail, PostListView


app_name = 'blog'

urlpatterns = [
    #path('', blog_post_list, name='blog_posts_list_url'),
    path('', PostListView.as_view(), name='blog_posts_list_url'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',
         blog_post_detail,
         name='blog_post_detail_url'),
]
