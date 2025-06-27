from typing import Any
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import UpdateView, DeleteView, ListView
from collections import defaultdict
from django.db.models import Q
# from .models import Category, SubCategory
from django.core.mail import send_mail
from .forms import *
# from django.contrib.auth.decorators import login_required
# from .models import FeaturedEvent

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    context_object_name = 'post_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['events'] = Agenda.objects.order_by('date_debut')[:6]
        # context['gastronomie_list'] = Gastronomie.objects.order_by('date')[:6]
        # context['ville_list'] = VillePatrimoine.objects.order_by('-date')[:6]
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

# section Culture et traditions
def culture_home(request):
    categories = Category.objects.all()
    featured = SubCategory.objects.filter(is_featured=True).first()  # On prend la première
    return render(request, 'culture_home.html', {
        'categories': categories,
        'featured': featured,
        })

def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    subcategories = category.subcategories.all()
    return render(request, 'culture_category_detail.html', {
        'category': category,
        'subcategories': subcategories,
    })

def subcategory_detail(request, category_slug, sub_slug):
    subcategory = get_object_or_404(SubCategory, slug=sub_slug, category__slug=category_slug)
    images = subcategory.images.all()
    return render(request, 'culture_subcategory_detail.html', {
        'subcategory': subcategory,
        'images': images,
    })

# section autour de babi
def autour_babi(request):
    lieux = Lieu.objects.filter(distance_km__lte=250).order_by('duree')
    weekend_idees = Lieu.objects.filter(weekend_spot=True)[:3]  # jusqu'à 3 suggestions
    # lieux = Lieu.objects.all()
    return render(request, 'autour_babi.html', {
        'lieux': lieux,
        'weekend_idees': weekend_idees,
    })

def lieu_autour_babi_detail(request, slug):
    lieu = get_object_or_404(Lieu, slug=slug)
    return render(request, 'autour_babi_detail.html', {
        'lieu': lieu,
    })

# section Nature
def nature(request):
    categories = {
        "plage": Lieu.objects.filter(type="plage"),
        "nature": Lieu.objects.filter(type="nature"),
        "randonnée": Lieu.objects.filter(type="randonnee"),  # ajoute ce type
        "animaux": Lieu.objects.filter(type="animaux"),       # ou "faune"
    }
    return render(request, 'nature.html', {'categories': categories})

def nature_detail(request, slug):
    lieu = get_object_or_404(Lieu, slug=slug)
    return render(request, 'nature_detail.html', {
        'lieu': lieu,
    })
# filtre de nature
def nature_filtre(request):
    lieux = Lieu.objects.all()

    # Filtres GET
    type_lieu = request.GET.get('type')
    difficulte = request.GET.get('difficulte')
    duree_max = request.GET.get('duree')
    acces = request.GET.get('acces')
    region = request.GET.get('region')
    tags = request.GET.getlist('tags')  # liste multiple
    recherche = request.GET.get('q')

    # Filtres dynamiques
    if type_lieu:
        lieux = lieux.filter(type=type_lieu)
    if difficulte:
        lieux = lieux.filter(niveau_difficulte=difficulte)
    if duree_max:
        lieux = lieux.filter(duree__lte=float(duree_max))
    if acces:
        lieux = lieux.filter(acces__icontains=acces)
    if region:
        lieux = lieux.filter(region__icontains=region)
    if tags:
        for tag in tags:
            lieux = lieux.filter(tags__nom__iexact=tag)
    if recherche:
        lieux = lieux.filter(Q(nom__icontains=recherche) | Q(description__icontains=recherche))

    # Liste de tous les tags pour le formulaire
    all_tags = Tag.objects.all()

    return render(request, 'nature_filtre.html', {
        'lieux': lieux.distinct(),
        'tags': all_tags,
    })

