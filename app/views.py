from typing import Any
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import UpdateView, DeleteView, ListView

from .forms import *

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    context_object_name = 'post_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['events'] = Agenda.objects.order_by('date_debut')[:6]
        context['gastronomie_list'] = Gastronomie.objects.order_by('date')[:6]
        context['ville_list'] = VillePatrimoine.objects.order_by('-date')[:6]
        return context

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
class CultureListView(ListView):
    model = Culture
    template_name = 'culture_list.html'
    context_object_name = 'cultures'

class CultureDetailView(DetailView):
    model = Culture
    template_name = 'culture_detail.html'
    context_object_name = 'culture'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['gallery'] = self.object.images.all()
        return context

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

# section agenda
def agenda_list(request):
    evenements = Agenda.objects.order_by('date_debut')
    return render(request, 'agenda_list.html', {'evenements': evenements})

def agenda_detail(request, slug):
    event = get_object_or_404(Agenda, slug=slug)
    return render(request, 'agenda_detail.html', {'event': event})

# section gastronomie
def gastronomie_list(request):
    plat = Gastronomie.objects.all()
    return render(request, 'gastronomie_list.html', {'plat':plat})

def gastronomie_detail(request, slug):
    plat = get_object_or_404(Gastronomie, slug=slug)
    return render(request, 'gastronomie_detail.html', {'plat':plat})

# section ville
def ville_list(request):
    villes = VillePatrimoine.objects.all()
    return render(request, 'ville_list.html', {'villes':villes})

def ville_detail(request, slug):
    ville = get_object_or_404(VillePatrimoine, slug=slug)
    return render(request, 'ville_detail.html', {'ville':ville})