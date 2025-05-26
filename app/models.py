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
    # Supprimer le fichier image associé lors de la suppression de l'article
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)

# section agenda
class Agenda(models.Model):
    titre = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    date_debut = models.DateField()
    date_fin = models.DateField(null=True, blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to='agenda_images/')
    lieu = models.CharField(max_length=255, blank=True)

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
        return self.titre



class Destinations(models.Model):
    ville = models.CharField(max_length=100)
    slug = models.SlugField(max_length=120, unique=True, blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to='destinations/', blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    date_publiée = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['ville']
        verbose_name = "ville en CI"
        verbose_name_plural = "Destinations en CI"
    
    def __str__(self):
        return self.ville

    def get_absolute_url(self):
        return reverse('destination_detail', args=[self.slug])
    
    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.ville)
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
    titre = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True) # editable=True; genere le slug automatiquement
    contenu = models.TextField()
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
        return self.titre
    
class CultureImage(models.Model):
    culture = models.ForeignKey(Culture, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='culture_images/')
    description = models.TextField(blank=True, null=True)

# section conseilVoyage
class ConseilVoyage(models.Model):
    titre = models.CharField(max_length=200)
    contenu = models.TextField()
    date_publication = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_publication']
        verbose_name = "Conseil de voyage"
        verbose_name_plural = "Conseils de voyage"

    def __str__(self):
        return self.titre

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
    titre = models.CharField(max_length=200)
    contenu = models.TextField()
    image = models.ImageField(upload_to='a_propos/', blank=True, null=True)
    date_modifiee = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titre
    