# section sortir
def sortie(request):
    tendances = Sortie.objects.filter(tendance=True).order_by('-date_ajout')[:4]
    categories = {
        "Bars": Sortie.objects.filter(type="bar").order_by('-date_ajout'),
        "Clubs": Sortie.objects.filter(type="club").order_by('-date_ajout'),
        "Spectacles": Sortie.objects.filter(type="spectacle").order_by('-date_ajout'),
        "Concerts": Sortie.objects.filter(type="concert").order_by('-date_ajout'),
        "Événements": Sortie.objects.filter(type="evenement").order_by('-date_ajout'),
    }
    return render(request, 'sortir.html', {
        'tendances': tendances,
        'categories': categories
    })

def sortie_detail(request, slug):
    sortie = get_object_or_404(Sortie, slug=slug)
    return render(request, 'sortie_detail.html', {
        'sortie': sortie
    })

# section loisir
def activites_loisir(request):
    categories = {
        "Parcs": ActiviteLoisir.objects.filter(categorie="parc"),
        "Sport": ActiviteLoisir.objects.filter(categorie="sport"),
        "Jeux": ActiviteLoisir.objects.filter(categorie="jeux"),
        "Centres de loisirs": ActiviteLoisir.objects.filter(categorie="centre_loisir"),
    }
    return render(request, 'loisir.html', {'categories': categories})

def activites_loisir_detail(request, slug):
    activite = get_object_or_404(ActiviteLoisir, slug=slug)
    return render(request, 'loisir_detail.html', {'activite': activite})

# Section shopping
def shopping(request):
    lieux = LieuShopping.objects.all().order_by('-date_ajout')
    return render(request, 'shopping.html', {'lieux': lieux})

def shopping_detail(request, slug):
    lieu = get_object_or_404(LieuShopping, slug=slug)
    return render(request, 'shopping_detail.html', {'lieu': lieu})

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
    categories = dict(Restaurant.CATEGORIES)
    prix_choices = dict(Restaurant.PRIX_CHOICES)
    # plats = PlatTypique.objects.all()
    # Récupération des filtres
    selected_category = request.GET.get('categorie') or ''
    selected_prix = request.GET.get('prix') or ''
    sort_by = request.GET.get('tri') or ''
    # Base queryset
    restaurants = Restaurant.objects.all()
    # Filtrage par catégorie
    if selected_category:
        restaurants = restaurants.filter(categorie=selected_category)
    # Filtrage par prix
    if selected_prix:
        restaurants = restaurants.filter(prix_moyen=selected_prix)
    # Tri
    if sort_by == 'popularite':
        restaurants = restaurants.order_by('-popularite')
    elif sort_by == 'nouveaute':
        restaurants = restaurants.order_by('-date_ajout')
    # Meilleurs restos (recommandés)
    meilleurs_restos = restaurants.filter(est_recommande=True)

    return render(request, 'restaurants_list.html', {
        'restaurants': restaurants,
        'categories': categories,
        'selected_category': selected_category,
        # 'plats': plats,
        'meilleurs_restos':meilleurs_restos,
        'prix_choices': prix_choices,
        'selected_prix': selected_prix,
        'sort_by': sort_by,
    })

def restaurants_detail(request, slug):
    resto = get_object_or_404(Restaurant, slug = slug)
    plats = resto.plats.all()
    return render(request, 'restaurant_detail.html', {
        'resto': resto,
        'plats': plats,
        })

# section info pratique
def infos_pratiques(request):
    blocs = InfoPratique.objects.all()
    return render(request, 'infos_pratiques.html', {'blocs':blocs})

# search
def search(request):
    query = request.GET.get('q', '').strip()
    results = []

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
    })

# section transport
def transport(request):
    categories = {
        "Bus & Cars": MoyenTransport.objects.filter(type='bus'),
        "Bateaux": MoyenTransport.objects.filter(type='bateau'),
        "Avions": MoyenTransport.objects.filter(type='avion'),
        "Taxis & VTC": MoyenTransport.objects.filter(type='taxi'),
        "Location de voitures": MoyenTransport.objects.filter(type='location'),
    }
    return render(request, 'transport.html', {'categories': categories})

def transport_detail(request, slug):
    transport = get_object_or_404(MoyenTransport, slug=slug)
    return render(request, 'transport_detail.html', {'transport': transport})