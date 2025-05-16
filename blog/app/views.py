from typing import Any
from django.shortcuts import render, redirect
from .models import *
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import UpdateView, DeleteView, ListView
from django.contrib.auth.models import User
from django.contrib.auth import login
from .forms import *
# from django.utils.translation import gettext_lazy as _


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

# section Destinations
class DestinationListView(ListView):
    model = Destinations
    template_name = 'destination_list.html'
    context_object_name = "destinations"

class DestinationDetailView(DetailView):
    model = Destinations
    template_name = 'destination_detail.html'
    context_object_name = 'destination'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['gallery'] = self.object.images.all()
        return context

# section Culture et traditions
def culture_view(request):
    # culture = Culture.objects.first() # on suppose qu'une seule entrée
    cultures = Culture.objects.all()
    return render(request, 'culture.html', {'cultures':cultures})

# section conseilVoyage
def conseils_view(request):
    conseils = ConseilVoyage.objects.all()
    return render(request, 'conseils.html', {'conseils':conseils})

# section contact
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'contact_success.html', {'form':form}) # page de remerciement
    else:
        form = ContactForm()
        return render(request, 'contact.html', {'form':form})
    
# section A Propos
def a_propos_page(request):
    # contenu = APropos.objects.last() # récupère le dernier contenu "À propos"
    return render(request, 'a_propos.html')