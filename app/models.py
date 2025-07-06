from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver
import os
from django.utils.text import slugify
# from django.contrib.auth.models import User
# from ckeditor.fields import RichTextField
# from django.utils.translation import gettext_lazy as _

STATUS = ((0, "Draft" ) , (1, "Published"))

# section post
class Post(models.Model):
    title = models.CharField( max_length=200 , unique= True)
    slug = models.SlugField( max_length=200 , unique= True, blank=True)
    author = models.ForeignKey(User , on_delete= models.CASCADE, related_name = 'blog_posts', ) #permet de savoir qui a créé le post
    created_on = models.DateTimeField( auto_now_add= True)
    updated_on = models.DateTimeField( auto_now= True)
    content = models.TextField()
    status = models.IntegerField( choices= STATUS , default=0)
    image = models.ImageField( upload_to='post_images/', null=True, blank=True)  # Nouveau champ pour l'image

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug': self.slug})
    
    def save(self, *args, **kwargs):
        if not self.slug or Post.objects.filter(slug=self.slug).exclude(pk=self.pk).exists():
            base_slug = slugify(self.titre)
            slug = base_slug
            counter = 1
            while Post.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f'{base_slug}-{counter}'
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)
        

@receiver(pre_delete, sender=Post)
def delete_post_image(sender, instance, **kwargs):
    # Supprime le fichier image associé lors de la suppression de l'article
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)

# section culture et  tradiction
class Category(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='culture/categories/', blank=True, null=True)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = "Catégorie culturelle"
        verbose_name_plural = "Catégories culturelles"

    def __str__(self):
        return self.title

class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories')
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='culture/subcategories/', blank=True, null=True)
    slug = models.SlugField(unique=True)
    is_featured = models.BooleanField(default=False)
    quartier = models.CharField(max_length=100, blank=True, null=True)
    adresse = models.TextField(blank=True, null=True)
    activite = models.CharField(max_length=250, blank=True, null=True)
    horaire = models.CharField(max_length=100, blank=True, null=True)
    services = models.TextField(blank=True, null= True, help_text="Services et équipements disponibles")
    parking = models.BooleanField(default=False)
    accessibility = models.CharField(max_length=255, blank=True, null=True, help_text="Infos transport et accessibilité")
    conseil = models.CharField(max_length=255, blank=True, null=True)
    telephone = models.CharField(max_length=50, blank=True, null=True)
    site_web = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    tarif = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = "Culture Sub_Catégorie"
        verbose_name_plural = "Cultures Sub_Catégories"

    def __str__(self):
        return f"{self.category.title} - {self.title}"

class GalleryImage(models.Model):
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='culture/gallery/', blank=True, null=True)
    caption = models.CharField(max_length=255, blank=True)

    class Meta:
        verbose_name = "Image de galerie culture"
        verbose_name_plural = "Images de galerie cultures"
    def __str__(self):
        return f"Image for {self.subcategory.title}"

