from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from .models import Post, PostImage
from .forms import PostForm, PostImageFormSet
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.forms import modelformset_factory
# Create your views here.

class PostList(generic.ListView):
    queryset = Post.objects.filter(status = 1).order_by('-created_on')
    template_name = 'index.html'
    context_object_name = 'posts'

class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'post_details.html'
    context_object_name = 'post'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        print(f"Post Detail View appelé avec le slug: {obj.slug}")  # Debug
        return obj

def create_post(request):
    print('vue executee')
    if request.method == 'POST':
        post_form = PostForm(request.POST, request.FILES)

        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.author = request.user
            post.save()

            # Gérer l’upload multiple
            for img in request.FILES.getlist('images'):
                PostImage.objects.create(post=post, image=img)

            return redirect('post_detail', slug=post.slug)
    else:
        post_form = PostForm()
        # image_form = PostImageForm()

    return render(request, 'create_post.html', {'post_form':post_form})


@login_required
def update_post(request, slug):
    post = get_object_or_404(Post, slug=slug, author=request.user)
    formset_class = PostImageFormSet

    if request.method == 'POST':
        post_form = PostForm(request.POST, request.FILES, instance=post)
        formset = formset_class(request.POST, request.FILES, queryset=PostImage.objects.filter(post=post))

        if post_form.is_valid() and formset.is_valid():
            post_form.save()

            # Lier chaque instance d'image au post et gérer la suppression
            for form in formset:
                if form.cleaned_data.get('DELETE'):
                    if form.instance.pk:  # Vérifie que l'ID existe
                        form.instance.delete()
                        print(f"Image {form.instance.id} supprimée.")  # Debug pour vérifier la suppression
                else:
                    image = form.save(commit=False)
                    image.post = post
                    image.save()

            # Gérer les nouvelles images ajoutées via <input name="new_images" multiple>
            for img in request.FILES.getlist('new_images'):
                PostImage.objects.create(post=post, image=img)

            # Redirection après enregistrement
            print(f"Redirection vers 'post_detail' avec slug {post.slug}")  # Debug pour vérifier la redirection
            return redirect('post_detail', slug=post.slug)
        else:
            print("Formulaire invalide")  # Debug pour vérifier si les formulaires sont invalides
    else:
        post_form = PostForm(instance=post)
        formset = formset_class(queryset=PostImage.objects.filter(post=post))

    return render(request, 'update_post.html', {
        'post': post,
        'formset': formset,
        'post_form': post_form
    })



 