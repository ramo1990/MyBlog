from typing import Any
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import UpdateView, DeleteView, ListView
from collections import defaultdict
from django.db.models import Q

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

class PostAllList(generic.ListView):
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'posts'
    paginate_by = 9  # facultatif : pagination

    def get_queryset(self):
        return Post.objects.filter(status=1).order_by('-created_on')

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
    contenu = APropos.objects.all().order_by('-updated_on') # récupère le dernier contenu "À propos"
    return render(request, 'a_propos.html', {'contenu': contenu})

# def ajouter_apropos(request):
#     if request.method == 'POST':
#         form = AProposForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('a_propos')
#     else:
#         form = AProposForm()
#     return render(request, 'ajouter_apropos.html', {'form':form})

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

# section Hebergement
def hebergements_list(request):
    hebergements = Hebergement.objects.all().order_by('categorie', 'quartier')
    
    categories = defaultdict(list)
    for h in hebergements:
        categories[h.get_categorie_display()].append(h)
    
    # print("Nombre d'hébergements :", hebergements.count())
    # for h in hebergements:
    #     print(" -", h.title, "| Catégorie:", h.get_categorie_display())

    return render(request, 'hebergements_list.html', {
        'categories':dict(categories)
        })

def hebergement_detail(request, slug):
    hebergement = get_object_or_404(Hebergement, slug = slug)
    return render(request, 'hebergement_detail.html', {'hebergement': hebergement})

# section où manger
def restaurants_list(request):
    restaurants = Restaurant.objects.all().order_by('categorie', 'quartier')

    categories = defaultdict(list)
    for r in restaurants:
        categories[r.get_categorie_display()].append(r)
    
    return render(request, 'restaurants_list.html', {'categories': dict(categories)})

def restaurants_detail(request, slug):
    restaurant = get_object_or_404(Restaurant, slug = slug)
    return render(request, 'restaurant_detail.html', {'restaurant': restaurant})

# section info pratique
def infos_pratiques(request):
    blocs = InfoPratique.objects.all()
    return render(request, 'infos_pratiques.html', {'blocs':blocs})

# section Que faire ?
def que_faire(request):
    categories = CategorieActivite.objects.prefetch_related('activites').all()
    return render(request, 'que_faire.html', {'categories':categories})

def detail_activite(request, slug):
    activite = get_object_or_404(Activite, slug=slug)
    return render(request, 'detail_activite.html', {'activite':activite})

# search
def search(request):
    query = request.GET.get('q', '').strip()
    results = []
    # destinations = []
    # restaurants = []
    # ville_patrimoine = []
    # post = []
    # agenda = []
    # culture = []
    # conseil_voyage = []
    # gastronomie = []
    # hebergement = []
    # Info_pratique = []
    # que_faire = []

    if query:
        destinations = Destinations.objects.filter(Q(title__icontains=query) | Q(content__icontains=query))
        restaurants = Restaurant.objects.filter(Q(title__icontains=query) | Q(categorie__icontains=query))
        ville_patrimoine = VillePatrimoine.objects.filter(Q(title__icontains=query) | Q(content__icontains=query))
        post = Post.objects.filter(Q(title__icontains=query) | Q(content__icontains=query))
        agenda = Agenda.objects.filter(Q(title__icontains=query) | Q(content__icontains=query))
        culture = Culture.objects.filter(Q(title__icontains=query) | Q(content__icontains=query))
        conseil_voyage = ConseilVoyage.objects.filter(Q(title__icontains=query) | Q(content__icontains=query))
        gastronomie = Gastronomie.objects.filter(Q(title__icontains=query) | Q(content__icontains=query))
        hebergement = Hebergement.objects.filter(Q(title__icontains=query) | Q(content__icontains=query))
        que_faire = Activite.objects.filter(Q(title__icontains=query) | Q(content__icontains=query))

        results = {
            'destinations':destinations,
            'restaurants':restaurants,
            'ville_patrimoine':ville_patrimoine,
            'post':post,
            'agenda':agenda,
            'culture':culture,
            'conseil_voyage':conseil_voyage,
            'gastronomie':gastronomie,
            'hebergement':hebergement,
            # 'Info_pratique':Info_pratique,
            'que_faire':que_faire,
        }
    return render(request, 'search_results.html', {
        'query':query,
        'results':results
        # 'destinations':destinations,
        # 'restaurants':restaurants,
        # 'ville_patrimoine':ville_patrimoine,
        # 'post':post,
        # 'agenda':agenda,
        # 'culture':culture,
        # 'conseil_voyage':conseil_voyage,
        # 'gastronomie':gastronomie,
        # 'hebergement':hebergement,
        # 'Info_pratique':Info_pratique,
        # 'que_faire':que_faire,
    })

# Carousel Slide
# def home(request):
#     slides = CarouselSlide.objects.filter(active=True).order_by('order')
#     return render(request, 'index.html', {'slides':slides})