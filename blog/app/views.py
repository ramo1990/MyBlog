from django.shortcuts import render
from .models import Post
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import UpdateView, DeleteView


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

class DetailView(generic.DetailView):
    model = Post
    template_name = 'post_details.html'

# permettre a certains users de modifier ou supprimer leur post
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields =  ['title', 'content', 'image']
    template_name = 'post_edit.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author or self.request.user.is_superuser
    
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'
    template_name = 'post_confirm_delete.html'

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author or self.request.user.is_superuser