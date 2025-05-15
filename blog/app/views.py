from django.shortcuts import render, redirect
from .models import *
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import UpdateView, DeleteView, ListView
from django.contrib.auth.models import User
from django.contrib.auth import login
from .forms import *


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
    
# Creer un user via formulaire
def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)  # Connecte l'utilisateur après l'inscription
            return redirect('home')  # Redirection après l'inscription
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

class DestinationListView(ListView):
    model = Destinatoins
    template_name = 'destination_list.html'
    context_object_name = "destinations"