# section autour de babi
class Lieu(models.Model):
    NIVEAU_DIFFCULTE = (
        ("facile", "Facile"),
        ("moyen", "Moyen"),
        ("difficile", "Difficile")
    )
    nom = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='lieux/', blank=True, null=True)
    quartier = models.CharField(max_length=255,blank=True, null=True)  # Ex : "Grand-Bassam", "Azaguié"
    adresse = models.TextField(blank=True, null=True)
    distance_km = models.FloatField(blank=True, null=True)  # distance depuis Abidjan
    duree = models.FloatField(blank=True, null=True)  # durée approximative en heures
    horaire = models.CharField(max_length=100, blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    weekend_spot = models.BooleanField(default=False, verbose_name="Idée de sortie du week-end")
    niveau_difficulte = models.CharField(max_length=50, choices= NIVEAU_DIFFCULTE, blank=True, null=True)
    saison_ideale = models.CharField(max_length=100, blank=True, null=True)
    equipement_conseille = models.TextField(blank=True, null=True)
    # acces = models.TextField(blank=True, null=True)  # infos de transport, routes, etc
    region = models.CharField(max_length=100, blank=True, null=True)
    date_evenement = models.DateTimeField(auto_now_add=True)
    horaire = models.CharField(max_length=255, blank=True, null=True)
    age_minimum = models.PositiveIntegerField(blank=True, null=True)    
    activite = models.CharField(max_length=250, blank=True, null=True)
    services = models.TextField(blank=True, null= True, help_text="Services et équipements disponibles")
    parking = models.BooleanField(default=False)
    accessibility = models.CharField(max_length=255, blank=True, null=True, help_text="Infos transport et accessibilité")
    conseil = models.CharField(max_length=255, blank=True, null=True)
    telephone = models.CharField(max_length=50, blank=True, null=True)
    site_web = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    tarif = models.CharField(max_length=100, blank=True, null=True)
    
    type = models.CharField(max_length=100, choices=[
        ("nature", "Nature"),
        ("culture", "Culture"),
        ("plage", "Plage"),
        ("gastronomie", "Gastronomie"),
        ("village", "Village"),
        ("randonnee", "Randonnee"),
        ("animaux", "Animaux"),
        ("village", "Village"),
        ("parc", "Parc"),
        ("sport", "Activité sportive"),
        ("centre_loisir", "Centre de loisirs"),
        ("jeux", "Jeux pour enfants"),
    ])

    class Meta:
        verbose_name = "Autour de Babi"
        verbose_name_plural = "Autour de Babis"
    def __str__(self):
        return self.nom
# Tags multiples
    tags = models.ManyToManyField('Tag', blank=True)
class Tag(models.Model):
    nom = models.CharField(max_length=50)
    def __str__(self):
        return self.nom
    
# section loisir
class ActiviteLoisir(models.Model):
    CATEGORIES = [
        ("parc", "Parc"),
        ("sport", "Activité sportive"),
        ("centre_loisir", "Centre de loisirs"),
        ("jeux", "Jeux pour enfants"),
        ("cinema", "Cinema"),
        ("autre", "Autre"),
    ]

    nom = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to='loisirs/', blank=True, null=True)

    categorie = models.CharField(max_length=50, choices=CATEGORIES)
    localisation = models.CharField(max_length=255, blank=True, null=True) 
    activite_proposee = models.CharField(max_length=255, blank=True, null=True)

    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)

    horaire = models.CharField(max_length=255, blank=True, null=True)
    tarif = models.CharField(max_length=100, blank=True, null=True)
    age_minimum = models.PositiveIntegerField(blank=True, null=True)
    accessibilite = models.TextField(blank=True, null=True)

    site_web = models.URLField(blank=True, null=True)
    telephone = models.CharField(max_length=50, blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)

    date_ajout = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Activité de loisir"
        verbose_name_plural = "Activités de loisir"

    def __str__(self):
        return self.nom

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nom)
        super().save(*args, **kwargs)


# Section shopping
class LieuShopping(models.Model):
    TYPES = [
        ("marche", "Marché local"),
        ("boutique", "Boutique artisanale"),
        ("mall", "Centre commercial"),
        ("concept_store", "Concept Store"),
        ("autre", "Autre"),
    ]

    nom = models.CharField("Titre", max_length=255)
    slug = models.SlugField("Slug", unique=True, blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to='shopping/', blank=True, null=True)
    type = models.CharField(max_length=50, choices=TYPES)
    adresse = models.CharField(max_length=255)
    region = models.CharField(max_length=100, blank=True, null=True)
    heure_ouverture = models.CharField(max_length=100, blank=True, null=True)
    services = models.TextField(blank=True, null= True, help_text="Services et équipements disponibles")
    parking = models.BooleanField(default=False)
    accessibility = models.CharField(max_length=255, blank=True, null=True, help_text="Infos transport et accessibilité")
    conseil = models.CharField(max_length=255, blank=True, null=True)
    telephone = models.CharField(max_length=50, blank=True, null=True)
    site_web = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    date_ajout = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Lieu de shopping"
        verbose_name_plural = "Lieux de shopping"

    def __str__(self):
        return self.nom

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nom)
        super().save(*args, **kwargs)

# section sortie
class Sortie(models.Model):
    TYPES_SORTIE = [
        ("bar", "Bar"),
        ("club", "Club"),
        ("concert", "Concert"),
        ("spectacle", "Spectacle"),
        ("evenement", "Événement"),
    ]

    nom = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='sorties/', blank=True, null=True)
    type = models.CharField(max_length=50, choices=TYPES_SORTIE)
    adresse = models.CharField(max_length=255)
    region = models.CharField(max_length=100, blank=True, null=True)
    acces = models.CharField(max_length=255, blank=True, null=True)  # bus, taxi, voiture, etc.

    date_debut = models.DateTimeField(blank=True, null=True)
    date_fin = models.DateTimeField(blank=True, null=True)
    horaire = models.CharField(max_length=100, blank=True, null=True)
    age_minimum = models.PositiveIntegerField(blank=True, null=True)
    tarif = models.CharField(max_length=100, blank=True, null=True)
    dress_code = models.CharField(max_length=100, blank=True, null=True)

    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)

    tendance = models.BooleanField(default=False)
    date_ajout = models.DateTimeField(auto_now_add=True)
    site_web = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    programme = models.TextField(blank=True, null=True)
    tarif_moyen = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = "Sortie"
        verbose_name_plural = "Sorties"

    def __str__(self):
        return self.nom

