from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver
import os
from django.utils.text import slugify
# from ckeditor.fields import RichTextField

STATUS = ((0, "Draft" ) , (1, "Published"))

# section post
class Post(models.Model):
    title = models.CharField(max_length=200 , unique= True)
    slug = models.SlugField(max_length=200 , unique= True, blank=True)
    author = models.ForeignKey(User , on_delete= models.CASCADE, related_name = 'blog_posts') #permet de savoir qui a créé le post
    created_on = models.DateTimeField(auto_now_add= True)
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    status = models.IntegerField(choices= STATUS , default=0)
    image = models.ImageField(upload_to='post_images/', null=True, blank=True)  # Nouveau champ pour l'image

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

# section agenda
class Agenda(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    date_debut = models.DateField(null=True, blank=True)
    date_debut_texte = models.CharField(max_length=100, blank=True)
    date_fin = models.DateField(null=True, blank=True)
    content = models.TextField()
    image = models.ImageField(upload_to='agenda_images/', null=True, blank=True)
    place = models.CharField(max_length=255, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.titre)
            slug = base_slug
            count = 1
            while Agenda.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{count}"
                count += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

# section destinations
class Destinations(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=120, unique=True, blank=True)
    content = models.TextField()
    image = models.ImageField(upload_to='destinations/', blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['title']
        verbose_name = "ville d'abidjan"
        verbose_name_plural = "Destinations abidjan"
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('destination_detail', args=[self.slug])
    
    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            num = 1
            while Destinations.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{num}"
                num += 1
            self.slug = slug
        super().save(*args, **kwargs)

class ImageSupplementaire(models.Model):
    destination = models.ForeignKey(Destinations, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='destinations/gallery/')
    description = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"Image de {self.destination.ville}"

# section culture et  tradiction
class Culture(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True) # editable=True; genere le slug automatiquement
    content = models.TextField()
    image = models.ImageField(upload_to='cultures_images/', blank=True, null=True)
    video_url = models.URLField(blank=True, null=True, help_text="Coller ici l'URL Youtube")
    audio_file = models.FileField(upload_to='culture_audio/',blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug or Culture.objects.filter(slug=self.slug).exclude(pk=self.pk).exists():
            base_slug = slugify(self.titre)
            slug = base_slug
            counter = 1
            while Culture.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f'{base_slug}-{counter}'
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    
class CultureImage(models.Model):
    culture = models.ForeignKey(Culture, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='culture_images/')
    description = models.TextField(blank=True, null=True)

# section conseilVoyage
class ConseilVoyage(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200 , unique= True, blank=True)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date']
        verbose_name = "Conseil de voyage"
        verbose_name_plural = "Conseils de voyage"
    
    def save(self, *args, **kwargs):
        if not self.slug: # or ConseilVoyage.objects.filter(slug=self.slug).exclude(pk=self.pk).exists():
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1
            while ConseilVoyage.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f'{base_slug}-{counter}'
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

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

# section gastronomie
class Gastronomie(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)    
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='gastronomie_images/', blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

#section ville et patrimoine
class VillePatrimoine(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='villes_patrimoine/', blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

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
    prix_min = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='hebergements/', blank=True, null=True)
    site_web = models.URLField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title

# section où manger
class Restaurant(models.Model):
    CATEGORIES = [
        ('gastro', 'Gastronomie'),
        ('rapide', 'Restauration rapide'),
        ('local', 'Cuisine locale'),
        ('cafes', 'Café & Boulangeries'),
    ]

    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    content = models.TextField()
    categorie = models.CharField(max_length=20, choices=CATEGORIES)
    quartier = models.CharField(max_length=100)
    adresse = models.TextField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    image = models.ImageField(upload_to='restaurants/', blank=True, null=True)
    site_web = models.URLField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.slug)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

# Infos pratique
class InfoPratique(models.Model):
    icon = models.CharField(max_length=10, help_text= "Ex: 📍, 🛂, 💱")
    title = models.CharField(max_length=100)
    content = models.TextField(help_text= "Utilise des listes en HTML, ex: <ul><li>...</li></ul>")

    def __str__(self):
        return self.title

# Que faire ?
class CategorieActivite(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    icon = models.CharField(max_length=10, help_text="Emoji ou icône")

    def __str__(self):
        return self.name

class Activite(models.Model):
    categorie = models.ForeignKey(CategorieActivite, on_delete=models.CASCADE, related_name='activites')
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    content = models.TextField()
    image = models.ImageField(upload_to='activites/', blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title