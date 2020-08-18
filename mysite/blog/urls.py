from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.PostList.as_view(), name='post_list'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('post/<int:pk>', views.PostDetail.as_view(), name='post_detail'),
    path('post/new/', views.PostCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/edit/',
         views.PostUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/remove/', views.PostDeleteView.
         as_view(), name='post_remove'),
    path('post/drafts/', views.DraftPostList.as_view(), name='post_draft_list'),
    path('post/<int:pk>/add_comment/',
         views.add_comment_to_a_post, name='add_comment'),
    path('comments/<int:pk>/approve_comment/',
         views.approve_comment, name='approve_comment'),
    path('comments/<int:pk>/remove_commnts/',
         views.remove_comment, name='remove_comment'),
    path('post/<int:pk>/publish', views.publish_post, name='publish_post'),
]
