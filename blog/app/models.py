from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import pre_delete
from django.utils.text import slugify
import os
# Create your models here.

STATUS = ((0, "Draft"), (1, "Published"))

class Post(models.Model):
           title = models.CharField(max_length=100, unique=True)
           slug = models.SlugField(max_length=200, unique=True, blank=True) # Ajout de blank=True pour permettre à Django de le remplir automatiquement
           author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
           created_on = models.DateTimeField(auto_now_add=True)
           updated = models.DateTimeField(auto_now=True)
           content = models.TextField()
           status = models.IntegerField(choices=STATUS, default=0)
        #    image = models.ImageField(upload_to='post_images/', null=True, blank=True)
           
           class Meta:
                   ordering = ['-created_on']
           def __str__(self):
                    return self.title

           def save(self, *args, **kwargs):
                # Génère le slug automatiquement si le slug est vide
                if not self.slug:
                      self.slug = slugify(self.title)
                super().save(*args, **kwargs)

# Supprimer l'image principale si le post est supprimé
# @receiver(pre_delete, sender=Post)
# def delete_post_image(sender, instance, **kwargs):
#     if instance.image:
#         if os.path.isfile(instance.image.path):
#             os.remove(instance.image.path)
            
# Nouveau modèle : Images multiples
class PostImage(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='post_images/')

    def __str__(self):
          return f"Image for post: {self.post.title}"
    
# Supprimer les fichiers d'image multiples si un PostImage est supprimé
@receiver(pre_delete, sender=PostImage)
def delete_post_extra_image(sender, instance, **kwargs):
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)
