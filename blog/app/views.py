from django.shortcuts import render, redirect
from django.views import generic
from .models import Post, PostImage
from .forms import PostForm
# Create your views here.

class PostList(generic.ListView):
    queryset = Post.objects.filter(status = 1).order_by('-created_on')
    template_name = 'index.html'
    context_object_name = 'posts'

class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'post_details.html'
    context_object_name = 'post'

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