# section contact
class MessageContact(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField(null=True, blank=True)
    sujet = models.CharField(max_length=200)
    message = models.TextField()
    date_envoi = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nom} - {self.sujet}"
    
# section A propos
class APropos(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='a_propos/', blank=True, null=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

# section hebergement
class Hebergement(models.Model):
    CATEGORIES = [
        ('luxe', 'Hôtel de luxe'),
        ('moyen', 'Hôtel milieu de game'),
        ('location', 'Location de vacances'),
        ('atypique', 'Hébergement atypique'),
    ]
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    content = models.TextField()
    categorie = models.CharField(max_length=20, choices=CATEGORIES)
    quartier = models.CharField(max_length=100)
    adresse = models.TextField()
    heure_ouverture = models.CharField(max_length=100, blank=True, null=True)
    services = models.TextField(blank=True, null= True, help_text="Services et équipements disponibles")
    parking = models.BooleanField(default=False)
    accessibility = models.CharField(max_length=255, blank=True, null=True, help_text="Infos transport et accessibilité")
    conseil = models.CharField(max_length=255, blank=True, null=True)
    telephone = models.CharField(max_length=50, blank=True, null=True)
    site_web = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    tarif = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='hebergements/', blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title

# section où manger
class Restaurant(models.Model):
    CATEGORIES = [
        ('resto', 'Restaurant'),
        ('rapide', 'Restauration rapide'),
        ('local', 'Cuisine locale'),
        ('maquis', 'Maquis'),
        ('rooftop', 'Rooftop'),
        ('cafes', 'Café & Boulangeries'),
    ]
    PRIX_CHOICES = [
        ('bas', 'Moins de 3 000 FCFA'),
        ('moyen', 'Entre 3 000 et 7 000 FCFA'),
        ('haut', 'Plus de 7 000 FCFA'),
    ]

    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    content = models.TextField()
    categorie = models.CharField(max_length=20, choices=CATEGORIES)
    quartier = models.CharField(max_length=100)
    adresse = models.TextField()
    specialite = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    horaires = models.CharField(max_length=100, blank=True, null=True)
    prix_moyen = models.CharField(max_length=50,choices=PRIX_CHOICES, blank=True, null=True)
    image = models.ImageField(upload_to='restaurants/', blank=True, null=True)
    site_web = models.URLField(blank=True, null=True)
    est_recommande = models.BooleanField(default=False)
    date_ajout = models.DateTimeField(auto_now_add=True)
    popularite = models.PositiveIntegerField(default=0)  # compteur de clics ou visites
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    conseil = models.CharField(max_length=255, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.slug)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Restaurant/où manger"
        verbose_name_plural = "Restaurants/où manger"

    def __str__(self):
        return self.title
    
############
# Infos pratique
class InfoPratique(models.Model):
    icon = models.CharField(max_length=10, help_text= "Ex: 📍, 🛂, 💱")
    title = models.CharField(max_length=100)
    content = models.TextField(help_text= "Utilise des listes en HTML, ex: <ul><li>...</li></ul>")

    def __str__(self):
        return self.title

# section transport
class MoyenTransport(models.Model):
    TYPES = [
        ('bus', 'Bus / Car'),
        ('bateau', 'Bateau'),
        ('avion', 'Avion'),
        ('taxi', 'Taxi / VTC'),
        ('location', 'Location de voiture'),
    ]

    nom = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    type = models.CharField(max_length=50, choices=TYPES)
    description = models.TextField()
    image = models.ImageField(upload_to='transports/', blank=True, null=True)
    region = models.CharField(max_length=100, blank=True, null=True)
    horaires = models.CharField(max_length=255, blank=True, null=True)
    tarifs = models.CharField(max_length=255, blank=True, null=True)
    site_web = models.URLField(blank=True, null=True)
    telephone = models.CharField(max_length=100, blank=True, null=True)
    conseil = models.CharField(max_length=255, blank=True, null=True)
    zone_desservi = models.CharField(max_length=255, blank=True, null=True)
    services = models.TextField(blank=True, null= True, help_text="Services et équipements disponibles")
    # parking = models.BooleanField(default=False)
    # telephone = models.CharField(max_length=50, blank=True, null=True)
    site_web = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    # date_ajout = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Moyen de transport"
        verbose_name_plural = "Transports"

    def __str__(self):
        return self.nom
