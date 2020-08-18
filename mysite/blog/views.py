from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .models import Post, Comment
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PostForm, CommentForm
from django.views.generic import (
    TemplateView, ListView, CreateView, DetailView, UpdateView, DeleteView)
from django.utils import timezone
from django.contrib import auth

# Create your views here.


class AboutView(TemplateView):
    template_name = "about.html"


class PostList(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'post_list.html'

    def get_queryset(self):
        return Post.objects.filter(publish_date__lte=timezone.now()).order_by('-publish_date')


class PostDetail(DetailView):
    model = Post
    template_name = 'post_detail.html'


class PostCreateView(LoginRequiredMixin, CreateView):
    login_url = '/login'
    redirect_field_name = 'blog:post_list'
    form_class = PostForm
    model = Post
    # template_name = "post_form.html"


class PostUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login'
    redirect_field_name = 'blog/post_edit.html'
    form_class = PostForm
    model = Post
    # template_name = ".html"


class PostDeleteView(LoginRequiredMixin, DeleteView):
    login_url = '/login'
    redirect_field_name = 'blog/post_remove.html'
    model = Post
    success_url = reverse_lazy('blog:post_list')
    # template_name = ".html"


class DraftPostList(LoginRequiredMixin, ListView):
    # login_url = '/login'
    # redirect_field_name = 'blog/post_list.html'
    # model = Post
    # context_object_name = 'drafts'
    # template_name=''
    model = Post
    context_object_name = 'posts'
    template_name = 'post_drafts_list.html'

    def get_queryset(self):
        return Post.objects.filter(publish_date__lte=timezone.now()).order_by('-publish_date')


    def get_queryset(self):
        return Post.objects.filter(publish_date__isnull=True).order_by('-create_date')
################################### For Posts ###########################################


@login_required
def publish_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('blog:post_detail', pk=pk)

#################################### For Comments ########################################


def add_comment_to_a_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = CommentForm(request.POST or None)

    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
        return redirect('blog:post_detail', pk=post.pk)

    return render(request, 'blog/comment_form.html', {'form': form})


@login_required
def approve_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('blog:post_detail', pk=comment.post.pk)


@login_required
def remove_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('blog:post_detail', post_pk)

##################################### Login and Logout ###################################
